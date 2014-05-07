==========================================
Checking required software
==========================================
An often occuring theme in bioinformatics is installing software. Here we wil
go over some steps to help you check whether you actually have the right
software installed. There's an optional excerise on how to install ``sickle``.

Programs used in this workshop
==============================
The following programs are used in this workshop:

    - Bowtie2_
    - Velvet_
    - parallel_
    - samtools_
    - CD-HIT_
    - AMOS_
    - sickle_
    - Picard_
    
.. _Bowtie2: http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
.. _Velvet: http://www.ebi.ac.uk/~zerbino/velvet/
.. _xclip: http://sourceforge.net/projects/xclip/
.. _parallel: https://www.gnu.org/software/parallel/
.. _samtools: http://samtools.sourceforge.net/
.. _CD-HIT: https://code.google.com/p/cdhit/
.. _AMOS: http://sourceforge.net/apps/mediawiki/amos/index.php?title=AMOS
.. _sickle: https://github.com/najoshi/sickle
.. _Picard: http://picard.sourceforge.net/index.shtml

All programs are already installed, all you have to do is load the virtual
environment for this workshop. Once you are logged in to the server run::

    source /proj/g2013206/metagenomics/virt_env/mg-workshop/bin/activate

You deactivate the virtual environment with::
    
    deactivate

NOTE: This is a python virtual environment. The binary folder of the virtual
environment has symbolic links to all programs used in this workshop so you
should be able to run those without problems.


Using which to locate a program
===============================
An easy way to determine whether you have have a certain program installed is
by typing::

    which programname
    
where ``programname`` is the name of the program you want to use. The program
``which`` searches all directories in ``$PATH`` for the executable file
``programname`` and returns the path of the first found hit. This is exactly
what happens when you would just type ``programname`` on the command line, but
then ``programname`` is also executed. To see what your ``$PATH`` looks like,
simply ``echo`` it::
    
    echo $PATH

Check all programs in one go with which
==================================================
To check whether you have all programs installed in one go, you can use ``which``.

    bowtie2
    bowtie2-build
    velveth
    velvetg
    shuffleSequences_fastq.pl
    parallel
    samtools


Iterate over the programs calling ``which`` on each of them::

    $ req_progs="bowtie2 bowtie2-build velveth velvetg parallel samtools shuffleSequences_fastq.pl"
    $ echo $req_progs
    bowtie2 bowtie2-build velveth velvetg parallel samtools shuffleSequences_fastq.pl
    $ for p in $req_progs; do which $p || echo $p not in PATH; done
    /home/idb/bin/bowtie2
    /home/idb/bin/bowtie2-build
    /home/idb/downloaded_software/velvet_1.2.03/velveth
    /home/idb/downloaded_software/velvet_1.2.03/velvetg
    /usr/local/bin/parallel
    /home/idb/bin/samtools

As you can see all programs are found, except tablet in this case. If any of
the installed programs is missing, try to install them yourself or ask. If you
are having troubles following these examples, try to find some bash tutorials
online next time you have some time to kill. Educating yourself on how to use
the command line effectively increases your productivity immensely.

(Optional excercise) Install sickle by yourself
===============================================
Follow these steps only if you want to install ``sickle`` by yourself.
Installation procedures of research software often follow the same pattern.
Download the code, *compile* it and copy the binary to a location in your
``$PATH``. The code for sickle is on https://github.com/najoshi/sickle. I
prefer *compiling* my programs in ``~/src`` and then copying the resulting
program to my ``~/bin`` directory, which is in my ``$PATH``. This should get
you a long way::

    mkdir -p ~/src

    # Go to the source directory and clone the sickle repository
    cd ~/src
    git clone https://github.com/najoshi/sickle
    cd sickle

    # Compile the program
    make

    # Create a bin directory
    mkdir -p ~/bin
    cp sickle ~/bin
