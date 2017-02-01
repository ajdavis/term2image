==========
term2image
==========

Install
=======

Compatible with Python 2.7 and Python 3.

.. code-block:: none

  python -m pip install term2image

Usage
=====

Read the output of a terminal command like "man" or "ls" and write a PNG.

.. code-block:: none

  usage: term2image [-h] [-i INFILE] [-o OUTFILE]

  Convert terminal command output to an image

  optional arguments:
    -h, --help            show this help message and exit
    -i INFILE, --infile INFILE
    -o OUTFILE, --outfile OUTFILE

Example
=======

Output of ``man which | term2image -o which.png``:

.. image:: which.png
