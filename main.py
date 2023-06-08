from modules.download.download import Download
from modules.edit.compilers.sound import SoundCompiler
from modules.edit.compilers.video import VideoCompiler
from modules.edit.effects.audio.reverb import Reverb
from modules.edit.effects.audio.speed import Speed

# path = Download('https://www.youtube.com/watch?v=MoN9ql6Yymw').download()
path = 'output/Daylight.wav'
compiler = VideoCompiler([Reverb(), Speed(1.5)], path.split('\\')[-1].split('.')[0] + '.wav')
compiler.compile()
