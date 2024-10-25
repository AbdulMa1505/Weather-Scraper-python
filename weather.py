import requests
import sys
sys.path.append('C:\\Users\\Abdul Malik\\AppData\\Roaming\\Python\\Python312\\site-packages')

from bs4 import BeautifulSoup
def get_weather(city):
    city=input("enter the name of the city\n")
    search =f"weather in {city}"
    try:
        url =f"https://www.google.com/search?&q={search}"
        r=requests.get(url)
        s=BeautifulSoup(r.text,"html.parser")
        update=s.find("div",class_="BNeawe").text
        print(f"Weather in {city}: {update}")
    except requests.exceptions.RequestException  as e:
        print(f"An error occurred while fetching weather data: {e}")

if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    get_weather(city)
