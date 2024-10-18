#Lab 5: Advanced Functions (Convert scripts to functions.)

"""
In this assignment, you will go back to your working code from 
previous assignments and convert your scripts to functions.

To begin, you can literally copy and paste the old code to this 
file then turn it into a working function. 

Test the functions with the values indicated and make sure
you get the results you expect to get.
"""

print("\n########## PART 1 ##########\n")

#PART 1 - Convert 03Lab part 2 to a function

#FUNCTION NAME: fractionGC
#PARAMETERS: 1 (A DNA sequence)
#PURPOSE: The function should:
#           (1) Clean the DNA sequence.
#	    (2) Use a "for" loop to iterate through the DNA sequence.
#	    (3) Count the number of G's and C's in the DNA sequence.
#           (4) Calculate the fraction (NOT PERCENT) of G's and C's in the DNA sequence. 
#	    (5) Return the fraction of G's and C's in the DNA sequence.
#RETURN VALUES: The fraction of G's and C's in the DNA sequence. (A float)

#== FUNCTION 1 ==

def fractionGC(dna):
    dna = dna.upper().strip()
    print(dna)
    for base in dna:
        print(base)
    count=0
    for base in dna:
        if base == "G" or base == "C":
            count+=1
    print("Count of no. of G's and C's:", count)
    gc_content= "GC content is", str(count/len(dna))
    return gc_content
    
gc_content = fractionGC("\n AgGctgTtgC \t\n")
print(gc_content)

#EXAMPLE: 
#gc_content = fractionGC("\n AgGctgTtgC \t\n")
#print (gc_content)

#The function would return:
#   0.6

test_seq1="GACCTTTAC"
gc_content = fractionGC(test_seq1)
print(gc_content)


test_seq2="GATCCTGGCTCAGGACGAACGCTGGCGGCGTGCTTAACACATGCAAGTCGAGCGGTAAGGCCCTTCGGGGTACACGAGCGGCGAACGGGTGAGTAACACGTGGGTGATCTGGGGCCCCATCTA"
gc_content = fractionGC(test_seq2)
print(gc_content)

#Test the function with the sequence from EXAMPLE and verify your result.
#Test the function again with "test_seq1" and test_seq2".
#Return the "GC" content of "test_seq1" to "gc_content". 
#Test it again with "test_seq2".


print("\n########## PART 2 ##########\n")

#PART 2 - Convert 03Lab part 3 to a function

#FUNCTION NAME: count_DNA_bases
#PARAMETERS: 1 (A DNA sequence)
#PURPOSE: The function should:
#           (1) Count the number of each type of base in the DNA sequence.
#           (2) Return the counts of each type of base in the DNA sequence.
#           (3) Also print out a table as shown below.
#RETURN VALUES: The counts of each type of base in the DNA sequence. (A tuple)
#                   [NOTE: Return the counts EXACTLY in this order: A's, T's, G's and C's.]
# Example tuples: my_tuple1=(x,y,z)  my_tuple2=(1,2,3,4)


#== FUNCTION 2 ==

def count_DNA_bases(dna):
    a_count = 0
    t_count = 0
    g_count = 0
    c_count = 0
    for base in dna:
        if base == "A":
            a_count+=1
        elif base == "T":
            t_count+=1
        elif base == "G":
            g_count+=1
        elif base == "C":
            c_count+=1
    return(a_count,t_count,g_count,c_count)
    

#TEST DATA FOR PART 2:
test_dna1="AAGCTACGTGGGTGACTTTGCCGATTTAAGCCTGGGAA"

DNAcounts=count_DNA_bases(test_dna1)
print (DNAcounts)
print("\n\tA\t",DNAcounts[0])
print("\tT\t",DNAcounts[1])
print("\tG\t",DNAcounts[2])
print("\tC\t",DNAcounts[3])

#EXAMPLE:
#DNAcounts=count_DNA_bases(test_dna1)
#print (DNAcounts)

#The function would print a table:
#   A   9
#   T	10
#   G	12
#   C	7

#The function would return:
#   (9, 10, 12, 7)


print("\n########## PART 3 ##########\n")

#PART 3 - Convert 03Lab part 4 to a function

#Use the random.shuffle function to make and print 10 random lists of names.

names=['Tara','Merkel','Bob','Dwight','Chrysanthemum','Tiny Tim','Boba Fett','Lando','Sgt. Rock','Beyonce']
#print(names) #prints the unshuffled names

#== FUNCTION 3 ==

import random

def rand_list(people):
    for name in range(10):
        random.shuffle(names)
        print(names)

names=['Tara','Merkel','Bob','Dwight','Chrysanthemum','Tiny Tim','Boba Fett','Lando','Sgt. Rock','Beyonce']
rand_list(names)


print("\n########## PART 4 ##########\n")

#PART 4 -  Convert 04Lab part 2 to a function

#FUNCTION NAME: codon_list
#PARAMETERS: 1 (A sequence)
#PURPOSE: The function should:
#   (1) Iterate through the sequence.
#   (2) Divide the sequence into sections of 3-base codons with NO OVERLAPPING.
#   (3) Add the codons to a list.
#   [NOTE: If a group is not 3 bases long, do not include it in the list.]
#   (4) Return the list.
#RETURN VALUES: A list of codons. (A list)

#== FUNCTION 4 ==

def codon_list(seq):
    base_list = []
    for base in dna1:
        print(base)
    for i in range(0,len(dna1),3):
        codon1=dna1[i:i+3]
        base_list.append(codon1)
    if len(codon1)==3:
        print(base_list)


dna1="AUGGGAAGC"
codon_list(dna1)


#EXAMPLE:
#dna1="AUGGGAAGC"
#codons=codon_list(dna1)
#print (codons)

#The function would return:
#   ["AUG","GGA","AGC"]


