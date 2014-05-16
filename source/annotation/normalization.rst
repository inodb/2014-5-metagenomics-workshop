==========================================================
Normalization of count data from the metagenomic data sets
==========================================================
An important aspects of working with metagenomics is to apply proper
normalization procedures to the retrieved counts. There are several
ways to do this, and in part the method of choice is dependent on
the research question investigated, but in part also based on more
philosphical considerations. Let's start with a bit of theory.

Why is normalization important?
===============================
Generally, sequencing data sets are not of the same size. In addition,
different genes and genomes come in different sizes, which means that
*at equal coverage, the number of mapped reads to a certain gene or
region will be directly dependent on the length of that region*.
Luckily, the latter scenario is not a huge issue for Pfam families
(although it exists), and we will not care about it more today. We
will however care about the size of the sequencing libraries. To make
relatively fair comparisons between sets, we need to normalize the
gene counts to something. Let's begin with checking how unequal the
librairies are. You can do that by counting the number of sequences
in the FASTA files, by checking for the number of ">" characters in
each file, using ``grep``::

    grep -c ">" <input file>
    
As you will see, there are quite substantial differences in the
number of reads in each library. How do we account for that?

What normalization methods are possible?
========================================

The choice of normalization method will depend on what research
question we want to ask. An easy way of removing the technical
bias related to different sequencing effort in different libraries
is to simply divide each gene count with the total library size.
That will yield a relative proportion of counts to that gene. To
make that number easier to interpret, we can multiply it by
1,000,000 to get *the number of reads corresponding to that gene
or feature per million reads*.

    (counts of gene X / total number of reads) * 1000000

This is a quick way of normalizing, but it does not consider
the composition of the sample. Say that you are interested in
studying bacterial gene content within e.g. different plant hosts.
Then the interesting changes in bacterial composition might be
drowned by genetic material from the host plant. That will then
have a huge impact on the gene abundances of the bacteria, even if
those abundances are actually the same. The same applies to complex
microbial communities with both bacteria, single-cell eukaryotes
and viruses. In such cases, it might be better to consider a
normalization to the number of bacteria in the sample (or eukaryotes
if that is what you want to study). One way of doing that is to
count the number of reads mapping to the 16S rRNA gene in each
sample. You can then divide each gene count with the number of
16S rRNA counts, to yield a genes per 16S proportion.

    (counts of gene X / counts of 16S rRNA gene)
    
There is a few problems with using the 16S rRNA gene in this way.
The most prominient one is that the gene exists in a single copy in
some bacteria, but in multiple (sometimes >10) copies in other
species. That means that this number will not truly be a per-genome
estimate. Other genetic markers, such as the *rpoB* gene has been
suggested for this, but has not yet taken off.

Finally, we could imagine a scenario in which you are only
interested in the proportion of different annotated features in
your sample. One can then instead divide to the total number of
reads mapped to *something* in the database used. That will give
relative proportions, and will remove a lot of "noise", but will
have the limitation that only the well-defined part of the
microbial community can be studied, and the rest is ignored.

    (counts of gene X / total number of mapped reads)

    
Trying out some normalization methods
=====================================
We are now ready to try out these methods on our data.

Which method should we settle with?
===================================
