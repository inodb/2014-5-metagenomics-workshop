======================================================================
Estimating differentially abundant protein families in the metagenomes
======================================================================
Finally, we are about to do some real analysis of the data, and look
at the results! To do this, we will use the R statistical program.
You start the program by typing::
    
    R
    
To get out of R, you type ``q()``. You will then be asked if you want
to save your workspace. Typing "y" (yes) might be smart, since that
will remember all your variables until the next time you use R in the
same directory!
    
Loading the the count tables
============================

We will begin by loading the count tables from HMMER into R::

    b1 = read.table("baltic1.hmmsearch", sep = "")

To get the number of entries of each kind, we will use the R command ``rle``.
We want to get the domain list, which is the third column. For ``rle`` to be
able to work with the data, we must also convert it into a proper vector.::

    raw_counts = rle(as.vector(b1[,3]))
    b1_counts = as.matrix(raw_counts$lengths)
    row.names(b1_counts) = raw_counts$values
    
Repeat this procedure for all four data sets.

Apply normalizations
====================

We will now try out the three different normalization methods to see their
effect on the data. First, we will try by normalizing to the number of reads
in each sequencing library. Find the note you have taken on the data set sizes.
Then apply a command like this on the data::

    b1_norm1 = b1_counts / 118025
    
You will now see counts in the range of 10^-5 and 10^6. To make these numbers
more interpretable, let's also multiply them by 1,000,000 to yield the counts
per million reads::

    b1_norm1 = b1_counts / 118025 * 1000000
    
Do the same thing for the other data sets.

We would then like to compare all the four data sets to each other. Since R's
merge function really suck for multiple data sets, I have provided this
function for merging four data sets. Copy and paste it into the R console::
    
    merge_four = function(a,b,c,d,names) {
    m1 = merge(a,b,by = "row.names", all = TRUE)
    row.names(m1) = m1[,1]
    m1 = m1[,2:3]
    m2 = merge(c, m1, by = "row.names", all = TRUE)
    row.names(m2) = m2[,1]
    m2 = m2[,2:4]
    m3 = merge(d, m2, by = "row.names", all = TRUE)
    row.names(m3) = m3[,1]
    m3 = m3[,2:5]
    m3[is.na(m3)] = 0
    colnames(m3) = c(names[4], names[3], names[1], names[2])
    return(as.matrix(m3))
    }
    
You can then try it by running this command on the raw counts::
    
    norm0 = merge_four(b1_counts,b2_counts,swe_counts,ind_counts,c("Baltic 1","Baltic 2","Sweden", "India"))

You should then see a matrix containing all counts from the four data
sets, with each row corresponding to a Pfam family. Next, run the same
command on the normalized data and store the output into a variable, called
for example ``norm1``. The total abundance of mobility domains can then be
visualzied using the following command::

    barplot(colSums(norm1))

We can then repeat the normalization procedure, by instead normalizing to
the number of 16S rRNA counts in each library. This can be done similarly
to the division by total number of reads above::

    b1_norm2 = b1_counts / 21
    
This time, we won't multiply by a million, as that would make numbers
much larger (and harder to interpret).

Follow the above procedure for all the data sets, and finally store the
end result from ``merge_four`` into a variable, for example called ``norm2``.

Finally, we will do the same for the third type of normalization, the
division by the mapped number of reads. This can, once more, be done as
above::

    b1_norm3 = b1_counts / 22
    
Follow the above procedure for all the data sets, and store the final
result from ``merge_four`` into a variable, for example called ``norm3``.

A note on saving plots
======================
Note that if you would like to save your plots to a PDF file you can run
the command::

    pdf("output_file_name.pdf", width = 10, height = 10)
    
and then you can just run all the R commands as normal. Instead of getting
plots printed on the screen, all the plots will be output to the specified
PDF file, and can later be viewed in e.g. Acrobat Reader. When you are
finished plotting you can finalize the PDF file using the command::

    dev.off()
    
This closes the PDF and enables other software to read it. Please note that
it will be considered a "broken" PDF until the ``dev.off()`` command is run!

Comparing normalizations
========================

Let us now quickly compare the three normalization methods. As a quick
overview, we can just make three colorful barplots next to each other,
each representing one normalization method::

    layout(matrix(c(1,3,2,4),2,2))
    barplot(norm0, col = 1:nrow(norm1), main = "Raw gene counts")
    barplot(norm1, col = 1:nrow(norm1), main = "Counts per million reads")
    barplot(norm2, col = 1:nrow(norm2), main = "Counts per 16S rRNA")
    barplot(norm3, col = 1:nrow(norm3), main = "Relative abundance")
    
As you can see, each of these plots will tell a slightly different story.
Let's take a closer look at how normalization affect the behavior of some
genes. First, we can see if there are any genes that are present in all
samples. This is easily investigated by the following command, which takes
counts if a value is larger than zero, counts the number of occurences per
per row (rowSums), and finally outputs all the rows from ``norm1`` where
this sum is exactly four::

    norm1[rowSums(norm1 > 0) == 4,]

If that didn't give you much luck, you can try if you can find any genes
that occur in at least three samples::

    norm1[rowSums(norm1 > 0) >= 3,]

Select one of those and find out its row number in the count table.
Hint: ``row.names(norm1)`` will help you here! Now lets make boxplots for
that row only::

    x = <insert your selected row number here>
    layout(matrix(c(1,3,2,4),2,2))
    barplot(norm0[x,], main = paste(row.names(norm1)[x], "- Raw gene counts"))
    barplot(norm1[x,], main = paste(row.names(norm1)[x], "- Counts per million reads"))
    barplot(norm2[x,], main = paste(row.names(norm2)[x], "- Counts per 16S rRNA"))
    barplot(norm3[x,], main = paste(row.names(norm3)[x], "- Relative abundance"))
    
You can now try this for a number of other genes (by changing the value of
``x``) and see how normalization affects your story.

**Question: Which normalization method would be most suitable to use in this case? Why?**


Visualizing differences in gene abundance
=========================================

One neat way of visualizing metagenomic count data is through heatmaps. R has a built-in
heatmap function, that can be called using the (surprise...) ``heatmap`` command.
However, you will quickly notice that this function is rather limited, and we will
therefore install a package containing a better one - the ``gplots`` package. You can do
this by typing the following command::

    install.packages("gplots")
    
Just answer "yes" to the questions, and the package will be installed locally for your
user. After installation you load the package by typing::

    library(gplots)

After this, you will be able to use the more powerful ``heatmap.2`` command. Try,
for example, this command on the data::

    heatmap.2(norm1, trace = "none", col = colorpanel(255,"black","red","yellow"), margin = c(5,10), cexCol = 1, cexRow = 0.7)
    
The trace, margin, cexCol and cexRow options are just there to make the plot look better
(play around with them if you wish). The ``col = colorpanel(255,"black","red","yellow")``
option creates a scale from black to yellow where yellow means highly abundant and black
lowly abundant. To make more clear which genes that are not even detected, let's add a
grey color to that for genes with zero count::

    heatmap.2(norm1, trace = "none", col = c("grey",colorpanel(255,"black","red","yellow")), margin = c(5,10), cexCol = 1, cexRow = 0.7)

You will now notice that it is hard to see the differences for the lowly abundant genes.
To aid in this, we can add a variance-stabilizing transform (fancy name for squareroot)
to the data::

    norm1_sqrt = sqrt(norm1)

You can then re-run the ``heatmap.2`` command on the newly created ``norm1_sqrt``
variable.

Sometimes, it makes more sense to apply a logarithmic transform to the data instead of
the squareroot. This, however, is a bit more tricky since we have zeros in the data.
For fun's sake, we can try::

    norm1_log10 = log10(norm1)
    heatmap.2(norm1_log10, trace = "none", col = c("grey",colorpanel(255,"black","red","yellow")), margin = c(5,10), cexCol = 1, cexRow = 0.7)

This should give you an error message. The easiest way to solve this problem is to add
some small number to the matrix before the ``log10`` command. Since we will display this
number with grey color anyway, it will in this case, and for this application, matter
much exactly what number you add. You can, for example, choose 1::

    norm1_log10 = log10(norm1 + 1)
    heatmap.2(norm1_log10, trace = "none", col = c("grey",colorpanel(255,"black","red","yellow")), margin = c(5,10), cexCol = 1, cexRow = 0.7)

Before we end, let's also try another kind of commonly used visualization, the PCA plot.
Principal Component Analysis (PCA) essentially builds upon projecting complex data onto a
2D (or 3D) surface, while trying to separate the data points as much as possible. This
can be useful for finding groups of observations that fit together. We will use the built-in
PCA command called ``prcomp``::

    norm1_pca = prcomp(norm1_sqrt)

Note that we used the data created using the variance stabilizing transform. There are more
sophisticated ways of reducing the influence of very large values, but many times the
squareroot is sufficient. We can visualize the PCA using a plotting command called ``biplot``::

    layout(1)      
    biplot(norm1_pca, cex = 0.5)
    
To see the proportion of variance explained by the different components, we can use the
normal plot command::

    plot(norm1_pca)
    
We want the first two bars to be as large as possible, since that means that the dataset
can be easily simplified to two dimensions. If all bars are of roughly equal height, the
projection to a 2D surface has caused a loss of much of the information of the data, and
we can not trust the patterns in the PCA plot as much.

If we do the PCA on the relative abundance data (normalization three), we can get a view
of which Pfam domains that dominate in these samples::

    norm3_pca = prcomp(norm3)
    biplot(norm3_pca, cex = 0.5)

And that's the end of the lab. If you have lots of time to spare, you can move on to the
bonus excersize, in which we will analyze the 16S rRNA data generated by Metaxa2 further,
to understand which bacterial species that are present in the samples.
