import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


# Define styles
styles = getSampleStyleSheet()
style_title = styles['Title']
style_table = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, 0), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Courier'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])

# Create PDF
pdf_name = 'example.pdf'
doc = SimpleDocTemplate(pdf_name, pagesize=letter, title="PDF Report Summary Average Grouped Data Based on Location & Property Type")
elements = []

# Add title
title = 'Grouped Data'
# elements.append(title)

# # Define a paragraph style
# style = ParagraphStyle(name='Normal', fontSize=12)

# # Create a paragraph with the style
# my_paragraph = Paragraph(title, style)

# Group data by location and property type and calculate averages
# grouped_data = pd.DataFrame(data[1:], columns=data[0]).groupby(['Location', 'Property Type']).agg({'Price': 'mean', 'Sq Ft': 'mean', 'Rooms': 'mean'}).reset_index()


data = pd.read_csv('Program_2_PropertyData.csv')
print(data)

grouped_price = data.groupby('location').agg({'price':'mean'}).reset_index()
avg_price_data = list(grouped_price.columns) + grouped_price.values.tolist()

# Create table and add to elements
avg_price_tbl = Table(avg_price_data)
avg_price_tbl.setStyle(style_table)
elements.append(avg_price_tbl)


# Output title
title = 'PDF Report Summary Average Grouped Data Based on Location & Property Type'
# elements.append(title)

grouped_data = data.groupby(['location', 'property_type']).agg(
    {'price': 'mean', 'sq_footage': 'mean', 'num_bedrooms': 'mean', 'num_bathrooms': 'mean'}).reset_index()
grouped_data = grouped_data.rename(
    columns={'location': 'Location',
             'property_type': 'Property Type', 'price': 'Avg Price',
             'sq_footage': 'Avg Sqft', 'num_bedrooms': 'Avg Bedrooms',
             'num_bathrooms': 'Avg Bathrooms'})
print(grouped_data)

# Convert data to list of lists for table
table_data = [list(grouped_data.columns)] + grouped_data.values.tolist()
print(table_data)
# Create table and add to elements
table = Table(table_data)
table.setStyle(style_table)
elements.append(table)

# Build PDF
doc.build(elements)
