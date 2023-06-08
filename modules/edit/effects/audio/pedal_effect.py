from pedalboard import Plugin

from modules.edit.effects.audio.audio_effect import AudioEffect


class PedalEffect(AudioEffect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def edit(self) -> Plugin:
        raise NotImplementedError
