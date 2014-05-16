======================================================================
Estimating differentially abundant protein families in the metagenomes
======================================================================
Finally, we are about to do some real analysis of the data, and look
at the results! To do this, we will use the R statistical program.
You start the program by typing::
    
    R
    
Loading the the count tables
============================

We will begin by loading the count tables from HMMER into R::

    b1 = read.table("baltic1.hmmsearch", sep = "", comment.char = "", skip = 3)

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
per million reads:

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
    
    merge_four(b1_counts,b2_counts,swe_counts,ind_counts,c("Baltic 1","Baltic 2","Sweden", "India"))

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

Comparing normalizations
========================

Let us now quickly compare the three normalization methods. As a quick
overview, we can just make three colorful barplots next to each other,
each representing one normalization method::

    layout(matrix(1:3,1,3))
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

That shoudn't have given you much luck. Let's see if we can find any genes
that occur in at least three samples::

    norm1[rowSums(norm1 > 0) >= 3,]

Better! Select one of those and find out its row number in the count table.
Hint: ``row.names(norm1)`` will help you here! Now lets make boxplots for
that row only::

    x = <insert your selected row number here>
    layout(matrix(1:3,1,3))
    barplot(norm1[x,], main = paste(row.names(norm1)[x], "- Counts per million reads"))
    barplot(norm2[x,], main = paste(row.names(norm2)[x], "- Counts per 16S rRNA"))
    barplot(norm3[x,], main = paste(row.names(norm3)[x], "- Relative abundance"))
    
You can now try this for a number of other genes (by changing the value of
``x``) and see how normalization affects your story.

**Question: Which normalization method would be most suitable to use in this case?**

