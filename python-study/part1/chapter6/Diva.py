class Diva:
    version = "v3"

    def __init__(self, name="Diva"):
        self.name = name

    def song(self, title="song"):
        print(self.name + " sing the " + title)

    def medley(self):
        self.song()
        self.song("second song")
        self.song("third song")


def print_diva_info(diva: Diva):
    print("====")
    print("Name: ", diva.name)
    print("Version: ", diva.version)


if __name__ == "__main__":
    default_diva = Diva()
    named_diva1 = Diva("Diva1")
    named_diva2 = Diva("Diva2")

    print_diva_info(default_diva)
    print_diva_info(named_diva1)
    print_diva_info(named_diva2)
