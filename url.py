import tkinter
import pyshorteners

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0, short_url))


root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("300x150")


longurl_label = tkinter.Label(root, text="Enter your URL",font="impack 20 bold",bg="black",fg="red")
longurl_label.pack(pady="20")
longurl_entry = tkinter.Entry(root,font="10",bd=3,width=120,bg="yellow")
shorturl_label=tkinter.Label(root, text="Output shortened URL",font="impack 20 bold",bg="black",fg="cyan",pady="1")
shorturl_entry = tkinter.Entry(root,font="10",bd=3,width=30,bg="cyan")
shorten_button = tkinter.Button(root, text="click me", command=shorten,bg="black",fg="cyan")

longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()

root.mainloop()