#FINAL PROJECT - Priyanshi Shah

##SPECIAL NOTES: DO NOT INCLUDE ANY FUNCTION CALLS IN YOUR FINAL CODE
## ALSO, USE THE FUNCTION NAMES EXACTLY AS I HAVE WRITTEN THEM
##  AND DO NOT CHANGE THE NUMBER OR TYPES OF PARAMETERS

# NOTE: Function 1 and 3 do not return values. Instead, they write files.
#       For Function 1 and 3 you can return 1 if you like but not necessary.
#       
#       Function 2 DOES return a value though (see below).

#Global Variables used in functions 1 and 2 below:
standard_code = {
     "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
     "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
     "UAA": "*", "UAG": "*", "UGA": "*", "UGU": "C", "UGC": "C",
     "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
     "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
     "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
     "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I",
     "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
     "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
     "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
     "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
     "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
     "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

#Function 1: Reads in a DNA sequence fasta file,
#            and outputs a Fasta file of protein translations.
#            This function uses the global variable standard_code above.
#            The output fasta will have the same titles as the input file.


def dna_2_prot(f1, f2="translated_fasta.txt"):
    """f1=input file name, f2=output file name"""

    inputfile=open(f1,'r')
    outputfile=open(f2,'w')
    name, seq = None, []
    for line in inputfile:
        if line[0]==">":
            if name:
                seq = ''.join(seq)
            name, seq = line.strip(), []
        else:
            seq.append(line.strip())

        if len(seq) > 0:
            print(name, seq)
            seq = seq[0]
            seq=seq.upper().strip()
            rna= str(seq)
            rna=rna.replace("T","U")

            codon_list2 = []
            codon2 = ""
            for i in range(0,len(rna),3):
                codon2=rna[i:i+3]
                if len(codon2)== 3:
                    codon_list2.append(codon2)
            codon3 = ""
            for j in codon_list2:
                codon3 = codon3 + standard_code[j]
                if standard_code[j]== '*':
                    break
            print(codon3)
            print(" ")
            outputfile.write(codon3 + "\n")
    if name:
        seq = ''.join(seq)
    return  1 

#Example function call:

#dna_2_prot("testDNA.txt")


#Function 2: One hot encoding function. This function turns a DNA sequence in to
#            0s and 1s for computer analysis. This is useful for machine learning.
#            The function takes a DNA sequence as a parameter and returns a 2D list
#            (a list within a list) of the DNA in bits.

#For example if seq1 is:
seq1="AGCT"
#The one hot encoding of seq1 will be:
one_hot_for_seq1=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
#Each element of the list is a list of one_hot_encoding for each base of the sequence
# The order within each of the lists is A,G,T,C
#if the base is an A, the list will be [1,0,0,0]
#if the base is a G, the list will be  [0,1,0,0]..etc.
#Here another example:
seq2="AATTT"
one_hot_for_seq2=[[1,0,0,0],[1,0,0,0],[0,0,0,1],[0,0,0,1],[0,0,0,1]]


def hot_code_DNA(seq):
    """Input is a DNA sequence of any length"""
    arr_a = [1,0,0,0]
    arr_g = [0,1,0,0]
    arr_c = [0,0,1,0]
    arr_t = [0,0,0,1]
    result_arr = []
    for character in seq:
        if character[0] == "A":
            result_arr.append(arr_a)
        elif character[0] == "G":
            result_arr.append(arr_g)
        elif character[0] == "C":
            result_arr.append(arr_c)
        elif character[0] == "T":
            result_arr.append(arr_t)
    #print(result_arr)
    return(result_arr)

#Test function call:
output=hot_code_DNA(seq1)
print(output)
##Should print: [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

#output=hot_code_DNA(seq2)
#print(output)
##Should print: [[1,0,0,0],[1,0,0,0],[0,0,0,1],[0,0,0,1],[0,0,0,1]]


#Function 3: Reads in a fasta file and searches for a given motif. Outputs a
#    file of the number of times that the motif was found in each sequence. The
#    output file will be tab-delimited.

#Here is a little code snippet that might be useful. 

"""
import re
Seq1="MNGMNNMNRVFRLVQRM"
y=re.findall("V[A-Z]R[ML]",Seq1)
print(y)
['VFRL', 'VQRM']
"""
#And the output should look like this
"""
SeqName     Motif       Hits            
Seq1        MN[A-Z]        2
Seq2        MN[A-Z]        0
Seq3        MN[A-Z]        1
""" 

def motif_finder(f1, motif, f2="motifs.txt"):
    """f1=input file name, motif=the motif pattern, f2=output file name"""
    inputfile=open(f1,'r')
    outputfile=open(f2,'w')
    name, seq = None, []
    outputfile.write("SeqName" + "\t\t" + "Motif" + "\t\t" + "Hits \n")
    for line in inputfile:
        if line[0]==">":
            if name:
                seq = ''.join(seq)
            name, seq = line.strip(), []
        else:
            seq.append(line.strip())

        if len(seq) > 0:
            print(name, seq)
            seq = seq[0]
            codon4 = ""

            import re
            y=re.findall(motif,seq)
            print(y)
            outputfile.write(name[1:] + "\t\t" + motif + "\t" + str(len(y)) + "\n")
    if name:
        seq = ''.join(seq)
    return 1

#Example function call:

#motif_finder("testProtein-2.txt","MN[A-Z]")


