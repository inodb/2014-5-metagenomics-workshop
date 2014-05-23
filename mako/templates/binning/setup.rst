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

All programs and scripts that you need for this workshop are already installed, all you have to do is load the virtual
environment. Once you are logged in to the server run::

    ${commands['activate']}

If you'd wish to inactivate this virtual environment you could run::
    
    deactivate # Don't run this now

NOTE: This is a python virtual environment. The binary folder of the virtual
environment has symbolic links to all programs used in this workshop so you
should be able to run those without problems.

Check that the programs are available
=====================================
After you have activated the virtual environment the following commands should execute properly and you should be able to see some brief instructions on how to run the different programs respectively.

CONCOCT::

    ${commands['check_activate']['concoct']}


BLAST::

    ${commands['check_activate']['rpsblast']}

