==================
Gene finding
==================
Now that you have assembled the data into contigs next natural step to do is
annotation of the data, i.e. finding the genes and doing functional annotation
of those. For gene finding a range of programs are available (Metagene
Annotator, MetaGeneMark, Orphelia, FragGeneScan), here we will use Prodigal
which is very fast and has recently been enhanced for metagenomics. We will use
the -p flag which instructs Prodigal to use the algorithm suitable for
metagenomic data. We will not continue with the data from the morning but will
use another dataset consisting of 11 samples from a time series sampling of
surface water in the Baltic Sea. Sequencing was done with Illumina MiSeq here
generating on average 835,048 2 x 250 bp reads per sample. The reads can be
found here::

    /proj/g2013206/metagenomics/reads/

The first four numbers in the filename represent a date. All samples are from
2012. R1 and R2 both contain one read of a pair. They are ordered, so the first
four lines in R1 are paired with the read in the first four lines of R2. They
are in CASAVA v1.8 format (http://en.wikipedia.org/wiki/FASTQ_format).

You can find the contigs from a combined assembly on reads from all samples here::

    /proj/g2013206/metagenomics/assembly/baltic-sea-ray-noscaf-41.1000.fa

They have been constructed with Ray using a kmer of 41 and no scaffolding. Only
contigs >= 1000 are in this file.

Note that all solutions (i.e. the generated outputs) for the exercises are also in::

    /proj/g2013206/metagenomics/

In all the following exercises you should again use the virtual environment to
get all the necessary programs::

    source /proj/g2013206/metagenomics/virt_env/mg-workshop/bin/activate

It’s time to run Prodigal. First create an output directory with a copy of the
contig file::

    mkdir -p ~/metagenomics_workshop2/prodigal
    cd ~/metagenomics_workshop2/prodigal
    cp /proj/g2013206/metagenomics/assembly/baltic-sea-ray-noscaf-41.1000.fa .

Then run Prodigal on the contig file (~2m20)::

    prodigal -a baltic-sea-ray-noscaf-41.1000.aa.fa \ 
                  -d baltic-sea-ray-noscaf-41.1000.nuc.fa \
                   -i baltic-sea-ray-noscaf-41.1000.fa \
                   -f gff -p meta \
                   > baltic-sea-ray-noscaf-41.1000.gff

This will produce 3 files, a fasta file with the gene sequences (nucleotides) a
fasta file with the protein sequences (aminoacids) and a gff file that is a
standardised file type for showing annotations. It’s a tab delimited file that
can be viewed by e.g. ::

    less baltic-sea-ray-noscaf-41.1000.gff

Pass the option -S to less if you don’t want lines to wrap

An explanation of the gff format can be found at
http://genome.ucsc.edu/FAQ/FAQformat.html
