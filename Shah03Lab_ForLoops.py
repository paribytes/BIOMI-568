#-------------------------------------------------------------------------------
#PYTHON LAB 3
#-------------------------------------------------------------------------------
import random

outfile=open('Shah03Lab.txt','w')

print("\n########## PART 1 ##########\n")
out=str("\n########## PART 1 ##########\n") # You can only write strings to a file!
outfile.write(out)

#PART 1 - STRING LOOPING & COUNTING

#(1) Use a "for" loop to iterate through the DNA sequence.
#(2) Count the number of G's and C's in the DNA sequence.
#(3) Print the number of G's and C's in the DNA sequence.

#DATASET FOR PART 1: try each of these options
test_dna1="GACCTTTAC"
test_dna2="GATCCTGGCTCAGGACGAACGCTGGCGGCGTGCTTAACACATGCAAGTCGAGCGGTAAGGCCCTTCGGGGTACACGAGCGGCGAACGGGTGAGTAACACGTGGGTGATCTGGGGCCCCATCTA"

#== PART 1 ==
gc_count1=0
for base in test_dna1:
    if base == "G" or base == "C":
        gc_count1+=1

print(gc_count1)
out=str(gc_count1) + "\n" # You can only write strings to a file!
outfile.write(out)

gc_count2=0
for base in test_dna2:
    if base == "G" or base == "C":
        gc_count2+=1
        
print(gc_count2)
out=str(gc_count2) + "\n" # You can only write strings to a file!
outfile.write(out)

#-------------------------------------------------------------------------------
print("\n########## PART 2 ##########\n")
out=str("\n########## PART 2 ##########\n") # You can only write strings to a file!
outfile.write(out)


#PART 2 - CLEAN the Sequence first then calculate the percentage of G and Cs 

nasty_dna="\n AgGctgTtgC \t\n"

# (1) Clean the DNA sequence.
# (2) Use a "for" loop to iterate through the DNA sequence.
# (3) Count the number of G's and C's in the DNA sequence.
# (4) Calculate the proportion of G and C nucleotides in the DNA sequence.
#       For example this proportion in DNA sequence "GACT" is 0.5. 
# (5) Print the percentage of G and C in the DNA sequence.

#To get percentage divide the count of G and C by the total length of the DNA
#Then multiply by 100. 0.5 becomes 50.0
#For example: len(clean_dna)


#== PART 2 ==
#cleaning the DNA sequence
nasty_dna = nasty_dna.upper()
clean_dna = nasty_dna.strip()
print(clean_dna)
out=str(clean_dna) + "\n" # You can only write strings to a file!
outfile.write(out)


#iterating
for base in clean_dna:
    print(base)
    out=str(base) + "\n" # You can only write strings to a file!
    outfile.write(out)

#counting the number of G and C's 
count=0
for base in clean_dna:
    if base == "G" or base == "C":
        count+=1
print(count)
out=str(count) + "\n" # You can only write strings to a file!
outfile.write(out)

#proportion of G and C content in the DNA sequence
length_dna= print(str(len(clean_dna)))
out=str(len(clean_dna)) + "\n" # You can only write strings to a file!
outfile.write(out)

gc_proportion = print(str(count/len(clean_dna)))
out=str(count/len(clean_dna)) + "\n" # You can only write strings to a file!
outfile.write(out)

#percentage of G and c in the DNA sequence
gc_percentage = print(str(count/len(clean_dna)*100))
out=str(count/len(clean_dna)*100)+ "\n" # You can only write strings to a file!
outfile.write(out)

#-------------------------------------------------------------------------------
print("\n########## PART 3 ##########\n")
out=str("\n########## PART 3 ##########\n") # You can only write strings to a file!
outfile.write(out)


#PART 3 - CHARACTER CLASSIFICATION

dna="AAGGTTCCCCG"*10

# (1) Count the number of each type of base in the DNA sequence.
# (2) Return the counts of each type of base in the DNA sequence.
# (3) Also print out a table of the counts as shown below.

#== PART 3 ==
a_count = 0
t_count= 0
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
print(a_count)
out=str(a_count) + "\n" # You can only write strings to a file!
outfile.write(out)
    
print(t_count)
out=str(t_count) + "\n" # You can only write strings to a file!
outfile.write(out)

print(g_count)
out=str(g_count) + "\n" # You can only write strings to a file!
outfile.write(out)
  
print(c_count)
out=str(c_count) + "\n" # You can only write strings to a file!
outfile.write(out)   

print("\tA\t", a_count)

out="\tA\t"+ str(a_count) + "\n" # You can only write strings to a file!
outfile.write(out)

print("\tT\t", t_count)

out="\tT\t"+ str(t_count) + "\n" # You can only write strings to a file!
outfile.write(out)

print("\tG\t", g_count)

out="\tG\t"+ str(g_count) + "\n" # You can only write strings to a file!
outfile.write(out)

print("\tC\t", c_count)

out="\tC\t"+ str(c_count) + "\n" # You can only write strings to a file!
outfile.write(out)


#The table should look like this:
#   A   9
#   T	10
#   G	12
#   C	7

#-------------------------------------------------------------------------------
print("\n########## PART 4 ##########\n")
out=str("\n########## PART 4 ##########\n") # You can only write strings to a file!
outfile.write(out)


#PART 4 - Using range and random

#Use the random.shuffle function to make and print 10 random lists of names.

names=['Tara','Merkel','Bob','Dwight','Chrysanthemum','Tiny Tim','Boba Fett','Lando','Sgt. Rock','Beyonce']
print(names) #prints the unshuffled names
out=str(names)  + "\n" # You can only write strings to a file!
outfile.write(out)

#== PART 4 ==
for name in range(10):
    random.shuffle(names)
    print(names)
    out=str(names) + "\n"
    outfile.write(out)
#-------------------------------------------------------------------------------
print("\n########## PART 5 ##########\n")
out=str("\n########## PART 5 ##########\n") # You can only write strings to a file!
outfile.write(out)


#PART 5 - Write everthing to a file!!

"""
For this last part, write all your results (PARTS 1 to 4) to a file called: YourName03Lab.txt
YourName should be changed to your name of course.

How to do this? It's easy!

(1) Put this code at the top of the file:
outfile=open('YourName03Lab.txt','w')

(2) After each print statement, add a line to write data to a file, for example:

print(names)
out=str(names) # You can only write strings to a file!
outfile.write(out)

(3) At the end of this file put this code:

outfile.close()

----------------------------------------------------------------------------------------------------------------------------------------
NOTE: For this assignment, you will be submitting your finished YourName03Lab.py file AND the YourName03Lab.txt file you just generated.
----------------------------------------------------------------------------------------------------------------------------------------

"""
outfile.close()
