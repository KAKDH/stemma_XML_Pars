# Stemma_XML_Pars

This repository contains scripts and data created in September 2023 to accompany the article 'A digital perspective on the role of a stemma in material-philological transmission studies' accepted for publication in Studier i Nordisk (scheduled for 2024). 

*1. Scripts*

In the Scripts folder you can find two Python scripts which can convert an TEI-XML apparatus criticus into an input file for PARS (part of PHYLIP package) to visualise relationships between manuscripts. Both scripts are based on my unpublished prepareParsInput.py script from 2017, which was revised into two separate versions in September 2023 to process differently structured inputs. 

1.1. parsInput_noLem.py
The parsInput_noLem.py script goes with testEd_noLem.xml and produces parsInput_noLem.txt, which then can be used directly as an input for PARS. 

parsInput_noLem.py requires a well-formatted TEI-XML with the <listWit> (witness list) element, which lists all the witnesses. It assumes that the <lem> (lemma) element does not have the wit (witness) attribute, but all <rdg> (reading) elements have the wit (witness) attribute with values pointing to the list of witnesses. 
It assigns the same numeric value to all witnesses that are not encoded in the <rdg> (reading) elements, assuming that they agree with lemma.

1.2 The parsInput_withLem.py script does with testEd_withLem.xml and produces parsInput_noLem.txt, which then can be used directly as an input for Pars. 

parsInput_withLem.py requires a well-formatted TEI-XML with the <listWit> (witness list) element, which lists all witnesses. It assumes that all the <lem> (lemma) and <rdg> (reading) elements have the wit (witness) attribute with values pointing to the list of witnesses. It assigns the same numeric value to all witnesses that are encoded in the same <rdg> or <lem> elements.



