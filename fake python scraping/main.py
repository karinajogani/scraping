from bs4 import BeautifulSoup
import requests
import json

url = 'https://realpython.github.io/fake-jobs/'
html = requests.get(url)
# print(html.text)
s = BeautifulSoup(html.text, 'html.parser')

data = s.find_all('div', class_='column is-half')

data_list = []
for d in data:
    data_dict ={
        'title' : d.find('h2', class_='title is-5').text,
        'sub_title' : d.find('h3',class_='subtitle is-6 company').text,
        'location' : d.find('p', class_='location').text.strip(),
        'date' : d.find('time').text,
    }

    data_list.append(data_dict)

    print(data_list)
    
    with open('data.json', 'w') as file:
        json.dump(data_list, file, indent=4)

# results = s.find(id='ResultsContainer')
# job_title = results.find_all('h2', class_='title is-5')

# # for get specific 1 title
# print(job_title[0].text)

# # for get all title
# for job in job_title:
#     print(job.text)

# # for get all locations 
# locations = results.find_all('p', class_='location')
# for location in locations:
#     print(location.text)

# for get all subtitles
# subtitles = results.find_all('h3', class_='subtitle is-6 company')
# for subtitle in subtitles:
#     print(subtitle.text)





