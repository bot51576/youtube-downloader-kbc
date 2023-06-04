from pytube import YouTube


def youtube_downloader(url: str, path: str):
    yt = YouTube(url)
    if path is None:
        yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download('./videos')
        
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download(path)
