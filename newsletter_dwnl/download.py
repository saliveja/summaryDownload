import pdfkit
import requests, bs4

def article_download(link, name):
    """Downloading the latest article."""

    res = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    links = []
    titles = []
    title_select = []
    link_select = []
    for article in soup.find_all('a'):
        links.append(article.get('href'))
        titles.append(article.get_text())

    indices = []
    for (index, item) in enumerate(links):
        if item == 'javascript:void(0)':
            indices.append(index)
    link_index = indices[0]
    item_pos = int(link_index) + 1
    new_link = links[item_pos]
    link_select.append(new_link)

    address = link_select[0]

    indices_0 = []
    for (index, item) in enumerate(titles):
        if item == '':
            indices_0.append(index)

    title_index = indices_0[0]
    item_pos = int(title_index) + 1
    new_title = titles[item_pos]
    characters = address[:5]
    for text in new_title:
        if text == characters:
            new_title = titles[item_pos]
        else:
            title_iter = iter(indices_0)
            title_index_1 = next(title_iter)
            title_index_2 = next(title_iter)
            title_index = str(title_index_2)
            item_pos = int(title_index) + 1
            new_title = titles[item_pos]
    title_select.append(new_title)
    title = title_select[0]

    filename = f'{name}, {title}.pdf'
    print(f"Creating PDF from address: {address}")
    pdfkit.from_url(address, f'pdf/{filename}')
    # converting html to pdf and downloading
    print(f"Created PDF '{title}' successfully!")

    quit()


#article_download("https://themacrocompass.substack.com/archive")
