from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.fx.speedx import speedx

from modules.edit.effects.audio.moviepy_effect import MoviePyEffect


class Speed(MoviePyEffect):
    def __init__(self, speed: float = 1.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = speed

    def edit(self, clip: AudioFileClip):
        clip = clip.set_fps(clip.fps * self.speed)
        return clip.fx(speedx, self.speed)
