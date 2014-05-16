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
Generally, sequencing data sets are not of the same size. In addition,
different genes and genomes come in different sizes, which means that
*at equal coverage, the number of mapped reads to a certain gene or
region will be directly dependent on the length of that region*.
Luckily, the latter scenario is not a huge issue for Pfam families
(although it exists), and we will not care about it more today. We
will however care about the size of the sequencing libraries. To make
relatively fair comparisons between sets, we need to normalize the
gene counts to something. Let's begin with checking how unequal the
librairies are. You can do that by counting the number of sequences
in the FASTA files, by checking for the number of ">" characters in
each file, using ``grep``::

    grep -c ">" <input file>
    
As you will see, there are quite substantial differences in the
number of reads in each library. How do we account for that?

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
