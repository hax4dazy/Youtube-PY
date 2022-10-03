from __future__ import unicode_literals
import youtube_dl

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def main():
    #ask the user for their video link
    video_link = input("Enter the video link: ")

    #ask the user if the link is a playlist
    playlist = input("Is this a playlist? (y/n): ")

    #ask the user for what output format they want
    print('Please enter the format you want to convert to. Your choices are mp3, mp4 and flac. (default is mp4)')
    output_format = input("Enter the output format: ")
    if output_format == '':
        output_format = 'mp4'
    

    #download  the video
    if playlist == "y":
        match output_format:
            case "mp3":
                ytl_mp3_plist = {
                    'format': 'bestaudio/best',
                    'outtmpl': '%(title)s.%(ext)s',
                    'playlist': True,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                with youtube_dl.YoutubeDL(ytl_mp3_plist) as ydl:
                    ydl.download([video_link])
            case "mp4":
                ytl_mp4_plist = {
                    'format': 'mp4',
                    'outtmpl': '%(title)s.%(ext)s',
                    'playlist': True,
                }
                with youtube_dl.YoutubeDL(ytl_mp4_plist) as ydl:
                    ydl.download([video_link])
            case "flac":
                ytl_flac_plist = {
                    'format': 'bestaudio/best',
                    'outtmpl': '%(title)s.%(ext)s',
                    'playlist': True,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'flac',
                    }],
                }
                with youtube_dl.YoutubeDL(ytl_flac_plist) as ydl:
                    ydl.download([video_link])
    else:
        match output_format:
            case "mp3":
                ytl_mp3 = {
                    'format': 'bestaudio/best',
                    'outtmpl': '%(title)s.%(ext)s',
                    'playlist': False,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                with youtube_dl.YoutubeDL(ytl_mp3) as ydl:
                    ydl.download([video_link])
            case "mp4":
                ytl_mp4 = {
                    'format': 'mp4',
                    'outtmpl': '%(title)s.%(ext)s',
                    'playlist': False,
                }
                with youtube_dl.YoutubeDL(ytl_mp4) as ydl:
                    ydl.download([video_link])
            case "flac":
                ytl_flac = {
                    'format': 'bestaudio/best',
                    'outtmpl': '%(title)s.%(ext)s',
                    'playlist': False,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'flac',
                    }],
                }
                with youtube_dl.YoutubeDL(ytl_flac) as ydl:
                    ydl.download([video_link])

main()