# gspread-parser
Python script that parses web information and saves it to a google sheet. 
Requires a google service account and set-up to run properly. Download the files and drag into the set up project folder to use.

# Usage

The script consists of three main parts: the web scraper, analyzer, and the spreadsheet.

## Web Scraper
For this project, I decided to scrape data from the website ge-tracker.com. The website provides real-time price information for items in the game Old School Runescape. 
![image](https://user-images.githubusercontent.com/53792798/130473015-a70bb608-efbf-4846-83f4-697c561e65e7.png)

The important information extracted is 'current price', 'buying quantity' and 'selling quantity'. This data is extracted from the html elements in the webpage using BeautifulSoup.

## Analyzer

The analyzer looks at converting the data into a google spreadsheet using Pandas and Pandas DataFrame. The spreadsheet contains all the data extracted with the date/time of extraction. The main calculation done is to look at data that was collected beyond a certain date and take the average of that by day. 

## Spreadsheet

The spreadsheet uses auto-formatting and auto color-coding. Price increases/decreases are color-coded as well as historical-highs and lows. It also provides information such as change over 1 day, 7 days, 1 month as well as variance in the data. 
![image](https://user-images.githubusercontent.com/53792798/130474989-71a26fa7-3787-408b-9a06-62d1bb2714ca.png)


# Future Ideas

1. Using the GE-tracker API or the official exchange API to retrieve the data much faster and more reliably. 
2. Having a way to automatically run the script at set time intervals. 
3. Potentially using bots to look at the data and make favourable trades/exchanges.


