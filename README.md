# wiki-search
A project which aims at finding the path taken to get to 'philosophy' while doing a wiki search.

Installations:
a) Installing BeautifulSoup::
If you’re using a recent version of Debian or Ubuntu Linux, you can install Beautiful Soup with the system package manager:

$ apt-get install python-bs4 (for Python 2)

$ apt-get install python3-bs4 (for Python 3)

Beautiful Soup 4 is published through PyPi, so if you can’t install it with the system packager, you can install it with easy_install or pip. The package name is beautifulsoup4, and the same package works on Python 2 and Python 3. Make sure you use the right version of pip or easy_install for your Python version (these may be named pip3 and easy_install3 respectively if you’re using Python 3).

$ easy_install beautifulsoup4

$ pip install beautifulsoup4

(The BeautifulSoup package is probably not what you want. That’s the previous major release, Beautiful Soup 3. Lots of software uses BS3, so it’s still available, but if you’re writing new code you should install beautifulsoup4.)

If you don’t have easy_install or pip installed, you can download the Beautiful Soup 4 source tarball and install it with setup.py.

$ python setup.py install

If all else fails, the license for Beautiful Soup allows you to package the entire library with your application. You can download the tarball, copy its bs4 directory into your application’s codebase, and use Beautiful Soup without installing it at all.

b) Possible problems after installation::
Beautiful Soup is packaged as Python 2 code. When you install it for use with Python 3, it’s automatically converted to Python 3 code. If you don’t install the package, the code won’t be converted. There have also been reports on Windows machines of the wrong version being installed.

If you get the ImportError “No module named HTMLParser”, your problem is that you’re running the Python 2 version of the code under Python 3.

If you get the ImportError “No module named html.parser”, your problem is that you’re running the Python 3 version of the code under Python 2.

In both cases, your best bet is to completely remove the Beautiful Soup installation from your system (including any directory created when you unzipped the tarball) and try the installation again.

If you get the SyntaxError “Invalid syntax” on the line ROOT_TAG_NAME = u'[document]', you need to convert the Python 2 code to Python 3. You can do this either by installing the package:

$ python3 setup.py install

or by manually running Python’s 2to3 conversion script on the bs4 directory:

$ 2to3-3.2 -w bs4

c) Installing a parser::
Beautiful Soup supports the HTML parser included in Python’s standard library, but it also supports a number of third-party Python parsers. One is the lxml parser. Depending on your setup, you might install lxml with one of these commands:

$ apt-get install python-lxml

$ easy_install lxml

$ pip install lxml

Another alternative is the pure-Python html5lib parser, which parses HTML the way a web browser does. Depending on your setup, you might install html5lib with one of these commands:

$ apt-get install python-html5lib

$ easy_install html5lib

$ pip install html5lib


Requirements and usages:
i. argparse - argparse is a full command-line argument parser tool, and handles both optional and required arguments.

ii. urllib2 - The urllib2 module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.

iii. bs4(beautiful soup 4.4.0) - Beautiful Soup is a Python library(bundled package libs) for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.

iv. soupstrainer - Beautiful Soup turns every element of a document into a Python object and connects it to a bunch of other Python objects. If you only need a subset of the document, this is really slow. But you can pass in a SoupStrainer as the parseOnlyThese argument to the soup constructor. Beautiful Soup checks each element against the SoupStrainer, and only if it matches is the element turned into a Tag or NavigableText, and added to the tree.

v. Tag - A Tag object corresponds to an XML or HTML tag in the original document. Tags have a lot of attributes and methods.

vi. Navigable String - A string corresponds to a bit of text within a tag. Beautiful Soup uses the NavigableString class to contain these bits of text.

vii. logging(logging facility for python) - This module defines functions and classes which implement a flexible event logging system for applications and libraries. The key benefit of having the logging API provided by a standard library module is that all Python modules can participate in logging, so your application log can include your own messages integrated with messages from third-party modules.

viii. asyncio -  (Asynchronous I/O, event loop, coroutines and tasks). This module provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives.

ix. .http_utils - Simple wrapper for python stdlib httplib

x. diy_framework - DIY is an asynchronous microframework to further explore Python35+, software architecture. It is composed of a simple HTTP/1.1 async server and the actual framework.

xi. php Laravel -  Laravel utilizes ‘Composer’ to manage its dependencies. Install composer - https://getcomposer.org/ and download laravel installer using the command – composer global require “laravel/installer” (https://laravel.com/docs/5.4/installation) on your terminal. Download XAMPP - https://www.apachefriends.org/index.html and SequelPro -https://www.sequelpro.com/
