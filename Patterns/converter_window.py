from tkinter import *
from Structural.adapter import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Converter window")
        self.geometry("400x200")

        self.button = Button(self, text="Audio", command=self.play_audio)
        self.button.pack(expand=True)

        self.button = Button(self, text="Midi", command=self.play_midi)
        self.button.pack(expand=True)

    def play_audio(self):
        track = AudioTrack()
        track.audio_record()

    def play_midi(self):
        track = AudioToMidiAdapter()
        track.audio_record()




