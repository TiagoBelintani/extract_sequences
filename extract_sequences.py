import os
import sys
from Bio import SeqIO

def filter_sequences(input_dir, output_dir, list_file):
    # Read desired sequences from the list file
    with open(list_file, 'r') as list_file:
        desired_sequences = [line.strip()[1:] for line in list_file if line.startswith(">")]

    # Iterate over .fas files in the input directory
    for fasta_file in os.listdir(input_dir):
        if fasta_file.endswith(".fas"):
            input_file_path = os.path.join(input_dir, fasta_file)
            output_file_path = os.path.join(output_dir, fasta_file)

            # Filter and write the desired sequences to the new file
            with open(output_file_path, 'w') as output_file:
                for record in SeqIO.parse(input_file_path, 'fasta'):
                    header = record.id
                    sequence = str(record.seq)

                    if header in desired_sequences:
                        output_file.write(f">{header}\n{sequence}\n")

if __name__ == "__main__":
    # Check if the correct number of arguments was provided
    if len(sys.argv) != 4:
        print("Usage: python script.py input_dir output_dir list_file")
        sys.exit(1)

    # Get command line arguments
    input_directory = sys.argv[1]
    output_directory = sys.argv[2]
    list_file_path = sys.argv[3]

    # Execute the filtering function
    filter_sequences(input_directory, output_directory, list_file_path)

