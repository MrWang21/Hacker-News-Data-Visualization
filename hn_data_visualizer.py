import requests
from operator import itemgetter
import plotly.express as px

# Make an API call and check the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Hacker News API status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts  = [] 
for submission_id in submission_ids:
    # Make a new API call for each submission
    url =  f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Skips over promotional post (Non-commentable posts)
    try:
        response_dict['descendants']    
    except KeyError:
        continue

    # Build a dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

# Sorts by number of comments in descending order
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),reverse=True)

# Gathers data used for visualization of top 10 commented post on top stories
submission_link, comments = [],[]
for submission_dict in submission_dicts[:10]:
    link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    submission_link.append(link)
    comments.append(submission_dict['comments'])

# Make Visualizations
title = "Top 10 most active discussions on Hacker News"
labels={'x': 'Article Name','y':'Comments'}
fig = px.bar(x=submission_link,y=comments,labels=labels, title=title)
fig.show()