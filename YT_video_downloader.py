from yt_dlp import YoutubeDL

def Download(link):
    ydl_opts = {}
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    except Exception as e:
        print(f"An error has occurred: {e}")
        return
    print("Download is completed successfully!")


def sanitize_url(url):
    if "&" in url:
        url = url.split("&")[0]
    return url

link = input("Enter the Youtube video URL: ")
link = sanitize_url(link)
Download(link)


