from pytube import YouTube

while True:
    t = input("Enter url:")
    yt = YouTube(t)
    print(yt.title)
    if input("Download video? (y/n)") == "y":
        q = input("Video/Sound (v/s)")
        if q == "v":
            vid = yt.streams.get_highest_resolution()
        elif q == "s":
            vid = yt.streams.get_audio_only()
        else:
            print("failed successfully")
            continue
        print("downloading from youtube.com")
        file = vid.download()
        print("download finished")
    else:
        print("failed successfully")
