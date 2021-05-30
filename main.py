import feedparser, datetime

velog_uri="https://v2.velog.io/rss/dev_shu"
feed = feedparser.parse(velog_uri)

markdown_text = """# Hello, there!
Your introduction goes here
## Recent blog posts
""" # list of blog posts will be appended here

lst = []


for i in feed['entries']:
    dt = datetime.datetime.strptime(i['published'], '%a, %d %b %Y %H:%M:%S %Z')$
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
