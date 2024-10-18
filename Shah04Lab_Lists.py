
#----------------------------------------------------------------------------
#PYTHON LAB 4: LISTS
#----------------------------------------------------------------------------

outfile=open('Shah_gc_output.txt','w')


print("\n########## PART 1 ##########\n")

#PART 1 - Append substrings to a list

#(1) Use a or loop to iterate through a sequence.
#(2) Divide the sequence into sections of 3 DNA bases with NO OVERLAP.
#(3) Append the 3-base codons to a list.
#[NOTE: If a group is not 3 bases long, do not include it in the list.]
#(4) Print the final list. 

#== PART 1 ==

seq1="AUGGGAAGC"   #This should print  ["AUG","GGA","AGC"]
seq2="AUGGGAAGCGCGG"  #This should print  ["AUG","GGA","AGC","GCG"]

#Here is a little snippet of code that should help.
#It uses a for loop to 'break up' a string into groups of 3 characters
# like with codons. Question - how do you then append then to a list?
print("-----------------FOR seq1-----------------")
base_list1=[]

for base1 in seq1:
    print(base1)

for i in range(0,len(seq1),3):
    codon1=seq1[i:i+3]
    base_list1.append(codon1)
    if len(codon1)==3:
        print(base_list1)

print("-----------------FOR seq2-----------------")
base_list2=[]

for base2 in seq2:
    print(base2)

for i in range(0,len(seq2),3):
    codon2=seq2[i:i+3]
    base_list2.append(codon2)
    if len(codon2)==3:
        print(base_list2)

#-------------------------------------------------------------------------------
print("\n########## PART 2 ##########\n")

#PART 2 - Change the length of the substrings

# Exactly the same as part 1 EXCEPT instead of 3-characters
#    it can be of length x, where x is an integer.
# For example if x=4, then if seq='AAAAGGGGCCCC' the loop would print
# ['AAAA','GGGG','CCCC']
# Feel free to copy paste and modify the loop from part 1

#== PART 2 ==

#Try it out with two different values of x and two different sequences
x=4 

seq4="AAAAGGGGCCCC"
seq5="AUGUAUGUCUGUCUGAUC"

print("-----------------FOR seq4-----------------")

base_list4=[]

for i in range(0,len(seq4),4):
    codon4=seq4[i:i+4]
    base_list4.append(codon4)
    if len(codon4)==4:
        print(base_list4)

print("-----------------FOR seq5-----------------")
#x=5
base_list5=[]

for i in range(0,len(seq5),5):
    codon5=seq5[i:i+5]
    base_list5.append(codon5)
    if len(codon5)==5:
        print(base_list5)


#------------------------------------------------------------------------------
print("\n########## PART 3 ##########\n")

#PART 3 -  Iterate through a list of strings, calculate value, write to file


#(1) Iterate through the list of sequences
#(2) Count G's and C's for each sequence nmer in a list.
#(3) Calculate the GC Percentage for the sequence nmer.
#(4) Write the sequence and its GC percentage (separated by a "Tab")
#    to a file named:
#       gc_output.txt

###A counting shortcut for string data:
'''
seq6="AGGT"
g_count=seq6.count("G")
print(g_count)
'''

#For example if given the following sequence list
#seq_list=["AAUG","AGCG","GCUA"]

#The loop would write the following to the file gc_output.txt
#AAUG    25.0
#AGCG    75.0
#GCUA    50.0

#== PART 3 ==

print("-----------------FOR seq_list6-----------------")
out=str("-----------------FOR seq_list6-----------------")
outfile.write(out)

seq_list6=["AAUG","AGCG","GCUA"]

for codon6 in seq_list6:
    print(codon6)

gc_count60=0

for base in seq_list6[0]:
    if base=="G" or base=="C":
        gc_count60+=1
    else:
        pass
print("GC count for AAUG is:",gc_count60)

gc_count61=0

for base in seq_list6[1]:
    if base=="G" or base=="C":
        gc_count61+=1
    else:
        pass
print("GC count for AGCG is:", gc_count61)

gc_count62=0
        
for base in seq_list6[2]:
    if base=="G" or base=="C":
        gc_count62+=1
    else:
        pass
print("GC count for GCUA is:", gc_count62)

gc_perc60= str(gc_count60/len(seq_list6[0])*100)
print(gc_perc60)

gc_perc61= str(gc_count61/len(seq_list6[1])*100)
print(gc_perc61)

gc_perc62= str(gc_count62/len(seq_list6[2])*100)
print(gc_perc62)

print("AAUG\t", gc_perc60)

out="\nAAUG\t"+ str(gc_perc60) + "\n"
outfile.write(out)

print("AGCG\t", gc_perc61)

out="AGCG\t"+ str(gc_perc61) + "\n"
outfile.write(out)

print("GCUA\t", gc_perc62)

out="GCUA\t"+ str(gc_perc62) + "\n"
outfile.write(out)



print("-----------------FOR seq_list7-----------------")
out=str("-----------------FOR seq_list7-----------------")
outfile.write(out)


seq_list7=["AAUGGAGACU","AGCGCCCC","GCUAAAAAAU"]

for codon7 in seq_list7:
    print(codon7)

gc_count70=0

for base in seq_list7[0]:
    if base=="G" or base=="C":
        gc_count70+=1
    else:
        pass
print("GC count for AAUGGAGACU is:",gc_count70)
    
gc_count71=0

for base in seq_list7[1]:
    if base=="G" or base=="C":
        gc_count71+=1
    else:
        pass
print("GC count for AGCGCCCC is:",gc_count71)

gc_count72=0

for base in seq_list7[2]:
    if base=="G" or base=="C":
        gc_count72+=1
    else:
        pass
print("GC count for GCUAAAAAA is:",gc_count72)


gc_perc70= str(gc_count70/len(seq_list7[0])*100)
print(gc_perc70)

gc_perc71= str(gc_count71/len(seq_list7[1])*100)
print(gc_perc71)

gc_perc72= str(gc_count72/len(seq_list7[2])*100)
print(gc_perc72)


print("AAUGGAGACU\t", gc_perc70)

out="\nAAUGGAGACU\t"+ str(gc_perc70) + "\n"
outfile.write(out)

print("AGCGCCCC\t", gc_perc71)

out="AGCGCCCC\t"+ str(gc_perc71) + "\n"
outfile.write(out)

print("GCUAAAAAA\t", gc_perc72)

out="GCUAAAAAA\t"+ str(gc_perc72) + "\n"
outfile.write(out)


outfile.close()

