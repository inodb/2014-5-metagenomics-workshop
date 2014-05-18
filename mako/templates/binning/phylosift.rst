Phylogenetic Classification using Phylosift
===========================================
In this workshop we'll extract interesting bins from the concoct runs and investigate which species they consists of. We'll start by using a plain'ol BLASTN search and later we'll try a more sophisticated strategy with the program Phylosift.

Extract bins from CONCOCT output
================================
The output from concoct is only a list of cluster id and contig ids respectively, so if we'd like to have fasta files for all our bins, we need to run the following script::
    
    ${commands['extract_fasta_help']}

Running it will create a separate fasta file for each bin, so we'd first like to create a output directory where we can store these files::

    ${'\n    '.join(commands['extract_fasta'])}

Now you can see a number of bins in your output folder::

    ${commands['list_bins']}
Phylosift
=========
Phylosift is a software created for the purpose of determining the phylogenetic composition of your metagenomic data. It uses a defined set of genes to predict the taxonomy of each sequence in your dataset. You can read more about how this works here: .. _Phylosift: http://phylosift.wordpress.com

