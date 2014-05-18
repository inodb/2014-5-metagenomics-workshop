==============================================
Determine gene coverage in metagenomic samples
==============================================
Ok, now that we know what functions are represented in the combined samples (we
could call it the Baltic meta-community, i.e. a community of communities), we
may want to know how much of the different functions (COG families and classes)
are present in the different samples, since this will likely change between
seasons. To do this we first map the reads from the different samples against
the contigs. We will use the mapping script that we used this morning. First
create a directory and cd there::

    mkdir -p ~/metagenomics_workshop2/map
    cd ~/metagenomics_workshop2/map

Copy the contig file and build an index on it for bowtie2. Note that this does
not work with a symbolic link, which is why we copy the contigs this time. We
are going to map all samples against the assembly in parallel which is why we
have to build the index of the assembly first. Otherwise all processes will all
be trying to build the index for the assembly at the same time. There’s no way
to do this step in parallel yet that we are aware of::

    cp /proj/g2013206/metagenomics/assembly/baltic-sea-ray-noscaf-41.1000.fa .
    bowtie2-build baltic-sea-ray-noscaf-41.1000.fa baltic-sea-ray-noscaf-41.1000.fa

You will end up with various baltic-sea-ray-noscaf-41.1000.fa.*.bt2 files that
represent the index for the assembly. It allows for faster alignment of
sequences, see http://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform
for more information.

Get a bash array with all the sample names
(http://www.linuxjournal.com/content/bash-arrays )::

    samplenames=( $(for s in /proj/g2013206/metagenomics/reads/*_R1.fastq.gz; do echo ${s: -16:4}; done) )
    echo ${samplenames[*]}

Map the reads for each sample in parallel (cancel this whenever because it
takes too much time)::

    parallel mkdir -p {} '&&' cd {} '&&' bash $METASSEMBLE_DIR/scripts/map/map-bowtie2-markduplicates.sh -ct 1 \
        /proj/g2013206/metagenomics/reads/{}_R1.fastq.gz  /proj/g2013206/metagenomics/reads/{}_R2.fastq.gz pair \
        ~/metagenomics_workshop2/map/baltic-sea-ray-noscaf-41.1000.fa asm bowtie2 \
        ::: ${samplenames[*]}

Since this step takes a lot of time you can cancel the task with Ctrl+C and
just copy the data that we have already generated::

    cp -r /proj/g2013206/metagenomics/map/* ~/metagenomics_workshop2/map

Next we want to figure out the coverage for every gene in every contig, for one
sample at a time. We will use the bedtools coverage command within the BEDTools
suite (https://code.google.com/p/bedtools/) that can parse a SAM/BAM file and a
gff file to extract coverage information for every gene::

    mkdir -p ~/metagenomics_workshop2/coverage-hist-per-feature-per-sample
    cd ~/metagenomics_workshop2/coverage-hist-per-feature-per-sample

Again make sure you have the bash array with all the sample names::

    samplenames=( $(for s in /proj/g2013206/metagenomics/reads/*_R1.fastq.gz; do echo ${s: -16:4}; done) )
    echo ${samplenames[*]}

Then run bedtools coverage on all samples using parallel (~4m)::

    parallel bedtools coverage -hist -abam ../map/{}/bowtie2/asm_pair-smds.bam \
        -b ../prodigal/baltic-sea-ray-noscaf-41.1000.gff \
        '>' {}-baltic-sea-ray-noscaf-41.1000.gff.coverage.hist ::: ${samplenames[*]}

Have a look at which files have been created with less again. The final four
columns give you the histogram i.e. coverage, number of bases with that
coverage, length of the contig/feature/gene, bases with that coverage expressed
as a ratio of the length of the contig/feature/gene.

Once you have run this for all samples you can combine these files with the COG
annotation file that you generated before with the script
br-sum-mean-cov-per-cog.py  (made by us) like this (~2m47)::

    mkdir -p ~/metagenomics_workshop2/cog-sum-mean-cov
    cd ~/metagenomics_workshop2/cog-sum-mean-cov
    br-sum-mean-cov-per-cog.py --samplenames <(for s in ${samplenames[*]}; do echo $s; done) \
        ../prodigal/baltic-sea-ray-noscaf-41.1000.gff ../prodigal/baltic-sea-ray-noscaf-41.1000.aa.fa \
        ../wmga-cog/output.2 ../coverage-hist-per-feature-per-sample/*.gff.coverage.hist \
        > cog-sum-mean-cov.tsv

Have a look at the table with less -S again.
