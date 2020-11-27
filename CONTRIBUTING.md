# Contributing

Contributions are always welcome. Just send a pull request and I'll review it when I can.

If there's any issues that interest you leave a comment and I'll assign you to them.

## Requirements

It's recommended that you use either Python 3.7, 3.8, or 3.9 to run this tool. You can find them <a href="https://www.python.org/downloads/">here</a> 

You will need [Flake8](https://flake8.pycqa.org/en/latest/index.html) and [Black](https://pypi.org/project/black/) for formatting purposes

For testing, you will need [Pytest](https://docs.pytest.org/en/stable/getting-started.html) 

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

## Testing

To run tests, simply run the following command in the root directory:

`pytest`

This will run all the tests located in the tests directory. As of now, tests are split between test_openfile
which contains all test related to opening files, and test_urls which contains tests related to url
responses. If you want to add tests, please put them in the proper file, as this helps with
organization. 

## Coverage

To generate a report, use the following command in the root directory:

`coverage html`

This will create a folder containing the report.
