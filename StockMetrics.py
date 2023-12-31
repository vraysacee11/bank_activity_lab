
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        for row in self.data:
            data_row = row[1:]
            y = []
            for x in data_row:
                try: 
                    y.append(float(x))
                except ValueError: 
                    continue
            average = stats.mean(y)
            rounded_average = rounded(average, 3)
            averages.append(rounded_average)
        return averages

    def median02(self):
        """pt2
        """
        ...

    def stddev03(self):
        """pt3
        """
        ...
