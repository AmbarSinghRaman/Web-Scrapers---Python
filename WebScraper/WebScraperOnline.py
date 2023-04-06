# Web scraper - This will find the data needed but it will only find it once!
from bs4 import BeautifulSoup
import requests
import time

unfamiliar_skill = input('Enter any unfamiliar skill related to the subject:\n>>> ')
print(f'Filltering out {unfamiliar_skill} from findings....')
time.sleep(0.25)

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    job_published_date = job.find('span', class_='sim-posted').text.replace('  ', '')

    if 'few' in job_published_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace('  ', '')
        skill_requirenments = job.find('span', class_='srp-skills').text.replace('  ', '')
        more_info = job.header.h2.a['href']
        
        if unfamiliar_skill not in skill_requirenments:
            print(f'\nCompany Name:  {company_name.strip()}\nSkills Requirenments:  {skill_requirenments.strip()}')
            print(f'\nMore Info:  {more_info}')
            print(f'\nTime Published:  {job_published_date.strip()}')
            print('\n#---------------------------------------------------------------------------------------------#\n')
