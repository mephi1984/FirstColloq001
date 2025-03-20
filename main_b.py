import csv
from collections import Counter
import re

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text.lower())


with open('result.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    definitions = [row['Definition'] for row in reader]

all_text = ' '.join(definitions)

words = clean_text(all_text).split()

word_counts = Counter(words)

most_common_words = word_counts.most_common(10)
print("10 самых часто встречающихся слов:")
for word, count in most_common_words:
    print(f"{word}: {count} раз")

