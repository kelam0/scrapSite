
# open a website using your default browser: can be a sharepoint or just google
import webbrowser
webbrowser.open('http://www.google.com/')

###################################################

# download a text file or csv from a website
import requests
res = requests.get('http://www.emmi-benchmarks.eu/assets/modules/rateisblue/file_processing/publication/processed/hist_EURIBOR_2016.csv')
# check for error in pull
try:
    res.raise_for_status()
    print(type(res))
except Exception as exc:
    print('There was a problem: %s' % (exc))

print(res.text[:250])

# save result as txt format in chunks of 100000 bytes.
playFile = open('SavedFixing.txt', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)

playFile.close()

###################################################


#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com'              # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
         print('Could not find comic image.')
    else:
         try:
             comicUrl = 'http:' + comicElem[0].get('src')
             # Download the image.
             print('Downloading image %s...' % (comicUrl))
             res = requests.get(comicUrl)
             res.raise_for_status()
         except requests.exceptions.MissingSchema:
             # skip this comic
             prevLink = soup.select('a[rel="prev"]')[0]
             url = 'http://xkcd.com' + prevLink.get('href')
             continue
         
        # Save the image to ./xkcd.
         imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
         for chunk in res.iter_content(100000):
             imageFile.write(chunk)
         imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')


###################################################


# scrape daily London precious metal fixing
import os, requests, bs4

url = 'http://www.kitco.com/gold.londonfix.html'
os.makedirs('.\\PreMetal', exist_ok=True)

#create csv that will contail all the data for the year

res = requests.get(url)
res.raise_for_status()

resSoup = bs4.BeautifulSoup(res.text)
print(type(resSoup))

table = resSoup.find('table', attrs = {'align':"center", 'border':"0", 'cellpadding':"4", 'cellspacing':"1", 'width':"100%"})
table_rows = table.find_all('tr')

for row in table_rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    if len([ele for ele in cols if ele]) > 0:
        print([ele for ele in cols if ele])


###################################################


# selenium package to control a browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
type(browser)

browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
type(linkElem)
linkElem.click() # follows the "Read It Online" link

browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my_real_email')
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('12345')
passwordElem.submit()

browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)     # scrolls to bottom
htmlElem.send_keys(Keys.HOME)    # scrolls to top

browser.back()
browser.forward()
browser.refresh()
browser.quit()
