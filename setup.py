from os.path import dirname, join

from setuptools import setup

import pm4pyclustering


def read_file(filename):
    with open(join(dirname(__file__), filename)) as f:
        return f.read()


setup(
    name=pm4pyclustering.__name__,
    version=pm4pyclustering.__version__,
    description=pm4pyclustering.__doc__.strip(),
    long_description=read_file('README.md'),
    author=pm4pyclustering.__author__,
    author_email=pm4pyclustering.__author_email__,
    py_modules=[pm4pyclustering.__name__],
    include_package_data=True,
    packages=['pm4pyclustering', 'pm4pyclustering.algo', 'pm4pyclustering.algo.other',
              'pm4pyclustering.algo.other.anchors', 'pm4pyclustering.algo.other.anchors.versions',
              'pm4pyclustering.algo.other.anchors.interface', 'pm4pyclustering.algo.other.clustering',
              'pm4pyclustering.algo.other.clustering.versions', 'pm4pyclustering.algo.other.conceptdrift',
              'pm4pyclustering.algo.other.conceptdrift.utils', 'pm4pyclustering.algo.other.conceptdrift.versions',
              'pm4pyclustering.util', 'pm4pyclustering.util.anchors'],    url='http://www.pm4py.org',
    license='GPL 3.0',
    install_requires=[
        'pm4py',
        'joblib',
        'lime'
    ],
    project_urls={
        'Documentation': 'http://pm4py.pads.rwth-aachen.de/documentation/',
        'Source': 'https://github.com/pm4py/pm4py-source',
        'Tracker': 'https://github.com/pm4py/pm4py-source/issues',
    }
)
