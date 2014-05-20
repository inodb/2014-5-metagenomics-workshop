===============================
Functional annotation
===============================
Now that we have extracted the genes/proteins we want to functionally annotate
those. There are a bunch of ways of doing this. We will use webMGA to do do
rpsBLAST searches against the COG database. COGs are clusters of orthologs
genes, i.e.  evolutionary counterparts in different species, usually with the
same function (http://www.ncbi.nlm.nih.gov/COG/). Many COGs have known
functions and the COGs are also grouped at a higher level with functional
classes.

To download the protein sequences that Prodigal generated, open a local
terminal and type::

    mkdir -p ~/metagenomics/cfa/prodigal
    cd ~/metagenomics/cfa/prodigal
    scp username@milou.uppmax.uu.se:~/metagenomics/cfa/prodigal/baltic-sea-ray-noscaf-41.1000.aa.fa .

To get COG classifications of your proteins, go to webMGA
http://weizhong-lab.ucsd.edu/metagenomic-analysis/ and select Server  /
Function annotation / COG. Upload the protein file
(``baltic-sea-ray-noscaf-41.1000.aa.fa``) and use the default -e value cutoff.
rpsBLAST is used, which is a BLAST based on position specific scoring matrices
(pssm). For each COG, one such pssm has been constructed. These are compiled
into a database of profiles that is searched against.
http://www.ncbi.nlm.nih.gov/staff/tao/URLAPI/wwwblast/node20.html. rpsBLAST is
more sensitive than a normal BLAST, which is important if genomes in your
metagenome are distant from existing sequences in databases. It is also faster
than searching against all proteins out there.

When the search is done you get a zipped folder. On milou, create the
directory::

    mkdir -p ~/metagenomics/cfa/wmga-cog

Use wget or curl to download the zip file on uppmax or use scp to upload it to
that folder i.e.::

    scp output.zip username@milou.uppmax.uu.se:~/metagenomics/cfa/wmga-cog

Then unzip the file on kalkyl::

    cd ~/metagenomics/cfa/wmga-cog
    unzip output.zip

Have a look at the README.txt to see what all the files represent. The file
output.2 includes detailed information on the classifications for every protein
with a hit below the -e value cutoff. View them with::

    less README.txt
    less -S output.2

NOTE: If the queueing takes too much time you can also just copy the results
from the project dir::

    cp -r /proj/g2014113/metagenomics/cfa/wmga-cog/ ~/metagenomics/cfa/

**Question: What seem to be the 3 most abundant COG classes in our combined
sample (not taking coverage into account)?**
.. less output.2.class | tail -n +2 | sort -nk2,2 | tail -3
   J       1895    Translation, ribosomal structure and biogenesis 
   R       2031    General function prediction only 
   E       2308    Amino acid transport and metabolism 
