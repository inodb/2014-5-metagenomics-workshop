==========================================================
Normalization of count data from the metagenomic data sets
==========================================================
An important aspects of working with metagenomics is to apply proper
normalization procedures to the retrieved counts. There are several
ways to do this, and in part the method of choice is dependent on
the research question investigated, but in part also based on more
philosphical considerations. Let's start with a bit of theory.

Why is normalization important?
===============================


What normalization methods are possible?
========================================


Which method should we use?
===========================

    
Trying out some normalization methods
=====================================
Before we run ``hmmsearch``, we will look at its available options::

    hmmsearch -h
    
As you will see, the program takes a substantial amount of arguments.
In this workshop we will work with the table output from HMMER, which
you get by specifying the ``--tblout`` option together with a file
name. We also want to make sure that we only got statistically
relevant matches, which we can do using the E-value option. The


Which method should we settle with?
===================================
