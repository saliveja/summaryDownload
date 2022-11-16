import feedparser
import requests, bs4
import summarize

def sum_medium(link):
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
    address = links[0]
    date = dates[0]
    date_select = date[:16]

    req1 = requests.get(address, headers={'User-Agent': 'Mozilla/5.0'})
    soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
    html = soup1.find_all('p')
    for text in html:
        article = text.text
        article_to_sum.append(article)

    article_str = ' '.join(article_to_sum)
    sum = summarize.summarize(article_str, 0.05)
    return title, date_select, sum, address
    dates.clear()
