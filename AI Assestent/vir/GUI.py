from tkinter import*
from PIL import Image , ImageTk
import speech_to_text
import action
root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False , False)
root.config(bg="#6F8FAF")


# ====== Functions ======
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END , 'User--->'+ user_val+"\n")
    if bot_val != None:
        text.insert(END , "BOT <---"+str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()

def User_send():
    User_send = entry.get()
    bot = action.Action(User_send)
    text.insert(END , 'User--->'+ User_send+"\n")
    if bot != None:
        text.insert(END , "BOT <---"+str(bot)+"\n")
    if bot == "ok sir":
        root.destroy()

    
    #print("Send button clicked!")

def delete_text():
    text.delete('1.0' , "end")
    #print("Delete button clicked!")  




#frame
frame = LabelFrame(root , padx= 50 ,  pady= 20 , borderwidth= 2 ,  relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row = 0 ,  column= 1 ,  padx= 55 ,  pady =  30)


# text label
text_lable = Label(frame, text = "AI Assistant" , font=("comic Sans ms" ,  14 , "bold" ) , bg = "#356696")
text_lable.grid(row= 0 ,  column= 0 , padx= 10 , pady= 10)

# image
# image = ImageTk.PhotoImage(Image.open("image/assistent.png"))
# image_lable = Label(frame, image= image)
# image_lable.grid(row = 1 ,  column= 0 , pady= 20)

img = Image.open("image/assistent.png")
img = img.resize((300, 300), Image.LANCZOS)
image = ImageTk.PhotoImage(img)
image_label = Label(frame, image=image, bg="#6F8FAF")
image_label.grid(row=1, column=0, pady=20)

# adding a text widget

# text = Text(root , font= ('courier 10 bold') , bg = "#356696")
# text.grid(row= 2 , column= 0)
# text.place(x = 85 , y = 400 , width = 380 , height = 100)

text = Text(root,
            font=('Courier', 10, 'bold'),
            bg="#356696",
            fg="white",
            relief="ridge",
            wrap="word")
text.place(x=69, y=480, width=380, height=70)


# entry widget

entry = Entry(root,
              font=('Courier', 11),
              bg="#DDE6ED",
              fg="black",
              relief="sunken",
              justify="center")
entry.place(x=100, y=560, width=290, height=30)

# buttons

# ==== Buttons Section ====

button1 = Button(root, text="ASK", bg="#356696", fg="white",
                 font=("Comic Sans MS", 10, "bold"),
                 pady=10, padx=25, borderwidth=3, relief=SOLID,
                 command=ask)
button1.place(x=70, y=610)

button3 = Button(root, text="Delete", bg="#356696", fg="white",
                 font=("Comic Sans MS", 10, "bold"),
                 pady=10, padx=25, borderwidth=3, relief=SOLID,
                 command=delete_text)
button3.place(x=225, y=610)

button2 = Button(root, text="Send", bg="#356696", fg="white",
                 font=("Comic Sans MS", 10, "bold"),
                 pady=10, padx=25, borderwidth=3, relief=SOLID,
                 command=User_send)
button2.place(x=380, y=610)







root.mainloop()