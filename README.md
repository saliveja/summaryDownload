# README

**Main program: summary_and_download.py**

## Introduction

- This program summarizes the latest article from sources focusing on
analysis of crypto markets and macro economics.
- The user can select which articles to download.
- The selected articles to download will be converted from html to pdf.
- The main program is: summary_and_download.py

**Articles included in the program:**

* [The Knower](https://theknower.substack.com/archive)
* [Wrong a lot](https://wrongalot.substack.com/archive)
* [Kyla](https://kyla.substack.com/archive)
* [Ansem](https://blknoiz06.substack.com/archive)
* [Cobie](https://cobie.substack.com/archive)
* [Scarpa](https://medium.com/@TraderScarpa/)
* [Hayes](https://cryptohayes.medium.com/)
* [Foo69](https://fooo69.medium.com/)
* [Godcomplex182](https://medium.com/@godcomplex182/)
* [cryptocreddy](https://medium.com/@cryptocreddy/)
* [0xgodking](https://medium.com/@0xgodking/)
* [Onchainwizard](https://onchainwizard.substack.com/archive)
* [No sleep](https://nosleep.substack.com/archive)
* [Kyle](https://0xfren.substack.com/archive)
* [The reading ape](https://thereadingape.substack.com/archive)
* [Nat](https://crypto.nateliason.com/)
* [Rain and coffee](https://rainandcoffee.substack.com/archive)
* [The Macro compass](https://themacrocompass.substack.com/archive)
* [Not boring](https://www.notboring.co/)

## Installation & Dependencies
```
$ git clone github.com/darkrenaissance/wiki
```

Save the program where you want your files downloaded (or modify code)
Anywhere on ~/PATH update, install wget, and install wkhtmltox tool:

```
$ sudo apt update
$ sudo apt install wget
$ wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd
$ sudo apt install ./wkhtmltox_0.12.6-1.focal_amd64.deb
```

**Install or update pip**

`$ pip install -U pip`

**Install requires modules**

Syntax for pip installations:

`pip3 install <NAME OF MODULE>`

These modules are needed to run the program:
- requests
- bs4
- spacy
- string
- heapq *(This module shall be a part of the standard library in Python)*
- pdfkit
- feedparser

**Issues with spacy module**

- Spacy can also be installed using `pip3 install -U spacy`
- Some distributions return: OSError: [E050] Can't find model 'en_core_web_sm'
- This is addressed [spaCy github page](https://github.com/explosion/spaCy/issues/4577)
- Type:
```
$ pip3 install spacy
$ python3 -m spacy download en_core_web_sm
```

## Run
```
$ cd ~/wiki/tools/newsletter_dwnl
$ python summary_and_download.py
```
