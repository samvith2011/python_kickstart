import requests as r
#Work in progress
site = requests.get("https://www.youtube.com/")

print(site.text.count("youtube"))