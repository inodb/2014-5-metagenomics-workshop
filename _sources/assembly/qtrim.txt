==========================================
Quality trimming Illumina paired-end reads
==========================================
In this excercise you will learn how to quality trim Illumina paired-end reads.
The most common Next Generation Sequencing (NGS) technology for metagenomics.

Sickle
======
For quality trimming Illumina paired end reads we use the library sickle which
trims reads from 3' end to 5' end using a sliding window. If the mean quality
drops below a specified number remaining part of the read will be trimmed.


Downloading a test set
======================
Today we'll be working on a small metagenomic data set from the anterior nares
(http://en.wikipedia.org/wiki/Anterior_nares).

.. image:: https://raw.github.com/inodb/2013-metagenomics-workshop-gbg/master/images/nostril.jpg


So get ready for your first smell of metagenomic assembly - pun intended. Run
all these commands in your shell::
    
    # Download the reads and extract them
    mkdir -p ~/asm-workshop
    mkdir -p ~/asm-workshop/data
    cd ~/asm-workshop/data
    wget http://downloads.hmpdacc.org/data/Illumina/anterior_nares/SRS018585.tar.bz2
    tar -xjf SRS018585.tar.bz2

If successfull you should have the files::

    $ ls -lh ~/asm-workshop/data/SRS018585/
    -rw-rw-r-- 1 idb idb 36M Apr 18  2011 /home/<username>/asm-workshop/data/SRS018585/SRS018585.denovo_duplicates_marked.trimmed.1.fastq
    -rw-rw-r-- 1 idb idb 36M Apr 18  2011 /home/<username>/asm-workshop/data/SRS018585/SRS018585.denovo_duplicates_marked.trimmed.2.fastq

If not, try to find out if one of the previous commands gave an error.


Running sickle on a paired end library
======================================
I like to create directories for specific parts I'm working on and creating
symbolic links (shortcuts in windows) to the input files. One can use the
command ``ln`` for creating links. The difference between a symbolic link and a
hard link can be found here:
http://stackoverflow.com/questions/185899/what-is-the-difference-between-a-symbolic-link-and-a-hard-link.
In this case I use symbolic links so I know what path the original reads have,
which can help one remember what those reads were::
    
    mkdir -p ~/asm-workshop/sickle
    cd ~/asm-workshop/sickle
    ln -s ../data/SRS018585/SRS018585.denovo_duplicates_marked.trimmed.1.fastq pair1.fastq
    ln -s ../data/SRS018585/SRS018585.denovo_duplicates_marked.trimmed.2.fastq pair2.fastq

Now run sickle::

    # check if sickle is in your PATH
    which sickle
    # Run sickle
    sickle pe \
        -f pair1.fastq \
        -r pair2.fastq \
        -t sanger \
        -o qtrim1.fastq \
        -p qtrim2.fastq \
        -s qtrim.unpaired.fastq
    # Check what files have been generated
    ls
