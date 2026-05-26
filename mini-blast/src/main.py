query = "ATGCGTAC"
database = "GGGATGCGTTTAAA"

def get_kmers(sequence, k=3):
    kmers = []

    for i in range(len(sequence) - k + 1):
        kmers.append((sequence[i:i+k], i))

    return kmers

def find_matches(query_kmers, database):
    matches = []

    for kmer, query_pos in query_kmers:
        start = 0

        while True:
            db_pos = database.find(kmer, start)

            if db_pos == -1:
                break

            matches.append({
                "kmer": kmer,
                "query_pos": query_pos,
                "db_pos": db_pos
            })

            start = db_pos + 1

    return matches

def extend_match(query, database, query_pos, db_pos, k):
    
    score = 0
    
    alignment_query = ""
    alignment_db = ""

    i = 0

    while (
        query_pos + i < len(query)
        and db_pos + i < len(database)
    ):

        q_char = query[query_pos + i]
        d_char = database[db_pos + i]

        alignment_query += q_char
        alignment_db += d_char

        if q_char == d_char:
            score += 1
        else:
            score -= 1

        if score < 0:
            break

        i += 1

    return {
        "query_alignment": alignment_query,
        "db_alignment": alignment_db,
        "score": score
    }

query_kmers = get_kmers(query)

matches = find_matches(query_kmers, database)

for match in matches:

    result = extend_match(
        query,
        database,
        match["query_pos"],
        match["db_pos"],
        3
    )

    print(result)
    