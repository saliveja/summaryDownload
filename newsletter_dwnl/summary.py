import requests, bs4
import summarize


def summary(link):
    """Summary of chosen articles."""

    article_to_sum = []
    titles = []
    dates = []
    descriptions = []
    links = []

    res = requests.get(link)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    result = soup.find_all("div", class_="portable-archive-post")
    for post in result:
        post_title = post.find("a", class_="post-preview-title")
        titles.append(post_title.text)
        title = f"'{titles[0]}'"

        post_description_html = post.find("a",
                                     class_="post-preview-description")
        descriptions.append(post_description_html.text[13:])
        description = descriptions[0]

        post_url = post.find("a", class_="post-preview-description")
        links.append(post_url['href'])
        address = links[0]

        post_date = post.find("time")
        dates.append(post_date['datetime'][:10])
        date = dates[0]

    # article_to_sum = []
    # titles =[]
    # dates = []
    # date_select = []
    # link_select = []
    # title_select = []
    #
    # res = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
    # res.raise_for_status()
    # soup = bs4.BeautifulSoup(res.content, 'html.parser')
    #
    # for article in soup.find_all('div'):
    #     dates.append(article.get('title'))
    #     for date in dates:
    #         if date != None and date.startswith('2022'):
    #             date_select.append(date)
    #             # appends all items for dates in url
    #             # append all dates starting with 2022
    #
    # links = []
    # for article in soup.find_all('a'):
    #     links.append(article.get('href'))
    #     # appending all href in parsed url
    #     titles.append(article.get_text())
    #     # appending list with all titles from parsed url
    #
    # indices = []
    # for (index, item) in enumerate(links):
    #     # for index and item in link list
    #     if item == 'javascript:void(0)':
    #         indices.append(index)
    #         # appending the index before the needed link
    # link_index = indices[0]
    # # link index is 0 in first position in list
    # item_pos = int(link_index) + 1
    # # the link needed in the next after javascript, hence +1
    # new_link = links[item_pos]
    # # the link pointed to is the link with the new assigned index
    # link_select.append(new_link)
    # # the new link is appended to link_select
    #
    # address = link_select[0]
    # date = date_select[0][:10]
    # # selection of how the date is to be displayed
    #
    # indices_0 = []
    # for (index, item) in enumerate(titles):
    #     # index and title in list titles
    #     if item == '':
    #         # if item in list is ''
    #         indices_0.append(index)
    #         # append the index to the list indices_0
    #
    # title_index = indices_0[0]
    # # title_index returns value 0 in list indices_0
    # item_pos = int(title_index) + 1
    # # the position of the title is the item after '', hence + 1
    # new_title = titles[item_pos]
    # # the new title is the position in the list defined in item_position
    # title_iter = iter(indices_0)
    # title_index_1 = next(title_iter)
    # title_index_2 = next(title_iter)
    # title_index = str(title_index_2)
    # item_pos = int(title_index) + 1
    # new_title = titles[item_pos]
    # title_select.append(new_title)
    # title = title_select[0]
    #
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
    return title, date, description, sum, address
    print(f"{title}, {date}\n{sum}\n{address}")

summary("https://themacrocompass.substack.com/archive")
