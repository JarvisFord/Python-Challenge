#HOMEWORK PART 2

#total votes cast
import csv
with open('/Users/jarvis/Downloads/NUCHI201902DATA1-master/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    data = list(csv_reader)
    row_count = len(data)
print(row_count)

import csv
with open('/Users/jarvis/Downloads/NUCHI201902DATA1-master/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    row_count = 0
    ballot_names = []
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0
    vote_list = ["",0]
    for row in csv_reader:
        if row[2] not in ballot_names:
            ballot_names.append(str(row[2]))
        if row[2] == "Khan":
            khan_count += 1
        if row[2] == "Correy":
            correy_count += 1
        if row[2] == "Li":
            li_count += 1
        if row[2] == "O'Tooley":
            otooley_count += 1
        row_count += 1
    vote_list.append("Khan", khan_count)
print(khan_count)
print(row_count)
print("Khan: " + str(((khan_count/row_count) * 100)) + "% (" + str(khan_count) + ")") #ADD FOR THE REST OF THE CANDIDATES
print(vote_list)


print(ballot_names)






#results
print('Total Votes Cast: ' + str(row_count))
