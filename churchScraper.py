import requests
from bs4 import BeautifulSoup
import re
import csv

for i in range(300):

    print(i)

    # Send a GET request to the Google search URL
    url = 'https://www.adventistdirectory.org/SearchResults.aspx?&EntityType=C&AdmFieldID=NAD&SortBy=0&PageIndex=' + \
        str(i)
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # print(soup)

    # Extract the search results
    search_results = soup.find_all('a', href=re.compile(r'EntityID=\d+'))

    # Loop through the search results and extract the information you need
    # for result in search_results:
    # Extract the title and URL of the search result
    # print(result.text)

    # Open the output file
    with open("nadChurches.csv", "a", newline="") as f:
        writer = csv.writer(f)

        # Initialize the variables
        odd_line = ""
        counter = 0

        # Loop through each line of the input
        for result in search_results:
            # If the counter is odd, the current line is the second column of a row
            # print(result.text)
            if counter % 2 == 1:
                writer.writerow([odd_line, result.text.strip()])

            # If the counter is even, the current line is the first column of a row
            else:
                odd_line = result.text.strip()

            # Increment the counter
            counter += 1
