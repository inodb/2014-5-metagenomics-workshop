==============================================================
Extracting rRNA encoding reads and annotating them
==============================================================
Taxonomic composition of a sample can be based on e.g. BLASTing the contigs
against a database of reference genomes, or by utilising rRNA sequences.
Usually assembly doesn’t work well for rRNA genes due to their highly conserved
regions, therefore extracting rRNA from contigs will miss a lot of the
taxonomic information that can be obtained by analysing the reads directly.
Analysing the reads also has the advantage of being quantitative, i.e. we don’t
need to calculate coverages by the mapping procedure we applied for the
functional genes above. We will extract rRNA encoding reads with the program
sortmeRNA which is one of the fastest software solutions for this. The program
sortmeRNA has built-in multithreading support so this time we use that for
parallelization. These are the commands to run::

    mkdir -p ~/metagenomics/cta/sortmerna
    cd ~/metagenomics/cta/sortmerna
    samplenames=(0328 0403 0423 0531 0619 0705 0709 1001 1004 1028 1123)
    for s in ${samplenames[*]}
        do sortmerna -n 2 --db \
        /proj/g2014113/src/sortmerna-1.9/rRNA_databases/silva-arc-16s-database-id95.fasta \
        /proj/g2014113/src/sortmerna-1.9/rRNA_databases/silva-bac-16s-database-id85.fasta \
        --I /proj/g2014113/metagenomics/cta/reads/${s}_pe.fasta \
        --accept ${s}_rrna \
        --other ${s}_nonrrna  \
        --bydbs  \
        -a 8  \
        --log ${s}_bilan  \
        -m 5242880
    done

Again, this command takes rather long to run (~5m per sample) so just copy the results if you don’t feel like waiting::

    cp /proj/g2014113/metagenomics/cta/sortmerna/* ~/metagenomics/cta/sortmerna
 
It outputs the reads or part of reads that encode rRNA in a fasta file. These
rRNA sequences can be classified in many ways, and again blasting them against
a suitable database is one option. Here we use a simple and fast method (unless
you have too many samples), the classifier tool at RDP (ribosomal database
project). This uses a naive bayesian classifier trained on many sequences of
defined taxonomies. It gives bootstrap support values for each taxonomic level;
usually the support gets lower the further down the hierarchy you go. Genus
level is the lowest level provided. You can use the web service if you prefer,
and upload each file individually, or you can use the uppmax installation of
RDP classifier like this (~4m)::

    mkdir -p ~/metagenomics/cta/rdp
    cd ~/metagenomics/cta/rdp
    for s in ../sortmerna/*_rrna*.fasta
        do java -Xmx1g -jar /glob/inod/src/rdp_classifier_2.6/dist/classifier.jar \
        classify \
        -g 16srrna  \
        -b `basename ${s}`.bootstrap  \
        -h `basename ${s}`.hier.tsv  \
        -o `basename ${s}`.class.tsv  \
        ${s}
    done
