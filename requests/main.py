import requests

response = requests.get("https://api.github.com/users/hussainsheriffC/repos")
# print(response.json())
# print(type(response.json()))
# print(response.json()[0])
my_projects = response.json()

for project in my_projects:
    print(f"project name: {project['name']}\n project url: {project['html_url']}\n")