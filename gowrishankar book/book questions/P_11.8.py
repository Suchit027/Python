class Track:
    def __init__(self, song, artist):
        self.song = song
        self.artist = artist

    def printing(self, vocalist):
        print(self.song + ' ' + self.artist)


test = Track('one', 'two')
test.printing(test)
