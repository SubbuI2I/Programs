# Program - 2
""" 
Here is an another usecase case for developing a program that can analyze their property data and generate reports. The company has data for all the properties they manage, including the property type, location, price, number of bedrooms and bathrooms, and square footage.
The program should be able to do the following:
Read the property data from a CSV file.
Calculate the average price and square footage of properties in each location.
Calculate the average number of bedrooms and bathrooms for each property type.
Generate a report that summarizes the data for each location and property type.
The report should include the following information:
The location and property type.
The average price and square footage.
The average number of bedrooms and bathrooms.
The report should be saved to a PDF file.
To complete this task, you will need to use Python libraries such as pandas for data manipulation, NumPy for numerical computations, and reportlab for generating PDF files. You will also need to have a good understanding of Python's file I/O operations and data structures.
"""

import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

data = pd.read_csv('samplecsvformat.csv')
#print(data)

# region commented
# filtered_data = data.loc[data['location']=='London']
# data = data.sort_values(['location'], ascending=True)

# avg_price_filtered_data = data.groupby('location')['price'].mean()
# print(avg_price_filtered_data)

# location_groups = data.groupby(['location'])
# for loc, group in location_groups:
#     print(f"Location: {loc}")
# print(f"type: {type}")
# avg_bedrooms_filtered_data = group.groupby('property_type')['num_bedrooms'].mean()
# print(avg_bedrooms_filtered_data)
# avg_bathrooms_filtered_data = group.groupby('property_type')['num_bathrooms'].mean()
# print(avg_bathrooms_filtered_data)
# avg_price_filtered_data = group.groupby('property_type')['price'].mean()
# print(avg_price_filtered_data)
# avg_sqfoot_filtered_data = group.groupby('property_type')['sq_footage'].mean()
# print(avg_sqfoot_filtered_data)

# filtered_data = filtered_data.groupby('property_type')
# for Property_Type, group in filtered_data:
#     print(f"Property Type: {Property_Type}")
#     print (group)

# grouped_data = data.groupby(['location','property_type']).agg({'price':'mean', 'sq_footage':'mean','num_bedrooms':'mean','num_bathrooms':'mean'})
# print(grouped_data)
# endregion commented


pdf = canvas.Canvas('report.pdf', pagesize=(600, 800), bottomup=100)
# print(pdf.getAvailableFonts())
pdf.setFont('Courier-Bold', 12)
pdf.drawAlignedString(450, 780, 'PDF Report for Property Data')

# average price, square footage by location
pdf.drawAlignedString(120, 720, 'Avg Price, Sq. Footage by Location')
avg_price_loc = data.groupby('location')[['price', 'sq_footage']].mean().reset_index()
#print(avg_price_loc)
avg_price_loc = avg_price_loc.rename(
    columns={
     'location':'Location',
    'price': 'Avg Price',
    'sq_footage': 'Avg Sq.ft',
    'num_bathrooms': 'Avg Bathrooms'
    })
tbl_data = [list(avg_price_loc)] + avg_price_loc.values.tolist()
#print(tbl_data)
table = Table(tbl_data)
pdf.setFont('Courier', 12)
table.wrapOn(pdf, 0, 0)
table.drawOn(pdf, 20, 600)

# average bed rooms, bath rooms by property type
pdf.setFont('Courier-Bold', 12)
pdf.drawAlignedString(310, 550, 'Avg Bedrooms, Bathrooms by Property Type')
avg_rooms_prop = data.groupby('property_type').agg(
    {'num_bedrooms': 'mean', 'num_bathrooms': 'mean'}).reset_index()
avg_rooms_prop = avg_rooms_prop.rename(
    columns={
    'location':'Location',
    'property_type':'Property Type',
    'price': 'Avg Price',
    'sq_footage': 'Avg Sq.ft',
    'num_bedrooms': 'Avg Bedrooms',
    'num_bathrooms': 'Avg Bathrooms'
    })
tbl_data = [list(avg_rooms_prop)] + avg_rooms_prop.values.tolist()
#print(avg_rooms_prop)
table = Table(tbl_data)
pdf.setFont('Courier', 12)
table.wrapOn(pdf, 0, 0)
table.drawOn(pdf, 20, 450)

# average summary report by each location and property type
avg_loc_prop = data.groupby(['location', 'property_type']).agg(
    {
        'price': 'mean',
        'sq_footage': 'mean',
        'num_bedrooms': 'mean',
        'num_bathrooms': 'mean'
    }).reset_index()
avg_loc_prop = avg_loc_prop.rename(
    columns = {
    'location':'Location',
    'property_type':'Property Type',
    'price': 'Avg Price',
    'sq_footage': 'Avg Sq.ft',
    'num_bedrooms': 'Avg Bedrooms',
    'num_bathrooms': 'Avg Bathrooms'
})

tbl_data = [list(avg_loc_prop)] + avg_loc_prop.values.tolist()
table = Table(tbl_data)
pdf.showPage()
pdf.setFont('Courier-Bold', 12)
pdf.drawAlignedString(450, 750, 'Summary Report for Location and Property Type')
pdf.setFont('Courier', 12)
table.wrap(0, 0)
table.drawOn(pdf, 50, 500)
pdf.save()
