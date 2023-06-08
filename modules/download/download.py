import os

from moviepy.audio.io.AudioFileClip import AudioFileClip
from pytube import YouTube
from modules.base import Base


class Download(Base):
    def __init__(self, url: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url

    def download(self):
        # for i in YouTube(self.url).streams.all():
        #     print(i.audio_codec)
        stream = YouTube(self.url).streams.filter(only_audio=True).first()
        path = stream.download(filename=stream.default_filename)
        AudioFileClip(path).write_audiofile(path.replace('.mp4', '.wav'), 44100, 2, 2000, codec='pcm_s32le')
        os.remove(path)
        print(path.replace('.mp4', '.wav'))
        return path.replace('.mp4', '.wav')
