import csv 

csv_file_path = r'C:\Users\Matthew Durney\Desktop\python-challenge\PyBank\Resources\budget_data.csv'
Budget_Output = r'C:\Users\Matthew Durney\Desktop\python-challenge\PyBank\analysis\Budget_Output.txt'

# Declare and set Months and Net Profits/Losses to 0
Months = 0
Net = 0

# Open and read the CSV file
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip header row
    csv_header = next(csv_reader)

    # Set list of Months along with Profits/Losses
    Months_List = []
    Net_List = []
   
    # Loop through each month
    for row in csv_reader:

        # Calculate # of Months and Net Profits/Losses
        Months += 1
        Net += int(row[1])
        
        # Create list for Months column
        Months_List.append(row[0])
        # Create list for Profits/Losses column
        Net_List.append(int(row[1]))

        # Net Change is new column showing increase or decrease in profits/losses from month to month
        Net_Change = [] 
        # Loop again to calculate Net Change for each month and add values to list 
        for i in range(1, len(Net_List)):
             Net_Change.append(Net_List[i]-(Net_List[i-1]))


# Calculate Average Change    
Average_Change = sum(Net_Change)/ len(Net_Change)

# Find the Greatest Profict Increase/Decrease 
Greatest_Profit_Increase = max(Net_Change)
Greatest_Profit_Decrease = min(Net_Change)

# Find the index number to use for month correlation
index1 = Net_Change.index(Greatest_Profit_Increase)
index2 = Net_Change.index(Greatest_Profit_Decrease)

# Save output to be printed and exported to text file
Output = (
"Financial Analysis\n"
"---------------------\n"
f"Total Months: {Months}\n"
f"Total: ${Net}\n"
f"Average Change: ${Average_Change:.2f}\n"
f"Greatest Increase in profits: {Months_List[index1 +1]} (${Greatest_Profit_Increase})\n"
f"Greatest Decrease in profits: {Months_List[index2 +1]} (${Greatest_Profit_Decrease})\n"
)

# Export output to text file 
with open(Budget_Output, "w") as txt_file: 
    txt_file.write(Output)