from modules.edit.effects.video.video_effect import VideoEffect


class Spectrum(VideoEffect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def edit(self, *args, **kwargs):
