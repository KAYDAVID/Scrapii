# scrape.py

import os
import requests

from BeautifulSoup import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

import logging;
logging.basicConfig()

sch = BlockingScheduler()

def main():
    url = 'https://www.indeed.com/jobs?q=software+developer&l=Barrington%2C+IL'
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    matches = soup.findAll(name = 'div', attrs={'class': 'title'})

    #for match in matches:
    #    print match.text

    for jobTitle in matches:
        if "Entry" in jobTitle.text:
            os.system("osascript /Users/davidkay/Desktop/Python/sentMessage.scpt +18477910357 'Job' ")
            break
        elif "Jr" in jobTitle.text:
            os.system("osascript /Users/davidkay/Desktop/Python/sentMessage.scpt +18477910357 'Job2' ")
            break
    return;

sch.add_job(main, 'interval', seconds=3)
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
try:
    sch.start()
except (KeyboardInterrupt, SystemExit):
    pass
main()
