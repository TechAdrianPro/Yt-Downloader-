import tkinter as tk
from pytube import YouTube

def download_video():
    try:
        url = url_entry.get()
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        status_label.config(text="Pobieranie zakończone pomyślnie!")
    except Exception as e:
        status_label.config(text=f"Błąd: {str(e)}")

# Tworzenie interfejsu Tkinter
root = tk.Tk()
root.title("Pobieranie filmów z YouTube")

url_label = tk.Label(root, text="Wprowadź adres URL filmu YouTube:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

download_button = tk.Button(root, text="Pobierz", command=download_video)
download_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
