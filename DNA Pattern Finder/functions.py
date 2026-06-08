def PatternCount(text, pattern):
   
   count = 0
   for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
        count += 1
   print(count)

def mostAppearedSeq(text, length):
    patterns = {}
    for i in range(len(text) - length + 1):
        pattern = text[i:i+length]
        if pattern not in patterns:
            patterns[pattern] = 1
        else:
            patterns[pattern] = patterns.get(pattern) + 1
    max = 0
    for value in patterns.values():
        if max < value:
            max = value
    max_seq = ""
    for key, value in patterns.items():
        if value == max:
            max_seq = key
    print(patterns)
    print(max)
    print(max_seq)

def minSkew():
    text = input("Insert DNA Sequence: ")
#    text =
    skew = 0
    skew_line = []
    min = 0
    min_list = []
    for i in range(len(text)):
        if text[i] == "G":
            skew += 1
        elif text[i] == "C":
            skew -= 1
        else:
            skew += 0
        skew_line.append(skew)
    for i in range(len(skew_line)):
        if skew_line[i] < min:
            min = skew_line[i]
    for i in range(len(skew_line)):
        if skew_line[i] == min:
            min_list.append(i+1)
    print(skew_line)
    print(min)
    print(min_list)

def hammingDistance():
    seq_one = input("Insert First Sequence: ")
    seq_two = input("Insert Second Sequence: ")
    #seq_one = "GGACGTGCACGATAACTGTTAAGAAGACTGCGTATGGCACAGGATAAACTAGCTTAGGACATTGGAAACCCCACCTGGGTCTCTCGTAGGCAGTTAGACGTCAGTGGAAATCGGCGAGCCACGGATTGACCGGGTATCCCCATGACTGGGTCAGGGAATTAGACAAAATACAACCGCAAGCTCTATGAAGTGTCGATCCATGTCGGCGCCACTGCTAGTAACCAAGATCCGAGCTTGCGGGCACAAATTACACAATCCTCGTATTCTAGCGTCCGACGTAGCACTCAGGTAGCGTCAGTACTCACAACCGCCTCTCGGTTAGTGTATCCATCGAAGGCGGGGGCCTCTAGGACGAGCGGTAGTATTCAACAAAGGGCAAAGTTTCTTGTCCCGAGCTTAGAAGCCAACAGCGGATTAACAGAACATCTATCTCGGACTCCGCACACAATCACCCAGGGACCCGCTGGACATGTACGATCTGGGAGTCTGCGTGTACTCACCAAGTTAAGTAGGTATAATGCCCGGCTTAAGGCAACTCAATCACGCCTGACCCCGAGCGTCTGGAAGATGTCGCGCGTTCCTCGGTTTAGTCGCCTAGCCACAATTTAGGGAGTAAGTGCGGGGGCGTGTGAAAATTGAGAGAGGTTAAGGGTGCGATGCACTCGAGAAACTTGAAACTTGGGCCTTAGAGTCACGTCACCCGCCCAATCCTAGTCCTGGTAACCGATATCAGAAGACCTTAATAGAATAGAGATAGTGCAAATACCGGTGATTTTGCAAGGTCCCTCTCATGGAACGACGTGTGGCCATATGAGAGCAGCAGCCGCTCAGATCCAAAGGCGTACCCGGCGCGTTTTGACGATACCAAGGGACTACTTAAAATGGTAAACTAGGGCGGTGTACGGGACCGTGAATCAGCAGTAATGACTGTTTAAGCTGCATTATGACTTACCACAACGTATTGTGCTATATACTGCCGGACTCCCGCGTCGTTTCAATCGCTGACTTATCGTTTACCTGAAAAAACCCATTTATGCTAATCCTCCAAATAAGGGTATGCAAGTTGGATAGTAGTGGGCCACGACAACCGCACCGCCCGGGATAGAAGCAAGCCCAAC"
    #seq_two = "TGCGATAGCTTAGTGAACATTAACGCCTTGCTTGGTCAGTTGAAAGCATGCCGGCTCCGGTTACGGTTCCGAGATGAGCCATCATGTAATCCATGTCTGCTTTCGACATCACGACCATTAGTATATGAGAATTTCATTCCACATTGATCAAACTGCTATTTGGGCCGGGGTACAAGCAATCTACAGGCACTCCGAAAGCGGCAGGGGGGCGAATTAACCATATATACCTGTATAACTTCTTCCTAGACTGACTTAGCTAGCGCATTATTTGAAGCGAGGCGACAACTTCCTCTGATAGCGCTGTTGCCGTTCGGGGCCTTTCTAATCTGTGGCCTGCACATTTTGCACTTATCATGTCATGACAGTGGTCCACTGCAACCCTTGTCAGTAATTCAAAGAGTCAGTCACTTCCCAACTTCTTAGTGCTCGGACGGATTAGCGATGGCGACTGTCGCGTCAATAATGTACGGAATGCACGGCCCTATTCTTGGATTCAAAAGAGGGAGCCGGCTTAGCGCGTAGATCCACAGACGTTCGCGGTAGCAACCGAACTGCTAGCCACCCGCGCTTGGAATTCGTACACGTGCCCCTAATCCATGGTGTGTACGTCGGGAAGAGGTATGGACTGCGATACTTCTGGCTCCTAGATTCGCTTATTTCTGTGGGGGTGCCGCGGAGTCCGTTCCTGATTACTGGATATGGATATACCGTTCCTGTATACCTATCTATACAGTTGTTCCAAAAACACGCGGATCGACCTCTAATGAAAATCCTCAGTGCTTACCGTCTACTTGATAGTCCTAATATACGTTATCCAGGAAGTGGACTGGTCGGTAACACGAAATAACCCCGTCACCGCTCAACGAGTCCTACTGGTGCCTCCGCACTTTAGAAACTGCCGACATATGAGCTGAGGCGCAGTAGTTCTAACGGTTCTATCTTTGGTCGAATAGAGTTGAGGACGCTGGAGGGATTGGCGGCTCCCCTCGTGTACCCTGAGCAGTACGAAGGCAAATGGGAAAACAACGCATGATACTCGCGTTTCGTTTGGTACGAGGGGCCGATACGTTTACAATTTCCGAGCAGGTAGTAAACGTTATTAGCAGTCGCAATGGAGA"
    count = 0
    if len(seq_one) == len(seq_two):
        for i in range(len(seq_one)):
            if seq_one[i] != seq_two[i]:
                count += 1
        print(count)
    else:
        print("Ensure both strings are of same length!")
        hammingDistance()

def hammingDistanceizer(seq_one, seq_two):
    count = 0
    if len(seq_one) == len(seq_two):
        for i in range(len(seq_one)):
            if seq_one[i] != seq_two[i]:
                count += 1
        return(count)
    else:
        print("Ensure both strings are of same length!")
        hammingDistance()

def aprxPatternMatch(text, pattern, k):
    list = []
    indices = []
    for i in range(len(text) - len(pattern) + 1):
        list.append(hammingDistanceizer(text[i:i+len(pattern)],pattern))
    for i in range(len(list)):
        if list[i] <= k:
            indices.append(i)
    print(indices)
    print(list)
    print(len(indices))

def reverseComplement(sequence):
    reverseComplement = ""
    for i in range(len(sequence)-1,-1,-1):
        if sequence[i] == "A":
            reverseComplement += "T"
        if sequence[i] == "G":
            reverseComplement += "C"
        if sequence[i] == "C":
            reverseComplement += "G"
        if sequence[i] == "T":
            reverseComplement += "A"
    print(reverseComplement)

def motifEnumeration(dna, k, d):
    dna += " "
    k = int(k)
    d = int(d)
    patterns = []
    sequences = []
    j = 0
    for i in range(len(dna)):
        if dna[i]  == " ":
            seq = dna[j:i]
            j = i+1
            sequences.append(seq)
    for x in range(len(sequences)):
        piece = sequences[x]
        for n in range(len(piece) - k +1):
            pattern = piece[n:n+k]
            patterns.append(pattern)
    
    print(sequences)
    print(patterns)