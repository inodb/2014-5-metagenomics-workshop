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
avoid getting a lot of noise matches, we will specify and E-value of
10^-5, that is that we would by chance get a match with a similarly good
alignment in 1 out of 100000 cases. This can be set with the ``-E 1e-5``
option. Finally, to speed up the process a little, we will use the
``--cpu`` option to get multi-core support. On the Uppmax machines you can
use up to 16 cores for the HMMER runs.

To specify the HMM-file database and the input data set, we just type in
the names of those two files at the end of the command. Finally we add in
the ``> /dev/null`` string, to avoid getting the screen cluttered with 
sequence alignments that HMMER outputs. That should give us the following
command::

    hmmsearch --tblout <output file> -E 1e-5 --cpu 8 ~/Pfam/Pfam-mobility.hmm <input file (protein format)> > /dev/null
    
Now run this command on all four input files that we just have downloaded. When the
command has finished for all files, we can move on to the normalization exercise.
