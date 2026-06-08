import numpy as np

def align_pw(seq_a, seq_b):
    n = len(seq_a)
    m = len(seq_b)
    match = 1
    mismatch = -1
    indel = -2
    score_matrix = np.empty((n+1,m+1))
    for i in range(0, n+1):
        score_matrix[i][0] = i*indel
    for j in range(0, m+1):
        score_matrix[0][j] = j*indel
    for i in range(1, n+1):
        for j in range(1, m+1):
            tree = []
            if seq_a[i-1] == seq_b[j-1]:
                    x = score_matrix[i-1][j-1] + match
                    tree.append(x)
            if seq_a[i-1] != seq_b[j-1]:
                    y = score_matrix[i-1][j-1] + mismatch
                    tree.append(y)
        
            zi = score_matrix[i-1][j] + indel
            zj = score_matrix[i][j-1] + indel
            tree.append(zi)
            tree.append(zj)
            score_matrix[i][j] = max(tree)
    print (score_matrix)
    i = n+1
    j = m+1
    while i > 0 and j > 0:
        check = []
        if score_matrix[i][j] - score_matrix[i-1][j-1] == match:
            check.append(score_matrix[i-1][j-1])
        if score_matrix[i][j] - score_matrix[i-1][j-1] == mismatch:
            check.append(score_matrix[i-1][j-1])
        if score_matrix[i][j] - score_matrix[i][j-1] == indel:
            check.append(score_matrix[i][j-1])
        if score_matrix[i][j] - score_matrix[i-1][j] == indel:
            check.append(score_matrix[i-1][j])
        cmax = max(check)