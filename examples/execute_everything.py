import inspect
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

if __name__ == "__main__":
    from examples import clustering_example
    from examples import concept_drift

    print("\n\nclustering_example")
    clustering_example.execute_script()
    print("\n\nconcept_drift")
    concept_drift.execute_script()
