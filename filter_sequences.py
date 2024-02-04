import os
from Bio import SeqIO

# Source directory
dir_source = "in_dir"

# Destination directory
dir_destination = "out_dir"

# Path to the lista.txt file
path_lista = "/guest/triatominae/tiagob/arthur_/individual_loci_clean/lista.txt"

# Read desired sequences from the lista.txt file
with open(path_lista, 'r') as lista_file:
    desired_sequences = [line.strip()[1:] for line in lista_file if line.startswith(">")]

# Iterate over .fas files in the source directory
for fasta_file in os.listdir(dir_source):
    if fasta_file.endswith(".fas"): #see final format and change (fas, fa or fasta) 
        path_fasta_file = os.path.join(dir_source, fasta_file)
        path_destination_file = os.path.join(dir_destination, fasta_file)

        # Filter and write the desired sequences to the new file
        with open(path_destination_file, 'w') as destination_file:
            for record in SeqIO.parse(path_fasta_file, 'fasta'):
                header = record.id
                sequence = str(record.seq)

                if header in desired_sequences:
                    destination_file.write(f">{header}\n{sequence}\n")
