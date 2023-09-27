# Web-Scraping-Treasury-Auctions

This code is a Python script that performs web scraping to collect data about treasury auctions from the U.S. Department of the Treasury's website, specifically from the URL provided. The script collects data from PDF files, extracts relevant information, and then performs some data analysis before exporting the results to a CSV file.

Here's a breakdown of what the code does step by step:

1. Import Necessary Libraries:
- requests: Used to make HTTP requests to access web pages.
- re: Regular expressions library for pattern matching.
- pdfplumber: A library for extracting text and data from PDF files.
- pandas: A data manipulation library.
- datetime: For working with dates and times.
- BytesIO: A class from the io module for reading binary data as a file-like object.

2. Define Lists to Store Data:
- dates, terms, and amounts are empty lists that will be used to store the extracted data.
  
3. Set the Start and End Dates:
- start_date and end_date represent the time period for which the script will collect data (in this case, the entire year 2022).

4. Define the URL:
- URL is the base URL for the U.S. Department of the Treasury's auction announcements.

5. Initialize a Loop Over Dates:
- The script uses a loop to iterate through dates from start_date to end_date. For each date, it constructs a URL for that specific month and year.

6. Fetch and Process PDF Files:
- Within the loop, it sends an HTTP GET request to the constructed URL to retrieve the page's content.
- It uses a regular expression (re.findall) to extract filenames of PDF files from the page.
- For each filename, it constructs the PDF URL and fetches the PDF content.
- It then uses pdfplumber to extract text from each page of the PDF.
- Regular expressions are again used to extract specific information like issue date, term, and total offering amount from the text.
- Extracted data is appended to the corresponding lists (dates, terms, and amounts).

7. Create a DataFrame:
- After collecting data for all dates, it creates a Pandas DataFrame with columns 'Date', 'Term', and 'Amount' using the collected data.

8. Print the DataFrame:
- It prints the first few rows of the DataFrame to the console using df.head().

9. Data Analysis and Export:
- The script attempts to create a plot of the DataFrame (it references a non-existent 'Ratio' column, which may be an error).
- It calculates the mean of the 'Ratio' column grouped by 'Security' (there's no 'Security' column in the DataFrame).
- Finally, it exports the DataFrame to a CSV file named 'auction_data.csv' without an index column.
