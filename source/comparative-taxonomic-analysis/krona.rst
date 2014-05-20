===============================
Visualising taxonomy with KRONA
===============================
To get a graphical representation of the taxonomic classifications you can use
KRONA, which is an excellent program for exploring data with hierarchical
structures in general. The output file is an html file that can be viewed in a
browser. Again make a directory for KRONA::

    mkdir -p ~/metagenomics/cta/krona
    cd ~/metagenomics/cta/krona

And run KRONA, concatenating the archaea and bacteria class files together at the same time like this and providing the name of the sample::

    ktImportRDP \
    <(cat ../rdp/0328_rrna.silva-arc-16s-database-id95.fasta.class.tsv ../rdp/0328_rrna.silva-bac-16s-database-id85.fasta.class.tsv),0328 \
    <(cat ../rdp/0403_rrna.silva-arc-16s-database-id95.fasta.class.tsv ../rdp/0403_rrna.silva-bac-16s-database-id85.fasta.class.tsv),0403 \
    <(cat ../rdp/0423_rrna.silva-arc-16s-database-id95.fasta.class.tsv ../rdp/0423_rrna.silva-bac-16s-database-id85.fasta.class.tsv),0423 \
    <(cat ../rdp/0531_rrna.silva-arc-16s-database-id95.fasta.class.tsv ../rdp/0531_rrna.silva-bac-16s-database-id85.fasta.class.tsv),0531 \
    <(cat ../rdp/0619_rrna.silva-arc-16s-database-id95.fasta.class.tsv ../rdp/0619_rrna.silva-bac-16s-database-id85.fasta.class.tsv),0619 \
    <(cat ../rdp/0705_rrna.silva-arc-16s-database-id95.fasta.class.tsv ../rdp/0705_rrna.silva-bac-16s-database-id85.fasta.class.tsv),0705 \
    <(cat ../rdp/0709_rrna.silva-arc-16s-database-id95.fasta.class.tsv ../rdp/0709_rrna.silva-bac-16s-database-id85.fasta.class.tsv),0709 \
    <(cat ../rdp/1001_rrna.silva-arc-16s-database-id95.fasta.class.tsv ../rdp/1001_rrna.silva-bac-16s-database-id85.fasta.class.tsv),1001 \
    <(cat ../rdp/1004_rrna.silva-arc-16s-database-id95.fasta.class.tsv ../rdp/1004_rrna.silva-bac-16s-database-id85.fasta.class.tsv),1004 \
    <(cat ../rdp/1028_rrna.silva-arc-16s-database-id95.fasta.class.tsv ../rdp/1028_rrna.silva-bac-16s-database-id85.fasta.class.tsv),1028 \
    <(cat ../rdp/1123_rrna.silva-arc-16s-database-id95.fasta.class.tsv ../rdp/1123_rrna.silva-bac-16s-database-id85.fasta.class.tsv),1123

The ``<()`` in bash can be used for process substitution
(http://tldp.org/LDP/abs/html/process-sub.html ). Just for your information,
the above command was actually generated with the following commands::

    cmd=`echo ktImportRDP; for s in ${samplenames[*]}; do echo '<('cat ../rdp/${s}_rrna.silva-arc-16s-database-id95.fasta.class.tsv ../rdp/${s}_rrna.silva-bac-16s-database-id85.fasta.class.tsv')',$s; done`
    echo $cmd

Copy the resulting file rdp.krona.html to your local computer with scp and open it in firefox.
