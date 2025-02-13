def CountNucleotides(filename):
    # counts = {"A":0, "C":0, "G":0, "T":0}

    with open(filename, 'r') as file:
        sequence = file.read().strip()
    count_A = sequence.count('A')
    count_C = sequence.count('C')
    count_G = sequence.count('G')
    count_T = sequence.count('T')

    print(count_A, count_C, count_G, count_T)

CountNucleotides("C:\\Users\\Xin Tang\\Downloads\\rosalind_dna (4).txt")


