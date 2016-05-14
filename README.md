# html-element-mapreduce
Originally developed by Scot Matson for a class assignment as San Jose State University.
This application in its current implementation runs a sequential Crawler/MapReduce job
to scrape web data and sum the total number of HTML elements across all pages.

### Build

* Developed with Python 3.5.1

* Initial release v0.01

### Directory Structure

* /crawler - Files used for the web crawler

* /mapreduce - Files used for the mapreduce implementation

* /web_pages - Temporary storage for web sites

* /out - Results of the mapreduce operation as CSV

### Required Modules

* [Requests](http://docs.python-requests.org/en/master/)

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

* [Validators](https://pypi.python.org/pypi/validators)

* [html5lib](https://github.com/html5lib/html5lib-python)

The easiest way to go about installing these modules is with [pip](https://python-packaging-user-guide.readthedocs.io/en/latest/installing/#use-pip-for-installing).
Be sure that you are using a version of pip that is compatible with python 3.

### Future Development

* Parallel processing

* Error logs

* Better data parsing

* Database incorporation

* Introduce OOP for improved code structuring
