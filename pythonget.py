import requests
import json
url = 'https://uom.lk'

html = requests.get(f"{url}/efac")

# soup = BeautifulSoup(html, 'html.parser')

# tags = soup('a')

# for tag in tags:
#     print(tag.get('href'))

print(html.content)
