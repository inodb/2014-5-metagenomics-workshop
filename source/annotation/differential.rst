================================================================
Search amino acid sequences with HMMER against the Pfam database
================================================================
It is time to do the actual Pfam annotation of our metagenomes!

    
Running ``hmmsearch`` on the translated sequence data sets
==========================================================
Before we run ``hmmsearch``, we will look at its available options::

    hmmsearch -h
    
As you will see, the program takes a substantial amount of arguments.
In this workshop we will work with the table output from HMMER, which
you get by specifying the ``--tblout`` option together with a file
name. We also want to make sure that we only got statistically
relevant matches, which we can do using the E-value option. The
E-value (Expect-value) is an estimation of how often we would expect
to find a similar hit by chance, given the size of the database. To
avoid getting a lot of noise
