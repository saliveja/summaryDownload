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

    print(f"Creating PDF from address: {address}")
    pdfkit.from_url(address, f"/home/x/Documents/newsletter_pdf/{name}, '{title}'.pdf")
    # converting html to pdf and downloading
    print(f"Created PDF {title} successfully!")
    links.clear()
