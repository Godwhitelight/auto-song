import numpy as np
from moviepy.video.VideoClip import VideoClip, ImageClip
import matplotlib.pyplot as plt

from modules.edit.compilers.sound import SoundCompiler


class VideoCompiler(SoundCompiler):
    def __init__(self, effects, filename, *args, **kwargs):
        super().__init__(effects, filename, *args, **kwargs)

    def compile(self):
        audio_clip = super().compile()
        video_clip = VideoClip()
        video_clip.set_audio(audio_clip)

        duration = audio_clip.duration
        samplerate = audio_clip.fps
        window = 1  # time window to analyze in seconds
        samplecount = int(duration)  # number of time windows to process
        signalscale = 0.01  # signal scale factor

        for num in range(samplecount):
            print('Processing from {} to {} s'.format(num * window, (num + 1) * window))
            signal = np.array([])
            # Read the signal according to the sample rate and convert it into a workable format
            readframes = np.fromstring(audio_clip.get_frame(samplerate), dtype=np.int16)
            # obtain left and right channels and times them by the signal scale so they smaller
            left, right = readframes[0::2] * signalscale, readframes[1::2] * signalscale
            # concat them
            signal = np.concatenate((signal, (left + right) / 2))
            # Plot the signal.
            plt.figure()
            a = plt.subplot(frameon=False)
            # set limits to make it look nicer
            a.set_ylim([-20000, 20000])
            # set the x axis
            x = np.arange(44100 * window) / 44100
            # split the plot into ten different parts each represensting a 20th of a second x for time,signal for signal
            y = np.split(x, 20)
            m = np.split(signal, 20)
            plt.axis('off')
            # position the plot WITHOUT the axis and white background
            fig = plt.gcf()
            fig.patch.set_alpha(0.0)
            fig.set_size_inches(9, 9)
            # combine the split segmets by plotting each and converting each to an imageclip
            for i in range(0, 19):
                plt.plot(y[i], m[i], color='yellow', linewidth=2)

                fig.canvas.draw()

                # Get the RGBA buffer from the figure
                w, h = fig.canvas.get_width_height()
                buf = np.frombuffer(fig.canvas.tostring_argb(), dtype=np.uint8)
                buf.shape = (w, h, 4)

                # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
                buf = np.roll(buf, 3, axis=2)

                # clips = imagetoclip(buf, video_clip, num + ((i + 1) / 10))
                frame = ImageClip(buf)
                # Set the start and end time
                frame = frame.set_start(currenttime)

                frame = frame.set_end(currenttime + 0.05)
                # append to the clips array
                clips.append(frame)
                # combine EVERY clip we have plotted so far to avoid bugs with the composite video function

        clips = concatenate(clips, method="compose")


