============================================
Mapping reads back to the assembly
============================================

Overview
======================

There are many different mappers available to map your reads back to the
assemblies. Usually they result in a SAM or BAM file
(http://genome.sph.umich.edu/wiki/SAM). Those are formats that contain the
alignment information, where BAM is the binary version of the plain text SAM
format. In this tutorial we will be using bowtie2
(http://bowtie-bio.sourceforge.net/bowtie2/index.shtml).


The SAM/BAM file can afterwards be processed with Picard
(http://picard.sourceforge.net/) to remove duplicate reads. Those are likely to
be reads that come from a PCR duplicate (http://www.biostars.org/p/15818/).


BEDTools (http://code.google.com/p/bedtools/) can then be used to retrieve
coverage statistics.


There is a script available that does it all at once. Read it and try to
understand what happens in each step::
    
    less `which map-bowtie2-markduplicates.sh`
    map-bowtie2-markduplicates.sh -h

Bowtie2 has some nice documentation: http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml

**Question: what does bowtie2-build do?**

Picard's documentation also exists! Two bioinformatics programs in a row with
decent documentation! Take a moment to celebrate, then have a look here:
http://sourceforge.net/apps/mediawiki/picard/index.php?title=Main_Pageon 

**Question: Why not just remove all identitical pairs instead of mapping them
and then removing them?**

**Question: What is the difference between samtools rmdup and Picard MarkDuplicates?**



Mapping reads with bowtie2
==========================
Take an assembly and try to map the reads back using bowtie2. Do this on an
interactive node again, and remember to change the 'out_21' part to the actual output directory that you generated::

    # Create a new directory and link files
    mkdir -p ~/asm-workshop/bowtie2
    cd ~/asm-workshop/bowtie2
    ln -s ../velvet/out_21/contigs.fa contigs.fa
    ln -s ../sickle/pair1.fastq pair1.fastq
    ln -s ../sickle/pair2.fastq pair2.fastq

    # Run the everything in one go script. 
    map-bowtie2-markduplicates.sh -t 1 -c pair1.fastq pair2.fastq pair contigs.fa contigs map > map.log

Inspect the ``map.log`` output and see if all went well.

**Question: What is the overall alignment rate of your reads that bowtie2 reports?**

Add the answer to the doc_.


Some general statistics from the SAM/BAM file
=============================================
You can also determine mapping statistics directly from the bam file. Use for
instance::
    
    # Mapped reads only
    samtools view -c -F 4 map/contigs_pair-smds.bam
     
    # Unmapped reads only
    samtools view -c -f 4 map/contigs_pair-smds.bam

From:
http://left.subtree.org/2012/04/13/counting-the-number-of-reads-in-a-bam-file/.
The number is different from the number that bowtie2 reports, because these are
the numbers after removing duplicates. The ``-smds`` part stands for running
``samtools sort``, ``MarkDuplicates.jar`` and ``samtools sort`` again on the
bam file. If all went well with the mapping there should also be a
``map/contigs_pair-smd.metrics`` file where you can see the percentage of
duplication. Add that to the doc_ as well.


Coverage information from BEDTools
=============================================
Look at the output from BEDTools::

    less map/contigs_pair-smds.coverage

The format is explained here
http://bedtools.readthedocs.org/en/latest/content/tools/genomecov.html. The
``map-bowtie2-markduplicates.sh`` script also outputs the mean coverage per
contig::

    less map/contigs_pair-smds.coverage.percontig

**Question: What is the contig with the highest coverage? Hint: use sort -k**

.. _doc: https://docs.google.com/spreadsheet/ccc?key=0AvduvUOYAB-_dDdDSVhqUi1KQmJkTlZJcHVfMGI3a2c#gid=3
