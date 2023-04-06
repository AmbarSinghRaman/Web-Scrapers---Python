# Web scraper = This will show data from a local html file!
from bs4 import BeautifulSoup

with open ('C:/Users/jraman/PythonProjects/WebScraperCalculatorConverter/basics/home.html', 'r') as html_file:
    content_html_file = html_file.read()
    
    soup = BeautifulSoup(content_html_file, 'lxml')
    courses_cards = soup.find_all('div', class_='card')
    
    for course in courses_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'\nCourse: {course_name} Price: {course_price}\n')
