
class Entity:       # Можно его тоже сделать абстрактным и от него создавать экземпляры
    def __init__(self, sound):
        self.sound = sound

    def play(self):
        return self.sound


class EQ(Entity):
    def __init__(self, eqed):
        self.eqed = eqed

    def play(self):
        return f"EQ[{self.eqed.play()}]"


class Compressor(Entity):
    def __init__(self, compressed):
        self.compressed = compressed

    def compress(self):
        return f"Compress[{self.compressed.play()}]"



