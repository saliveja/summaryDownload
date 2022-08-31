import feedparser
import requests, bs4
import summarize

def sum_medium(link, link_index):
    """Summary of selected medium articles."""

    links = []
    article_to_sum = []
    titles = []
    dates = []

    feed = feedparser.parse(link)
    for entry in feed.entries:
        link_selection = entry.link
        links.append(link_selection)
        title = entry.title
        titles.append(title)
        date = entry.published
        dates.append(date)

    title = titles[0]
    address = links[link_index]

    req1 = requests.get(address, headers={'User-Agent': 'Mozilla/5.0'})
    soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
    html = soup1.find_all('p')
    for text in html:
        article = text.text
        article_to_sum.append(article)

    article_str = ' '.join(article_to_sum)
    sum = summarize.summarize(article_str, 0.05)
    return title, date, sum, address
    dates.clear()

# sum_medium("https://medium.com/@cryptocreddy/feed", 0)