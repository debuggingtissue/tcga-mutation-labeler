import sys
import csv


def get_case_ids_with_mutation(mutation_of_interest):
    with open(mutation_file_path) as tsv_file:
        reader = csv.reader(tsv_file, delimiter='\t')
        rows_with_mutation_of_interest = []
        for row in reader:
            if row[1] == mutation_of_interest:
                rows_with_mutation_of_interest.append(row[0])
        return rows_with_mutation_of_interest


if __name__ == '__main__':
    print(sys.argv)
    tcga_cases_directory_path = sys.argv[1]
    mutation_file_path = sys.argv[2]
    mutation_of_interest = sys.argv[3]
    output_path = sys.argv[4]

    case_ids_with_mutation = get_case_ids_with_mutation(mutation_of_interest)
    
    print(case_ids_with_mutation)

    print(tcga_cases_directory_path)
    print(mutation_file_path)
    print(output_path)
