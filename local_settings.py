'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'klla90LUQikptTUZWApxg2oDg'
MY_CONSUMER_SECRET = 'xnuUsYOFqHHXDMARoyGKT4xJIxXJf1QVNl2MBJ1MUTbt1kKHbW'
MY_ACCESS_TOKEN_KEY = '706461719594475520-t0sWT6KuGzqnIqnBUMj8hVZRm4CSXmB'
MY_ACCESS_TOKEN_SECRET = '8UBipyh4B3pvFRp453HSL13lZMD4JN6hIG56hWOeBLdN4'

SOURCE_ACCOUNTS = ["J_Gibsonn, DziekDB"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 6 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = "tweets.txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "jgibson_ebooks" #The name of the account you're tweeting to.
