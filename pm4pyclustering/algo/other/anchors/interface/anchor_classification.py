class AnchorClassification(object):
    def __init__(self, log, target, classes, parameters=None):
        pass

    def train(self):
        raise Exception("not implemented")

    def predict(self, trace):
        raise Exception("not implemented")

    def explain(self, trace, threshold=-0.01):
        raise Exception("not implemented")