# html-element-mapreduce
Originally developed by Scot Matson for a class assignment as San Jose State University.
This application in its current implementation runs a sequential Crawler/MapReduce job
to scrape web data and sum the total number of HTML elements across all pages.

### Project Contributors

* Scot Matson

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


### Contributing To This Project
The current implenetation of this repository is strictly for academic purposes. Only assigned members
of the group will be considered for pull requests. This code is free to use with the exception that it
is not incorporated into your own assignment. (i.e., don't steal my code if you are not in my group)

#### Setting Up Your Local Repo

* Clone this project onto your local machine

    git clone https://github.com/scotmatson/html-element-mapreduce.git

* Create your own development branch

    git branch [branch name]

* When you are ready to commit to the master repo, first update your GitHub branch

    git push origin master

* Make a pull request to the master repository. I will handle merging your files.

* If you are behind master, you will need to rebase! Make sure you have the master repo set up as a remote
  Perform this operation from YOUR master branch, else risk losing your work!

    git remote add [name] https://github.com/scotmatson/html-elements-mapreduce.git

    git fetch [name]

    git rebase [name]/master

* Locally merge master into your branch and resolve any conflicts.

### Notes
It looks like the Requests library is having difficulty obtaining data
on SJSU_premier. This is probably something we can fix with additional parameters.
As long as it works in your development space, it is not a pressing issue.
Regardless, it is worth pointing out as it may effect you if you are on campus.
