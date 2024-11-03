#this is a place where i can write all of the functions related to getting information from the user
from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

#prompt --> is what going to ask the user to input before they give us the date
#allow_default=False -->  tells us if we should have a default value of today's date
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format) #fromat to specify, the way we want to get the date
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format) # clean up the date that the user type in and gives it to the user in format that the user needs
    except ValueError:
        print("Invalid date format.. Please enter the date in DD-MM-YYYY format")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value...")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
    
def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense):").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print ("Invalid category... Please enter 'I' for Income or 'E' for Expense")
    return get_category()

def get_description():
    return input("Enter a description (optional): ")