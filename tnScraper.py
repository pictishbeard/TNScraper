# from bs4 import BeautifulSoup
# import requests

# url='https://www.airbnb.co.uk/rooms/50633275?source_impression_id=p3_1636295285_%2FbxfUUr%2BHs5Da6w9&guests=1&adults=1'
# req=requests.get(url)
# content=req.text

# soup=BeautifulSoup(content)

# raw=soup.findAll('')

# print(content)

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import requests
# import json

# data = []
# for page in range(1):
#     url = "https://www.airbnb.co.uk/rooms/50633275?source_impression_id=p3_1636295285_%2FbxfUUr%2BHs5Da6w9&guests=1&adults=1".format(page)
#     # html = urlopen(url)
#     req=requests.get(url)
#     soup = BeautifulSoup(req, "html.parser")
#     Container = soup.find_all("div", {"class": "_1gw6tte"})
#     for i in Container:
#         entry = {'property type': i.find("a", {"class": "_b8stb0"}).get_text(),
#                  'amenities': i.find("div", {"class": "_1ynbv25"}).get_text()}
#         data.append(entry)
#         # TODO Add more attributes


# print(json.dumps(data))

import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

all_jobs = []

for page in range(1):

    url = "https://www.airbnb.co.uk/rooms/50633275={}".format(page)
    html = urlopen(url)
    request = urllib.request.Request(url, headers={'User-Agent': '*'}) 
    urllib.request.urlopen(request).read()
    soup = BeautifulSoup(html,"html.parser")
    Container = soup.find_all("div", {"class":"_1gw6tte"})
    for i in Container:
        try:
            propertyTitle = i.find("span", {"class":"_b8stb0"}).get_text() # .get_text(strip=True)
            propertyofType = i.find("div", {"class":"_xcsyj0"}).get_text()
            propertyDetails = i.find("ol",{"class":"_194e2vt2"}).get_text()
            propertyAmenities = i.find("div",{"class":"_1byskwn"}).get_text()

            print(propertyTitle, propertyofType, propertyDetails, propertyAmenities)

            job_dict = {}
            job_dict['Property Title'] = propertyTitle
            job_dict['Property Type'] = propertyofType
            job_dict['Property Details'] = propertyDetails
            job_dict['Propert Amenities'] = propertyAmenities


            all_jobs.append(job_dict)

        except AttributeError as ex:
            print('Error:', ex)

# --- after loop ---

f = open('output.json', 'w')
f.write(json.dumps(all_jobs, ident=2))
f.close()