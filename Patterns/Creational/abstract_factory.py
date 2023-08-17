''' Обычно сперва создают класс Абстрактной фабрики, и от нее наследуются более узкие фабрики, сейчас пропустим '''


class EQsFactory:       # Factory is instance, not a methon
    def __init__(self):
        self._eqsfactory = [FabFilter(5, "Pro Q"), UAD(4, "UAD"), Waves(7, "Waves")]

    @property
    def eqs(self):
        return self._eqsfactory


class EQ:                   # main fabric
    def __init__(self, bands, name):
        self.bands = bands
        self.name = name

    @property
    def getBands(self):     # mandatory method for sub fabrics
        return self.bands


class FabFilter(EQ):

    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands


class Waves(EQ):

    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands


class UAD(EQ):

    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands

