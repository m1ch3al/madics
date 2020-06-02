"""
A setuptools based on setup module for MADIS.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name="m1ch3al-autonomous-drone-internal-system-configuration",
    version="0.1",
    description="The MAD Internal Configuration System (yaml).",
    # The project's main homepage.
    url="https://github.com/m1ch3al/madics.git",
    # Author details
    author="Renato Sirola",
    author_email="renato.sirola@gmail.com",
    # Choose your license
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    # What does your project relate to?
    keywords="sensors ros hardware drone autonomy",
    include_package_data=True,
    package_dir={'': 'src'},
    zip_safe=False,
    package_data={
        'madis.configuration': ['*/*.yaml', '*.yaml'],
    },
    packages=[
        'madis.configuration'
    ],
    #namespace_packages=['madis', 'cmre.autonomy', 'cmre.autonomy.d2caf']
)

