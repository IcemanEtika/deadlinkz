# deadlinkz
Python tool that checks for dead urls in a txt or html file

You will need Python 3.8.5 to run this tool. Get it <a href="https://www.python.org/downloads/">here</a> if you don't have it

# Features
* Good links will appear green, bad will appear red, and unknown will appear grey
* Supports windows and linux style arguments (e.g, --version and -v both work for version)
* Supports parallelization via the use of threads
* Gets only request headers for optimization

# Run Instructions

First clone the repository using

`git clone https://github.com/IcemanEtika/deadlinkz.git`

To run open cmd in root of the repo, and type main.py followed by one of the supported arguments:

* -a or --all filename.extension to check all URLs in file
* -g or --good filename.extension to check only good URLs in file
* -b or --bad filename.extension to check only bad URLs in file
* -v or --version
* -h or --help

# Error Codes

An error code of **0** means that the program functioned as correctly, **1** can appear when checking for all files and means that
a broken/invalid URL was found in the file, and **2** means that the specified file could not be found.

To get the error code after the program has functioned, you can use:

`echo %ERRORLEVEL%`

after execution finishes.

Please note that index.txt is for test purposes only and you can modify/remove the file if you want to

