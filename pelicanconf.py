#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = "Kili.io, Inc"
SITENAME = "Kili"
SITEURL = "http://help.kili.io"

TIMEZONE = "Africa/Nairobi"

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.rss.xml"
CATEGORY_FEED_ATOM = "feeds/%s.rss.xml"
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = (("kili", "http://kili.io"),)

# Social widget
SOCIAL = (("github", "http://github.com/kili"),
          ("twiter", "http://www.twiter.com/kili_cloud"),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True 

# global metadata to all the contents
#DEFAULT_METADATA = (('key', 'val'),)

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'img',
    'js',
    'css',
    'extra/robots.txt',
    'CNAME',
    ]

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

#kili specific prefs
GITHUB_URL = "http://github.com/kili/help.kili.io"
#DISQUS_SITENAME = "kilihelpdocs"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (1969, 12, 31, 23, 59, 59) 
THEME = "pelican-kili-theme"
HIDE_SIDEBAR = True
CUSTOM_CSS = 'css/kili.css'
SHOW_ARTICLE_AUTHOR = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARCHIVES_ON_MENU = False
DEFAULT_DATE_FORMAT = ('%B %d, %Y')
