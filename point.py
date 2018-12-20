from reader_factory import ReaderFactory

class Point:
    """
    make point in coordinate axis
    """

    def __init__(self, coordinates):
        """
        initialize point
        :param x: x of coordinate axis
        :param y: y of coordinate axis
        """
        self.x = x
        self.y = y

    def __str__(self):
        return '{} {}'.format(self.x,self.y)

    def main(self):
        reader = ReaderFactory()
        coordinates = reader.get_reader('points_sheet.csv')
        return coordinates
