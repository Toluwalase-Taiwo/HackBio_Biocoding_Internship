# Bioinformatics Tools

A collection of Python tools for DNA sequence analysis and biological growth modeling.

## Features

- DNA to Protein Translation
- Hamming Distance Calculator
- Logistic Growth Curve Generator

## Functions

### DNA to Protein Translation
Translates DNA sequences into protein sequences using the standard genetic code. Handles start/stop codons and includes a complete codon table.

```python
dna_sequence = "ATGGCCATGGCGCCCAGAACT"
protein_sequence = translate_dna_to_protein(dna_sequence)
```

### Hamming Distance Calculator
Calculates the Hamming distance between two sequences of equal length. Useful for comparing genetic sequences or strings.

```python
distance = hamming_distance("ATCG", "ACCG")
```

### Logistic Growth Curve
Models population growth using the logistic function, allowing customizable carrying capacity and growth rate parameters.

```python
growth = logistic_growth_curve(x=10, L=1000, k=0.5)
```

## Requirements
- Python 3.x
- No additional packages required

## Usage
Run the script and follow the prompts for the logistic growth curve parameters. For DNA translation and Hamming distance calculations, modify the input sequences as needed.


