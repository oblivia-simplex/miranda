from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='miranda',
    version='1.3',
    description='Miranda is a Python-based UPnP client application designed to discover, query and interact with UPnP devices, particularly Internet Gateway Devices (aka, routers).',
    long_description=readme(),
    url='https://code.google.com/archive/p/mirandaupnptool/',
    author='Craig Heffner',
    author_email='dev@sourcesec.com',
    license='MIT',
    packages=['miranda'],
    scripts=['bin/miranda','bin/portmapper.sh'],
    zip_safe=False)
