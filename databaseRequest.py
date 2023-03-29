import requests

# Set the URL of the ASP.NET Web Forms page
url = "https://www.adventistdirectory.org/SearchResults.aspx/default.aspx"

# Set the form data for the postback
form_data = {
    "_ctl0:SearchType": "radSearchNameOnly",
    "_ctl0:ctlSelectAdmField:ddlDivision": "NAD"
}

# Send the postback request
response = requests.post(url, data=form_data)

# Print the response content
print(response.content)
