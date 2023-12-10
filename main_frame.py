from breezypythongui import EasyFrame

class MainFrame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="~Genshin Pity~")
        self.config(bg="darksalmon")