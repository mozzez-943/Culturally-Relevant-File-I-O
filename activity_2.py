import csv

source_file = open('students.csv', 'r')
destination_file = open('filtered_students.txt', 'w')

reader = csv.DictReader(source_file)

for row in reader:
    # Each row is a dictionary
    if float(row['Grade']) >= 50:
        # Each row is a dictionary
        destination_file.write(f'{row["Name"]}\n')

source_file.close()
destination_file.close()