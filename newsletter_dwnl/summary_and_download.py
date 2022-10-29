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
from pprint import pprint
import argparse
import sys
import numpy as np
import pandas as pd
from tabulate import tabulate

class TextSummaryDownload:
    """program that on selection summarize and download newsletters."""

    def __init__(self):
        """initializing."""
        self.index = index
        self.dicts = get_dicts()
        self.link = link

    def print_help_message(self):
        """print help text and description"""

        print("This is a program to summarize and download selected newsletters.\n"
              "When selecting action you should only specify one argument.\n\n")

        data = [['-i <index>', 'Summarizes selected newsletter'],
                ['-d <download>', 'Downloading selected newsletter'],
                ['-l <list>', 'Returns the list of newsletter']]
        info = tabulate(data, headers=["cmd", "syntax: summary_and_download.py "
                                              "<index> <download> <list> (one pos arg)",
                                       " ", " "])
        print(info)

    def get_dicts(self):
        file = 'dict.json'
        with open(file, 'r+') as f:
            dicts = json.load(f)

        return dicts

    # def display_summary_list(self, args):
    #     """command -l in parser"""
    #     if args.list:
    #         display_summary_headers()

    def summary_headers(self):
        """Prints an enumerated list of all authors to choose summary of"""

        print("\n")

        for i, item in enumerate(self.dicts, 1):
            print(f"{i} - {item.strip()}")
        print("\n")

    # def display_sumall(self, args):
    #     """-sa in parser, summary of all articles."""
    #
    #     if args.sumall:
    #         all_articles_summary()

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

    # def display_summary(self, args):
    #     """-s in parser. Displays summary of selected newsletters."""
    #
    #     if args.summary:
    #         summarize_chosen_article()

    def summarize_chosen_article(self):
        """Displays a summary of an article based on users choice"""

        for i, (item, dct) in enumerate(self.dicts.items()):
            if i == args.index:
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

    def download(self, choice=100):
        """Downloading selected article."""

        while True:
            if choice == 100:
                choice = args.index

            for i, (item, dct) in enumerate(self.dicts.items()):
                if i == choice:
                    name = item
                for key, index in dct.items():
                    link = dct["link"]

                if link.endswith('feed'):
                    dm.download_medium(link)
                else:
                    d.article_download(link)

    # def delete_newsletter(self):
    #     """-del in parser. Delete selected newsletter."""
    #
    #     if args.delete:
    #         remove_dictItem()

    def remove_dictItem(self):
        """Removing key and value from dictionary"""

        dict_copy = copy.copy(self.dicts)

        for i,  item in enumerate(dict_copy.keys()):
            if i == choice:
                choice = item
                del self.dict[choice]
                print(f"You removed {choice}")

                print("\n")
                for i, item in enumerate(dict_copy, 1):
                    print(f"{i} - {item.strip()}")
                    print("\n")

    def parser_main(self):
        """argparser - storing arguments and setting default functions."""
        parser = argparse.ArgumentParser(
            prog='Newsletter summary and download',
            description='summary and download of selected newsletters')

        parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
        subparsers = parser.add_subparsers(
            help="{subcommand}[-h] shows all the options")

        # summary arg
        parser_summary = subparsers.add_parser('summary', help=
        'summary of selected newsletter', aliases=['s'])

        parser_summary.add_argument('i', 'index', help=
        'summary of selected newsletters', action='store_true')

        parser_summary.add_argument('a', 'sumall', help=
        'summary of all newsletters', action='store_true')
        parser_summary.set_defaults(func=summarize_chosen_article)


        # download arg
        parser_download = subparsers.add_parser('download', help=
        'downloading selected newsletters', aliases=['d'])

        parser_download.add_argument('i', 'index', help=
        'downloading selected newsletters', action='store_true')
        parser_download.set_defaults(func=download)


        # list arg
        parser_list = subparsers.add_parser('list', help=
        'displays list of newsletters that can be summarized and downloaded',
                                            aliases=['l'])

        parser_list.add_argument('i', 'index', help=
        'displays list of newsletters that can be summarized and downloaded',
                                 action='store_true')
        parser_list.set_defaults(func=summary_headers)

        ## edit arg
        # parser_edit = subparser.add_parser('edit', help=
        # 'edit newsletter list', aliases=['e'])
        # parser_edit.set_defaults(func=remove_dictItem)



        parser.parse_args()
        args.func(args)

if __name__ == '__main__':
    sd = TextSummaryDownload()
    sd.parser_main()