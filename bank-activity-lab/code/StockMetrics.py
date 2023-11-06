
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
            rounded_average = round(average, 3)
            averages.append(rounded_average)
        return averages

    def median02(self):
        """pt2
        """
        medians = []
        for row in self.data:
            data_row = row[1:]
            y = [float(x) for x in data_row if x != ""]
            if y: 
                median = stats.median(y)
                medians.append(median)
        return medians 


    def stddev03(self):
        """pt3
        """
        standard_deviations = []
        for row in self.data:
            data_row = row[1:]
            y = [float(x) for x in data_row if x != ""]
            if y:
                if len(y) > 1:
                   std_dev = stats.stdev(y)
                   rounded_std_dev = round(std_dev, 3)
                   standard_deviations.append(rounded_std_dev)
        return standard_deviations
                 

