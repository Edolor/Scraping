"""Searches for the href tag in a given html file given the url.
Catches a network down error and an invalid url entered error.
"""
import re
import urllib.request

def display(contents):
    """Check for a tag and print the output if found."""
    if contents:
        contents = str(contents)
        href_regex = re.compile(r"href=\".*?\"")
        href_group = href_regex.findall(contents)
        if href_group:
            for href in href_group:
                print(href)

def locate_hrefs(url):
    """Prints all href tags, found in the url provided."""
    contents = ""
    try: 
        html = urllib.request.urlopen(url)
    except Exception as error_message:
        error_message = str(error_message)
        # -3 stands for failure in name resolution.
        # -2 stands for name or service not known.
        err_regex = re.compile(r"(-3)|(-2)")
        err_group = err_regex.search(error_message)

        if err_group != None:
            if err_group.group(1) == "-3":
                print("Could not establish a connection, your internet service may be down.")
            elif err_group.group(2) == "-2":
                print("Invalid url entered.")
    else:
        contents = html.read()
        display(contents)
        #print(contents)

url = "https://docs.python.org/3/library/urllib.html"
locate_hrefs(url)
