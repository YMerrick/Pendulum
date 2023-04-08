from setuptools import setup

setup(
    name="pendulum",
    version="0.1",
    packages=['src'],
    install_requires=[
        'aiohttp',
        'aiosignal',
        'async-timeout',
        'attrs',
        'cffi',
        'charset-normalizer',
        'discord.py',
        'frozenlist',
        'geographiclib',
        'geopy',
        'h3',
        'idna',
        'multidict',
        'numpy',
        'pycparser',
        'pytz',
        'requests',
        'timezonefinder',
        'wcwidth',
        'yarl'
    ]
)