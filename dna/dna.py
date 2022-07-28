import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py sample.csv sequence.txt ")
    elif sys.argv[1].endswith('.csv') == False:
        sys.exit("Invalid DNA file. Usage: python dna.py sample.csv sequence.txt")
    elif sys.argv[2].endswith('.txt') == False:
        sys.exit("Invalid sequence file. Usage: python dna.py sample.csv sequence.txt")

    # TODO: Read database file into a variable
    database = []
    with open(sys.argv[1], 'r') as database_file:
        reader_database = csv.DictReader(database_file)
        for row in reader_database:
            database.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as sequence_file:
        reader_sequence = sequence_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    matches = {}

    for key in database[0]:
        matches[key] = str(longest_match(reader_sequence, key))

    # TODO: Check database for matching profiles

    for i in range(len(database)):
        # Dict comparison algorithm sourced from: https://stackoverflow.com/questions/4527942/comparing-two-dictionaries-and-checking-how-many-key-value-pairs-are-equal
        shared_items = {k: database[i][k] for k in database[i] if k in matches and database[i][k] == matches[k]}
        if len(shared_items) == (len(matches) - 1):
            print(f"{database[i]['name']}")
            return
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
