query = "CCGTTATTGGGGGGCAAAGATGGAGTCCTCCTCTTATCATATTTGTATTGACGACAGCCGTGTTCCCGGTTTCCTCAGAGATTTAAGAATAAGGGCTTAT"

def complement(base):
    if base == "A":
        return "T"
    if base == "T":
        return "A"
    if base == "G":
        return "C"
    if base == "C":
        return "G"

def rev_cDNA(query):
    query = query[::-1]
    cDNA = ""
    for n in query:
        cDNA += complement(n)
    return cDNA

print("5' " + rev_cDNA(query) + " 3'")