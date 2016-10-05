from setuptools import setup

setup(
    name='fflpy',
    version='1.0',
    py_modules=['fflpy'],
    install_requires=[
        'nflgame',
        'Click'
    ],
    entry_points='''
        [console_scripts]
        fflpy=fflpy:cli
    '''
)