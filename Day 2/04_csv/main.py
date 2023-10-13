import csv

# funkcje dedykowane do pracy z danymi w formacie csv
with open('names.csv', 'r') as file:
    csv_reader = csv.reader(file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t', lineterminator="\n")

        for row in csv_reader:
            csv_writer.writerow(row)


# klasy dedykowane do pracy z danymi w formacie csv
with open('names.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    with open('new_names2.csv', 'w') as new_file:
        headers = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=headers, lineterminator='\n')

        for row in csv_reader:
            csv_writer.writerow(row)
