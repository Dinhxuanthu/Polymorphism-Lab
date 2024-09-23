def play_instrument(instrument):
    print(instrument.play())
class Guitar:
    def play(self):
       print("playing the guitar")
guitar = Guitar()
play_instrument(guitar)
guitar = Guitar()
play_instrument(guitar)