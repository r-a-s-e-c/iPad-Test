from pyscript import display, document
from datetime import datetime

now = datetime.now()
display(now.strftime("%m/%d/%Y, %H:%M:%S"))
html_str = "<b>where will this display?</b>"

def print_message(*args):
    display(html_str, target="resultdiv")

touch_area = document.querySelector("#touch-area")
status_display = document.querySelector("#status")
start_x = 0
start_y = 0

def touch_start(event):
    nonlocal start_x, start_y
    status_display.innerText = "Touch started"
    start_x = event.touches[0].clientX
    start_y = event.touches[0].clientY

def touch_end(event):
    nonlocal start_x, start_y
    status_display.innerText = "Touch ended"
    end_x = event.changedTouches[0].clientX
    end_y = event.changedTouches[0].clientY
    delta_x = end_x - start_x
    delta_y = end_y - start_y

    if abs(delta_x) > 50 or abs(delta_y) > 50:
        if abs(delta_x) > abs(delta_y):
            if delta_x > 0:
                status_display.innerText = "Swipe right"
            else:
                status_display.innerText = "Swipe left"
        else:
            if delta_y > 0:
                status_display.innerText = "Swipe down"
            else:
                status_display.innerText = "Swipe up"
    start_x = 0
    start_y = 0

touch_area.addEventListener("touchstart", touch_start)
touch_area.addEventListener("touchend", touch_end)
