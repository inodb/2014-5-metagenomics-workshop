=================================================
Comparative functional analysis with R
=================================================
Having this table one can use different statistical and visualisation software
to analyse the results. One option would be to import a simpler version of the
table into the program Fantom, a graphical user interface program developed for
comparative analysis of metagenome data. You can try this in the end of the day
if you have time.

But here we will use the statistical programming language R to do some simple
analysis. cd to the directory where you have the cog-sum-mean-cov.tsv file.
Then start R::

    cd ~/metagenomics_workshop2
    R

and import the data::

    tab_cog <- read.delim("cog-sum-mean-cov/cog-sum-mean-cov.tsv")

Assign the different columns with descriptors to vectors of logical names::

    cogf <- tab_cog[,1] # cog family
    cogfd <- tab_cog[,2] # cog class
    cogc <- tab_cog[,3] # cog family descriptor
    cogcd <- tab_cog[,4] # cog class descriptor

Make a matrix with the coverages of the cog families::

    cogf_cov <- as.matrix(tab_cog[,5:ncol(tab_cog)]) # coverage in the different samples

And why not put sample names into a vector as well::

    sample <- colnames(cogf_cov)
    sample

Let’s clean the sample names a bit::

    for (i in 1:length(sample)) {
        sample[i] <- matrix(unlist(strsplit(sample[i],"_")), 1)[1,4]
    }

Since the coverages will differ depending on how many reads per sample we have
we can normalise by dividing the coverages by the total coverage for the sample
(only considering cog-annotated genes though)::

    for (i in 1:ncol(cogf_cov)) {
        cogf_cov[,i] <- cogf_cov[,i]/sum(cogf_cov[,i])
    }

The cogf_cov gives coverage per cog family. Let’s summarise within cog classes
and make a separate matrix for that::

    unique_cogc <- levels(cogc)
    cogc_cov <- matrix(ncol = length(sample), nrow = length(unique_cogc))
    colnames(cogc_cov) <- sample
    rownames(cogc_cov) <- unique_cogc
    for (i in 1:length(unique_cogc)) {
        these <- grep(paste("^", unique_cogc[i],"$", sep = ""), cogc)
        for (j in 1:ncol(cogf_cov)) {
            cogc_cov[i,j] <- sum(cogf_cov[these,j])
        }
    }


OK, now let’s start playing with the data. We can for example do a pairwise
plot of coverage of cog classes in sample1 vs. sample2::

    plot(cogc_cov[,1], cogc_cov[,2])

or make a stacked barplot showing the different classes in the different
samples::

    barplot(cogf_cov, col = rainbow(100), border=NA)
    barplot(cogc_cov, col = rainbow(10), border=NA)

The vegan package contains many nice functions for doing (microbial) ecology
analysis. Load vegan::

    install.packages("vegan") # not necessary if already installed
    library(vegan)

If installing doesn't work for you have a look here
http://www.stat.osu.edu/computer-support/mathstatistics-packages/installing-r-libraries-locally-your-home-directory

We can calculate pairwise distances between the samples based on their
functional composition. In ecology pairwise distance between samples is
referred to as beta-diversity, although typically based on taxonomic
composition rather than functional::

    cogf_dist <- as.matrix(vegdist(t(cogf_cov), method="bray", binary=FALSE, diag=TRUE, upper=TRUE, na.rm = FALSE))  
    cogc_dist <- as.matrix(vegdist(t(cogc_cov), method="bray", binary=FALSE, diag=TRUE, upper=TRUE, na.rm = FALSE))  

You can visualise the distance matrices as a heatmaps::

    image(cogf_dist)
    image(cogc_dist)

Are the distances calculated on the different functional levels correlated?::

    plot(cogc_dist, cogf_dist)

Now let’s cluster the samples based on the distances with hierarchical
clustering. We use the function "agnes" in the "cluster" library and apply
average linkage clustering::

    install.packages("cluster") # not necessary if already installed
    library(cluster)

    cluster <- agnes(cogf_dist, diss = TRUE, method = "average")
    plot(cluster, which.plots = 2, hang = -1, label = sample, main = "", axes = FALSE, xlab = "", ylab = "", sub = "")

Alternatively you can use the function heatmap, that calculates distances both
between samples and between features and clusters in two dimensions::

    heatmap(cogf_dist, scale = "none")
    heatmap(cogc_dist, scale = "none")

And let’s ordinate the data in two dimensions. This can be done e.g. by PCA
based on the actual coverage values or by e.g. PcOA or NMDS (non-metrical
dimensional scaling). Let's do NMDS::

    mds <- metaMDS(cogf_dist)
    plot(mds$points[,1], mds$points[,2], pch = 20, xlab = "NMDS1", ylab = "NMDS2", cex = 2)

We can color the samples according to date (provided your samples are ordered
according to date). There are some nice color scales to choose from here
http://colorbrewer2.org/::

    install.packages("RColorBrewer") # not necessary if already installed
    library(RColorBrewer)
    color = brewer.pal(length(sample), "Reds") # or select another color scale!

    mds <- metaMDS(cogf_dist)
    plot(mds$points[,1], mds$points[,2], pch = 20, xlab = "NMDS1", ylab = "NMDS2", cex = 5, col = color)

Let’s compare with how it looks if we base the clustering on COG class coverage
instead::

    mds <- metaMDS(cogc_dist)
    plot(mds$points[,1], mds$points[,2], pch = 20, xlab = "NMDS1", ylab = "NMDS2", cex = 5, col = color)

In addition to these examples there are of course infinite ways to analyse the
results in R. One could for instance find COGs that significantly differ in
abundance between samples, do different types of correlations between metadata
(nutrients, temperature, etc) and functions, etc. Leave your R window open,
since we will compare these results with taxonomic data in a bit.
