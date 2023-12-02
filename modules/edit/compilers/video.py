from typing import List

import numpy as np
from moviepy.video.VideoClip import VideoClip, ImageClip
import matplotlib.pyplot as plt

from modules.edit.compilers.sound import SoundCompiler
from modules.edit.effects.effect import Effect


class VideoCompiler(SoundCompiler):
    def __init__(self, effects: List[Effect], filename, *args, **kwargs):
        super().__init__(effects, filename, *args, **kwargs)

    def compile(self):
        audio_clip = super().compile()
        print(audio_clip)

