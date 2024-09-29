from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="song-analyzer",
    version="1.0.1",
    author="Jatin Kolluru",
    author_email="jatinkolluru@gmail.com",
    description="A CLI tool for analyzing audio files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jatinkolluru/song-analyzer",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "librosa",
        "numpy",
        "click",    
        "tabulate",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "song-analyzer=song_analyzer.cli:cli",
        ],
    },
)
