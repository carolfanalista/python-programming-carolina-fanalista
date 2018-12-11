# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght 
# Use separate functions for the input and the output 


'''
Pseudo-code:open the file
            read just one line at a time
            if the word "Homo sapiens" is in the header-> copy all the records till next header
            print the length and the organism
             
'''



open_file=open("sprot_prot.fasta")
for line in open_file:
    i=0
    open_file.readline()   
           if line[0]==">"
               if"homo sapiens" not in line[0]:
                   print(line[i])
                   i++
                   



