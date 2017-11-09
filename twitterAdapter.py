import tweepy

class TwitterAdapter():
    api = None
    user = None
    def __init__(self):
        self.setTwitterApi()
        self.setTwitterUser()

    def setTwitterUser(self):
        if (self.user is None):
            self.user = self.getTwitterApi().get_user('spotweetpy')

    def setTwitterApi(self):
        if(self.api is None):
            auth = tweepy.OAuthHandler('qcwrmAocu3cuCT5D8iMB3DdWI', 'tUUZ1s56ry3yVrAhrOs7gG7R6VDQ2yhaKIDBekeMvOOXLSoLSD')
            auth.set_access_token('925749601159835649-ug6nuUq8Z5aQfkedjBskTpgFGf7kQxk','AOh9W58ZpdcBcPlnDP7Ni4TRiABiD5W3cMliG1xPwFBhV')
            self.api = tweepy.API(auth)
    def getTwitterApi(self):
        return self.api
    def tweetear(self, mensaje):
        self.api.update_status(mensaje)



ta = TwitterAdapter()


print ta.user

variable = ta.getTwitterApi().user_timeline(ta.user.id, count=5)
print len(variable)
for var in variable:
    print var


#https://docs.python.org/2.4/lib/timer-objects.html
