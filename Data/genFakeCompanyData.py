#!/usr/bin/env python3

import random
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of records you want to generate
num_records = 1000

# Define possible values for Series and Company-Type
series_values = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zulu']
company_types = ['Mid-Level', 'Start-Up', 'Enterprise']

# Initialize lists to store the data
company_ids = []
country_codes = []
series_list = []
company_types_list = []
order_values = []

# Generate the data
for _ in range(num_records):
    company_ids.append(fake.unique.uuid4())
    country_codes.append(fake.country_code())
    series_list.append(random.choice(series_values))
    company_types_list.append(random.choice(company_types))
    order_values.append(round(random.uniform(1000, 1000000), 2))  # Random order value between 1000 and 1,000,000

# Create a DataFrame
df = pd.DataFrame({
    'Company-ID': company_ids,
    'Country Code': country_codes,
    'Series': series_list,
    'Company-Type': company_types_list,
    'Order-Value': order_values
})

# Save to a CSV file (optional)
df.to_csv('fake_data.csv', index=False)

# Display the first few records
print(df.head())
