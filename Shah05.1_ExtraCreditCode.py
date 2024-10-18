##PART 1: Convert the code below into a function
import re
##Purpose: To find all the sequences in a list that have a given motif
##Name: motif_finder
##Parameters: 2 (a string and a list)
##Return Value: A list 

##ORIGINAL CODE

motif="KW"
prot_list=["KWER","GKW","RRRRK","RRRKWRR"]


kw_list=[]
for p in prot_list:
    if re.search(motif, p):
        kw_list.append(p)
    else:
        pass
print(kw_list)



##Use this name to convert the code above (do not change it the name of the function)

def motif_finder(motifs,protein):
    kw_list=[]
    for p in prots:
        if re.search(mo, p):
            kw_list.append(p)
        else:
            pass
    return(kw_list)

##TEST THE FUNCTION WITH THE FOLLOWING CODE

mo="QW"
prots=["QWER","GKQW","RRRRK","RRRKQWRR","RRGK"]

matches=motif_finder(mo, prots)
print(matches) #should print ["QWER","GKQW","RRRKQWRR"]


#PART 2: Make a function that cleans the sequences
##Name: clean_seq
##Parameters: 1 (a list of strings)
##Return Value: a list of cleaned strings

crapola=["\t YWVV QwSLMLpii\n","\t  GKqW\n","\t rrrrRK\n ","RRR  KqwllRR"]


def clean_seq_list(sequence):
    cleanseq= [x.upper().strip().replace(" ","") for x in sequence]
    return(cleanseq)


##TEST THE FUNCTION WITH THE FOLLOWING CODE

crapola=["\t YWVV QwSLMLpii\n","\t  GKqW\n","\t rrrrRK\n ","RRR  KqwllRR"]
output=clean_seq_list(crapola)
print(output) #should print ['YWVVQWSLMLPII', 'GKQW', 'RRRRRK', 'RRRKQWLLRR']


#PART 3: Improve motif_finder by using clean_seq_list WITHIN the function
#to clean the sequences before searching for motifs. Call it motif_finder_improved
##Name: motif_finder_improved
##Parameters: 2 (a string and a list)
##Return Value: A list 

def clean_seq_list(sequence):
    cleanseq= [x.upper().strip().replace(" ","") for x in sequence]
    return(cleanseq)

def motif_finder_improved(motifseq, cleanseq):
    kw_list1=[]
    for p in clean_seq_list(crapola2):
        if re.search(motif2, p):
            kw_list1.append(p)
        else:
            pass
    return(kw_list1)

##TEST THE FUNCTION WITH THE FOLLOWING CODE

motif2="PLR"
crapola2=["\t YWVV QwSLMLplri\n","\t  GKqW\n","\t rrrplrRK\n ","RRR  KqwllRR"]

matches2=motif_finder_improved(motif2, crapola2)
print(matches2) #should print ['YWVVQWSLMLPLRI', 'RRRPLRRK']

