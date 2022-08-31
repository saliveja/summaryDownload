import requests, bs4
from requests.exceptions import InvalidSchema, MissingSchema
import summarize


def summary(title_index, date_index, link, index):
    """Summary of chosen articles."""

    article_to_sum = []
    titles =[]
    dates = []

    res = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    for article in soup.find_all('div'):
        dates.append(article.get('title'))

    links = []
    for article in soup.find_all('a'):
        links.append(article.get('href'))
        titles.append(article.get_text())

    # print(dates)
    address = links[index]
    title = titles[title_index]
    date = dates[date_index]
    date_list = list(date)[:10]
    # slice_date = date_list[:10]
    slice_str = ''.join(date_list)

    req1 = requests.get(address, headers={'User-Agent': 'Mozilla/5.0'})
    soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
    html = soup1.find_all('p')
    for text in html:
        article = text.text
        article_to_sum.append(article)
    article_str = ' '.join(article_to_sum)
    sum = summarize.summarize(article_str, 0.05)
    if len(sum) < 300:
        sum = article_str
        print("!! THIS IS A PAYWALLED ARTICLE !!")
    return title, date, sum, address
    # print(f"{title}, {slice_str}\n{sum}\n{address}")

# summary(8, 31, "https://onchainwizard.substack.com/archive", 8)
