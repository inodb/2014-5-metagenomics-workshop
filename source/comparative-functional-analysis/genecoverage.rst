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

    mkdir -p ~/metagenomics/cfa/map
    cd ~/metagenomics/cfa/map

Copy the contig file and build an index on it for bowtie2::

    cp /proj/g2014113/metagenomics/cfa/assembly/baltic-sea-ray-noscaf-41.1000.fa .
    bowtie2-build baltic-sea-ray-noscaf-41.1000.fa baltic-sea-ray-noscaf-41.1000.fa

You will end up with various baltic-sea-ray-noscaf-41.1000.fa.*.bt2 files that
represent the index for the assembly. It allows for faster alignment of
sequences, see http://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform
for more information.

Now we will use some crazy bash for loop to map all the reads. This actually
prints the mapping command instead of executing, because it takes too much time
to run it, it does however create the directories::

    for s in /proj/g2014113/metagenomics/cfa/reads/*_R1.fastq.gz; do
        echo mkdir -p $(basename $s _R1.fastq.gz)
        echo cd $(basename $s _R1.fastq.gz)
        echo map-bowtie2-markduplicates.sh -ct 1 \
            $s ${s/R1/R2} pair \
            ~/metagenomics/cfa/map/baltic-sea-ray-noscaf-41.1000.fa asm \
            bowtie2
        echo cd ..
    done

The for loop iterates over all the first mates of the pairs. It then creates a
directory using the basename of the pair with the directory part and the
postfix removed, goes to that dir and runs ``map-bowtie2-markduplicates.sh`` on
both mates of the pair. Try to change the for loop such that it only maps one
sample.

**Question: Can you think of an easy way to parallelize this?**
.. Add an & after bowtie2

    For more examples on how to parallelize this check: http://bit.ly/gwbash

If you sort of understand what's going on in the for loop above you are welcome
to copy the data that we have already generated::

    cp -r /proj/g2014113/metagenomics/cfa/map/* ~/metagenomics/cfa/map/

Take a look at the files that have been created. Check
``map-bowtie2-markduplicates.sh -h`` for an explanation of the different files.

**Question what is the mean coverage for contig-394 in sample 0328?**
.. 0

Next we want to figure out the coverage for every gene in every contig per
sample. We will use the bedtools coverage command within the BEDTools suite
(https://code.google.com/p/bedtools/) that can parse a SAM/BAM file and a gff
file to extract coverage information for every gene::

    mkdir -p ~/metagenomics/cfa/coverage-hist-per-feature-per-sample
    cd ~/metagenomics/cfa/coverage-hist-per-feature-per-sample

Run bedtools coverage on one sample (~4m)::

    for s in 0328; do
        bedtools coverage -hist -abam ~/metagenomics/cfa/map/$s/bowtie2/asm_pair-smds.bam \
            -b ../prodigal/baltic-sea-ray-noscaf-41.1000.gff \
            > $s-baltic-sea-ray-noscaf-41.1000.gff.coverage.hist
    done

Copy the other ones::

    cp /proj/g2014113/metagenomics/cfa/map/coverage-hist-per-feature-per-sample/* .

Have a look at which files have been created with less again. The final four
columns give you the histogram i.e. coverage, number of bases with that
coverage, length of the contig/feature/gene, bases with that coverage expressed
as a ratio of the length of the contig/feature/gene.

Now what we want to is do is to extract the mean coverage per COG instead of
per gene. Remember that multiple genes can belong to the same COG so we will
take the sum of the mean coverage from those genes. We will use the script
``br-sum-mean-cov-per-cog.py`` (made by us) for that. First make a directory
again and go there::

    mkdir -p ~/metagenomics/cfa/cog-sum-mean-cov
    cd ~/metagenomics/cfa/cog-sum-mean-cov

The script expects a file with one samplename per line so we will create an
array with those sample names
(http://www.thegeekstuff.com/2010/06/bash-array-tutorial/)::

    samplenames=(0328 0403 0423 0531 0619 0705 0709 1001 1004 1028 1123)
    echo ${samplenames[*]}
    for s in ${samplenames[*]}; do echo $s; done

Now we can use process substitution to give the script those sample names
without having to store it to a file first.

**Question: What is the difference between the following statements?**::

    echo ${samplenames[*]}
    cat <(echo ${samplenames[*]})
    cat <(echo ${samplenames[*]} | tr ' ' '\n') 

.. First one just echoes
   second one concatenates the contents of the "file" with samplenames to stdout
   the last one adds newlines

Run the the script that computes the sum of mean coverages per COG (~2m47)::
    br-sum-mean-cov-per-cog.py --samplenames <(echo ${samplenames[*]} | tr ' ' '\n') \
        ../prodigal/baltic-sea-ray-noscaf-41.1000.gff ../prodigal/baltic-sea-ray-noscaf-41.1000.aa.fa \
        ../wmga-cog/output.2 ../coverage-hist-per-feature-per-sample/*.gff.coverage.hist \
        > cog-sum-mean-cov.tsv

Have a look at the table with less -S again.

**Question: What is the sum of mean coverages for COG0038 in sample 0423?**
