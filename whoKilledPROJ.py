"""
Mini project: who killed mr boddy
due 10/23/23
alena hemminger
"""
# hard-code all people's DNA sequences
scarlet = 'CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATTCAGGAAGCGGCAGGAATAAGGAAAAGCAGC'
peacock = 'AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCC'
white = 'ATATCCCGTACGTTAGAAGCATAATAGATATAGGGGETATAGAGGATACATCGATCGATTTATTTTTACCCCGAT'
plum = 'CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG'
mustard = 'CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG'
green = 'TTTGATCTCTAGCTAGCTCGCGCTCATAGCTCGCTATATAGCGCGCTAGCTGACTATCGATCGATCGATCGCTA'

# samples from weapon looking for in each person
sample1 = 'CATA'
sample2 = 'ATGC'

# create lists of both DNAs and names in order to use for loop
# create counter and signal to stop for loop and find suspect
dnas = [scarlet, peacock, white, plum, mustard, green]
names = ['Scarlet', 'Peacock', 'White', 'Plum', 'Mustard', 'Green']
count = 0
stopCounter = 0

for suspectDNA in dnas:
    if sample1 in suspectDNA and sample2 in suspectDNA:
        print('match')
        stopCounter = 1
    else:
        print('mismatch')
        # stopCounter is signal to stop counting so that count 
        # can find suspect's name in names list
        if stopCounter == 0:
            count += 1
        else: 
            print(names[count], 'is guilty')
            
# extension 2: print indices of string containing DNA match
guiltyName = names[count]
guiltyDNA = dnas[count]
indice1 = guiltyDNA.find(sample1)
indice2 = guiltyDNA.find(sample2)

print("DNA sample matches are found at letters", indice1,"-", indice1+3, "and", 
      indice2, "-", indice2+3, "in", guiltyName, "'s DNA string:", guiltyDNA)

    
