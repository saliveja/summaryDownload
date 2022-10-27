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
import copy
import json
from pprint import pprint
import argparse
import sys
import numpy as np
import pandas as pd

class TextSummaryDownload:
    """program that on selection summarize and download newsletters."""

    def __init__(self, choice='', index='', ):
        """initializing."""
        self.choice = choice
        self.index = index
        self.dicts = get_dicts()

    def print_help(self):
        """print help text and description"""

        print("This is a program to summarize and download selected newsletters.\n\n"
              ""
              "syntax: summary_and_download.py <index> <download> <list>\n"
              "You only need to specify one argument.\n\n"

        info = {'-i index': 'Index selects the newsletter you want to summarize',
                 '-d download': 'Download selects the newsletter you want to '
                                'download', '-l list':
                     'List returns the list of newsletter',
                 '-h help': 'Help returns this message'}


    def get_dicts(self):
        file = 'dict.json'
        with open(file, 'r+') as f:
            dicts = json.load(f)

        return dicts


    def display_summary_headers(self):
        """Prints an enumerated list of all authors to choose summary of"""

        print("\n")

        for i, item in enumerate(self.dicts, 1):
            print(f"{i} - {item.strip()}")
        print("\n")


    def all_articles_summary(self):
        """Printing summary of all articles in the dict"""

        for i, (item, dct) in enumerate(self.dicts.items()):
            name = item
            for key, index in dct.items():
                link = dct["link"]

            if link.endswith('feed'):
                title, date, sum, address = sm.sum_medium(link)
            else:
                title, date, sum, address = summary.summary(link)


        print(f"\n{i + 1} - {name}, '{title}':\n{date} \n{sum}")
        print(address)


    def summarize_chosen_article(self, index):
        """Displays a summary of an article based on users choice"""

        dicts = get_dicts()

        while True:
            # display_summary_headers()

            # choice = input("\nEnter the # of article you want "
            #                     "to summarize: \n(Enter 0 for summary of all)\n"
            #                     "If you want to delete a dictionary item, press x\t")

            choice = args.index

            if choice == int(-1):
                all_articles_summary()
            # elif choice == 'x':
            #     remove_dictItem()

            for i, (item, dct) in enumerate(dicts.items()):
                if i == choice:
                    name = item
                for key, link in dct.items():
                    link = dct['link']
                if link.endswith('feed'):
                    title, date, sum, address = sm.sum_medium(link)
                else:
                    title, date, sum, address = summary.summary(link)

            print(f"\n{i + 1} - {name}, '{title}':\n{date} \n{sum}")
            print(address)

            answer_download = input("\nDo you want to download this article? y/n\t")
            if answer_download.lower() == "y":
                download(choice)

            answer_to_question = \
                    input("\nDo you want to summarize another article? y/n  ")

            if answer_to_question.lower() == "n":
                print("bye")
                quit()



    def download(choice=100):
        """Downloading selected article."""

        dicts = get_dicts()

        while True:
            if choice == 100:
                choice = args.download

            for i, (item, dct) in enumerate(dicts.items()):
                if i == choice:
                    name = item
                for key, index in dct.items():
                    link = dct["link"]

                if link.endswith('feed'):
                    dm.download_medium(link)
                else:
                    d.article_download(link)

            answer_to_question = \
                input("Do you want to download another article? y/n ")

            if answer_to_question.lower() == "n":
                break
            else:
                display_summary_headers()
                choice = (int(input("\nWith index number, select the article you "
                                    "would like to download: ")) - 1)
                continue

    def remove_dictItem(choice=100):
        """Removing key and value from dictionary"""

        dicts = get_dicts()
        dict_copy = copy.copy(dicts)

        print("\n")
        for i, item in enumerate(dicts, 1):
            print(f"{i} - {item.strip()}")
        print("\n")

        choice = (int(input("With index number, select the dictionary item you want "
                           "to delete. Press 'q' when finished:\t")) - 1)

        while True:
            for i,  item in enumerate(dict_copy.keys()):
                if i == choice:
                    choice = item
                    del dict[choice]
                    print(f"You removed {choice}. Continue select or press 'q'.\t")

                    print("\n")
                    for i, item in enumerate(dict, 1):
                        print(f"{i} - {item.strip()}")
                        print("\n")




                # elif choice == "q":
                #     break
                # elif len(dict_copy) == 0:
                #     print("The dictionary is empty. Do you want to add newsletters"
                #           "to the dictionary? y/n\t")

if  __name__=='__main__':
    parser = argparse.ArgumentParser(
        description='summary and download of selected newsletters')
    group = parser.add_mutually_exclusive_group()
    index = group.add_argument('-i', '--index', action='store_true',
                       help='select newsletter to summarize and download')
    download = group.add_argument('-d', '--download', action='store_true',
                       help='select to download')
    list = group.add_argument('-l', '--list', action='store_true',
                                  help='returning list')
    args = parser.parse_args()

#
# display_summary_headers()
# summarize_chosen_article()


#get_dicts()


#download()
