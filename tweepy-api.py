import tweepy

auth = tweepy.OAuthHandler("1MHM1gkFbq5gjn3dfuZaZ0JJl", "kGU7I07srw5oCddsvYrR1KdvleoHaR5jr79qzo6q8osyi0VLxY")
auth.set_access_token("1320700746-DSDrMt774GeMQa4Rvn4xvy9L4zFqx3krYSyuCvI", "RdKWuMevLto4HcHWNOAjmqS1K8lw5YF5xTYr8xCv8qCMW")

api = tweepy.API(auth)

# Get the User object for twitter...
user = api.get_user('realDonaldTrump')
print(user.screen_name)
print(str(user.followers_count) + " followers")


print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)
