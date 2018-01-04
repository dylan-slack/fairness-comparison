class Metric:
    def __init__(self, actual, predicted):
        self.actual = actual
        self.predicted = predicted
        self.name = 'Name not implemented'  ## This should be replaced in implemented metrics.

    def calc(self):
        raise NotImplementedError("calc() in Metric is not implemented")

    def get_metric_name(self):
        return self.name
