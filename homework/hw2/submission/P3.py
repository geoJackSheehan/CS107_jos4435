#!/usr/bin/env python3
# File       : P3.py
# Description: DNA complement
# Copyright 2022 Harvard University. All Rights Reserved.

def dna_complement(seq):
    """Compute the DNA complement.

    Parameters
    ----------
    seq : str
        Input DNA sequence.

    Returns
    -------
    res : str or None
        Result complement DNA string in upper case letters.  None for invalid
        input.
    """

    seq = seq.upper()
    complementary_seq = []
    for letter in seq:
        if letter == "A":
            complementary_seq.append("T")
        elif letter == "T":
            complementary_seq.append("A")
        elif letter == "G":
            complementary_seq.append("C")
        elif letter == "C":
            complementary_seq.append("G")
        else:
            return None
    
    res = ''.join(complementary_seq)
    return res

if __name__ == "__main__":
    print('Demo:')
    print("mixed case INPUT string: 'aTgCcGtATaCgGcGt'")
    print(f"mixed case OUTPUT string: '{dna_complement('aTgCcGtATaCgGcGt')}'")
    print("invalid INPUT string: 'atgcNNNNNNNatgc'")
    print(f"invalid OUTPUT string: {dna_complement('atgcNNNNNNNatgc')}")
