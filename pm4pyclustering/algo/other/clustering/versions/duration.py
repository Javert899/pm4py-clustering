import numpy as np
from sklearn.cluster import Birch
from sklearn.metrics import silhouette_score

from pm4py.objects.log.log import EventLog
from pm4py.statistics.traces.log import case_statistics


def apply(log, parameters=None):
    """
    Apply clustering based on case duration

    Parameters
    ------------
    log
        Event log
    parameters
        Parameters of the algorithm

    Returns
    ------------
    list_logs
        List of sublogs
    """
    if parameters is None:
        parameters = {}
    min_n_clusters_to_search = parameters["min_n_clusters_to_search"] if "min_n_clusters_to_search" in parameters else 2
    max_n_clusters_to_search = parameters["max_n_clusters_to_search"] if "max_n_clusters_to_search" in parameters else 5
    parameters["sorted"] = False
    data = np.asarray(case_statistics.get_all_casedurations(log, parameters=parameters)).reshape(-1, 1)
    outputs = []
    for cluster_size in range(min_n_clusters_to_search, max_n_clusters_to_search + 1):
        db = Birch(n_clusters=cluster_size).fit(data)
        labels = db.labels_
        silh_score = silhouette_score(data, labels)
        outputs.append((labels, silh_score))
    outputs = sorted(outputs, key=lambda x: x[-1], reverse=True)
    labels = outputs[0][0]
    sublogs = []
    for i in range(len(log)):
        label = labels[i]
        while label >= len(sublogs):
            sublogs.append(EventLog())
        sublogs[label].append(log[i])
    return sublogs
