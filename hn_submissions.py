from operator import itemgetter
import requests

#Making API Call and storing the response

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status Code: {r.status_code}")

#Processing information about each submission.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:20]:
    #Separate API call for each submission
    
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print (f"Submission ID: {submission_id}\tStatus: {r.status_code}")
    response_dict = r.json()

    #Building a dictionary for each article - 

    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://hacker-news.firebaseio.com/v0/item/{submission_id}",
        'comments': response_dict['descendants'],
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key = itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion Link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")



