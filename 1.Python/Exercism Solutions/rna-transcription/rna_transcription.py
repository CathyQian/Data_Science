def to_rna(dna_strand):
    rna_strand = ''
    map = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    for dna in dna_strand:
        try:
            rna_strand += map[dna]
        except ValueError:
            print('Character {} is invalid input!'.format(dna))
    return rna_strand
