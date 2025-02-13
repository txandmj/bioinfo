def dnaToRna(filename):
    # counts = {"A":0, "C":0, "G":0, "T":0}
    with open(filename, 'r') as file:
        sequence = file.read().strip()
        sequence = sequence.replace('T', 'U')

    print(sequence)

dnaToRna("C:\\Users\\Xin Tang\\Downloads\\rosalind_rna.txt")