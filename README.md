
Script to Filter Nucleotide Sequences
This script is designed to filter nucleotide sequences from .fas files based on a provided list in lista.txt. The filtered sequences are saved in a new directory.

Requirements:
Python 3.x
Biopython (can be installed with pip install biopython)
How to Use:
Clone or download the repository.

Ensure you have Python installed on your system. You can download it from python.org.

Install the Biopython library with the command:

Copy code
pip install biopython
Place your .fas files in the directory /guest/triatominae/tiagob/arthur_/individual_loci_clean/.

Edit the file lista.txt in the directory /guest/triatominae/tiagob/arthur_/individual_loci_clean/ to contain the sequences you want to keep, one per line, in the format >SequenceName.

Run the script:

bash
Copy code
python filter_sequences.py
The filtered sequences will be saved in the directory /guest/triatominae/tiagob/arthur_/individual_loci_clean/new/.






