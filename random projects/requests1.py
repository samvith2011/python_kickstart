import requests as r
#Work in progress
site = r.get("https://www.youtube.com/")

print(site.text.count("67"))