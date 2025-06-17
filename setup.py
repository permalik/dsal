from setuptools import find_packages, setup

setup(
    name="dsal-python",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "black",
        "isort",
    ],
    entry_points={
        "console_scripts": [
            "ds_array = ds_array.main:main",
            "al_bubble_sort = al_bubble_sort.main:main",
        ],
    },
)
