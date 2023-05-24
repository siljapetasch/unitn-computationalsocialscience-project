import csv
import re

# Open the text file and read the data
with open('pre_war_2.txt', 'r') as file:
    data = file.read()

# Split the data into articles
articles = data.split('End of Document')

csv_data = []

# Loop through each article
for article in articles:
    # Check if article is not empty
    if article.strip() != '':
        # Split the article into lines
        lines = article.strip().split('\n')

        title = lines[0]
        source = lines[1]
        
        # Extract date using regex
        match_date = re.search(r'\d{1,2}\.\s*(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s*\d{4}', lines[2])
        date = match_date.group() if match_date else ''

        # Extract length using regex
        match_length = re.search(r'Length:\s*(\d+)', article)
        length = match_length.group(1) if match_length else ''

        # Find the index of the line where the 'Body' starts
        body_start_index = lines.index('Body') + 2  # Add 2 because the body starts after two lines

        # Extract body content
        body_lines = []
        for line in lines[body_start_index:]:
            if line.strip() not in ['Weblink:', 'Graphic', 'Load-Date:', 'Original Gesamtseiten-PDF']:
                body_lines.append(line)
            else:
                break
        body = ' '.join(body_lines)
        
        csv_data.append({
            'Title': title,
            'Source': source,
            'Date': date,
            'Length': length,
            'Body': body,
        })

# Write data to CSV
with open('pre_war_2.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Source', 'Date', 'Length', 'Body']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in csv_data:
        writer.writerow(row)

print("Data has been written to 'articles.csv'.")
