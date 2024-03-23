from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url, on_progress_callback=progress_function)
        stream = yt.streams.get_highest_resolution()
        print("Rozpoczynam pobieranie...")
        stream.download()
        print("Pobieranie zakończone pomyślnie!")
    except Exception as e:
        print(f"Błąd: {str(e)}")

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = (bytes_downloaded / total_size) * 100
    print(f"Pobieranie... {progress:.2f}%")

def main():
    # URL filmu YouTube
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Możesz zmienić ten URL na dowolny inny
    download_video(url)

if __name__ == "__main__":
    main()
