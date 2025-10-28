import requests

#Making an API call and storing the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

#Storing the response in a variable - 
response_dict = r.json()
print(f"Total Repositories: {response_dict['total_count']}")

#Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

#Examining the first repository
repo_dict = repo_dicts[0]
print(f"\n Keys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
