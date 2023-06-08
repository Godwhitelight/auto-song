from modules.edit.edit_module import Edit
from pedalboard import Reverb as ReverbPlugin
from modules.edit.effects.audio.pedal_effect import PedalEffect


class Reverb(PedalEffect):
    """
    Reverb effect

    An effect that adds reverberation to the audio
    reverberation is the persistence of sound after the sound is produced.


    :param room_size: The room size of the reverb effect
    :param damping: The damping of the reverb effect
    :param wet_level: The wetness of the reverb effect
    :param dry_level: The dryness of the reverb effect
    :param width: The width of the reverb effect
    :param freeze_mode: The freeze mode of the reverb effect

    :type room_size: float
    :type damping: float
    :type wet_level: float
    :type dry_level: float
    :type width: float
    :type freeze_mode: float

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def edit(self):
        return ReverbPlugin(*self.args, **self.kwargs)
