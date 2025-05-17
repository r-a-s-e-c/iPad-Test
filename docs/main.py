from pyscript import display
from datetime import datetime

now = datetime.now()
display(now.strftime("%m/%d/%Y, %H:%M:%S"))
html_str = "<b>where will this display?</b>"

def print_message():
    display(html_str, target="resultdiv")
