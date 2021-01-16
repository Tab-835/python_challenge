import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

# list for candidate names
candidate_names = []

# list for number of votes
votes_numbers = []

# list for percentage of total votes
percent_votes = []
total_votes = 0

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] not in candidate_names:
            candidate_names.append(row[2])
            index = candidate_names.index(row[2])
            votes_numbers.append(1)

        else:
            index = candidate_names.index(row[2])
            votes_numbers[index] += 1

    for votes in votes_numbers:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    winner = max(votes_numbers)
    index = votes_numbers.index(winner)
    winning_candidate = candidate_names[index]

print("Election Results")
print("---------------------------")
print(f"Total Votes: {str(total_votes)}")
print("---------------------------")
for i in range(len(candidate_names)):
    print(f"{candidate_names[i]}: {str(percent_votes[i])} ({str(votes_numbers[i])})")
print("---------------------------")
print(f"Winner: {winning_candidate}")
print("---------------------------")

output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidate_names)):
    line = str(f"{candidate_names[i]}: {str(percent_votes[i])} ({str(votes_numbers[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))