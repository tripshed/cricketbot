#==============================================#
#                                              #
#         Reddit Comment Crawler v1.0          #
#                                              #
#==============================================#

import praw
import feedparser
import time

r = praw.Reddit('Comment Scraper v1.0 by u/ppyil. Code available on https://github.com/sa2812/cricketbot')
r.login(username='username',password='password')              #enter login details
subreddit=r.get_subreddit('subreddit')                        #insert subreddit to crawl
post_limit = 25                                               #the number of posts on the subreddit to crawl
subreddit_posts = subreddit.get_hot(limit=post_limit)
subids = set()
for submission in subreddit_posts:
    subids.add(submission.id)
subid = list(subids)

Australia = 'http://www.espncricinfo.com/rss/content/story/feeds/2.xml'
Bangladesh = 'http://www.espncricinfo.com/rss/content/story/feeds/25.xml'
England = 'http://www.espncricinfo.com/rss/content/story/feeds/1.xml'
India = 'http://www.espncricinfo.com/rss/content/story/feeds/6.xml'
New_Zealand = 'http://www.espncricinfo.com/rss/content/story/feeds/5.xml'
Pakistan = 'http://www.espncricinfo.com/rss/content/story/feeds/7.xml'
South_Africa = 'http://www.espncricinfo.com/rss/content/story/feeds/3.xml'
Sri_Lanka = 'http://www.espncricinfo.com/rss/content/story/feeds/8.xml'
West_Indies = 'http://www.espncricinfo.com/rss/content/story/feeds/4.xml'
Zimbabwe = 'http://www.espncricinfo.com/rss/content/story/feeds/9.xml'
endmessage = 'This comment was generated by /u/cricketbot. Cricketbot can be found on [Github](http://sa2812.github.io/cricketbot/). News stories from [ESPNCricinfo](http://espncricinfo.com).'

while True:
    i=0
    while i < post_limit:
        submission = r.get_submission(submission_id=subid[i])
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        with open('C:/Users/Sunny/Documents/Reddit Bot/alreadydone.txt', 'r') as f:
            already_done = [line.strip() for line in f]
        f.close()
        for comment in flat_comments:
            try:
                if "Cricketbot, give me Australian news" in comment.body and comment.id not in already_done:
                    info = feedparser.parse(Australia)
                    listings = ['**[Australian](http://www.cricket.com.au/ "Australian Cricket Board") Cricket News** \n \n']
                    for entry in info.entries:
                        listings.append('- ['+entry.title+']('+entry.link+') \n \n')
                        comment1 = ''.join(listings)
                        comment2 = comment1+endmessage
                    comment.reply(comment2)
                    already_done.append(comment.id)
                    with open("C:/Users/Sunny/Documents/Reddit Bot/alreadydone.txt", "a") as f:
                        f.write("\n"+comment.id)
                    f.close()
            except AttributeError:
                pass
            try:
                if "Cricketbot, give me Bangladeshi news" in comment.body and comment.id not in already_done:
                    info = feedparser.parse(Bangladesh)
                    listings = ['**[Bangladeshi](http://www.tigercricket.com/ "Bangladeshi Cricket Board") Cricket News** \n \n']
                    for entry in info.entries:
                        listings.append('- ['+entry.title+']('+entry.link+') \n \n')
                        comment1 = ''.join(listings)
                        comment2 = comment1+endmessage
                    comment.reply(comment2)
                    already_done.append(comment.id)
                    with open("C:/Users/Sunny/Documents/Reddit Bot/alreadydone.txt", "a") as f:
                        f.write("\n"+comment.id)
                    f.close()
            except AttributeError:
                pass
            try:
                if "Cricketbot, give me English news" in comment.body and comment.id not in already_done:
                    info = feedparser.parse(England)
                    listings = ['**[English](http://www.ecb.co.uk/ "English Cricket Board") Cricket News** \n \n']
                    for entry in info.entries:
                        listings.append('- ['+entry.title+']('+entry.link+') \n \n')
                        comment1 = ''.join(listings)
                        comment2 = comment1+endmessage
                    comment.reply(comment2)
                    already_done.append(comment.id)
                    with open("C:/Users/Sunny/Documents/Reddit Bot/alreadydone.txt", "a") as f:
                        f.write("\n"+comment.id)
                    f.close()
            except AttributeError:
                pass
            try:
                if "Cricketbot, give me Indian news" in comment.body and comment.id not in already_done:
                    info = feedparser.parse(India)
                    listings = ['**[Indian](http://www.bcci.tv/ "Board of Control of Cricket in India") Cricket News** \n \n']
                    for entry in info.entries:
                        listings.append('- ['+entry.title+']('+entry.link+') \n \n')
                        comment1 = ''.join(listings)
                        comment2 = comment1+endmessage
                    comment.reply(comment2)
                    already_done.append(comment.id)
                    with open("C:/Users/Sunny/Documents/Reddit Bot/alreadydone.txt", "a") as f:
                        f.write("\n"+comment.id)
                    f.close()
            except AttributeError:
                pass
            try:
                if "Cricketbot, give me Kiwi news" in comment.body and comment.id not in already_done:
                    info = feedparser.parse(New_Zealand)
                    listings = ['**[Kiwi](http://www.blackcaps.co.nz/ "New Zealand Cricket Board") Cricket News** \n \n']
                    for entry in info.entries:
                        listings.append('- ['+entry.title+']('+entry.link+') \n \n')
                        comment1 = ''.join(listings)
                        comment2 = comment1+endmessage
                    comment.reply(comment2)
                    already_done.append(comment.id)
                    with open("C:/Users/Sunny/Documents/Reddit Bot/alreadydone.txt", "a") as f:
                        f.write("\n"+comment.id)
                    f.close()
            except AttributeError:
                pass
            try:      
                if "Cricketbot, give me Pakistani news" in comment.body and comment.id not in already_done:
                    info = feedparser.parse(Pakistan)
                    listings = ['**[Pakistani](http://www.pcb.com.pk/ "Pakistan Cricket Board") Cricket News** \n \n']
                    for entry in info.entries:
                        listings.append('- ['+entry.title+']('+entry.link+') \n \n')
                        comment1 = ''.join(listings)
                        comment2 = comment1+endmessage
                    comment.reply(comment2)
                    already_done.append(comment.id)
                    with open("C:/Users/Sunny/Documents/Reddit Bot/alreadydone.txt", "a") as f:
                        f.write("\n"+comment.id)
                    f.close() 
            except AttributeError:
                pass
            try:
                if "Cricketbot, give me South African news" in comment.body and comment.id not in already_done:
                    info = feedparser.parse(South_Africa)
                    listings = ['**[South African](http://www.cricket.co.za/ "Cricket South Africa") Cricket News** \n \n']
                    for entry in info.entries:
                        listings.append('- ['+entry.title+']('+entry.link+') \n \n')
                        comment1 = ''.join(listings)
                        comment2 = comment1+endmessage
                    comment.reply(comment2)
                    already_done.append(comment.id)
                    with open("C:/Users/Sunny/Documents/Reddit Bot/alreadydone.txt", "a") as f:
                        f.write("\n"+comment.id)
                    f.close() 
            except AttributeError:
                pass
            try:
                if "Cricketbot, give me Sri Lankan news" in comment.body and comment.id not in already_done:
                    info = feedparser.parse(Sri_Lanka)
                    listings = ['**[Sri Lankan](http://www.srilankacricket.lk/ "Sri Lanka Cricket") Cricket News** \n \n']
                    for entry in info.entries:
                        listings.append('- ['+entry.title+']('+entry.link+') \n \n')
                        comment1 = ''.join(listings)
                        comment2 = comment1+endmessage
                    comment.reply(comment2)
                    already_done.append(comment.id)
                    with open("C:/Users/Sunny/Documents/Reddit Bot/alreadydone.txt", "a") as f:
                        f.write("\n"+comment.id)
                    f.close() 
            except AttributeError:
                pass
            try:
                if "Cricketbot, give me West Indian news" in comment.body and comment.id not in already_done:
                    info = feedparser.parse(West_Indies)
                    listings = ['**[West Indian](http://www.windiescricket.com/ "West Indies Cricket Board") Cricket News** \n \n']
                    for entry in info.entries:
                        listings.append('- ['+entry.title+']('+entry.link+') \n \n')
                        comment1 = ''.join(listings)
                        comment2 = comment1+endmessage
                    comment.reply(comment2)
                    already_done.append(comment.id)
                    with open("C:/Users/Sunny/Documents/Reddit Bot/alreadydone.txt", "a") as f:
                        f.write("\n"+comment.id)
                    f.close() 
            except AttributeError:
                pass
            try:
                if "Cricketbot, give me Zimbabwean news" in comment.body and comment.id not in already_done:
                    info = feedparser.parse(Zimbabwe)
                    listings = ['**[Zimbabwean](http://www.zimcricket.org/ "Zimcricket") Cricket News** \n \n']
                    for entry in info.entries:
                        listings.append('- ['+entry.title+']('+entry.link+') \n \n')
                        comment1 = ''.join(listings)
                        comment2 = comment1+endmessage
                    comment.reply(comment2)
                    already_done.append(comment.id)
                    with open("C:/Users/Sunny/Documents/Reddit Bot/alreadydone.txt", "a") as f:
                        f.write("\n"+comment.id)
                    f.close() 
            except AttributeError:
                pass
        i+=1
    time.sleep(600)
