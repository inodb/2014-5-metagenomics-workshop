==========================================================
Translating nucleotide sequences into amino acid sequences
==========================================================
The first step before we can annotate the contigs with Pfam domains using
HMMER will be to translate the reads into amino acid sequences. This is
necessary because HMMER (still) does not translate nucleotide sequnces
into protein space on the fly (like,for example, BLAST). For completing
this task we will use ``transeq``, part of the `EMBOSS <http://emboss.sourceforge.net>`_
package.
    
Running ``transeq`` on the sequence data sets
=============================================
To run ``transeq``, take a look at its available options::

    transeq -h
    
A few options are important in this context. First of all, we need to
supply an input file, using the (somewhat bulky) option ``-sequence``.
Second, we also need to specify an output file, otherwise transeq will
simply write its output to the screen. This is specified using the
``-outseq`` option.

However, if we just run ``transeq`` like this we will
run into two additional problems. First, ``transeq`` by default just
translate the reading frame beginning at the first base in the input sequnece,
and will ignore any bases in the reading frames beginning with base two
and three, as well as those on the reverse-complementary strand. Second,
the software will add stop characters in the form of asterixes ``*`` whenever
it encounters a stop codon. This will occasionally cause HMMER to choke, so we
want stop codons to instead be translated into X characters that HMMER can handle.
The following excerpt form the `HMMER creator's blog <http://selab.janelia.org/people/eddys/blog/?p=424>`_
on this subject is one of my personal all-time favorites in terms of computer
software documentation:

    There’s two ways people do six-frame translation. You can translate each
    frame into separate ORFs, or you can translate the read into exactly six
    “ORFs”, one per frame, with * chararacters marking stop codons. HMMER
    prefers that you do the former. Technically, * chararacters aren’t legal
    amino acid residue codes, and the author of HMMER3 is a pedantic nitpicker,
    passive-aggressive, yet also a pragmatist: so while HMMER3 pragmatically
    accepts * chararacters in input “protein” sequences just fine, it pedantically
    relegates them to somewhat suboptimal status, and it passively-aggressively
    figures that any suboptimal performance on *-containing ORFs is your own
    fault for using *’s in the first place.
    
To avoid making Sean Eddy angry and causing other problems for our HMMER runs,
we will use the ``-frame 6`` option to ``transeq`` in order to get translations
of all six reading frames, and the ``-clean`` option to convert stop codons to X
instead of *.

That should give us the command:

    transeq -sequence <input file> -outseq <output file> -frame 6 -clean
    
Now run this command on all X input files that we just have downloaded. When the
command has finished for all files, we can move on to the actual annotation.
