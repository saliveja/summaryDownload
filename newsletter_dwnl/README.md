# README

**Main program: summary_and_download.py**

## Introduction

- This program summarizes the latest article from sources focusing on
analysis of crypto markets and macro economics.
- The user can select which articles to summarize and download, add newsletters
to list or remove unwanted ones.
- The selected articles to download will be converted from html to pdf.
- The main program is: summary_and_download.py
- The syntax is: **summarydownload.py <s/summary/d/download/add/delete/del> <-h>/<i><br>**

<h2>examples</h2> <br>

Summarize first article
```
$ summarydownload.py s 1 
```
Download the fifth article

```
$ summarydownload d 5 
```

Using help (observe that help had -h and not only the letter)

```
$ summarydownload.py s -h
```


## Installation & Dependencies
```
$ git clone github.com/darkrenaissance/wiki
```

Save the program where you want your files downloaded (or modify code)
Anywhere on ~/PATH update, install wget, and install wkhtmltox tool:

```
$ sudo apt update
$ sudo apt install wget
$ wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6.1-2.bullseye_amd64.deb 
$ sudo apt install ./wkhtmltox_0.12.6-1.focal_amd64.deb
(The two last commands are including packages for Ubuntu. Please check needed package for your OS here: 
https://wkhtmltopdf.org/downloads.html)
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
- json
- argparse
- os
- glob
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
$ cd ~/summaryDownload/newsletter_dwnl
$ python summary_and_download.py <s/summary/d/download/add/delete/del> <-h>/<i>
```
