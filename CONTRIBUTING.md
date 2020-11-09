# Contributing

Contributions are always welcome. Just send a pull request and I'll review it when I can.

If there's any issues that interest you leave a comment and I'll assign you to them.

## Requirements

You will need Python 3.8.5 to run this tool. Get it <a href="https://www.python.org/downloads/">here</a> if you don't have it
You will also need [Flake8](https://flake8.pycqa.org/en/latest/index.html) and [Black](https://pypi.org/project/black/) for formatting purposes
If you want Telescope functionality you can install it [here](https://github.com/Seneca-CDOT/telescope)

## Installation

Clone the repository using the following command:

`git clone https://github.com/IcemanEtika/deadlinkz.git`

You should be good to go after doing this. Please refer to README.md for run instructions.

## Source Code Formatting

After you make any changes, be sure to run the formatter. To do this, use the following command:

`black main.py`

This will automatically format the file.

After you do this, run the linter with the following command and fix any errors it may give:

`flake8 main.py`