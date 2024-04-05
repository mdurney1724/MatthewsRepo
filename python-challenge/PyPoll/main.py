import csv 

csv_file_path = r'C:\Users\Matthew Durney\Desktop\python-challenge\PyPoll\Resources\election_data.csv'
Election_Output = r'C:\Users\Matthew Durney\Desktop\python-challenge\PyPoll\analysis\Election_Output.txt'

# Declare and set Total Votes to 0
Total_Votes = 0

# Create empty list of Candidates
Candidates = []

# Use dictionary to store Candidates (keys) and Vote Counts (values)
Vote_Counts = {}
# Use dictionary to store Candidates (keys) and Vote Percentages (values)
Vote_Percentages = {}

# Open and read the CSV file
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip header row
    csv_header = next(csv_reader)

    # Loop through each vote
    for row in csv_reader:
        
        # Calculate Total Votes and locate Candidate Names 
        Total_Votes += 1
        Candidate_Name = row[2]
              
        # If-statement to add new Candidates to Candidates list, as well set their initial vote count to 0 in dictionary when added
        if row[2] not in Candidates:
            Candidates.append(row[2])
            Vote_Counts[Candidate_Name] = 0
        # Calculate Vote Count for each Candidate added to dictionary
        Vote_Counts[Candidate_Name] += 1

# Find the Percentage of the Votes gained per Candidate
for i in Vote_Counts:
    Vote_Percentages[i]= (Vote_Counts[i]/Total_Votes)

# Find the Inverse of the Vote Counts to find the Winner
inverse = [(value,key) for key,value in Vote_Counts.items()]
Winner = max(inverse)[1]

# Create variables that give desired output from Vote_Counts and Vote_Percentages dictionaries
First_Candidate = list(Vote_Counts.keys())[0]
Second_Candidate=list(Vote_Counts.keys())[1] 
Third_Candidate=list(Vote_Counts.keys())[2]    

First_Candidate_Votes=list(Vote_Counts.values())[0]  
Second_Candidate_Votes=list(Vote_Counts.values())[1] 
Third_Candidate_Votes=list(Vote_Counts.values())[2]      

First_Candidate_Percentage = (list(Vote_Percentages.values())[0]) * 100
Second_Candidate_Percentage = (list(Vote_Percentages.values())[1]) * 100
Third_Candidate_Percentage = (list(Vote_Percentages.values())[2]) * 100

# Save output to be able to print and export to text file
Output = (
"Election Results\n"
"---------------------\n"
f"Total Votes: {Total_Votes}\n"
"---------------------\n"
f"{First_Candidate} : {round(First_Candidate_Percentage, ndigits=3)}% ({First_Candidate_Votes})\n"
f"{Second_Candidate} : {round(Second_Candidate_Percentage, ndigits=3)}% ({Second_Candidate_Votes})\n"
f"{Third_Candidate} : {round(Third_Candidate_Percentage, ndigits=3)}% ({Third_Candidate_Votes})\n"
"---------------------\n"
f"Winner:  {Winner}\n"
)

# Export output to text file  
with open(Election_Output, "w") as txt_file: 
    txt_file.write(Output)