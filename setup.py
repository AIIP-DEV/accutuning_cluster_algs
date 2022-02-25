import os
from setuptools import setup, find_packages
import datetime as dt
try:
    from pip.req import parse_requirements
    from pip.download import PipSession
except:
    from pip._internal.req import parse_requirements
    from pip._internal.network.session import PipSession

    
install_requires_gen = parse_requirements(
    os.path.join(
        os.path.dirname(__file__),
        "requirements.txt",
    ),
    session=PipSession(),
)
install_requires = [str(i.requirement) for i in install_requires_gen]

setup(
    name="accutuning_cluster_algs",
    version="0.1.0",
    packages=find_namespace_packages(),
    include_package_data=True,
    python_requires="3.8",
    install_requires=install_requires,
)
