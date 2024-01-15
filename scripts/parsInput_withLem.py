# parsInput_withLem.py
# Convert xml-based edition to Pars input, where witnesses are specified in the lemma and in the readings
# This script is based on prepareParsInput.py written by Katarzyna Anna Kapitan on 27 November 2017
# It has been revised by Katarzyna Anna Kapitan on 17 September 2023
import sys
import xml.etree.ElementTree as etree
import numpy as np
import re

'''
This script takes an XML-TEI encoded transcription with apparatus <app> <lem> <rdg>,
where lemmas and readings have witnesses assigned. 
It prepares an input file for Pars program (part of PHYLIP package).
It first creates a list with all the places of variation,
then supplies missing shelfmarks to lemma, and assigns numeric values to each witness. 
At the end it sorts the witnesses alphabetically, still in lists by single <app>,
transposes the list, and creates an output file, which serves as input for Pars
'''

file = 'testEd_withLem.xml'

def prepareParsInput_withLem(file):
    print("The process has started - wait and be patient")
    tree = etree.parse(file)
    ns = {'tei' : 'http://www.tei-c.org/ns/1.0'}
    root = tree.getroot()
    body = root[1][0] # This assumes that first you have <teiHeader> with all the metadata, and your transcription is in <body>

    #Create a list with all places of variation
    myList = []
    for app in body.iter('{http://www.tei-c.org/ns/1.0}app'):
        shelfmarks = []
        lem = app.find('{http://www.tei-c.org/ns/1.0}lem')
        shelfmarks += [lem.attrib]
        for rdg in app.iter('{http://www.tei-c.org/ns/1.0}rdg'):
            rdgAttrib = rdg.attrib
            rdgText = rdg.text
            shelfmarks += [rdgAttrib]
        myList += [shelfmarks]

    # Now we look at individual apparatus elements and assign numberic values to variants.
    result = []
    for placeOfvariation in myList:
        singleAppRes = []
        nrOfReadings = int(len(placeOfvariation))
        number = 0
        for variant in placeOfvariation:
            nrOfwitneses = len(variant['wit'].split(' '))
            witness = variant['wit'].split(' ')
            for index, siglum in enumerate(witness):
                singleAppRes += [siglum + "-" + str(number)]
            number+=1
        result += [singleAppRes]

    numberOfWitnesses = len(result[0])

    # Sort the results alphabetically by sigla
    sortedResults = []
    for eachList in result:
        sortedResults += [sorted(eachList)]
 
    if len(sortedResults) != len(myList):
        print("Error, something went wrong you don;t have enough lists within results")
    else:
        print("Great, len(sortedResults) equals len(myList). It means you have", len(sortedResults), "places of variation")
    

    # Convert your results into a numpy array, so you can modify it.
    resultsArray = np.array(sortedResults)
    resultsArray = np.transpose(resultsArray)
    
    # Start to prepare output file
    newResults = []
    for i in range(len(resultsArray[:,0])):
        #print(A[i,0])
        k = re.sub('(-.*)',"", resultsArray[i,0]).replace('#', '')
        for m in range(10-len(k)):
            k = k + ' '
        for j in range(len(resultsArray[0,:])):
             l = re.sub('^(.*-)',"", resultsArray[i,j])
             k = k + l
        newResults.append(k)

    numberOfVariants = str(len(sortedResults))
    
    parsInputFile = "   " + str(numberOfWitnesses) + "  " + numberOfVariants + "\n"
    for i in newResults:
        parsInputFile = parsInputFile + i + "\n"
    # Save the putput file
    f = open("parsInput_withLem.txt", "w")
    f.write(parsInputFile)
    f.close()
    print("The process is done, look for parsInput.txt file in the same folder where you have your input file")
    
prepareParsInput_withLem(file)
