==========================================
Checking required software
==========================================
Before we begin, we will quickly go through the required software and datasets
for this workshop. For those who are already command-line-skilled there will
also be a possibility to install the Metaxa2 tool for rRNA finding, but this
is not required to complete the workshop.

Programs used in this workshop
==============================
The following programs are used in this workshop:

    - `EMBOSS (transeq)`__
    - HMMER_
    - Optionally: Metaxa2_

.. __: http://emboss.sourceforge.net
.. _HMMER: http://hmmer.janelia.org
.. _Metaxa2: http://microbiology.se/software/metaxa2/

All programs but Metaxa2 are already installed, all you have to do is load
the virtual environment for this workshop. Once you are logged in to the
server run::

    source /proj/g2014113/metagenomics/virt-env/mg-workshop/bin/activate

You deactivate the virtual environment with::
    
    deactivate

NOTE: This is a python virtual environment. The binary folder of the virtual
environment has symbolic links to all programs used in this workshop so you
should be able to run those without problems.


Check all programs in one go with which
==================================================
To check whether you have all programs installed in one go, you can use ``which``
to test for the following programs::

    hmmsearch
    transeq
    blastall
    
Data and databases used in this workshop
========================================
In this workshop, we are (due to time constraints) going to use a simplified version
of the `Pfam <http://pfam.xfam.org/>`__ database, including only protein families
related to plasmid replication and maintenance. This database is pre-compiled and can
be downloaded from http://microbiology.se/teach/scilife2014/pfam.tar.gz
Download it using the following commands::

    mkdir -p ~/Pfam
    cd ~/Pfam
    wget http://microbiology.se/teach/scilife2014/pfam.tar.gz
    tar -xzvf pfam.tar.gz
    
In addition, you will need to obtain the following data sets for the workshop::

    XXX
    YYY
    ZZZ
    
HOW DO WE COPY THESE!!!??!?


(Optional excercise) Install Metaxa2 by yourself
===============================================
Follow these steps only if you want to install ``Metaxa2`` by yourself.
The code for Metaxa2 is available from http://microbiology.se/sw/Metaxa2_2.0rc3.tar.gz
You can install Metaxa2 as follows::

    # Create a src and a bin directory
    mkdir -p ~/src
    mkdir -p ~/bin 

    # Go to the source directory and download the Metaxa2 tarball
    cd ~/src
    wget http://microbiology.se/sw/Metaxa2_2.0rc3.tar.gz
    tar -xzvf Metaxa2_2.0rc3.tar.gz
    cd Metaxa2_2.0rc3

    # Run the installation script
    ./install_metaxa2
    
    # Try to run Metaxa2 (this should bring up the main options for the software)
    metaxa2 -h

If this did not work, you can try this manual approach::

    cd ~/src/Metaxa2_2.0rc3
    cp -r metaxa2* ~/bin/
    
    # Then try to run Metaxa2 again
    metaxa2 -h
    
If this brings up the help message, you are all set!
    
