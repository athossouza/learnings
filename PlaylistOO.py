from abc import ABC
from collections.abc import MutableSequence

class Playlist(MutableSequence):
    def __getitem__(self, item):
        super().__getitem__()

filmes = Playlist()