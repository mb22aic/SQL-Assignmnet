# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 02:14:30 2023

@author: manoj
"""
import numpy as np
import pandas as pd
import random
import string
from datetime import datetime, timedelta


# Number of samples
n = 1000


# Nominal data: customer ids Generate 1000 random unique ID values
CustomerID = random.sample(range(50000, 90000), n)

# List of BranchID

BranchID = ["A55", "A66", "B11", "H65", "E99"]
Branch_data = {
    "BranchID": ["A55", "A66", "B11", "H65", "E99"],
    "Branch City": ["Springfield", "Rivertown", "Lakeside", "Mountainview", "Seaville"],
    "Branch Address": [
        "123 Main St, Springfield, IL 62701",
        "456 Elm St, Rivertown, CA 90210",
        "789 Oak St, Lakeside, TX 75001",
        "101 Pine St, Mountainview, AZ 85001",
        "202 Cedar St, Seaville, FL 33101",
    ],
    "Branch PostCode": ["IL 62701", "CA 90210", "TX 75001", "AZ 85001", "FL 33101"],
}

Account_Type = ["Debit", "Credit"]

# Ordinal Data: Generate 1000 random address_ids
BranchID = [random.choice(BranchID) for i in range(n)]

# Nominal data: Account_Number Generate 1000 random unique ID values
Account_Number = random.sample(range(10000, 40000), n)

# Function to generate a random LoanID
def generate_LoanID(length=8):
    # Pool of characters to choose from (letters and digits)
    characters = string.ascii_uppercase + string.digits
    LoanID = "".join(random.choice(characters) for _ in range(length))
    return LoanID


# Nominal Data: Generate 100 random policy numbers
LoanID = [generate_LoanID() for _ in range(n)]


# Interval data: Age of construction
Account_Open_Year = np.random.randint(2000, 2023, n)
Account_Open_month = np.random.randint(1, 13, n)
Account_Open_day = np.random.randint(1, 29, n)
Account_Open_Date = [
    f"{Account_Open_Year[i]}-{str(Account_Open_month[i]).zfill(2)}-"
    f"{str(Account_Open_day[i]).zfill(2)}"
    for i in range(n)
]

# Generating random account type
Account_Type = [random.choice(Account_Type) for i in range(n)]

# Ratio data: Price of the house
Account_Balance = np.random.lognormal(mean=9, sigma=0.7, size=n).astype(int)

# Create DataFrame
df_account = pd.DataFrame(
    {
        "Account_Number": Account_Number,
        "CustomerID": CustomerID,
        "BranchID": BranchID,
        "LoanID": LoanID,
        "Account_Open_Date": Account_Open_Date,
        "Account_Type": Account_Type,
        "Account_Balance": Account_Balance,
    }
)

# Account table index
df_account.set_index("Account_Number")

# Save the Account DataFrame to a CSV file with the specified file path
df_account.to_csv(
    r"C:\Users\manoj\OneDrive\Documents\SQL Assigment - Manoj\Account_table.csv",
    index=False,
)

# Save the Branch DataFrame to a CSV file with the specified file path

df_branch = pd.DataFrame(Branch_data)

# Save the DataFrame to a CSV file with the specified file path
df_branch.to_csv(
    r"C:\Users\manoj\OneDrive\Documents\SQL Assigment - Manoj\Branch_table.csv",
    index=False,
)


# List of first names and last names
first_names = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emma",
    "Frank",
    "Grace",
    "Henry",
    "Ivy",
    "Jack",
]
last_names = [
    "Smith",
    "Johnson",
    "Brown",
    "Lee",
    "Garcia",
    "Davis",
    "Martinez",
    "Jackson",
    "Lopez",
    "Hill",
]


# Nominal Data: Generate 1000 random names
random_names = [
    random.choice(first_names) + " " + random.choice(last_names) for i in range(n)
]

# Ratio Data: Generate 100 random ages between 18 and 65
random_ages = [random.randint(18, 65) for _ in range(n)]

# Nominal Data: Function to generate a random phone number
def generate_phone_number():
    # Generate a random 10-digit phone number
    phone_number = "07"  # Country code (assuming it's the United States)
    phone_number += "".join(
        random.choices("0123456789", k=8)
    )  # Generate 9 random digits
    return phone_number


# Generate 10 random phone numbers
num_phone_numbers = n
phone_numbers = [generate_phone_number() for _ in range(num_phone_numbers)]

# List of gender options
genders = ["Male", "Female", "Other", "Prefer not to say"]

# Nominal Data: Generate 10 random gender values
random_genders = [random.choice(genders) for _ in range(n)]

# Interval data: Age of construction
DOB_Year = np.random.randint(1950, 2015, n)
DOB_month = np.random.randint(1, 13, n)
DOB_day = np.random.randint(1, 29, n)
DOB = [
    f"{DOB_Year[i]}-{str(DOB_month[i]).zfill(2)}-" f"{str(DOB_day[i]).zfill(2)}"
    for i in range(n)
]

# Create DataFrame
df_customer = pd.DataFrame(
    {
        "CustomerID": CustomerID,
        "Customer_Name": random_names,
        "Age": random_ages,
        "Phone_Number": phone_numbers,
        "Gender": random_genders,
        "DOB": DOB,
    }
)

# Save the DataFrame to a CSV file with the specified file path
df_customer.to_csv(
    r"C:\Users\manoj\OneDrive\Documents\SQL Assigment - Manoj\Customer_table.csv",
    index=False,
)

# Ratio data: Price of the house
Loan_Amount = np.random.lognormal(mean=9, sigma=1, size=n).astype(int)

# Create DataFrame
df_Loan = pd.DataFrame(
    {"LoanID": LoanID, "CustomerID": CustomerID, "Loan_Amount": Loan_Amount}
)

# Save the DataFrame to a CSV file with the specified file path
df_Loan.to_csv(
    r"C:\Users\manoj\OneDrive\Documents\SQL Assigment - Manoj\Loan_table.csv",
    index=False,
)
