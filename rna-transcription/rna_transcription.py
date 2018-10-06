def to_rna(dna_strand):
    c = ''
    for x in dna_strand:
        if x == 'C':
            c += 'G'
        elif x == 'G':
            c += 'C'
        elif x == 'T':
            c += 'A'
        elif x == 'A':
            c += 'U'
    return c
