import sys
from InFormsXssFinder import InFormsXssFinder
from UrlXssFinder import UrlXssFinder

def main():

    if len(sys.argv) < 2:
        sys.stderr.write("Usage : __init__.py -url http://randomUrl.com")
        sys.exit(1)

    if sys.argv[1] == '-url':
        url = sys.argv[2]
    else:
        sys.stderr.write("First parameter must be '-url' followed by a valid login url.")
        sys.exit(1)

    inFormXssFinder = InFormsXssFinder(url)
    inFormXssFinder.findXss()

if __name__ == "__main__":
    main()

