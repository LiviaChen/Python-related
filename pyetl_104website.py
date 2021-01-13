import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

# url = 'https://www.104.com.tw/jobs/search/?keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E5%B8%AB&order=1&jobsource=2018indexpoc&ro=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

content_page = []

for i in range(1, 4):  # run 3 pages
    url = f'https://www.104.com.tw/jobs/search/?ro=0&keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E5%B8%AB&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=12&asc=0&page={i}&mode=s&jobsource=2018indexpoc'
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    job_link = soup.findAll('h2', {'class': 'b-tit'})  # bs4.element.ResultSet
    job_links = []
    for i in job_link:
        try:
            job_links.append('https:' + i.a['href'].split('?')[0])
        except:
            pass
    job_number = []
    for i in job_links:
        job_number.append(i.split('/')[-1])
    for i in job_number:
        content_page.append(r'https://www.104.com.tw/job/ajax/content/' + i)

total_list = []

columns = ['company_name', 'job_title', 'location', 'location_details', \
           'google_map', 'job_description', 'required_business_trip', 'salary', 'required_specialty']

for i in content_page:
    single_list = []
    url = i
    headers = {'Referer': 'https://www.104.com.tw/job/' + i.split('/')[-1]}
    res = requests.get(url=url, headers=headers)
    json_data = json.loads(res.text)
    single_list.append(json_data['data']['header']['custName'])
    single_list.append(json_data['data']['header']['jobName'])
    single_list.append(json_data['data']['jobDetail']['addressRegion'])

    if json_data['data']['jobDetail']['addressDetail'] == '':
        single_list.append('無提供')
    else:
        single_list.append(json_data['data']['jobDetail']['addressDetail'])

    single_list.append(
        f'https://maps.google.com/?q={json_data["data"]["jobDetail"]["latitude"]},{json_data["data"]["jobDetail"]["longitude"]}')

    if json_data['data']['jobDetail']['jobDescription'] == '':
        single_list.append('無')
    else:
        single_list.append(json_data['data']['jobDetail']['jobDescription'])

    if json_data['data']['jobDetail']['businessTrip'][0] == '無':
        single_list.append('否')
    elif json_data['data']['jobDetail']['businessTrip'][0] == '需':
        single_list.append('是')
    else:
        single_list.append(json_data['data']['jobDetail']['businessTrip'])

    single_list.append(json_data['data']['jobDetail']['salary'])
    specialty_list = []

    if len(json_data['data']['condition']['specialty']) == 0:
        single_list.append('無')
    else:
        for i in range(len(json_data['data']['condition']['specialty'])):
            specialty_list.append(json_data['data']['condition']['specialty'][i]['description'])
        single_list.append(specialty_list)

    total_list.append(single_list)

df = pd.DataFrame(data=total_list, columns=columns)
print(df)

df.to_csv(r'./data104.csv', index=0, encoding='utf-8-sig')