import sys
import re
total = len(sys.argv)
cmdargs = str(sys.argv)
second = str(sys.argv[1])
fa = open(str(second),'r')
file = fa.read()
file = file.upper()
#print file
file = file.replace('\n','')
file = file.replace('NULL','')

DNA_AA = {'TTT': 'F', 'TTC' : 'F', 'TTA': 'L', 'TTG' : 'L', 'TCT' : 'S','TCC':'S', 'TCA' : 'S', 'TCG' : 'S', 'TAT' : 'Y' , 'TAC' : 'Y', 'TGT' : 'C', 'TGC' : 'C', 'TGA' : '', 'TGG' : 'W', 'CTT' : 'L', 'CTC':'L', 'CTA' : 'L','CTG' : 'L',  'CCT' : 'P', 'CCC' : 'P',  'CCA' : 'P', 'CCG' : 'P',  'CAT' : 'H', 'CAC' : 'H', 'CAA' : 'Q', 'CAG' : 'Q', 'CGT' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R',  'ATT' : 'I',  'ATC' : 'I',  'ATA' : 'I',  'ATG' : 'M',  'ACT' : 'T',  'ACC' : 'T',  'ACA' : 'T',   'ACG' : 'T', 'AAT': 'N', 'AAC': 'N',  'AAA': 'K', 'AAG': 'K',  'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT' : 'V', 'GTC' : 'V',  'GTA' : 'V',  'GTG' : 'V',  'GCT' : 'A',   'GCC' : 'A',   'GCA' : 'A',   'GCG' : 'A',  'GAT' : 'D', 'GCC' : 'D',  'GAA' : 'E',  'GAG' : 'E', 'GAC' : 'D',  'GGT' : 'G',  'GGC' : 'G', 'GGA' : 'G',   'GGG' : 'G' , 'TAA' : '', 'TAG' : '', 'XXX' : 'X' }  


#print DNA_AA[str(second)]

def Get_AA(a):
	return DNA_AA[str(a)]

filetest = "ATGTCCGTTAAAGAGATCAAGGGC"

def Convert_to_AA(s):
	i = 0
	l = len(s)
	alist = []
	while (i+3) <= l:
		codon = s[i:i+3]
		if codon[0] == "N" or codon[1] == "N" or codon[2] == "N":
			codon = 'XXX' 
		alist.append(Get_AA(codon))
		i += 3
	result = "".join(alist)
	return result
#print Convert_to_AA(filetest)
#Get_AA(str(sys.argv[1]))

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def GetORF1AA(s):
	start = s.find('READING FRAME ONE') + 18
	end = s.find('READING FRAME TWO')
	s1 = s[start:end]
	commacount = s1.count(',')
	i = 1
	laa = []
	while i <  commacount:
		strt = find_nth(s1,",",i)+1
        	ed = find_nth(s1,",",i+1)
		#print strt
		#print ed
		#b = s1[strt:ed]
		#print Convert_to_AA(b)
		laa.append(Convert_to_AA(s1[strt:ed]))
		i += 1	
	return laa

def GetORF2AA(s):
        start = s.find('READING FRAME TWO') + 18
        end = s.find('READING FRAME THREE')
        print end
	s1 = s[start:end]
        commacount = s1.count(',')
        i = 1
        laa = []
        while i <  commacount:
                strt = find_nth(s1,",",i)+1
                ed = find_nth(s1,",",i+1)
                #print strt
                #print ed
                #b = s1[strt:ed]
                #print Convert_to_AA(b)
                laa.append(Convert_to_AA(s1[strt:ed]))
                i += 1
        return laa
def GetORF3AA(s):
        start = s.find('READING FRAME THREE') + 18
        end = s.find('READING FRAME FOUR')
        s1 = s[start:end]
        commacount = s1.count(',')
        i = 1
        laa = []
        while i <  commacount:
                strt = find_nth(s1,",",i)+1
                ed = find_nth(s1,",",i+1)
                #print strt
                #print ed
                #b = s1[strt:ed]
                #print Convert_to_AA(b)
                laa.append(Convert_to_AA(s1[strt:ed]))
                i += 1
        return laa
def GetORF4AA(s):
        start = s.find('READING FRAME FOUR') + 18
        end = s.find('READING FRAME FIVE')
        s1 = s[start:end]
        commacount = s1.count(',')
        i = 1
        laa = []
        while i <  commacount:
                strt = find_nth(s1,",",i)+1
                ed = find_nth(s1,",",i+1)
                #print strt
                #print ed
                #b = s1[strt:ed]
                #print Convert_to_AA(b)
                laa.append(Convert_to_AA(s1[strt:ed]))
                i += 1
        return laa
def GetORF5AA(s):
        start = s.find('READING FRAME FIVE') + 18
        end = s.find('READING FRAME SIX')
        s1 = s[start:end]
        commacount = s1.count(',')
        i = 1
        laa = []
        while i <  commacount:
                strt = find_nth(s1,",",i)+1
                ed = find_nth(s1,",",i+1)
                #print strt
                #print ed
                #b = s1[strt:ed]
                #print Convert_to_AA(b)
                laa.append(Convert_to_AA(s1[strt:ed]))
                i += 1
        return laa
def GetORF6AA(s):
        start = s.find('READING FRAME SIX') + 18
        end = len(s)
        s1 = s[start:end]
        commacount = s1.count(',')
        i = 1
        laa = []
        while i <  commacount:
                strt = find_nth(s1,",",i)+1
                ed = find_nth(s1,",",i+1)
                #print strt
                #print ed
                #b = s1[strt:ed]
                #print Convert_to_AA(b)
                laa.append(Convert_to_AA(s1[strt:ed]))
                i += 1
        return laa
GetORF1aa =  GetORF1AA(file)
GetORF2aa =  GetORF2AA(file)
GetORF3aa =  GetORF3AA(file)
GetORF4aa =  GetORF4AA(file)
GetORF5aa =  GetORF5AA(file)
GetORF6aa =  GetORF6AA(file)
fow = open("ORFAA.txt",'w')
#fow.write(GetORF1aa)
#fow.write(GetORF2aa)
#fow.write(GetORF2aa)
GetORF1aa = "\n".join(GetORF1aa)
GetORF2aa = "\n".join(GetORF2aa)
GetORF3aa = "\n".join(GetORF3aa)
GetORF4aa = "\n".join(GetORF4aa)
GetORF5aa = "\n".join(GetORF5aa)
GetORF6aa = "\n".join(GetORF6aa)

fow.write("Open Reading Frame 1"+'\n'+GetORF1aa+'\n'+"Open Reading Frame 2"+'\n'+GetORF2aa+'\n'+"Open Reading Frame 3"+'\n'+GetORF3aa+'\n'+'Open Reading Frame 4'+'\n'+GetORF4aa+'\n'+'Open Reading Frame 5'+'\n'+GetORF5aa+'\n'+'Open Reading Frame 6'+'\n'+GetORF6aa)

