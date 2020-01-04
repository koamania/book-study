from chapter6.Diva import Diva


class Miku(Diva):
    def __init__(self, module="class uniform"):
        self.module = module
        super().__init__("Miku")

    def dance(self):
        print("Dancing")

if __name__ == '__main__':
    hatsune_miku = Miku()
    print(hatsune_miku.module)
    print(hatsune_miku.version)
    print(hatsune_miku.name)
    hatsune_miku.dance()
    hatsune_miku.song("Hello worker")