import yt_dlp

URLS = ['https://www.youtube.com/watch?v=sAWOKzqsxo0&list=WL&index=46',
        'https://www.youtube.com/watch?v=NNYWht50APM&list=WL&index=6'
      ]
        
opts = {"noplaylist": True,
        'format': 'best/bestvideo+bestaudio',
        "cookiesfrombrowser": ("firefox",),
        }

with yt_dlp.YoutubeDL(opts) as ydl:
    ydl.download(URLS)
