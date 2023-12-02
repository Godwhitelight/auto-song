import os
from typing import List

from moviepy.audio.io.AudioFileClip import AudioFileClip
from pedalboard_native.io import AudioFile

from modules.edit.compilers.compiler import Compiler
from modules.edit.effects.audio.moviepy_effect import MoviePyEffect
from modules.edit.effects.audio.pedal_effect import PedalEffect
from pedalboard import Pedalboard

from modules.edit.effects.effect import Effect


class SoundCompiler(Compiler):
    def __init__(self, effects: List[Effect], *args, **kwargs):
        super().__init__(effects, *args, **kwargs)

    def compile(self):
        plugins = [effect.edit() for effect in self.effects if isinstance(effect, PedalEffect)]
        board = Pedalboard(plugins=plugins)
        with AudioFile(self.filename) as f:
            audio = f.read(f.frames)
            samplerate = f.samplerate

        effected = board(audio, samplerate)

        with AudioFile('output/pedal-' + self.filename, 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)

        clip = AudioFileClip('output/pedal-' + self.filename)
        for effect in self.effects:
            if isinstance(effect, MoviePyEffect):
                clip = effect.edit(clip)

        # clip.close()
        clip.write_audiofile('output/output-' + self.filename)
        os.remove('output/pedal-' + self.filename)
        return 'output/output-' + self.filename



