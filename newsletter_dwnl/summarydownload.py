#!/usr/bin/python3

import summary
import download as d
import summary_medium as sm
import download_medium as dm
import json
import argparse
import requests, bs4
import os
import glob
import copy
import feedparser

class TextSummaryDownload:
    """program which based on selection can summarize and download newsletters."""

    def __init__(self):
        """initializing."""
        self.file = self._path()
        self.dicts = self.get_dicts()

    def get_dicts(self):
        """loads the json file with all newsletter key pairs """

        with open(self.file, 'r+') as f:
            dicts = json.load(f)

        return dicts

    def _path(self):
        """defining path for 'newsdict.json'"""

        filename = 'newsdict.json'
        filepath = glob.glob(f'**/{filename}', recursive=True)
        # returns the path for the file 'dict.json'
        abs_path = os.path.abspath(filepath[0])
        # creating an absolute path
        # every user will clone the repo in different places
        # this automatizes the folder location

        return abs_path

    def summary_headers(self, args):
        """Prints a list of all authors in dict."""

        print("\n")

        for i, item in enumerate(self.dicts, 1):
            # for number (integer) and key in the dictionary list
            print(f"{i} - {item.strip()}")
            # printing number and key
        print("\n")

    def all_articles_summary(self):
        """Printing summary of all articles in the dict."""

        for i, (item, dct) in enumerate(self.dicts.items()):
            name = item
            # item is key name in json dict
            link = dct["link"]
            # link is the value connected to key 'link'
            if link.endswith('feed'):
                title, date, sum, address = sm.sum_medium(link)
                # 'summary_medium.py' parsing and summarizing medium newsletters
            else:
                title, date, sum, address = summary.summary(link)
                # 'summary.py' parsing and summarizing substack newsletter

            print(f"\n{i + 1} - {name}, '{title}':\n{date} \n{sum}")
            print(address)

    def summarize_chosen_article(self, args):
        """Summarize selected article."""

        index = int(args.index) - 1
        # index is argparse, command line selection
        if index == - 1:
            self.all_articles_summary()
        else:
            self.one_article_summary(index)

    def one_article_summary(self, index):
        """parsing and printing summary of newsletters."""

        for i, (item, dct) in enumerate(self.dicts.items()):
            if i == index:
                # if the number in the list equals args.index number
                name = item
                link = dct['link']
                if link.endswith('feed'):
                    # the medium articles endswith feed
                    # to access rss and parse the page
                    title, date, sum, address = sm.sum_medium(link)
                else:
                    title, date, sum, address = summary.summary(link)

                print(f"\n{i + 1} - {name}, '{title}':\n{date} \n{sum}")
                print(address)

    def download(self, args):
        """Downloading selected article."""

        index = int(args.index) - 1
        for i, item in enumerate(self.dicts.keys()):
            if i == index:
                link = self.dicts[item]["link"]
                name = item

                if link.endswith('feed'):
                    dm.download_medium(link, name)
                    # 'download_medium.py' to parse prog, convert to pdf
                    # and download with pdfkit
                else:
                    d.article_download(link, name)
                    # same as above but parsing with bs4 instead of feedparser

    def remove_dictItem(self, args):
        """Removing key and value from dictionary."""

        index = int(args.index) - 1
        dicts = self.dicts
        for i, item in enumerate(dicts.keys()):
            if i == index:
                # number is args.index
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
            with open(self.file, 'w') as f:
                # overwriting the old dict with new content
                json.dump(dicts, f, indent=2)
                # saving edited dict to json file again
        else:
            quit()

    def add_dict_item(self, args):
        """add dictionary item to dict.json"""

        dicts = self.get_dicts()
        entry = args.url
        # add <url> in argparser

        sub_names = []
        med_names = []

        if 'medium' in entry:
            # if the word 'medium' is in url address
            # creating two conditions
            if entry.endswith("/"):
                # if the users address input ends with '/'
                edit_entry = f"{entry}feed"
                # only the word 'feed' will be added
            else:
                edit_entry = f"{entry}/feed"
                # if it doesn't
                # '/feed' will be added to the url

            feed = feedparser.parse(edit_entry)
            for entry in feed.entries:
                author = entry.author
                med_names.append(author)
                name = f"{med_names[0]}"
                value = {"link": edit_entry}
                dicts[name] = value

        elif 'substack' in entry:
            # for substack blogs
            if entry.endswith("/"):
                # if url contains '/'
                edit_entry = f"{entry}archive"
                # add archive
            else:
                edit_entry = f"{entry}/archive"

            value = {"link": edit_entry}
            # the style of the dictionary keypair

            res = requests.get(entry)
            res.raise_for_status()
            # bs4 to parse substack url
            # getting page name
            # defining style of dict keypair
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            result_name = soup.find_all("div", class_="topbar-content")
            for post in result_name:
                post_name = post.find("a", class_="navbar-title-link")
                sub_names.append(post_name.text)
                # parsing html and adding latest post name to list 'names'
                name = f"{sub_names[0]}"
                dicts[name] = value
        else:
            print("At present the sites that can be parsed is medium"
                  "and substack. If you want to add others, contribute to the "
                  "program or be patient until more options can be added.")

        print(f"saving: {edit_entry}")

        self.save_dicts(dicts)

    def save_dicts(self, dicts):
        """saving new entry to dicts."""

        with open(self.file, 'w+') as f:
            json.dump(dicts, f, indent=2)

        print("completed")

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
        'summary of selected newsletter. Syntax: <s> <index> \n'
        '(0 summarizes all newsletters)', aliases=['s'])

        parser_summary.add_argument('index', help=
        'choose # of newsletter to summarize.')

        parser_summary.set_defaults(func=self.summarize_chosen_article)

        # download arg
        parser_download = subparsers.add_parser('download', help=
        'downloading selected newsletters. Syntax: <d> <index>', aliases=['d'])

        parser_download.add_argument('index', help=
        'Choose # of newsletter to download')
        parser_download.set_defaults(func=self.download)

        # list arg
        parser_list = subparsers.add_parser('list', help=
        'displays list of newsletters that can be summarized and downloaded.'
        'Syntax: <l>',
                                            aliases=['l'])
        # list requires no index and will return a list of all headers

        parser_list.set_defaults(func=self.summary_headers)

        # delete arg
        parser_delete = subparsers.add_parser('delete', help=
        'delete newsletter from list. Syntax: <del> <index>', aliases=['del'])

        parser_delete.add_argument('index', help=
        'Choose # of newsletter to remove')

        parser_delete.set_defaults(func=self.remove_dictItem)
        # del is the action, index the number of the newsletter to delete
        # 'func' calls for the function within this class

        # add arg
        parser_add = subparsers.add_parser('add', help=
        'add newsletter to list. Syntax: <add> <url>\n'
        '| url format (examples): '
        'https://cobie.substack.com/archive, '
        'https://cobie.substack.com, '
        'https://cobie.substack.com/, '
        'https://medium.com/@TraderScarpa/feed, '
        'https://medium.com/@TraderScarpa/, '
        'https://medium.com/@TraderScarpa', aliases=['add'])

        parser_add.add_argument('url', help=
        'Choose url to add')

        parser_add.set_defaults(func=self.add_dict_item)

        args = parser.parse_args()
        args.func(args)

if __name__ == '__main__':
    sd = TextSummaryDownload()
    sd.parser_main()



