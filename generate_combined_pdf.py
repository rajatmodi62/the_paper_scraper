import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import shutil as sh 
from pathlib import Path
import os 
import wget
from merge_pdf import merge_pdf
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

print(pdf_links[0].split('/')[-1])
print("going for downloading")

# print(pdf_links)
for pdf_no, link in enumerate(pdf_links):
    #extract the pdf_links from the list 
    print("trying.....",pdf_no,"out of",len(pdf_links))
    file_name = link.split('/')[-1]
    save_path = pdf_path/file_name
    wget.download("https://openaccess.thecvf.com/"+link, str(save_path))
    print("downloaded",pdf_no,"out of",len(pdf_links))

merge_pdf()