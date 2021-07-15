#from pynput.mouse import *
from pynput import mouse, keyboard
#mouse = Controller()

# Press and release
#mouse.press(Button.left)
#mouse.release(Button.left)

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    if not pressed:
        # Stop listener
        return True

# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
#listener = mouse.Listener(on_click=on_click)
#listener.start()