## JSON ##
# import json

# json_data = '{"name": "Bobbo", "age": 25}'
# data = json.loads(json_data)

# print(data)

# with open('data.json', 'r') as file:
#     data = json.load(file)

# print(data)

# data = {
#     "name": "Bobbo",
#     "age" : 37,
# }

# with open("output.json", "w") as file:
#     json.dump(data, file, indent=4)


# data = {
#     "name": "Bobbo",
#     "age" : 37,
# }
# json_string = json.dumps(data)
# print(json_string)

## API ##
# import requests

# response = requests.get("")

# if response.status_code == 200:
#     print(response.text)
# else:
#     print(f"Fel! Statuskod: {response.status_code}")

# data = {
#     "name": "Harry potter",
#     "author": "J.k Rowling"
# }

# response = requests.post("", json=data)

# if response.status_code == 201:
#     print(f"Lyckades, {response.text}")

# headers = {
#     "Authorization": "",
#     "Accept": "application/json"
# }

# response = requests.get("apiurl", headers=headers)

# params = {
#     "sort": "relevance",
#     "page": 1
# }

# response = requests.get("apiurl", params=params)

# response = requests.get("apiurl")
# if response.status_code == 200:
#     data = response.json()

## API test ##

# response = requests.get("https://jsonplaceholder.typicode.com/posts?format=json")

# if response.status_code == 200:
#     posts = response.json()
#     print(f"Antal posts {len(posts)}")
#     print(f"Inlägg 35: {posts[34]}")
# else:
#     print(f"Misslyckat! {response.status_code}")

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# if response.status_code == 200:
#     post = response.json()
#     print(f"Titel: {post["title"]}")
# else:
#     print(f"Misslyckat! {response.status_code}")

# updated_post = {
#     "id": 1,
#     "title": "Titel inlägg",
#     "body": "Innehåll hamnar här",
#     "userId": 1
# }

# response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated_post)

# if response.status_code == 201:
#     created_post = response.json()
#     print(f"Skapat Inlägg med id: {created_post["id"]}")

## HolidayAPI ##

# import requests

# api_key = "774d79a3-6981-4623-ac27-5805a46bd941"

# base_url = "https://holidayapi.com/v1/holidays"

# params = {
#     "key": api_key,
#     "country": "SE",
#     "year": 2023,
#     "language": "sv"
# }

# response = requests.get(base_url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     print("Heldagar för Sverige, 2024:\n")
#     for holiday in data["holidays"]:
#         print(f"{holiday['date']}: {holiday['name']}")
# else:
#     print(f"Något gick fel: Statuskod: {response.status_code}")