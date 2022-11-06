#TODO:
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
import argparse
import requests, bs4
import os

class TextSummaryDownload:
    """program which based on selection can summarize and download newsletters."""

    def __init__(self):
        """initializing."""
        self.file = 'data/dict.json'
        self.dicts = self.get_dicts()

    def get_dicts(self):

        with open(self.file, 'r+') as f:
            dicts = json.load(f)

        return dicts

    def summary_headers(self, args):
        """Prints a list of all authors in dict."""

        print("\n")

        for i, item in enumerate(self.dicts, 1):
            print(f"{i} - {item.strip()}")
        print("\n")

    def all_articles_summary(self, args):
        """Printing summary of all articles in the dict."""

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

    def summarize_chosen_article(self, args):
        """Summarize selected article."""

        i = args.index
        if i == 0:
            self.all_articles_summary()
        else:
            for i, (item, dct) in enumerate(self.dicts.items()):
                name = item
                for key, link in dct.items():
                    link = dct['link']
                    if link.endswith('feed'):
                        title, date, sum, address = sm.sum_medium(link)
                    else:
                        title, date, sum, address = summary.summary(link)

                    print(f"\n{i + 1} - {name}, '{title}':\n{date} \n{sum}")
                    print(address)

        # def function for download connected to argparse

    def download(self, args):
        """Downloading selected article."""

        index = int(args.index) - 1

        for i, item in enumerate(self.dicts.keys()):
            if i == index:
                link = self.dicts[item]["link"]
                name = item

                if link.endswith('feed'):
                    dm.download_medium(link)
                else:
                    d.article_download(link, name)

    def remove_dictItem(self, args):
        """Removing key and value from dictionary."""

        dicts = self.dicts
        index = int(args.index) - 1
        print(index)
        for i, item in enumerate(dicts.keys()):
            if i == index:
                delete = item

        rm_item = dicts.pop(delete)
        print(f"{rm_item} has been deleted")

        print("The new list will look like this:")
        for i, item in enumerate(dicts, 1):
            print(f"{i} - {item.strip()}")
        self.new_dict(dicts)

    def new_dict(self, dicts):
        """Save edited dictionary."""

        answer = input("Are you sure you want to save this list? y/n ")
        if answer == 'y':
            with open(self.file, 'a') as f:
                json.dump(dicts, f, indent=2)
        else:
            quit()

    def add_dict_item(self, args):
        """add dictionary item to dict.json"""

        dicts = self.get_dicts()
        entry = args.url

        names = []
        res = requests.get(entry)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        result_name = soup.find_all("div", class_="topbar-content")
        for post in result_name:
            post_name = post.find("a", class_="navbar-title-link")
            names.append(post_name.text)

        value = {"link": entry}
        name = f"{names[0]}"

        dicts[name] = value

        self.save_dicts(dicts)

    def save_dicts(self, dicts):
        """saving new entry to dicts."""

        with open(self.file, 'w') as f:
            json.dump(dicts, f, indent=2)

    def parser_main(self):
        """argparser - storing arguments and setting default functions."""
        parser = argparse.ArgumentParser(
            prog='Newsletter summary and download',
            description='summary and download of selected newsletters')

        # version
        parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
        subparsers = parser.add_subparsers(
            help="{subcommand}[-h] shows all the options")

        # summary arg
        parser_summary = subparsers.add_parser('summary', help=
        'summary of selected newsletter', aliases=['s'])

        parser_summary.add_argument('index', help=
        'choose # of newsletter to summarize. 0 summarizes all newsletters ')

        parser_summary.set_defaults(func=self.summarize_chosen_article)

        # download arg
        parser_download = subparsers.add_parser('download', help=
        'downloading selected newsletters', aliases=['d'])

        parser_download.add_argument('index', help=
        'Choose # of newsletter to download')
        parser_download.set_defaults(func=self.download)

        # list arg
        parser_list = subparsers.add_parser('list', help=
        'displays list of newsletters that can be summarized and downloaded',
                                            aliases=['l'])
        # list requires no index and will return a list of all headers

        parser_list.set_defaults(func=self.summary_headers)

        # delete arg
        parser_edit = subparsers.add_parser('delete', help=
        'delete newsletter from list', aliases=['del'])

        parser_edit.add_argument('index', help=
        'Choose # of newsletter to remove')

        parser_edit.set_defaults(func=self.remove_dictItem)
        # del is the action, index the number of the newsletter to delete
        # 'func' calls for the function within this class

        # add arg
        parser_edit = subparsers.add_parser('add', help=
        'add newsletter to list', aliases=['add'])

        parser_edit.add_argument('url', help=
        'Choose url to add')

        parser_edit.set_defaults(func=self.add_dict_item)

        args = parser.parse_args()
        args.func(args)

if __name__ == '__main__':
    sd = TextSummaryDownload()
    sd.parser_main()



