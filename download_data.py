import pandas as pd
import pprint

# Load spreadsheet
xl = pd.ExcelFile('./data.xlsx')

# Load a sheet into a DataFrame by its name
df = xl.parse('Sheet1')
df = df.fillna('None')

# Create a dictionary for prerequisites
prereq_dict = df.set_index('Name')['Prereq'].str.split(',').to_dict()

# Create a dictionary for units
units_dict = df.set_index('Name')['Units'].to_dict()

type_dict = df.set_index('Name')['Type'].to_dict()

pp = pprint.PrettyPrinter(indent=4)

course_names_list = list(prereq_dict.keys())

depth_dict = df.set_index('Name')['Depth'].to_dict()
# Print the prerequisites dictionary
#pp.pprint(prereq_dict)

# Print the units dictionary
#pp.pprint(units_dict)

#pp.pprint(type_dict)
