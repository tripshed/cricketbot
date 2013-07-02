cricketbot
==========

A bot for /r/cricket
-----------

Currently, the bot just crawls the comments of the front page of http://reddit.com/r/cricket and looks for comments of the type, "Cricketbot, give me [team] news". The bot can currently deal with the main Test playing nations:
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

Contents
-----------
- The License being used is the Common Development and Distribution License is an open source license which allows software to be used, modified, and shared.
- alreadydone.txt contains the comment IDs of comments which have already been replied to so that the bot does not reply twice.
- commentbot.py contains the bot which at present, searches all the comments and replies accordingly.
