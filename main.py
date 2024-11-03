# MATPLOTLIB --> allow us to plot and see the graph 
# PANDAS --> allow us to easily categorized & search for data within the csp file

import pandas as pd
import csv
from datetime import datetime
import os
from data_entry import get_date, get_amount, get_category, get_description

class CSV:
    # CSV_FILE --> variable, finance_data -->  name of file that we work with 
    CSV_FILE = "E:/python/finance_tracker/finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    
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

#write a function that will call these functions in the oreder that we want in oreder to collect our data
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

# Test the initialization
# if __name__ == "__main__":
#   print("Current Working Directory:", os.getcwd())
#   CSV.initialize_csv()
#   CSV.add_entry("03-11-2024",5000, "Income", "Interest")

add()