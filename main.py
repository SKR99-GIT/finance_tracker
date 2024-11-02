# MATPLOTLIB --> allow us to plot and see the graph 
# PANDAS --> allow us to easily categorized & search for data within the csp file

import pandas as pd
import csv
from datetime import datetime
import os

class CSV:
    # CSV_FILE --> variable, finance_data -->  name of file that we work with 
    CSV_FILE = "E:/python/finance_tracker/finance_data.csv"
    
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
            df = pd.DataFrame(columns=["date", "amount", "category", "description"])
            #dataframe --> object within pandas that allows us to access different rows, columns from a csv file

            #export the dataframe to a csv file
            df.to_csv(cls.CSV_FILE, index=False)
            print("CSV file created.")

# Test the initialization
if __name__ == "__main__":
    print("Current Working Directory:", os.getcwd())
    CSV.initialize_csv()