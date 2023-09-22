from abc import ABC, abstractmethod


class Audio(ABC):
    @abstractmethod
    def audio_record(self):
        pass


class Midi(ABC):
    @abstractmethod
    def midi_track(self):
        pass


class AudioTrack(Audio):
    def audio_record(self):
        print("Audio is playing..")


class MidiTrack(Midi):
    @abstractmethod
    def midi_track(self):
        print("Midi is playing..")


class AudioToMidiAdapter(Audio):        # Создаем класс Адаптор, Переопределяем обязательный метод
    def __init__(self):                 # и вызываем в нем метод из другого класса
        self.midi = MidiTrack()

    def audio_record(self):
        self.midi.midi_track()

