# MATPLOTLIB --> allow us to plot and see the graph 
# PANDAS --> allow us to easily categorized & search for data within the csp file

import pandas as pd
import csv
from datetime import datetime
import os
from data_entry import get_date, get_amount, get_category, get_description
import matplotlib.pyplot as plt

class CSV:
    # CSV_FILE --> variable, finance_data -->  name of file that we work with 
    CSV_FILE = "E:/python/finance_tracker/finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT =  "%d-%m-%Y"
    
    #1 initialize the csv file
    @classmethod
    def initialize_csv(cls):
        print("Initializing CSV...")
        
        # Create directory if it doesn't exist
        directory = os.path.dirname(cls.CSV_FILE)
        if not os.path.exists(directory):
            print(f"Creating directory: {directory}")
            os.makedirs(directory)
            
        #try to read in the csv file
        try:
            df = pd.read_csv(cls.CSV_FILE)
            print("CSV file found and loaded.")
            #if above code not work
        except FileNotFoundError:
            print("CSV file not found. Creating new file...")
            #crate the file (start by having some headings or columns)
            df = pd.DataFrame(columns=cls.COLUMNS)
            #dataframe --> object within pandas that allows us to access different rows, columns from a csv file

            #export the dataframe to a csv file
            df.to_csv(cls.CSV_FILE, index=False)
            print("CSV file created.")

    #2 add some entries to the file
    @classmethod
    def add_entry(cls,date, amount, category, description):
        #CSV writer
        new_entry = {
           "date": date,
           "amount": amount,
           "category": category,
           "description": description
        }
        #  opened a csv file in append mode
        with open(cls.CSV_FILE, "a", newline="") as csvfile: # a --> pending to the end of the file
            writer = csv.DictWriter(csvfile, fieldnames= cls.COLUMNS)
            #CSV WRITER --> take a dictionary and write it into the CSV file 
            writer.writerow(new_entry)
            print("Entry added successfully!")

    #3 give us all the transactions within date range
    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        # what we do next -->  convert all of the dates inside of the date column to a datetime object - use them to filter by different transactions
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        #create something known as a mask --> MASK = something that we can aooly to the different rows insiden of a data frame to see if we should select that row or not

        #check the entered date between start_date and end_date
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        #apply to every single row inside of dataframe and it's going to filter the different elements
        #returns a new filtered dataframe
        filtered_df = df.loc[mask]


        if filtered_df.empty:
            print("No transactions found in the gives data range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print (filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: LKR{total_income:.2f}")
            print(f"Total Expense: LKR{total_expense:.2f}")
            print(f"Net Savings: LKR{(total_income - total_expense):.2f}")


#write a function that will call these functions in the oreder that we want in oreder to collect our data
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

#if i want to plot it and want to see it on a graph --> use MATPLOTLIB
def plot_transactions(df):
    df.set_index('date', inplace=True)

    income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value=0)

    expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value=0)

#create a plot using matplotlib
    plt.figure(figsize=(10, 5)) #figure -->  setting up the screen/ canvas
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title('Income and Expenses Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

# Test the initialization
# if __name__ == "__main__":
#   print("Current Working Directory:", os.getcwd())
#   CSV.initialize_csv()
#   CSV.add_entry("03-11-2024",5000, "Income", "Interest")

#CSV.get_transactions("01-01-2024", "30-12-2024")
#add()

def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summery within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot (y/n)").lower == "y": 
                plot_transactions(df)
        elif choice == "3":
            print("Existing...")
            break
        else:
            print("Invalid choice.. Enter 1, 2 or 3")

if __name__ == "__main__":
    main()