from codon_tabe import *

def codon_translator(codon):
    return codon_table[codon]

def translation(mRNA):
    n = 0
    aa_seq = "N-"
    while n < len(mRNA)-1:
        codon = mRNA[n:n+3]
        aa_seq += codon_translator(codon) + "-"
        n += 3
    return(aa_seq + "C")


print(translation("CACGUCCGAAGGCCAAAUGCCACGUUAGGAUUGAUCCGAUUAAUAACCAAGCUCGAUUUUUUCCGUCCAAUUGGACUCAAGACGAUCGACUCCUUAGACG"))