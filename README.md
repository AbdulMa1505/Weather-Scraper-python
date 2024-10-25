## Weather Scraper
- This Python project scrapes the weather information for a given city using Google's search results. It uses the requests library to fetch the page and BeautifulSoup from the bs4 package to parse the HTML.
# Features
- Fetches real-time weather updates for a given city.
- Uses web scraping with BeautifulSoup to extract the information.
- Simple and easy-to-use implementation.
# Prerequisites
- Python 3.x
- requests library
- beautifulsoup4 library
# Notes
- Make sure that you have an active internet connection when running this script, as it fetches real-time data from Google search results.
- Web scraping might be against the terms of service of certain websites, so be careful not to abuse it.
# Troubleshooting
- If you get a ModuleNotFoundError for bs4, ensure it's installed by running:pip install beautifulsoup4
- If you encounter an issue with escape characters (\), ensure that the URL strings are properly formatted