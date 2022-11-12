import feedparser
import pdfkit

def download_medium(link, name):
    """Downloading the latest Medium article."""

    links = []
    titles = []


    feed = feedparser.parse(link)
    for entry in feed.entries:
        link_selection = entry.link
        links.append(link_selection)
        title = entry.title
        titles.append(title)

    title = titles[0]
    address = links[0]

    filename = f'{name}, {title}.pdf'
    print(f"Creating PDF from address: {address}")
    pdfkit.from_url(f'{address}, pdf/{filename}')
    # converting html to pdf and downloading
    print(f"Created PDF {title} successfully!")
    links.clear()
