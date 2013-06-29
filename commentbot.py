#==============================================#
#                                              #
#         Reddit Comment Crawler v1.0          #
#                                              #
#==============================================#

import praw

r = praw.Reddit('Comment Scraper v1.0 by u/ppyil. Code available on https://github.com/sunnyamrat/cricketbot')
r.login(username='username',password='password')              #enter login details
subreddit=r.get_subreddit('subreddit')                        #insert subreddit to crawl
post_limit = 25                                               #the number of posts on the subreddit to crawl
subreddit_posts = subreddit.get_hot(limit=post_limit)
subids = set()
for submission in subreddit_posts:
    subids.add(submission.id)
subid = list(subids)
i=0
while i < post_limit:
    submission = r.get_submission(submission_id=subid[i])
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    with open('alreadydone.txt', 'r') as f:
        already_done = [line.strip() for line in f]
    f.close()
    for comment in flat_comments:
        if "Hello" in comment.body and comment.id not in already_done:
            comment.reply('World!')                           #replies to the comment saying 'Hello'
            already_done.append(comment.id)
            with open("alreadydone.txt", "a") as f:
                f.write("\n"+comment.id)
            f.close()
    i+=1
