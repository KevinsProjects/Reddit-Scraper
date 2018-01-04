import praw
import argparse
import urllib
import logging

from settings import getClientSecret, getClientID, getUserAgent, default_subreddit

def checkIfImage( image ):
    if image.endswith( '.jpg' ):
        return True
    elif image.endswith( '.png' ):
        return True
    else:
        return False

def main():

    logging.captureWarnings(True)

    parser = argparse.ArgumentParser( description = 'Argument Parser for Hermes Scraper' )
    parser.add_argument('-amount', action='store', dest='amount_arg', type=int)
    parser.add_argument('--subreddit', action='store', dest='subreddit_arg', type=str)
    args = parser.parse_args()

    if args.subreddit_arg == None:
        subreddit = default_subreddit()
    else:
        subreddit = args.subreddit_arg

    reddit = praw.Reddit(client_id = getClientID(), client_secret = getClientSecret(), user_agent = getUserAgent())
    imgCount = 0

    for submission in reddit.subreddit(subreddit).top(limit=args.amount_arg):
        imageURL = submission.url
        if checkIfImage( imageURL ):
            imageExtension = imageURL.rsplit('/',1)[1].rsplit('.', 1)[1]

            print ('Downloading: ' + submission.title)
            print ('At URL: ' + imageURL)

            urllib.urlretrieve( imageURL, str(imgCount) + '.' + imageExtension )
            imgCount = imgCount + 1

            print ( "__ DONE __" )
            print


if __name__ == '__main__':
    main()
