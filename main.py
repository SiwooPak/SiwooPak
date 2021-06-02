import feedparser, datetime

velog_uri="https://v2.velog.io/rss/dev_shu"
feed = feedparser.parse(velog_uri)

markdown_text = """# 시우의 블로그 최근 업로드된 5개!<br>\n
update time: am 10, pm 10\n"""

## Recent blog posts

lst = []
cnt = 0

for i in range(1,6):
    dt = datetime.datetime.strptime(feed['entries'][i]['published'], '%a, %d %b %Y %H:%M:%S %Z')
    markdown_text += f"[{feed['entries'][i]['title']}]({feed['entries'][i]['link']}) - {dt}<br>\n"
    print(feed['entries'][i]['link'], feed['entries'][i]['title'])
	


f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
