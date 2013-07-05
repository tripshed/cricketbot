#cricketbot - a bot for /r/cricket

####Live scorecard
-----------
When a match thread is created by the bot, it will auto-update the body of the post in regular intervals with the current score of the match.

Usually in match threads, the OP isn't consistent with updating the match thread and so it is usually a static bit of text. This will allow for the score to continually update allowing for a new way to check the score and comment on the match simultaneously.

Possible expansion areas from here are to perhaps have a timeline in chronological order of the key moments of the game. This will take a lot longer to implement, however.


####Comment Replies
-----------
The bot crawls the comments of the front page of http://reddit.com/r/cricket and looks for comments of the type, "Cricketbot, give me [team] news". The bot can currently deal with the main Test playing nations:
- Australia (Australian)
- Bangladesh (Bangladeshi)
- England (English)
- India (Indian)
- New Zealand (Kiwi)
- Pakistan (Pakistani)
- South Africa (South African)
- Sri Lanka (Sri Lankan)
- West Indies (West Indian)
- Zimbabwe (Zimbabwean)

The bot responds with the top ESPNCricinfo articles on those countries.

So, Cricketbot is summoned when someone writes, for example, "Cricketbot, give me Indian news".

Current Status
-----------
Online!

Contents
-----------
- The License being used is the Common Development and Distribution License is an open source license which allows software to be used, modified, and shared.
- alreadydone.txt contains the comment IDs of comments which have already been replied to so that the bot does not reply twice.
- commentbot.py shows all the code required to make the bot run.
