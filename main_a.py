import requests
from bs4 import BeautifulSoup
import csv

url = 'https://bigblue.academy/en/data-science-glossary'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    content_div = soup.find('div', class_='content', id='post')

    if content_div:
        p_tags = content_div.find_all('p')

        with open('result.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Word', 'Definition', 'Category', 'Source'])

            skip_count = 0

            for i, p in enumerate(p_tags):
                if p.find('strong') and len(p.find_all()) == 1:
                    skip_count += 1

                    if skip_count <= 3:
                        continue

                    strong_text = p.strong.get_text(strip=True)

                    if i + 1 < len(p_tags):
                        next_p = p_tags[i + 1]
                        definition = next_p.get_text(strip=True)

                        writer.writerow([strong_text, definition, 'Data Science', 'BigBlue Data Academy'])
    else:
        print("Тег <div class='content' id='post'> не найден.")
else:
    print(f"Ошибка при запросе страницы: {response.status_code}")

