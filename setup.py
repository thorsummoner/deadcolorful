"""
    deadcolorful  simple dead pixel check
"""
import setuptools
setuptools.setup(
    name='deadcolorful',
    version='0.0.0-dev1',
    description='simple dead pixel check',
    packages=['deadcolor'],
    install_requires=[],
    entry_points={
        'gui_scripts': [
            'deadcolorful=deadcolor.__main__:main',
        ],
    }
)
