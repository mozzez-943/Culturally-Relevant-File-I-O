source_file = open('a1_dishes_by_votes.txt', 'r')
destination_file = open('a1_filtered_dishes.txt', 'w')

line = source_file.readline()

while line:
    dish, score = line.split(':')
    if int(score) >= 10:
        destination_file.write(f'{dish}\n')
    line = source_file.readline()