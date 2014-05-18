==================================
Metagenomics Workshop SciLifeLab
==================================

This repository holds the code for the website of the metagenomics workshop
held at SciLifeLab, Stockholm 21-23 May 2014. The website is written using
Sphinx_. The webpage can be found at:

http://inodb.github.io/2014-5-metagenomics-workshop/

and

http://2014-5-metagenomics-workshop.readthedocs.org/en/latest/assembly/index.html

How does it work?
-------------------------
In short, we use a python package called Sphinx_ to convert a bunch of text
files written in reStructuredText_ (reST) to HTML pages. Instead of editing the
HTML directly you change text files in the reST_ format. Those are the
``*.rst`` files in  the `source directory`_. That's all you need to know to
start `Contributing`_.

Contributing
-------------
We follow the Fork_ & pull_ model. It's not necessary to do anything on the
command line. All you have to is click on fork. Then you can  edit the
``*.rst`` files directly through the GitHub interface if you want. Only the
Sphinx specific commands will not work, such as the table of contents command
``toctree``. You can also `add new files`_ by clicking on the plus symbol next
to a directory. After you are satisfied with you changes you click on the pull
request button. Do note that changing the ``*.rst`` files does not change the
actual webpage, maybe somebody else (.e.g me) can do that for you. If you want
to learn how to compile the ``*.rst`` files to ``*.html``, please read on.

Compile the reST files to HTML locally
---------------------------------------
The only thing that is a bit more tricky is actually compiling the ``*.rst``
files to ``*.html`` files. This is not necessary to contribute since you can
see the results in Github (GitHub shows ``*.rst`` files as they would look like
in HTML by default). If you want to compile the files locally you would do::
    
    pip install sphinx  # install sphinx
    git clone https://github.com/inodb/2014-5-metagenomics-workshop
    make html

The resulting HTML pages are in the folder ``build/``. You can open the files
in your browser by typing e.g.
``file:///home/inodb/path/to/build/html/index.html`` in the address bar. If you
want to make changes you should:

1. fork_ this repo
2. clone your forked repo
3. Make the changes to the ``*.rst`` files
4. run ``make html``
5. look at the results
6. add the changes with ``git add files that you changed``
7. commit the changes with ``git commit``
8. push the changes to your own repo with ``git push``
9. do a pull_ request by clicking on the pull request button on the GitHub page
   of your repo

This only changes the ``*.rst`` files in the ``master`` branch, not the actual
webpage, which is in the ``gh-pages`` branch. How that is set up is explained
in the section.


Updating the HTML to GitHub Pages
--------------------------------------
The website is hosted on `GitHub Pages`. It works by having a branch called
``gh-pages`` on this repository, which has all the HTML. I used
brantfaircloth's `sphinx_to_github.sh`_ script to set it up. Basically it sets
up a ``gh-pages`` branch in the ``build/html`` folder of the repository, so
everytime you run ``make html`` it changes the files in that branch. You then
``cd build/html``, commit the new HTML files and push them to the ``gh-pages``
branch. After that the result can be viewed at:

http://yourusername.github.io/reponame/

I'll update the branch ``gh-pages`` myself after your pull request with the
changed ``*.rst`` files on the ``master`` branch was accepted.


.. _sphinx: http://sphinx-doc.org/
.. _fork: https://help.github.com/articles/fork-a-repo
.. _pull: https://help.github.com/articles/using-pull-requests
.. _reStructuredText: http://sphinx-doc.org/rest.html
.. _reST: http://sphinx-doc.org/rest.html
.. _source directory: https://github.com/inodb/2014-5-metagenomics-workshop/tree/master/source
.. _GitHub Pages: https://pages.github.com/
.. _add new files: https://github.com/blog/1327-creating-files-on-github
.. _sphinx_to_github.sh: https://gist.github.com/brantfaircloth/791759
