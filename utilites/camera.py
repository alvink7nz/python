import cv2
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk
from time import sleep

def capture_image(cap:cv2.VideoCapture):
    sleep(1)
    ret, frame = cap.read()
    if ret:
        name = askstring("Name", "Enter name of picture")
        if name:
            cv2.imwrite(f"c:/Users/alvin/Downloads/Pictures/{name}.jpg", frame)
            messagebox.showinfo("Info", "Image captured successfully!")
    else:
        messagebox.showerror("Error", "Failed to capture image.")

def main():
    root = tk.Tk()
    root.title("Camera with Capture")

    # Open the default camera (usually the first one)
    cap = cv2.VideoCapture(0)
    
    # Check if the camera opened successfully
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not open camera.")
        root.destroy()  # Close the Tkinter window if the camera fails to open
        return
    
    # Function to capture an image when the button is clicked
    capture_btn = tk.Button(root, text="Capture", command=lambda: capture_image(cap))
    capture_btn.pack()

    # Function to continuously display the camera feed
    def update():
        ret, frame = cap.read()
        if ret:
            # Convert the frame from BGR to RGB for displaying with Tkinter
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Resize the frame to fit the window
            frame_resized = cv2.resize(frame_rgb, (640, 480))
            # Convert the frame to an ImageTk object
            img = ImageTk.PhotoImage(image=Image.fromarray(frame_resized))
            # Update the label with the new image
            camera_label.img = img
            camera_label.config(image=img)
        # Schedule the update function to run after 10 milliseconds
        root.after(10, update)
    
    # Label to display the camera feed
    camera_label = tk.Label(root)
    camera_label.pack()
    
    # Start the update function to continuously update the camera feed
    update()
    
    root.mainloop()
    
    # Release the camera when the Tkinter window is closed
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
