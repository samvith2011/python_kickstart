import requests

from bs4 import BeautifulSoup
query = input("What is your search query for apple music? ")
query2 = query.replace(" ","%20")
response = requests.get(f"https://music.apple.com/us/search?term={query2}")




