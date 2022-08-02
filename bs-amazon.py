from bs4 import BeautifulSoup
import requests
import csv


#get html
url="https://www.amazon.co.uk/gp/bestsellers/musical-instruments/407784031/ref=zg_b_bs_407784031_1"
#Human trick
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# get all books
guitars = soup.find_all(id="gridItemRoot")

csv_headers = ['Rank', 'Title', 'Author', 'Price']
with open('amazon_guitars.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csv_headers)


for guitar in guitars:

    rank = guitar.find('span', class_='zg-bdg-text').text[1:]

    children = guitar.find('div', class_='zg-grid-general-faceout').div

    title = children.contents[1].text
    stars = children.contents[2].text
    price = children.contents[-1].text
   
    with open('amazon_guitars.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([rank, title, stars, price])