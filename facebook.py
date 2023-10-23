import facebook
import requests
import csv

page_id=""
app_id = '635668872093335'
app_secret = '61552042373210'
short_lived_token = 'YOUR_SHORT_LIVED_TOKEN'

params = {
    'grant_type': 'fb_exchange_token',
    'client_id': app_id,
    'client_secret': app_secret,
    'fb_exchange_token': short_lived_token
}

response = requests.get('https://graph.facebook.com/v13.0/oauth/access_token', params=params)
long_lived_token = response.json()['access_token']

group_id = '61552042373210'

graph = facebook.GraphAPI(access_token=long_lived_token, version='v13.0')

posts = graph.get_all_connections(group_id, 'feed', fields='message,comments')

all_data = []
for post in posts:
    post_data = []
    post_message = post.get('message')
    post_comments = post.get('comments')
    
    post_data.append(post_message)
    
    if post_comments:
        for comment in post_comments['data']:
            comment_message = comment.get('message')
            post_data.append(comment_message)
    
    all_data.append(post_data)
    
    with open('group_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Post', 'Comment'])
        writer.writerows(all_data)