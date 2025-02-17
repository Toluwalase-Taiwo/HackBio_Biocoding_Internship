# Create a dictionary of all genetic codes

genetic_code = {
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
        'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu', 'UUA': 'Leu', 'UUG': 'Leu',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'UUU': 'Phe', 'UUC': 'Phe',
        'AUG': 'Met',  # Start codon
        'UGU': 'Cys', 'UGC': 'Cys',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
        'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser', 'AGU': 'Ser', 'AGC': 'Ser',
        'UAU': 'Try', 'UAC': 'Try',
        'UGG': 'Trp',
        'CAA': 'Gln', 'CAG': 'Gln',
        'AAU': 'Asn', 'AAC': 'Asn',
        'CAU': 'His', 'CAC': 'His',
        'GAA': 'Glu', 'GAG': 'Glu',
        'GAU': 'Asp', 'GAC': 'Asp',
        'AAA': 'Lys', 'AAG': 'Lys',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGA': 'Arg', 'AGG': 'Arg',
        'UAA': '*', 'UAG': '*', 'UGA': '*'  # Stop codons
    }

def translate_dna_to_protein(dna_sequence):
    '''
    Translates a DNA sequence into a protein sequence following the central dogma of biology.
    
    Args:
        dna_sequence (str): Input DNA sequence 
        
    Returns:
        str: Protein sequence in amino acid code
    '''
        
    rna_sequence = dna_sequence.replace('T', 'U') #Convert DNA sequence to RNA by replacing 'T' with 'U'

    #Initialize an empty protein sequence
    protein_sequence = []
    for i in range(0, len(rna_sequence), 3):
        
        #Extract the current codon
        codon = rna_sequence [i : i + 3]

        # Check if codon is complete
        if len(codon) < 3:
            break
        
        #check if codon is a stop codon
        if genetic_code[codon] == "*":
            break
            
        #append the corresponding amino acid to the protein sequence
        protein_sequence.append(genetic_code[codon])
        
    return protein_sequence

# Example DNA sequence
dna_sequence = "ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
protein_sequence = translate_dna_to_protein(dna_sequence)
print(f'DNA sequence: {dna_sequence}')
print(f'Protein sequence: {protein_sequence}')

dna_sequence = 'ATGGCCATTGTA'
protein_sequence = translate_dna_to_protein(dna_sequence)
print(f'DNA sequence: {dna_sequence}')
print(f'Protein sequence: {protein_sequence}')

def logistic_growth_curve(x, L, k):
    """
    Logistic growth curve function.

    Parameters:
    x (float): input value
    L (float): carrying capacity
    k (float): growth rate

    Returns:
    float: output value of the logistic growth curve
    """
    sig = 1 / (1 + (2.71828 ** (-k * x)))
    return L * sig

L = float(input("Enter the carrying capacity (L): "))
k = float(input("Enter the growth rate (k): "))

x_values = range(1, 101)
logistic_values = [logistic_growth_curve(x, L, k) for x in x_values]

# Print the results
for x, logistic_value in zip(x_values, logistic_values):
    print(f"x = {x}, Logistic Value = {logistic_value}")

def hamming_distance(seq1, seq2):
    """
    Calculate the Hamming distance between two strings.
    Hamming distance is the number of positions at which corresponding characters differ.
    
    Args:
        seq1 (str): First string
        seq2 (str): Second string
        
    Returns:
        int or str: Hamming distance if strings are of equal length,
                   error message if strings have different lengths
    """
    # Check if sequences have equal length
    if len(seq1) != len(seq2):
        return f"Cannot calculate Hamming distance - sequences have different lengths: {len(seq1)} and {len(seq2)}"
    
    # Calculate Hamming distance by counting positions with different characters
    distance = sum(c1 != c2 for c1, c2 in zip(seq1, seq2))
    
    return distance

slack_username = 'Princesslase'
twitter_handle = 'Toluwaaalase'
result = ((hamming_distance(slack_username , twitter_handle)))
print(f"Hamming_distance of {slack_username} and {twitter_handle}: {result}")
