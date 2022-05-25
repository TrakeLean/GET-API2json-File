import requests
import json

urls = ("https://www.themealdb.com/api/json/v1/1/search.php?s=Brownie","http://google.com")
for url in urls:
    response = requests.get(url)
    try:
        response_info = response.json()
        with open("output.json", 'w', encoding='utf-8') as f:
            json.dump(response_info, f, ensure_ascii=False, indent=4)
            print(f"Success -------------- {url}")
    except requests.exceptions.JSONDecodeError as error:
        print(f"Api returns an Image - {url}")