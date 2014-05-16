======================================================================
Estimating differentially abundant protein families in the metagenomes
======================================================================
Finally, we are about to do some real analysis of the data, and look
at the results! To do this, we will use the R statistical program.
You start the program by typing::
    
    R
    
Reformatting the count tables
=============================

We will begin by loading the count table from HMMER into R::

    data = read.table("baltic1.hmmsearch", sep = "", comment.char = "", skip = 3)

To get the number of entries of each kind, we will use the R command ``rle``.
We want to get the domain list, which is the third column. For ``rle`` to be
able to work with the data, we must also convert it into a proper vector.::

    raw_counts = rle(as.vector(data[,3]))
    counts = as.matrix(raw_counts$lengths)
    row.names(counts) = raw_counts$values
    
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
    return(m3)
    }
    
    merge_four(b1_counts,b2_counts,swe_counts,ind_counts,c("Baltic 1","Baltic 2","India", "Sweden"))
    
    m1 = merge(b1_counts,b2_counts,by = "row.names", all = TRUE)
    row.names(m1) = m1[,1]
    m1 = m1[,2:3]
    m2 = merge(swe_counts, m1, by = "row.names", all = TRUE)
    row.names(m2) = m2[,1]
    m2 = m2[,2:4]
    m3 = merge(ind_counts, m2, by = "row.names", all = TRUE)
    row.names(m3) = m3[,1]
    m3 = m3[,2:5]
    m3[is.na(m3)] = 0
    colnames(m3) = c("Indian lake", "Swedish lake", "Baltic 1", "Baltic 2")
    
