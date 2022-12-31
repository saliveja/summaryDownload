import requests, bs4
import summarize


def summary(link):
    """Summary of chosen articles."""

    article_to_sum = []
    titles = []
    dates = []
    descriptions = []
    links = []
    names = []

    res = requests.get(link)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    result = soup.find_all("div", class_="portable-archive-post")
    for post in result:
        post_title = post.find("a", class_="post-preview-title")
        titles.append(post_title.text)
        title = f"{titles[0]}"

        # post_description_html = post.find("a",
        #                              class_="post-preview-description")
        # descriptions.append(post_description_html.text[13:])
        # description = descriptions[0]

        post_url = post.find("a", class_="post-preview-description")
        links.append(post_url['href'])
        address = links[0]

        post_date = post.find("time")
        dates.append(post_date['datetime'][:10])
        date = dates[0]

        #print(f"{title}, {date}\n{description}\n{address}\n\n")

    req1 = requests.get(address, headers={'User-Agent': 'Mozilla/5.0'})
    soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
    p_text = soup1.find_all('p')
    for text in p_text:
        article = text.text
        article_to_sum.append(article)
    article_str = ' '.join(article_to_sum)
    sum = summarize.summarize(article_str, 0.05)
    if len(sum) < 300:
        sum = article_str
        print(f"{title}, {date}\n{address}\n!!THIS IS A PAYWALLED ARTICLE!!")
    else:
        #print(f"{title}, {date}\n{sum}\n{address}\n\n")
        return title, date, sum, address


#
# summary("https://cryptocomresearch.substack.com/archive")
