import yt_dlp

URLS = ['Song Links Go Here'
        ]

opts = {'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        # 'outtmpl': r'%(playlist_index)s-%(title)s.%(ext)s',   # Number playlists songs
        'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
            }]
        }

with yt_dlp.YoutubeDL(opts) as ydl:
    ydl.download(URLS)