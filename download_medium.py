import feedparser
import pdfkit

def download_medium(name, link, link_index):
    """Downloading the latest Medium article."""

    links = []


    feed = feedparser.parse(link)
    for entry in feed.entries:
        link_selection = entry.link
        links.append(link_selection)

    address = links[link_index]

    print(f"Creating PDF from address: {address}")
    pdfkit.from_url(address, f"{name}.pdf")
    # converting html to pdf and downloading
    print(f"Created PDF {name} successfully!")
    links.clear()
