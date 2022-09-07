#TODO:
# 1) Add name of the article and date of release to the summary header.
# 2) Save pdfs to /~/pdf folder, not to the main folder,
# - name pdfs more descriptive, so every new one has a unique name (not overwriting)
# 3) CLI with users choices
# - Display all new headers
# - Display chosen summary
# - Display all summaries
# - Add/Delete a newsletter from the dict


import summary
import download as d
import summary_medium as sm
import download_medium as dm
from datetime import date, datetime, timedelta
import time
from requests.exceptions import InvalidSchema


def dictionary():

    dict = {
        "Knower's substack": {
            "date_index": 31,
            "link": "https://theknower.substack.com/archive",
            "link_index": 9,
            "title_index": 8},
        "Wrong a lot": {
            "date_index": 31,
            "link": "https://wrongalot.substack.com/archive",
            "link_index": 9,
            "title_index": 9},
        "Kyla": {
            "date_index": 31,
            "link": "https://kyla.substack.com/archive",
            "link_index": 9,
            "title_index": 9},
        "Ansem": {
            "date_index": 31,
            "link": "https://blknoiz06.substack.com/archive",
            "link_index": 5,
            "title_index": 6},
        "Cobie": {
            "date_index": 31,
            "link": "https://cobie.substack.com/archive",
            "link_index": 5,
            "title_index": 5},
        "Scarpa": {
            "link": "https://medium.com/@TraderScarpa/feed",
            "link_index": 0},
        "Hayes": {
            "link": "https://cryptohayes.medium.com/feed",
            "link_index": 0},
        "Foo69": {
            "link": "https://fooo69.medium.com/feed",
            "link_index": 0},
        "Godcomplex182": {
            "link": "https://medium.com/@godcomplex182/feed",
            "link_index": 0},
        "Cryptocreddy": {
            "link": "https://medium.com/@cryptocreddy/feed",
            "link_index": 0},
        "0xgodking": {
            "link": "https://medium.com/@0xgodking/feed",
            "link_index": 0},
        "Onchain Wizard Newsletter": {
            "date_index": 31,
            "link": "https://onchainwizard.substack.com/archive",
            "link_index": 8,
            "title_index": 8},
        "No Sleep": {
            "date_index": 31,
            "link": "https://nosleep.substack.com/archive",
            "link_index": 6,
            "title_index": 5},
        "Kyle's Newsletter": {
            "date_index": 31,
            "link": "https://0xfren.substack.com/archive",
            "link_index": 6,
            "title_index": 5},
        "The Reading Ape Newsletter": {
            "date_index": 29,
            "link": "https://thereadingape.substack.com/archive",
            "link_index": 10,
            "title_index": 9},
        "Nat's Newsletter": {
            "date_index": 90,
            "link": "https://crypto.nateliason.com/",
            "link_index": 6,
            "title_index": 6},
        "Rain And Coffee Newsletter": {
            "date_index": 31,
            "link": "https://rainandcoffee.substack.com/archive",
            "link_index": 10,
            "title_index": 9},
        "The Macro Compass Newsletter": {
            "date_index": 31,
            "link": "https://themacrocompass.substack.com/archive",
            "link_index": 10,
            "title_index": 9},
        "Not Boring Newsletter": {
            "date_index": 55,
            "link":"https://www.notboring.co/",
            "link_index" : 19,
            "title_index": 14
        },
    }
    return dict

def display_summary_headers():
    """Prints an enumerated list of all authors to choose summary of"""

    dict = dictionary()

    print("\n")

    for i, item in enumerate(dict, 1):
        print(f"{i} - {item.strip()}")
    print("\n")


def all_articles_summary():
    """Printing summary of all articles in the dict"""

    dict = dictionary()

    for i, (item, dct) in enumerate(dict.items()):
        name = item
        for key, index in dct.items():
            link = dct["link"]
            link_index = dct["link_index"]
            if key == "title_index":
                title_index = dct["title_index"]
            if key == "date_index":
                date_index = dct["date_index"]

        if link.endswith('feed'):
            title, date, sum, address = sm.sum_medium(link, link_index)
        else:
            title, date, sum, address = summary.summary(title_index,
                                                        date_index, link,
                                                        link_index)
            date_list = list(date)
            slice_date = date_list[:10]
            slice_str = ''.join(slice_date)

        print(f"\n{i + 1} - {name}, '{title}':\n{slice_str} \n{sum}")
        print(address)


def summarize_chosen_article():
    """Displays a summary of an article based on users choice"""

    dict = dictionary()

    while True:

        display_summary_headers()

        choice = (int(input("\nEnter the # of article you want "
                            "to summarize: \n(Enter 0 for summary of all)\t")) - 1)
        if choice == -1:
            all_articles_summary()

        for i, (item, dct) in enumerate(dict.items()):
            if i == choice:
                name = item
                for key, index in dct.items():
                    link = dct["link"]
                    link_index = dct["link_index"]
                    if key == "title_index":
                        title_index = dct["title_index"]
                    if key == "date_index":
                        date_index = dct["date_index"]

                if link.endswith('feed'):
                    title, date, sum, address = sm.sum_medium(link, link_index)
                else:
                    title, date, sum, address = summary.summary(title_index,
                                                                date_index, link,
                                                                link_index)
                    date_list = list(date)
                    slice_date = date_list[:10]
                    slice_str = ''.join(slice_date)

                print(f"\n{i + 1} - {name}, '{title}':\n{slice_str} \n{sum}")
                print(address)

        answer_download = input("\nDo you want to download this article? y/n  ")
        if answer_download.lower() == "y":
            download(choice)

        answer_to_question = \
                input("\nDo you want to summarize another article? y/n  ")

        if answer_to_question.lower() == "n":
            print("bye")
            quit()



def download(choice=100):
    """Downloading selected article."""

    dict = dictionary()

    while True:
        if choice == 100:
            choice = (int(input("\nWith index number, select the article you "
                           "would like to download: ")) - 1)

        for i, (item, dct) in enumerate(dict.items()):
            if i == choice:
                name = item
                for key, index in dct.items():
                    link = dct["link"]
                    link_index = dct["link_index"]

                if link.endswith('feed'):
                    dm.download_medium(name, link, link_index)
                else:
                    d.article_download(name, link, link_index)

        answer_to_question = \
            input("Do you want to download another article? y/n ")

        if answer_to_question.lower() == "n":
            print("enjoy")
            break
        else:
            display_summary_headers()
            choice = (int(input("\nWith index number, select the article you "
                                "would like to download: ")) - 1)
            continue

# def remove_dictItem():
#     """Removing key and values from dictionary"""
#
#     dict = dictionary()
#
#     answer = input("Do you want to delete a keypair in the dictionary? (y/q  ")
#
#     if answer.lower() = "q":
#         break
#
#     else:
#         print("\n")
#         for i, item in enumerate(dict, 1):
#             print(f"{i} - {item.strip()}")
#         print("\n")
#
#     selection = input("With number, select the item to remove: ")
#
#      for key, value in dict.items():
#             selection = dict[key]
#             removal = del dict[selection]
#
#             print(f"You removed {removal}. Continue select or press q when finished: ")





summarize_chosen_article()
# download()
