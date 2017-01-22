# -*- coding: utf-8 -*-
"""
@authors: kent and madeleine bonsma-fisher
based on: https://github.com/edgi-govdata-archiving/epa-eis/commit/f05a939b0ca6cc8d212f4a9d6969e05b7c39bee1
Description: 
---------
Usage: 
Example usage: 
---------
Installing Python:
- download and install Anaconda for your operating system (Python 3 is recommended) at this link:
 https://www.continuum.io/downloads
Anaconda contains Python, many common Python libraries, an IDE (Spyder)
and a command prompt (conda prompt).
Python libraries required:
- csv
- os
- sys
- urllib3
- BeautifulSoup
If any libraries are missing, run the following in the command prompt:
 pip install <libraryname>
 Example: pip install BeautifulSoup
 
Note: if using Windows, you'll need to use something other than the regular Windows command prompt. 
I recommend using conda prompt, included if you used Anaconda to get Python, or Git Bash.
"""

import csv
import os.path
import sys

import urllib3

# ------------------ functions --------------------

def url_to_divs(url):
    """
    This function takes a url (example: https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId=223815)
    and collects all the items that are of class "form-item" - this is the metadata we want.
    """
    import urllib3
    from bs4 import BeautifulSoup

    http = urllib3.PoolManager()
    r = http.request('GET', url)

    soup = BeautifulSoup(r.data, "lxml")
    
    mydivs = soup.findAll("div", { "class" : "form-item" })
    return mydivs

# ------------------------------------------------------------

# url 
base_url = "https://genius.com/"

song_url = "Shad-yaa-i-get-it-lyrics"
url = base_url+song_url

r = http.request('GET', url)
soup = BeautifulSoup(r.data, "lxml")

url2 = "https://genius.com/69162"
r2 = http.request('GET',url2)
soup2 = BeautifulSoup(r2.data, "lxml")

# find annotations
for annotation in soup.findAll("a"):
    print annotation.get("annotation-fragment")

# from annotation page, get annotation text
# the "content" tag contains the annotation.
# the "property" tag equal to "rap_genius:body" is the annotation text.
me = []
for m in soup2.findAll("meta"):
    me.append(m["content"])

