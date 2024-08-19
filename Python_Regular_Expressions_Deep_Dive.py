import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Updated regex pattern to exclude emails from 'exclude.com'
pattern = r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com\b)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
# i'm also utlizing \b to make sure that the domain 'exclude.com' is matched correctly and not as part of another domain
emails = re.findall(pattern, text)
print(emails)