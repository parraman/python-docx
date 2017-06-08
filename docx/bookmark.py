from .shared import Parented

class Bookmark(Parented):

    def __init__(self, bookmarkStart, parent):
        super(Bookmark, self).__init__(parent)
        self._bookmarkStart = bookmarkStart

    @property
    def name(self):
        return self._bookmarkStart.name

    @property
    def id(self):
        return self._bookmarkStart.id

    @name.setter
    def name(self):
        self._bookmarkStart.name = name

    @id.setter
    def id(self):
        self._bookmarkStart.id = id
