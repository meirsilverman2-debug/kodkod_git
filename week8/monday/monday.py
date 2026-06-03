# Level_1-basic:
# Exercise_1:

import requests

# response1 = requests.get("https://jsonplaceholder.typicode.com/users/1")

# data = response1.json()

# print(data["name"])
# print(data["email"])
# print(data["address"]["city"])

# response2 = requests.get("https://jsonplaceholder.typicode.com/posts")

# posts = response2.json()
# print(posts)
# print(len(posts))

# response3 = requests.get("https://jsonplaceholder.typicode.com/posts?userId=2")

# users_id = response3.json()

# for d in users_id:

#     print(d["title"])


# # Exercise_2:

# def safe_get(url):
#     response = requests.get(url)

#     if response.status_code == 200:
#         return response.json()
    
#     elif response.status_code == 404:
#         return None
    
#     else:
#         raise Exception(F"ERROR: {response.status}")

# data_somthing = safe_get("https://jsonplaceholder.typicode.com/posts?userId=2")
# print(data_somthing)

# response4 = requests.get("http://127.0.0.1:7700/greet?name=Moshe")

# print(response4.text)

# Level_2-intermediate:
# Exercise_4:


posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()

users = requests.get("https://jsonplaceholder.typicode.com/users").json()


d = {}

for user in users:
    user_id = user["id"]
    user_name = user["name"]

    d[user_id] = user_name

print(d)


























































# Example number 5:

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/users")
# def get_users(role: str = "all", page: int = 1):
#     return {"role": role, "page": page, "users": []}

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id}
















# Example number 4:

# import requests

# params = {"userId": 1}
# response = requests.get(
#     "https://jsonplaceholder.typicode.com/posts",
#     params = params
# )

# posts = response.json()
# print(f"Found {len(posts)} posts for user 1")

# for post in posts[:3]:
#     print(f"  - {post["title"]}")


# Example number 3:

# import requests

# update = {"id": 1, "title": "New_Title", "body": "New content", "userId": 1}


# r = requests.put("https://jsonplaceholder.typicode.com/posts/1",
#                  json=update)

# print(r.status_code)

# r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
# print(r.status_code)




# example number 2:

# import requests

# new_post = {
#     "title": "My first post",
#     "body": "This is the content",
#     "usersId": 1
# }


# response = requests.post(
#     "https://jsonplaceholder.typicode.com/posts",
#     json = new_post
# )


# print(response.status_code)
# print(response.json())


# Example number 1:

# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# print(response.status_code)
# print(response.json())
# print(response.text)

# data = response.json()
# print(data["title"])
# print(data["userId"])