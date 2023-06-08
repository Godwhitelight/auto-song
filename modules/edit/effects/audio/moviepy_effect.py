from moviepy.audio.io.AudioFileClip import AudioFileClip

from modules.edit.effects.audio.audio_effect import AudioEffect


class MoviePyEffect(AudioEffect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def edit(self, clip: AudioFileClip) -> AudioFileClip:
        raise NotImplementedError
