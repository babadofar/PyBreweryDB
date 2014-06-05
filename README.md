PyBreweryDB
===========

This is a Python wrapper around the BreweryDB API.  It is a work in progress with
only a handful of endpoints implemented at this point.


Documentation
-------------

Read the full `documentation <http://pymarvel.readthedocs.org>`__.


Installation
------------
Use pip::

    pip install pybrewerydb

`Python Package Index <https://pypi.python.org/pypi/pybrewerydb>`__.

Get yourself an API key to use https://www.brewerydb.com/auth/signup/ref/apps


Basic Usage
-----------

Create a PyBreweryDB instance using your api key:

    >>> from brewerydb.brewerydb import BreweryDB
    >>> brew_api = BreweryDB(key)
    >>> beers = brew_api.search_beers('fat tire')

Contributing
------------

Clone the repo at `http://github.com/dstegelman/pybrewerydb <http://github.com/dstegelman/pybrewerydb>`__.

Feel free to log issues in Github or, better yet, submit a Pull Request against the ``master`` branch.

Licensing
---------

PyBreweryDB is distributed under the MIT License.
    
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


### Authors

* Derek Stegelman

Heavily inspried and several linez of codez drawn from PyMarvel by @gpennington