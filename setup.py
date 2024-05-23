from setuptools import setup, find_packages

setup(
    name='enigma-project',
    version='1.0',
    packages=find_packages(),
    install_requires=['setuptools'],# otras dependencias
    entry_points={
        'console_scripts': [
            'enigma = main:main'
        ]
    }
)
