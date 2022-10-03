""" sources used: 
https://www.geeksforgeeks.org/loading-images-in-tkinter-using-pil/?ref=rp
https://tkdocs.com/tutorial/complex.html#labelframe
https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/
"""


#from cProfile import label
from tkinter import *
#from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image


def inputImage():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Image Files", "*.jpg")]
    )
    # opens the image
    img = Image.open(filepath)
     
    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 250), Image.ANTIALIAS)
 
    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)
  
    #destroy existing label and replace with painting label 
    greeting.destroy()
    btn.destroy()
    painting_lbl = Label(root, text="Your Painting:")
    painting_lbl.grid(column=0,row=0)

    # display the painting
    painting = Label(root, image = img)
    painting.image = img
    painting.grid(column = 1, row = 0)

    #create a label for the emotion
    emotion_lbl = Label(root, text="The Emotion Is:")
    emotion_lbl.grid(column=0,row=1)

    # display the emotion
    emotion_solution = StringVar()
    emotion_solution.set("sorry I don't know")

    emotion = Label(root, textvariable=emotion_solution)
    emotion.grid(column = 1, row = 1)

if __name__ == "__main__":
    #set up root
    root = Tk()
    root.title("Emotionizer 5000")
    root.geometry('700x400')

    #set up frame
    #mainFrame = ttk.Frame()

    #welcome page greeting
    greeting = Label(root, 
        text = "Welcome to Emotionizer!\n I can help you figure out the emotions of paintings!\nClick bellow to get started"
        )
    greeting.grid(column=1, row=0)


    # button widget with red color text inside
    btn = Button(root, 
        text = "Input Image",
        fg = "red",
        command=inputImage
        )
    # Set Button Grid
    btn.grid(column=1, row=1)

    root.mainloop()