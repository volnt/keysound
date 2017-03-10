import math

from pyaudio import PyAudio


class Audio(PyAudio):

    def __init__(self, bitrate=16000):
        PyAudio.__init__(self)

        self.bitrate = bitrate
        self.stream = self.open(format=self.get_format_from_width(1), channels=1, rate=self.bitrate, output=True)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        for stream in self._streams.copy():
            stream.stop_stream()

        self.terminate()

    def play(self, frequency, length):
        frames = ''.join([chr(int(math.sin(bit / ((self.bitrate / frequency) / math.pi)) * 127 + 128))
                          for bit in xrange(int(self.bitrate * length))])
        self.stream.write(frames)
