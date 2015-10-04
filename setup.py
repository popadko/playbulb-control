from setuptools import setup, find_packages
setup(
    name = "playbulb-control",
    version = "0.1",
    packages = find_packages(),
    install_requires=[
        'python-nmap>=0.4',
    ]
)