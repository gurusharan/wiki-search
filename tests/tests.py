import urllib2
from bs4 import BeautifulSoup, SoupStrainer, Tag, NavigableString

# Quick test to determine if a url is a "red" link on wikipedia.
def is_red_link(url):
   if "redlink=1" in url:
      return True
   return False

# Quick test to determine if url is a Wiki help page
def is_help_page(url):
   if "Help:" in url:
      return True
   return False

# Quick test for a special page on wiki
def is_special_page(url):
   if "Special:" in url:
      return True
   return False

# Quick test to exclude Wikipedia files
def is_file_page(url):
   if "File:" in url:
      return True
   return False
   
 # Given a BeautifulSoup Tag, return True if its immediate parent is italicized.
def is_italicized(tag):
   return tag.find_parent().name == "i"

# Return True if a Beautiful Soup Tag is within a table.
def is_in_table(tag):
   for parent in tag.parents:
      if parent.name == 'td' or parent.name == 'tr' or parent.name == 'table':
         return True
   return False

# Return True is a wiki url is a help page, or a file page, or a special page... 
def is_special_wiki_page(url):
   is_red = is_red_link(url)
   is_help = is_help_page(url)
   is_special = is_special_page(url)
   is_file = is_file_page(url)
   return (is_red or is_help or is_special or is_file)


# Return True if 'url' is a URL to a page on english wikipedia else return false.
def is_wiki_url(url):
   valid_http_start = url.startswith("http://en.wikipedia.org/wiki/")
   valid_https_start = url.startswith("https://en.wikipedia.org/wiki/")
   if valid_http_start or valid_https_start:
      return True
   return False

# Given a wiki URL, return the name of that page & return false if 'wiki_url' is not a wiki page.
def return_wiki_page_name(wiki_url):
   if is_wiki_url(wiki_url):
      url_split = wiki_url.split("/wiki/")
      page_name = url_split[1]
      return page_name
   return False
