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
import tensorflow as tf
import numpy as np

class_names = ['amusement', 'anger', 'awe', 'contentment', 'disgust', 'excitement', 'fear', 'sadness']

def inputImage():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    # opens the image
    img = Image.open(filepath).convert('RGB')
     
    # resize the image and apply a high-quality down sampling filter
    img2 = img.resize((120, 120), Image.ANTIALIAS)
    scale = 300/img.height
    if img.width*scale>400:
        scale = 400/img.width
    img = img.resize((int(img.width*scale), int(img.height*scale)), Image.ANTIALIAS)
 
    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)
  
    #destroy existing label and replace with painting label 
    greeting.destroy()
    # btn.destroy()
    painting_lbl = Label(root, text="Your Painting:")
    painting_lbl.grid(column=0,row=0)

    # display the painting
    painting.configure(image = img)
    painting.image = img
    painting.grid(column = 1, row = 0)

    # load the model and predict
    predictions = predictImage(img2)
    # score = tf.nn.softmax(predictions[0])
    predicted_class = class_names[np.argmax(predictions)]
    confidence = '%.2f'%(100*np.max(predictions))

    #create a label for the emotion
    emotion_lbl = Label(root, text="The Emotion Is: ")
    emotion_lbl.grid(column=0,row=1)

    # display the emotion
    emotion_solution = StringVar()
    emotion_solution.set(predicted_class)

    # emotion = Label(root, textvariable=emotion_solution)
    emotion.configure(textvariable=emotion_solution)
    emotion.grid(column = 1, row = 1)

     #create a label for the confidence
    confidence_lbl = Label(root, text="with a confidence of: ")
    confidence_lbl.grid(column=2,row=1)


    # display the confidence
    confidence_solution = StringVar()
    confidence_solution.set(confidence)

    # conf = Label(root, textvariable=confidence_solution)
    conf.configure(textvariable=confidence_solution)
    conf.grid(column = 3, row = 1)

def predictImage(img):
    model = tf.keras.models.load_model('model-10-acc_0.3222-valacc_0.2055.h5')
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    return predictions

if __name__ == "__main__":
    #set up root
    root = Tk()
    root.title("Emotionizer 5000")
    root.geometry('700x400')

    #set up frame
    #mainFrame = ttk.Frame()
    painting = Label(root, image = '')
    painting.image = ''
    emotion = Label(root, textvariable='')
    conf = Label(root, textvariable='')
    #welcome page greeting
    greeting = Label(root, 
        text = "Welcome to Emotionizer!\n I can help you figure out the emotions of paintings!\nClick below to get started"
        )
    greeting.grid(column=1, row=0)


    # button widget with red color text inside
    btn = Button(root, 
        text = "Input Image",
        fg = "red",
        command=inputImage
        )
    # Set Button Grid
    btn.grid(column=1, row=2)

    root.mainloop()