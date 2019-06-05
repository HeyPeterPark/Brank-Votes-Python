#PyPoll

import csv
from csv import reader

#Header: [Voter ID, County, Candidate] - [12864552, Marsh, Khan]
opened_file = open("Resources/election_data.csv", encoding ="utf-8")
read_file = reader(opened_file)
election_data = list(read_file)

#names & votes
names = {}
for row in election_data[1:]:
    candidate = row[2]
    if candidate in names:
        names[candidate] += 1
    else:
        names[candidate] = 1

total_votes = sum(names.values())
max_vote = max(names.values())

#names & %
vote_percentages = {}
for key in names:
    percentage = (names[key] / total_votes) * 100
    vote_percentages[key] = round(percentage, 0)

#winner name
for key in names:
    if names[key] == max_vote:
        winner = key
        print(winner)
    else: 
        pass

print(f'''
Election Results
{'-'*30}
Total Votes: {total_votes}
{'-'*30}''')
for key in names: 
    print(f'{key} {vote_percentages[key]}% ({names[key]})')
print(f'''{'-'*30}
Winner: {winner}
{'-'*30}
''')

#coulnd't figure out how to export a for loop into a txt :( 
textfile = open('PyPoll.txt', 'w')
textfile.write(f'''
Election Results
------------------------------
Total Votes: 3521001
------------------------------
Khan 63.0% (2218231)
Correy 20.0% (704200)
Li 14.0% (492940)
O'Tooley 3.0% (105630)
------------------------------
Winner: Khan
------------------------------
''')
textfile.close()





