import requests as r
#Fixed
site = r.get("https://www.youtube.com/")

print(site.text.count("youtube"))