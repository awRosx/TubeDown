from pytube import YouTube

print('Please, add your link to Youtube video!')
link = input()
yt = YouTube(link)

print('Title: ', yt.title)
print('View: ', yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('/videos')
print("Download complete!")
