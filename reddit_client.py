import praw

reddit_client = praw.Reddit(
        client_id='5yT0zVp43WD4Cw',
        client_secret='F98Ouux0m3eyPzYtE28AGE39Hzk',
        user_agent='app001',
        username='amd2007',
        password='qaz123')

def get_subreddit(key, limit=100):
    key = key or 'popular'
    offset = 3
    limit = int(limit) + offset
    subreddit = reddit_client.subreddit(key)
    items = []
    for submission in list(subreddit.hot(limit=limit))[3:]:
        url = 'https://i.reddit.com/r/'+subreddit.display_name 
        url += '/comments/'+submission.id
        items.append( submission.title + ' ' + url )
    return items

def display_subreddits(subreddits, limit=8):
    for subreddit in subreddits:
        print(subreddit)
        print('---')
        items = get_subreddit( subreddit, limit ) 
        for item in items:
            print(item)
            print('---')


