#! python3

import bs4, requests
opm = requests.get('https://www.opm.gov/policy-data-oversight/snow-dismissal-procedures/current-status/')
opm.raise_for_status()
#assign the html to the opmPage variable. The 'lxml' is to explicately define the parser. It will work without this, but will give an annoying warning every time to let you know i'ts defaulting ot lxml.
opmPage = bs4.BeautifulSoup(opm.text, 'lxml') 
#extract <h3s> within the StatusContainer element to find the status
opm_status = opmPage.select('.StatusContainer h3') 
#extract date class from within statuscontainer class to find the date the status applies to
opm_date = opmPage.select('.StatusContainer .Date')
#concat the two things you scraped
output = (opm_status + opm_date)
print(output[0].get_text())
print(output[1].get_text())
