import csv

source_file = open('a2_cultural_foods.csv', 'r')
destination_file = open('a2_foods_veg_halal.txt', 'w')

reader = csv.DictReader(source_file)

for row in reader:
    # Filtering for vegetarian and halal, treating each row as a dictionary
    if (row['Vegetarian'] == "yes") and (row['Halal'] == "yes"):
        destination_file.write(f'{row["Name"]}\n')

source_file.close()
destination_file.close()