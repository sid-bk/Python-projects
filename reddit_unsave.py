import praw
 
username = '' #replace with your username
pw = '' #replace with your password
r = praw.Reddit(user_agent='/u/'+username+' deleting all saved links')
 
r.login('username','pw',disable_warning=True)
 
for saved in r.user.get_saved(limit=1000):
    r.get_submission(str(saved.permalink)).unsave()
