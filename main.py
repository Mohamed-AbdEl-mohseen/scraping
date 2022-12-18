import csv

import requests
from bs4 import BeautifulSoup

r =requests.get('https://wuzzuf.net/search/jobs/?q=translation&a=hpb')
scr = r.content
soup = BeautifulSoup(scr, "lxml")
# print(scr)
job_titles = soup.find_all("h2", {"class":"css-m604qf"})
# print(job_titles)
company_name = soup.find_all("a", {"class":"css-17s97q8"})
# print(company_name)
locations = soup.find_all("span", {"class":"css-5wys0k"})
# print(locations)
intro = soup.find_all("div", {"class":"css-y4udm8"})
# print(intro)


for i in range(len(job_titles)):
    print(job_titles[i].text, company_name[i].text, locations[i].text, intro[i].text )

