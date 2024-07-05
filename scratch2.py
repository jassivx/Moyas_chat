import nltk
import numpy as np
import self
import sklearn
import pandas as pd

df = pd.read_csv('C:\\Users\\AKASH VISHWAKARMA\\Documents\\NLP Dataset\\NLPsample.csv')

from datagovindia import DataGovIndia

from datagovindia import DataGovIndia

# Replace with your actual API key (obtained from DataGovIndia)
YOUR_API_KEY = "579b464db66ec23bdd0000013ba19f6fc1d944eb73563fada397bb6c"

# Create a DataGovIndia object with your API key
datagovin = DataGovIndia(YOUR_API_KEY)

# Use methods provided by datagovindia to fetch data
# Refer to the library's documentation for specific methods and arguments

print(dir(DataGovIndia))
print(DataGovIndia.validate_api_key)

data = datagovin.get_data("579b464db66ec23bdd0000013ba19f6fc1d944eb73563fada397bb6c")
print(f'Number of records in table: {len(data)}')
data.head(5)

try:
    limit = self.get_resource_info(resource_id).get("total")
except KeyError as e:
    print(f"KeyError: {e} occurred. Response: {response}")
    limit = None  # Or handle this case appropriately

'''


datagovin.search_by_title('PIN CODE')


# Example: Search for datasets by keyword
keyword = "agriculture"
datasets = datagovin.search(q=keyword)

# Process the retrieved datasets
for dataset in datasets:
  print(dataset["title"])  # Access dataset title (may vary based on library structure)

# You can explore other methods for filtering, retrieving details, etc.
# based on the library's capabilities`
'''