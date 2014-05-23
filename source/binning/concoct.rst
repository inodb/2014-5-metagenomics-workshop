==========================================================
CONCOCT - Clustering cONtigs with COverage and ComposiTion
==========================================================
In this excercise you will learn how to use a new software for automatic and unsupervised binning of metagenomic contigs, called CONCOCT. 
CONCOCT uses a statistical model called a Gaussian Mixture Model to cluster sequences based on their tetranucleotide frequencies and their average coverage over multiple samples. 

The theory behind using the coverage pattern is that sequences having similar coverage pattern over multiple samples are likely to belong to the same species.
Species having a similar abundance pattern in the samples can hopefully be separated by the tetranucleotide frequencies.

We will be working with an assembly made using only the reads from this single sample, but since CONCOCT is constructed to be ran using the coverage profile over multiple samples, we'll be investigating how the performance is affected if we add several other samples.
This is done by mapping the reads from the other samples to the contigs resulting from this single sample assembly. 


Getting to know the test data set
=================================
Today we'll be working on a metagenomic data set from the baltic sea.
The sample we'll be using is part of a time series study, where the same location have been sampled twice weekly during 2013. This specific sample was taken march 22. 

Start by copying the contigs to your working directory::
    
    mkdir -p ~/binning-workshop
    mkdir -p ~/binning-workshop/data
    cd ~/binning-workshop/
    cp /proj/g2014113/nobackup/concoct-workshop/Contigs_gt1000.fa data/
    cp /proj/g2014113/nobackup/concoct-workshop/120322_coverage_nolen.tsv data/

You should now have one fasta file containing all contigs, in this case only contigs longer than 1000 bases is included to save space, and one comma separated file containing the coverage profiles for each contig.
Let's have a look at the coverage profiles::

    less -S ~/binning-workshop/data/120322_coverage_nolen.tsv

Try to find the column corresponding to March 22 and compare this column to the other ones. Can you draw any conclusions from this comparison?

We'd like to first run concoct using only one sample, so we remove all other columns in the coverage table to create this new coverage file::

    cut -f1,3 ~/binning-workshop/data/120322_coverage_nolen.tsv > ~/binning-workshop/data/120322_coverage_one_sample.tsv

Running CONCOCT
===============
CONCOCT takes a number of parameters that you got a glimpse of earlier, running::

    concoct -h

The contigs will be input as the composition file and the coverage file obviously as the coverage file. The output path is given by as the -b (--basename) parameter, where it is important to include a trailing slash if we want to create an output directory containing all result files. 
Last but not least we will set the length threshold to 3000 to speed up the clustering (the less contigs we use, the shorter the runtime)::

    mkdir -p ~/binning-workshop/concoct_output
    concoct --coverage_file ~/binning-workshop/data/120322_coverage_one_sample.tsv --composition_file ~/binning-workshop/data/Contigs_gt1000.fa -l 3000 -b ~/binning-workshop/concoct_output/3000_one_sample/

This command will normally take a couple of minutes to finish. When it is done, check the output directory and try to figure out what the different files contain.
Especially, have a look at the main output file:: 

    less ~/binning-workshop/concoct_output/3000_one_sample/clustering_gt3000.csv

This file gives you the cluster id for each contig that was included in the clustering, in this case all contigs longer than 3000 bases. 

For the comparison we will now run concoct again, using the coverage profile over all samples in the time series::

    concoct --coverage_file ~/binning-workshop/data/120322_coverage_nolen.tsv --composition_file ~/binning-workshop/data/Contigs_gt1000.fa -l 3000 -b ~/binning-workshop/concoct_output/3000_all_samples/

Have a look at the output from this clustering as well, do you notice anything different?

Evaluating Clustering Results
=============================
One way of evaluating the resulting clusters are to look at the distribution of so called Single Copy Genes (SCG:s), genes that are present in all bacteria and archea in only one copy. 
With this background, a complete and correct bin should have exactly one copy of each gene present, while missing genes indicate an inclomplete bin and several copies of the same gene indicate a chimeric cluster. 
To predict genes in prokaryotes, we use Prodigal that we then use as the query sequences for an RPS-BLAST search against the Clusters of Orthologous Groups (COG) database.
This RPS-BLAST search takes about an hour and a half for our dataset so we're going to use a precomputed result file.
Copy this result file along with two files necessary for the COG counting scripts::

    cp /proj/g2014113/nobackup/concoct-workshop/Contigs_gt1000_blast.out ~/binning-workshop/data/
    cp /proj/g2014113/nobackup/concoct-workshop/scg_cogs_min0.97_max1.03_unique_genera.txt ~/binning-workshop/data/
    cp /proj/g2014113/nobackup/concoct-workshop/cdd_to_cog.tsv ~/binning-workshop/data/

Before moving on, we need to install some R packages, please run these commands line by line::

    R
    install.packages("ggplot2")
    install.packages("reshape")
    install.packages("getopt")
    q()

With the CONCOCT distribution comes scripts for parsing this output and creating a plot where each cog present in the data are grouped accordingly to the clustering results, namely COG_table.py and COGPlot.R. These scripts are added to the virtual environment, try check out their usage::
    
    COG_table.py -h
    COGPlot.R -h

Let's first create a plot for the single sample run::

    COG_table.py -b ~/binning-workshop/data/Contigs_gt1000_blast.out -c ~/binning-workshop/concoct_output/3000_one_sample/clustering_gt3000.csv -m ~/binning-workshop/data/scg_cogs_min0.97_max1.03_unique_genera.txt --cdd_cog_file ~/binning-workshop/data/cdd_to_cog.tsv > ~/binning-workshop/cog_table_3000_single_sample.tsv
    COGPlot.R -s ~/binning-workshop/cog_table_3000_single_sample.tsv -o ~/binning-workshop/cog_plot_3000_single_sample.pdf

This command might not work for some R related reason. If you've tried getting it to work more than you wish to do, just copy the results from the workshop directory::

    cp /proj/g2014113/nobackup/concoct-workshop/cogplots/* ~/binning-workshop/    


This command should have created a pdf file with your plot. In order to look at it, you can download it to your personal computer with scp. OBS! You need to run this in a separate terminal window where you are not logged in to Uppmax::

    scp username@milou.uppmax.uu.se:~/binning-workshop/cog_plot_3000_single_sample.pdf ~/Desktop/

Have a look at the plot and try to figure out if the clustering was successful or not. Which clusters are good? Which clusters are bad? Are all clusters present in the plot?
Now, lets do the same thing for the multiple samples run::

    COG_table.py -b ~/binning-workshop/data/Contigs_gt1000_blast.out -c ~/binning-workshop/concoct_output/3000_all_samples/clustering_gt3000.csv -m ~/binning-workshop/data/scg_cogs_min0.97_max1.03_unique_genera.txt --cdd_cog_file ~/binning-workshop/data/cdd_to_cog.tsv > ~/binning-workshop/cog_table_3000_all_samples.tsv
    COGPlot.R -s ~/binning-workshop/cog_table_3000_all_samples.tsv -o ~/binning-workshop/cog_plot_3000_all_samples.pdf

And download again from your separate terminal window::

    scp username@milou.uppmax.uu.se:~/binning-workshop/cog_plot_3000_all_samples.pdf ~/Desktop

What differences can you observe for these plots? Think about how we were able to use samples not included in the assembly in order to create a different clustering result. Can this be done with any samples?

