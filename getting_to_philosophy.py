import argparse
import urllib2
from bs4 import BeautifulSoup, SoupStrainer, Tag, NavigableString


class getting_to_philosophy:
   # To define filters for HTML page here
   def __init__(self):
      self.div_id = "searchTerm" # search for links
      self.content_tags = ['p', 'ul', 'ol'] # the tags (w/in div) we will look for links w/in
   
   # Get a GTP link from this page & return that link
   # Return False on a bad url or no links available
   def get_philosophy_link(self, url): 
      self.set_page(url)
      self.page_name = return_wiki_page_name(url)

      # for a bad url or bad wiki page
      if self.page == False or self.page_name == False:  
         return False   
      
      self.soup = self.set_parser()
      return self.philosophy_link() 

   # To follow a url and then set self.page
   def set_page(self,url):
      self.url = url
      self.page = follow_url(self.url)

   # Set the parser to the div we're interested in
   def set_parser(self):
      strained = SoupStrainer('div', id=self.div_id)
      return BeautifulSoup(self.page, parse_only=strained)

   def seek_to_first_paragraph(self):
      # start our search for link at the first paragraph under self.div_id
      first_link_containing_element = self.soup.find('p')

      # if the paragraph is in a table, skip it (this was breaking the /Human page...)
      while is_in_table(first_link_containing_element):
         first_link_containing_element = first_link_containing_element.find_next('p')

      # if there's no first paragraph, then we should broaden the search to include all our content tags 
      if first_link_containing_element == None:
         first_link_containing_element = soup.find(self.content_tags)
      
      return first_link_containing_element
   
   # Get the first link on this page that satisfies the criteria of not in parens, 
   # not italicized, not red and not the same page.
   # Return the full http://en.wikipedia.org/wiki/... link or return false if no such link exists. 
   def philosophy_link(self):
      current_page_element = self.seek_to_first_paragraph()

      while current_page_element != None:
         no_parenthesized_links = remove_parenthesized_links(current_page_element)
         all_links = no_parenthesized_links.find_all('a')
         #check whether the following conditions are fulfilled before returning the link
         for link in all_links:
            if link['href'].startswith("/wiki/"):  
               full_link = "http://en.wikipedia.org" + link['href']
               is_wiki = is_wiki_url(full_link)
               is_special = is_special_wiki_page(full_link) # in ordet to check if the page is a help page, file page,...
               is_same_page = return_wiki_page_name(full_link) == self.page_name
               italicized = is_italicized(link)
               if is_wiki and not is_special and not italicized and not is_same_page:
                  return full_link
         
         current_page_element = current_page_element.find_next(self.content_tags)

      return False

# Given a BeautifulSoup Tag, check its children to remove any anchor elements inside parentheses.  
# Return a new Beautiful soup representation of this section.
def remove_parenthesized_links(tag):
   without_parens = []
   in_parens = False

   # each HTML tag will be in an individual cell
   # Eg: ['<a href="http://example.com/">', 'I linked to a page', '</a>']
   subtree_list = tag_subtree_as_list(tag)

   in_anchor = False
   in_parens = False
   for element in subtree_list:
      in_tag = False
      if element.startswith("<"):
         in_tag = True
         if element.startswith("<a"):
            in_anchor = True
         elif element.startswith("</a>"):
            in_anchor = False

      # don't look for parenthesis in any type of tag element
      if not in_tag:  
         for char in element:
            if char == "(":
               in_parens = True
            elif char == ")":
               in_parens = False

      # append this element if it's not an anchor, or if it's an anchor that's not in parens
      if (not in_anchor or (in_anchor and not in_parens)):
         without_parens.append(element)

   return BeautifulSoup("".join(without_parens))  


# Return the page at the given URL.
# Return False and print the exception if the URL is not valid/followable.
def follow_url(url):
   try:
      page = urllib2.urlopen(url)
      return page
   except (ValueError, urllib2.URLError) as e:
      print e
      return False

# Following the rules of Getting to Philosophy, hop from a start wiki url, to a destination url.
# Output the links on the path and the number of hops.
# 'limit' caps the number of pages we can visit before giving up.
def hop_to_wiki_url(start_wiki_url, destination_wiki_url, limit):
   start_page_name = return_wiki_page_name(start_wiki_url)
   end_page_name = return_wiki_page_name(destination_wiki_url)
   
   # handle the case that we start at our destination
   if start_page_name == end_page_name:
      print "Looks like we started at our destination page:",start_wiki_url
      print "0 hops"
      return
   
   # create our philosophy_link fetching object
   philosophy_links = getting_to_philosophy()

   # grab our first url
   next_url = philosophy_links.get_philosophy_link(start_wiki_url)
   
   hops = 0
   print start_wiki_url   
   while next_url != False and hops < limit:
      print next_url
      page_name = return_wiki_page_name(next_url)
      hops = hops + 1  

      if page_name == end_page_name:
         print "Arrived"
         print hops,"hops"
         return 

      next_url = philosophy_links.get_philosophy_link(next_url)
  

   print "Looks like we hit our page-limit, a dead-end, a loop, or a bad link."
   print "Unknown no. of hops."
   return




