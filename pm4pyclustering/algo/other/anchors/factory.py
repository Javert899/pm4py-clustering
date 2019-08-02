from pm4pyclustering.algo.other.anchors.versions import classic
import joblib

CLASSIC = "classic"

VERSIONS = {CLASSIC: classic.ClassicAnchorClassification}


def apply(log, target, classes, variant=CLASSIC, parameters=None):
    """
    Initialize the Anchors classification

    Parameters
    ------------
    log
        Log
    target
        Numerical target of the classification
    classes
        Classes (of the classification)
    parameters
        Parameters of the algorithm
    variant
        Variant of the algorithm to use, possible values: classic

    Returns
    ------------
    anchors
        Anchors classifier
    """
    if parameters is None:
        parameters = {}

    return VERSIONS[variant](log, target, classes, parameters=parameters)


def save(model, filename):
    """
    Saves a model

    Parameters
    -------------
    model
        Prediction model
    filename
        Name of the file where to save the model
    """
    joblib.dump(model, filename, compress=3)


def load(filename):
    """
    Loads a model

    Parameters
    -------------
    filename
        Name of the file where the model is saved

    Returns
    -------------
    model
        Prediction model
    """
    return joblib.load(filename)
