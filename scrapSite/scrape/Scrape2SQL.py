import ast, sys, datetime
import urllib2, sqlite3, string
from datetime import timedelta
from BeautifulSoup import BeautifulSoup

######## define cleaning function

def setup_clean_scrape():
    try:                        # clean the table Wavg from the database
        datab = sqlite3.connect('weightedAvg.db')
        cursor = datab.cursor()
        cursor.execute("DROP TABLE IF EXISTS Wavg;")
    except sqlite3.Error, e:    # in case of error loading the SQL database

        print "Error %s:" % e.args[0]
        sys.exit(1)
                                
    finally:                    # close the SQL database
        if datab:
            datab.close()
            
######## define scraping function for specific website

def scrapefct(url,day,ind):
    
    try:
        # in case of lack of data and '-' appears
        errorflag = False   # will insert the index element to have a full data set
        
        # use sqlite3 to create a database
        datab = sqlite3.connect('weightedAvg.db')
        cursor = datab.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS WAvg(id INT, spot_date TEXT, hour TEXT, weighted_avg REAL);")

        # start hour and index for sqlite
        hour = 0
        secondday = day   #YYYY-MM-DD  last
        tempday = secondday[9:10]
        tempday = int(tempday)+1
        if tempday < 10:
            tempday = "0" + str(tempday)
        else:
            tempday = str(tempday)
        secondday = secondday[0:8] + tempday
        index = ind  
        
        # prepare BeautifulSoup to scrape the webpage
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)

        # extract the table and the rows of the table
        tables = soup.findChildren('table')
        rows = tables[0].findChildren(['th','tr'])

        # go through every row and every cell to extract the weighted average
        for row in rows:
            cells = row.findChildren('td')
            counter = 0
            for cell in cells:
                value = cell.string
                counter += 1
                hourgap = string.zfill(hour,2) + " - " + string.zfill(hour+1,2)
                if counter == 6:     #weightedaverage for 1st day
                    try:
                        unicode(value).encode('ascii')
                    except UnicodeEncodeError:
                        errorflag = True
                    if errorflag == False:
                        cursor.execute("INSERT INTO WAvg VALUES(?,?,?,?)", (index, day, hourgap, float(unicode(value))))
                elif counter == 7 and errorflag == True:
                    cursor.execute("INSERT INTO WAvg VALUES(?,?,?,?)", (index, day, hourgap, float(unicode(value))))
                    errorflag = False
                elif counter == 14:  #weightedaverage for 2nd day
                    try:
                        unicode(value).encode('ascii')
                    except UnicodeEncodeError:
                        errorflag = True
                    if errorflag == False:
                        cursor.execute("INSERT INTO WAvg VALUES(?,?,?,?)", (index+24, secondday, hourgap, float(unicode(value))))
                        index += 1
                        hour += 1
                elif counter == 15 and errorflag == True:
                    cursor.execute("INSERT INTO WAvg VALUES(?,?,?,?)", (index+24, secondday, hourgap, float(unicode(value))))
                    index += 1
                    hour += 1
                    errorflag = False
                elif value is None:
                    break
        datab.commit()          # commit the changes done to the SQL database
    
    except sqlite3.Error, e:    # in case of error loading the SQL database

        print "Error %s:" % e.args[0]
        sys.exit(1)
                                
    finally:                    # close the SQL database
        if datab:
            datab.close()

######## define scrape for only 1 day, in the case where the 2nd day is today
def scrapefctalt(url,day,ind):
    
    try:
        # in case of lack of data and '-' appears
        errorflag = False   # will insert the index element to have a full data set
        
        # use sqlite3 to create a database
        datab = sqlite3.connect('weightedAvg.db')
        cursor = datab.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS WAvg(id INT, spot_date TEXT, hour TEXT, weighted_avg REAL);")

        # start hour and index for sqlite
        hour = 0
        index = ind
        
        # prepare BeautifulSoup to scrape the webpage
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)

        # extract the table and the rows of the table
        tables = soup.findChildren('table')
        rows = tables[0].findChildren(['th','tr'])

        # go through every row and every cell to extract the weighted average
        for row in rows:
            cells = row.findChildren('td')
            counter = 0
            for cell in cells:
                value = cell.string
                counter += 1
                hourgap = string.zfill(hour,2) + " - " + string.zfill(hour+1,2)
                if counter == 6:     #weightedaverage for 1st day
                    try:
                        unicode(value).encode('ascii')
                    except UnicodeEncodeError:
                        errorflag = True
                    if errorflag == False:
                        cursor.execute("INSERT INTO WAvg VALUES(?,?,?,?)", (index, day, hourgap, float(unicode(value))))
                        index += 1
                        hour += 1
                elif counter == 7 and errorflag == True:
                    cursor.execute("INSERT INTO WAvg VALUES(?,?,?,?)", (index, day, hourgap, float(unicode(value))))
                    errorflag = False
                    index += 1
                    hour += 1
                elif value is None:
                    break
        datab.commit()          # commit the changes done to the SQL database
    
    except sqlite3.Error, e:    # in case of error loading the SQL database

        print "Error %s:" % e.args[0]
        sys.exit(1)
                                
    finally:                    # close the SQL database
        if datab:
            datab.close()
######## define final day scrape

def scrapefctfinal(url,day,ind):
    
    try:
        # in case of lack of data and '-' appears
        errorflag = False   # will insert the index element to have a full data set
        
        # use sqlite3 to create a database
        datab = sqlite3.connect('weightedAvg.db')
        cursor = datab.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS WAvg(id INT, spot_date TEXT, hour TEXT, weighted_avg REAL);")

        # start hour and index for sqlite
        hour = 0
        index = ind
        
        # prepare BeautifulSoup to scrape the webpage
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)

        # extract the table and the rows of the table
        tables = soup.findChildren('table')
        rows = tables[0].findChildren(['th','tr'])

        # go through every row and every cell to extract the weighted average
        for row in rows:
            cells = row.findChildren('td')
            counter = 0
            for cell in cells:
                value = cell.string
                counter += 1
                hourgap = string.zfill(hour,2) + " - " + string.zfill(hour+1,2)
                if counter == 6:     #weightedaverage for 1st day
                    try:
                        unicode(value).encode('ascii')
                        cursor.execute("INSERT INTO WAvg VALUES(?,?,?,?)", (index, day, hourgap, float(unicode(value))))
                        index += 1
                        hour += 1
                    except UnicodeEncodeError:
                        break
                elif value is None:
                    break
        datab.commit()          # commit the changes done to the SQL database
        return index
    except sqlite3.Error, e:    # in case of error loading the SQL database

        print "Error %s:" % e.args[0]
        sys.exit(1)
                                
    finally:                    # close the SQL database
        if datab:
            datab.close()
            
######## define dbprint function to extract info from database testing purposes only

def dbprint():
    try:
        datab = sqlite3.connect('weightedAvg.db')
        with datab:
            cursor = datab.cursor() 
            cursor.execute("SELECT * FROM WAvg ORDER BY id")

            while True:
                row = cursor.fetchone()    
                if row == None:
                    break
                print row[0],row[1],row[2],"%.2f" %row[3]
                
        datab.close()
        
    except sqlite3.Error, e:    # in case of error loading the SQL database

        print "Error %s:" % e.args[0]
        sys.exit(1)

######## define an html render page to replace the previous page:

def renderScrapeSite():
    html = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>EPEX SPOT Weighted Average rate scraper</title>
        </head>
        <body>
        <h3> EPEX SPOT Weighted Average rate scraper </h3>
        <p>
        <input type="submit" value="Repopulate database" name="scrapeOrder" />
        <input type="submit" value="Clean database" name="cleanDbOrder" />
        <input type="submit" value="Update database" name="updateDbOrder" />
        <input type="submit" value="Go live" name="liveScrapeOrder" />
        </p>
        <table border = "1">
        <tr>
            <th> Date </th>
            <th> Hours </th>
            <th> Weighted Average </th>
        </tr>
        """
    datab = sqlite3.connect('weightedAvg.db')
    with datab:
        cursor = datab.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS WAvg(id INT, spot_date TEXT, hour TEXT, weighted_avg REAL);")
        cursor.execute("SELECT * FROM WAvg ORDER BY id")
        while True:
            row = cursor.fetchone()
            if row == None:
                break
        
            html += """
            <tr>
                <td> {r1} </td>
                <td> {r2} </td>
                <td> {r3:2.2f} </td>
            </tr>""".format(r1= row[1], r2 = row[2], r3 = row[3])

        html += """
        </table>
        </body>
        </html>
        """
    datab.close()
    return html
    
########################################################################
######## main function

def main():
######## loop of all necessary websites

    index = 1       # SQLite index for the weightedAvg.db

    #setup starting date
    day = 07
    month = 02
    year = 2013
    scrapingDate = datetime.date(year,month,day)
    datab = None

    setup_clean_scrape()
    tday = datetime.date.today()
    urlbase = "http://www.epexspot.com/en/market-data/intraday/intraday-table/"
    url = urlbase + tday.isoformat() + "/FR"
    index = scrapefctfinal(url,tday.isoformat(),index)
    """
    while scrapingDate < tday:
        urlday = scrapingDate.isoformat()
        urlbase = "http://www.epexspot.com/en/market-data/intraday/intraday-table/"
        url = urlbase + urlday + "/FR"

        print url
        scrapefct(url,urlday,index)

        index += 48 #read 2 days at a time
        scrapingDate = scrapingDate + timedelta(days=2)
        if scrapingDate + timedelta(days=1) >= datetime.date.today():
            scrapefctalt(url,urlday,index)
            index += 24
            index = scrapefctfinal(url,tday.isoformat(),index)
    """    
    dbprint()

####################
