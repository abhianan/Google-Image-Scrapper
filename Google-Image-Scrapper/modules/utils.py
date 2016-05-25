# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:41:18 2016

@author: ananab06
"""

from __future__ import unicode_literals

import time
from selenium import webdriver
import urllib2
from urllib import urlencode

def _get_search_url(query, page=0, per_page=10, lang='en'):

    params = {'nl': lang, 'q': query.encode(
        'utf8'), 'start': page * per_page, 'num': per_page}
    params = urlencode(params)
    url = u"http://www.google.com/search?" + params
    return url


def get_html(url):
    header = "Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0) Gecko/25250101"
    try:
        request = urllib2.Request(url)
        request.add_header("User-Agent", header)
        html = urllib2.urlopen(request).read()
        return html
    except urllib2.HTTPError as e:
        print "Error accessing:", url
        if e.code == 503 and 'CaptchaRedirect' in e.read():
            print "Google is requiring a Captcha. " \
                  "For more information see: 'https://support.google.com/websearch/answer/86640'"
        return None
    except Exception as e:
        print "Error accessing:", url
        print e
        return None


def get_browser_with_url(url, timeout=120, driver="firefox"):
    """Returns an open browser with a given url."""

    # choose a browser
    if driver == "firefox":
        browser = webdriver.Firefox()
    elif driver == "ie":
        browser = webdriver.Ie()
    elif driver == "chrome":
        browser = webdriver.Chrome()
    else:
        print "Driver choosen is not recognized"

    # set maximum load time
    browser.set_page_load_timeout(timeout)

    # open a browser with given url
    browser.get(url)

    time.sleep(0.5)

    return browser