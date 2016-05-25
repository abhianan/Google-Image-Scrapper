# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:41:18 2016

@author: ananab06
"""

from __future__ import unicode_literals

from modules import images
from modules import standard_search

search = standard_search.search
search_images = images.search

if __name__ == "__main__":
    import doctest
    doctest.testmod()
