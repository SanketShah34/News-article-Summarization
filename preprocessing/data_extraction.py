import requests
from bs4 import BeautifulSoup

def extract_from_url(input_control):
    input_url = input_control.get()
    resp = requests.get(input_url)  # request for the url and respone stored in resp
    html = resp.text  # gets the source code
    soup = BeautifulSoup(html, 'html.parser')
    source = soup.find_all('p')  # finds all paragraph tags
    return ". ".join([each_p.get_text(strip=True) for each_p in source])

def extract_from_textbox(input_control):
    return input_control.get("1.0", "end-1c")

def extract_from_browse(input_control):
    filename = input_control.get()
    file_object = open(filename, 'r')
    return file_object.read()