import requests
from bs4 import BeautifulSoup
import re
page = requests.get("http://ozolniekolicija-guo")
soup = BeautifulSoup(page.text, "html.parser")
soup.find(class_="contact_table")
s = soup.find_all("td")
s_str = ''.join(map(str,s))
tlf = re.findall(r'\d{8}',(s_str))
for t in tlf:
  print(t)