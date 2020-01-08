import sys
import csv
from os import listdir
from os.path import isfile, join, isdir
import ntpath

ntpath.basename("a/b/c")


def get_case_ids_with_mutation(mutation_of_interest):
    with open(mutation_file_path) as tsv_file:
        reader = csv.reader(tsv_file, delimiter='\t')
        rows_with_mutation_of_interest = []
        for row in reader:
            if row[1] == mutation_of_interest:
                rows_with_mutation_of_interest.append(row[0])
        return rows_with_mutation_of_interest


def get_subdirectory_paths(directory):
    subdirectory_paths = [
        join(directory, f) for f in listdir(directory)
        if (isdir(join(directory, f)) and '.DS_Store' not in f)
    ]
    if join(directory, '.DS_Store') in subdirectory_paths:
        subdirectory_paths.remove(join(directory, '.DS_Store'))
    subdirectory_paths = sorted(subdirectory_paths)
    return subdirectory_paths


def get_image_paths(directory):
    image_paths = [
        join(directory, f) for f in listdir(directory) if (isfile(join(directory, f)) and f.endswith(".svs"))
    ]
    if join(directory, '.DS_Store') in image_paths:
        image_paths.remove(join(directory, '.DS_Store'))
    image_paths = sorted(image_paths)
    return image_paths


def get_all_image_paths(case_directory_paths):
    all_image_paths = []
    for case_directory_path in case_directory_paths:
        for image_path in get_image_paths(case_directory_path):
            all_image_paths.append(image_path)
    return all_image_paths


def get_path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def label_images(all_image_paths):
    for image_path in all_image_paths:
        print(get_path_leaf(image_path))


if __name__ == '__main__':
    print(sys.argv)
    tcga_cases_directory_path = sys.argv[1]
    mutation_file_path = sys.argv[2]
    mutation_of_interest = sys.argv[3]
    output_path = sys.argv[4]

    case_ids_with_mutation = get_case_ids_with_mutation(mutation_of_interest)
    case_directory_paths = get_subdirectory_paths(tcga_cases_directory_path)
    all_image_paths = get_all_image_paths(case_directory_paths)
    mutation_true, mutation_false = label_images(all_image_paths)

    print(case_ids_with_mutation)
    print(get_subdirectory_paths(tcga_cases_directory_path))
    print(all_image_paths)

    print(tcga_cases_directory_path)
    print(mutation_file_path)
    print(output_path)
