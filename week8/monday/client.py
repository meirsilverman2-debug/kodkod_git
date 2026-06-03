# Level_1-basic:

#Exercise_1:

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")


print(response.json())
































# Example number 7:

# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/9999")

# if response.status_code == 200:
#     print("Go data:", response.json())
# elif response.status_code == 404:
#     print("Not found")
# else:
#     print(f"Unexpected status: {response.status_code}")