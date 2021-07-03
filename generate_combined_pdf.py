import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import shutil as sh 
from pathlib import Path
import os 
import wget
from merge_pdf import merge_pdf
from multiprocessing.pool import ThreadPool
import requests
from parfive import Downloader


#scrape all the pdfs on a webpage 
url = 'https://openaccess.thecvf.com/CVPR2021?day=all'
http = httplib2.Http()
response, content = http.request(url)

links=[]
for link in BeautifulSoup(content).find_all('a', href=True):
    #print("appending link")
    links.append(link['href'])


#check if the link is a pdf 
def is_link_pdf(link):
    if link[-3:]=="pdf":
        return True 
    return False 

pdf_links = []
for link in links:
    if is_link_pdf(link):
        pdf_links.append(link)

pdf_links = sorted(pdf_links)
print("total pdf links",len(pdf_links))
#print(pdf_links)

#next some directory management 
local_data_path = Path('.').absolute()
pdf_path = local_data_path/'pdf_artifacts'
if os.path.exists(str(pdf_path)):
    sh.rmtree(str(pdf_path))

local_data_path.mkdir(exist_ok=True)
pdf_path.mkdir(exist_ok=True)


dl = Downloader()
for link in pdf_links:
    file_name = link.split('/')[-1]
    save_path = pdf_path/file_name
    print("save+path",str(save_path))
    dl.enqueue_file("https://openaccess.thecvf.com/"+link, path = str(save_path))
print("done")
files = dl.download()
