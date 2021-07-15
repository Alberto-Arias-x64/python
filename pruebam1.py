from pynput import mouse, keyboard
#defining function to print when key is pressed
def on_press(key):
  print('{0} pressed'.format(key))
  #if key == Key.esc:
  #  return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()