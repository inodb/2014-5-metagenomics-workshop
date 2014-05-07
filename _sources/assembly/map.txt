============================================
Mapping reads back to the assembly
============================================

Overview
======================

There are many different mappers available to map your reads back to the
assemblies. Usually they result in a SAM or BAM file
(http://genome.sph.umich.edu/wiki/SAM). Those are formats that contains the
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
    map-bowtie2-markduplicates.sh -t 1 -c pair1.fastq pair2.fastq pair contigs.fa contigs map


Some general statistics from the SAM/BAM file
=============================================
A good way to assess the quality of an assembly is by mapping the reads back
and determining what proportion was mapped. Use for instance::
    
    # Mapped reads only
    samtools view -c -F 4 map/contigs_pair-smds.bam
     
    # Unmapped reads only
    samtools view -c -f 4 map/contigs_pair-smds.bam

From:
http://left.subtree.org/2012/04/13/counting-the-number-of-reads-in-a-bam-file/.
Try to determine what percentage of the pairs were mapping to your contigs and
add it to the doc_. If all went well with the mapping there should also be a
``map/contigs_pair-smd.metrics`` file where you can see the percentage of
duplication. Add that to the doc_ as well.

(Optional) Coverage information from BEDTools
=============================================
Look at the output from BEDTools::

    less map/contigs_pair-smds.coverage

.. _doc: https://docs.google.com/spreadsheet/ccc?key=0AvduvUOYAB-_dDJwcG1jbk1kTTY3eGZNazJGMUhfM3c#gid=3.
__ doc_ 
