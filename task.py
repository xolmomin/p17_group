import csv
import requests

url = 'https://jsonplaceholder.typicode.com/{}'

data = ('comments', 'posts')
for i in data:
    response = requests.get(url.format(i))
    if response.status_code == 200:
        json_data = response.json()
        with open(f'{i}.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=json_data[0].keys())
            writer.writeheader()
            writer.writerows(json_data)
