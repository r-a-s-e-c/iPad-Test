from pyscript import display
from datetime import datetime

now = datetime.now()
display(now.strftime("%m/%d/%Y, %H:%M:%S"))
display("where will this dsiplay?" target="resultdiv")
