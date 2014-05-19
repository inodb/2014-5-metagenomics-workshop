===========================================
Phylogenetic Classification using Phylosift
===========================================
In this workshop we'll extract interesting bins from the concoct runs and investigate which species they consists of. We'll start by using a plain'ol BLASTN search and later we'll try a more sophisticated strategy with the program Phylosift.

Extract bins from CONCOCT output
================================
The output from concoct is only a list of cluster id and contig ids respectively, so if we'd like to have fasta files for all our bins, we need to run the following script::
    
    extract_fasta_bins.py -h

Running it will create a separate fasta file for each bin, so we'd first like to create a output directory where we can store these files::

    mkdir -p ~/binning-workshop/concoct_output/3000_all_samples/fasta_bins
    extract_fasta_bins.py ~/binning-workshop/data/Contigs_gt1000.fa ~/binning-workshop/concoct_output/3000_all_samples/clustering_gt3000.csv --output_path ~/binning-workshop/concoct_output/3000_all_samples/fasta_bins/

Now you can see a number of bins in your output folder::

    ls ~/binning-workshop/concoct_output/3000_all_samples/fasta_bins

Using the graph downloaded in the previous part, decide one cluster you'd like to investigate further. We're going to use the web based BLASTN tool at ncbi, so lets first download the fasta file for the cluster you choose. Execute on a terminal not logged in to UPPMAX::
    
    scp username@milou.uppmax.uu.se:~/binning-workshop/concoct_output/3000_all_samples/fasta_bins/x.fa ~/Desktop/

Before starting to blasting this cluster, lets begin with the next assignment, since the next assignment will include a long waiting time that suits for running the BLASTN search.

Phylosift
=========
Phylosift is a software created for the purpose of determining the phylogenetic composition of your metagenomic data. It uses a defined set of genes to predict the taxonomy of each sequence in your dataset. You can read more about how this works here: http://phylosift.wordpress.com
I've yet to discover how to install phylosift into a common bin, so in order to execute phylosift, you'd have to cd into the phylosift directory::

    cd /proj/g2014113/src/phylosift_v1.0.1

Running phylosift will take some time (roughly 45 min) so lets start running phylosift on the cluster you choose::

    mkdir -p ~/binning-workshop/phylosift_output/
    ./phylosift all -f --output ~/binning-workshop/phylosift_output/ ~/binning-workshop/concoct_output/3000_all_samples/fasta_bins/x.fa

While this command is running, go to ncbi web blast service: 

http://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome

Upload your fasta file that you downloaded in the previous step and submit a blast search against the nr/nt database.
Browse through the result and try and see if you can do a taxonomic classification from these.

When the phylosift run is completed, browse the output directory::

    ls ~/binning-workshop/phylosift_output/

All of these files are interesting, but the most fun one is the html file, so lets download this to your own computer and have a look. Again, switch to a terminal where you're not logged in to UPPMAX::

    scp username@milou.uppmax.uu.se:~/binning-workshop/phylosift_output/x.fa.html ~/Desktop/

Did the phylosift result correspond to any results in the BLAST output?

