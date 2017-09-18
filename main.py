import argparse
import urllib2

if __name__ == "__main__":
   # build command-line parser
   parser = argparse.ArgumentParser(description='Getting to philosophy on Wikipedia.')
   parser.add_argument('STARTING_LINK', help='Link to English Wikipedia page to start hopping (http://en.wikipedia.org/wiki/some_page).')

   # parse command line arguments
   args = parser.parse_args() 


   # Check input url.. and try to follow the starting link to a webpage
   first_wiki = follow_url(args.STARTING_LINK)

   if first_wiki == False:
      print "Error following given link."
      print "Please enter a valid (English wikipedia) URL, http://en.wikipedia.org/wiki/some_page"
      print "Exiting..."
      exit() 

   # Check if the starting link is a wiki page
   if not is_wiki_url(args.STARTING_LINK):
      print "Starting link must be some to wikipedia page."
      print "Please enter a valid (English wikipedia) URL, http://en.wikipedia.org/wiki/some_page"
      print "Exiting..."
      exit() 


   destination_wiki = "http://en.wikipedia.org/wiki/Philosophy"
   limit = 100
   hop_to_wiki_url(args.STARTING_LINK, destination_wiki, limit)