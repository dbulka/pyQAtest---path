import csv
from abstractreader import AbscractReader
import logging


class CSVReader(AbscractReader):
    """
    csvfiles reader
    """

    def read(self, filename):
        """
        read a csv file
        :param Filename: file name
        :return: x,y - points of axis
        """
        x = []
        y = []
        with open(filename, newline='') as file:
            for row in csv.reader(file):
                print(row)
                str(row).split(';')
                try:
                    x.append(row[0])
                except:
                    logging.warning('TypeError')
                print(x)
                try:
                    y.append(row[1])
                except:
                    logging.warning('TypeError')
                print(y)
        return x,y

print(csv.__file__)
csv = CSVReader()
csv.read('points_sheet.csv')

