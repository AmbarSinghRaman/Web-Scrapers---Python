# Web scraper - This will show information after certain intervals of time! And create and store data in files!
from bs4 import BeautifulSoup
import requests
import time

unfamiliar_skill = input('Enter any unfamiliar skill related to the subject:\n>>> ')
print(f'Filltering out {unfamiliar_skill} from findings....')
time.sleep(0.25)

def find_jobs_python():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        job_published_date = job.find('span', class_='sim-posted').text.replace('  ', '')

        if 'few' in job_published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace('  ', '')
            skill_requirenments = job.find('span', class_='srp-skills').text.replace('  ', '')
            more_info = job.header.h2.a['href']
            
            if unfamiliar_skill.lower() not in skill_requirenments.lower():
                with open(f'C:/Users/------/-----/------/------/save/{index}.txt', 'w') as write_data:
                    write_data.write(f'\nCompany Name:  {company_name.strip()}\nSkills Requirenments:  {skill_requirenments.strip()}')
                    write_data.write(f'\nMore Info:  {more_info}')
                    write_data.write(f'\nTime Published:  {job_published_date.strip()}')
                    write_data.write('\n#---------------------------------------------------------------------------------------------#\n')
                print(f'File Saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs_python()
        wait_time = 600
        print(f'\nRefershing....\n')
        time.sleep(wait_time)
