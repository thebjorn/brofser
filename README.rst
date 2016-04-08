

brofser -- a thin convenience wrapper on top of Selenium
========================================================

Usage::

    from brofser import Browser
    b = Browser('Firefox')
    b.get('http://www.example.com')
    assert b.title == 'Example'
    b['#q'] = 'word'
    b('#cse-search-box input[name=sa]').click()
    b.close()


Installing from PyPI
--------------------

This is what you want if you just want to use brofser:

   pip install brofser


As a source package
-------------------
This is what you want if you are developing brofser or want
to make local changes to the source code.

   pip install -e <path>




See docs/ folder for documentation.
