'''
webbrowser     : Comes with Python and opens a browser to a specific page.

sys            : used for reading potential command line arguments.

requests       : Downloads files and web pages from the internet.

beautiful soup : Parses HTML, the format that web pages are written in.

selenium       : Launches and controls a web browser. Selenium is able to
                 fill in forms and simulate mouse clicks in this browser.
'''

# 11 - MapIt.py
# Gets a street address from the command line arguments or clipboard.
# Opens the web browser to the Google Maps page for the address.

import webbrowser as wb
import sys
import pyperclip
# Need to install pyperclip

# A web browser tab will open to the url stated.
# This is about the only thing the webbrowser module can do.

# If this list has more than just the filename in it,
# then len(sys.argv) evaluates to an integer greater than 1,
# meaning that command line arguments have indeed been provided.

if len(sys.argv) > 1:
    
    # Get address from command line
    # The sys.argv variable stores a list of the program's file name
    # and command line arguments.
    
    address = " ".join(sys.argv[1:])

    # sys.argv[1:] chops off the first element in the array
    # (which would be MapIt.py)
else:
    # Get address from clipboard
    address = pyperclip.paste()

wb.open('https://www.google.com/maps/place/' + address)







    
