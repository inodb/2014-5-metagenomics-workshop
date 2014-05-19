==========================================
Setup Environment
==========================================
This workshop will be using the same environment used for the assembly workshop. If you did not participate in the assembly workshop, please have a look at the introductory setup description for that. 

Programs used in this workshop
==============================
The following programs are used in this workshop:

    - CONCOCT_
    - Phylosift_
    - Blast_
 
.. _CONCOCT: http://github.com/BinPro/CONCOCT
.. _Phylosift: http://phylosift.wordpress.com/ 
.. _BLAST: http://blast.ncbi.nlm.nih.gov/

All programs are already installed, all you have to do is load the virtual
environment for this workshop. Once you are logged in to the server run::

    source /proj/g2014113/metagenomics/virt-env/mg-workshop/bin/activate

You deactivate the virtual environment with::
    
    deactivate

NOTE: This is a python virtual environment. The binary folder of the virtual
environment has symbolic links to all programs used in this workshop so you
should be able to run those without problems.

Check that the programs are available
=====================================
After you have activated the virtual environment the following commands should execute properly and you should be able to see some brief instructions on how to run the different programs respectively.

CONCOCT::

    concoct -h


BLAST::

    rpsblast --help


