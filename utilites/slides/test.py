from pynput import mouse

# Function to handle mouse click events
def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")

# Create an instance of Listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
