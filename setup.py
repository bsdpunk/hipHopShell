#from distutils.core import setup
from setuptools import setup, find_packages

#dependecy_links = ["git+https://github.com/pexpect/pexpect.git#egg=pexpect-0.1"]
install_requires = ['pyvmomi','pyvim', 'requests']

setup(
    name='hipHopShell',
    version='0.06',
    packages=['hhs',],
    install_requires=install_requires,
    entry_points = { 'console_scripts': [
        "hhs = hhs.hhs:cli", ],
        },
    author = "Dusty C",
    author_email = "bsdpunk@gmail.com",
    description = "A Modal Terminal for Composing HipHop",
    license = "BSD",
    keywords = "Shell cli terminal HipHop",
    url = 'bsdpunk.blogspot.com'
    )
