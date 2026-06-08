query = "CCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAGATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCTGCTTT"


def gc_content(query):
    gc = 0
    for n in query:
         if n == "G" or n == "C":
            gc +=1
            print()
    return gc/len(query)

print (gc_content(query))