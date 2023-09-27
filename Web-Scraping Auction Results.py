import requests
import re
import pdfplumber
import pandas as pd
from datetime import datetime, timedelta
from io import BytesIO

dates = []
terms = []
amounts = []

start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)

URL = 'https://www.treasurydirect.gov/auctions/announcements-data-results/announcement-results-press-releases/' 

current_date = start_date
while current_date <= end_date:
    url = f"{URL}{current_date.year}/{current_date.month:02d}/"

    response = requests.get(url)
    filenames = re.findall(r'R_\d{8}_\d\.pdf"', response.text)

    for filename in filenames:
        pdf_url = url + filename
        response = requests.get(pdf_url)  
        pdf = pdfplumber.open(BytesIO(response.content))

        for page in pdf.pages:
            text = page.extract_text()

            date_match = re.search(r'Issue Date (\w+ \d+, \d+)', text)
            term_match = re.search(r'Term (.*?) Bill', text)
            amount_match = re.search(r'Total Offering Amount \$(\d{1,3}(?:,\d{3})*\d{0,2})', text)

            if date_match and term_match and amount_match:
                date = date_match.group(1)
                term = term_match.group(1)
                amount = amount_match.group(1).replace(',', '')

                dates.append(date)
                terms.append(term)
                amounts.append(amount)

    current_date += timedelta(days=1)

df = pd.DataFrame({'Date': dates, 'Term': terms, 'Amount': amounts})

print(df.head())

df.to_csv('auction_data.csv', index=False)