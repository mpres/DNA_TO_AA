import sys

DNA_AA = {'TTT': 'F', 'TTC' : 'F', 'TTA': 'L', 'TTG' : 'L', 'TCT' : 'S','TCC':'S', 'TCA' : 'S', 'TCG' : 'S', 'TAT' : 'Y' , 'TAC' : 'Y', 'TGT' : 'C', 'TGC' : 'C', 'TGA' : 'W', 'TGG' : 'W', 'CTT' : 'L', 'CTC':'L', 'CTA' : 'L','CTG' : 'L',  'CCT' : 'P', 'CCC' : 'P',  'CCA' : 'P', 'CCG' : 'P',  'CAT' : 'H', 'CAC' : 'H', 'CAA' : 'Q', 'CAG' : 'Q', 'CGT' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R',  'ATT' : 'I',  'ATC' : 'I',  'AUA' : 'I',  'ATG' : 'M',  'ACT' : 'T',  'ACC' : 'T',  'ACA' : 'T',   'ACG' : 'T', 'AAT': 'N', 'AAC': 'N',  'AAA': 'K', 'AAG': 'K',  'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT' : 'V', 'GTC' : 'V',  'GTA' : 'V',  'GTG' : 'V',  'GTU' : 'A',   'GCC' : 'A',   'GCA' : 'A',   'GCG' : 'A',  'GAT' : 'D', 'GCC' : 'D',  'GAA' : 'E',  'GAG' : 'E',  'GGT' : 'G',  'GGC' : 'G', 'GGA' : 'G',    'GGG' : 'G' }

fname = str(sys.argv[1])
fo  = open(fname,"r")
fasta_file  =  fo.read()
fnum = fasta_file.find("\n")
fnum += 1
fo.close()
fasta_file = fasta_file[fnum:]

#print "The first exon is:",exon1
def Start_Codon(str,start):
	if str < start:
		return "end of file"
	l = len(str)
        i = start
        a = str[i:i+3]
        while a != "ATG" and (i) <= l:
		i += 3
		a = str[i:i+3]
 	if a == "ATG":
		return i
 	else:
		return "null" 

def Stop_Codon(str,start):
	if str < start:
		return "end of file"
 	l = len(str)
	i = start
	a = str[i:i+3]
	while a != "TAA" and a != "TAG" and a != "TGA" and i < l:
		i += 3
		a = str[i:i+3]
	if a != "TAA" or a != "TAG" or a != "TGA" or i >= l:
		return i
	else:
		return "null"
def Get_Last_Codon(str,s):
	stop4 = str.rfind("ATG",s)
	#stop2 = str.rfind("TAG",s)
	#stop3 = str.rfind("TGA",s)
	#stop = max(stop1,stop2,stop3)
	return stop4
def Get_Exon(str,s):
	start = Start_Codon(str,s)
        stop = Stop_Codon(str,start)
        if start == "null" or stop == "null":
		return "null"
	else:
		return str[start:stop+3]
def Get_ORF(str,s):
	exit  = 0
	start = Start_Codon(str,s)
        stop = Stop_Codon(str,start)
	last = Get_Last_Codon(str,1)
	ORF = []
	while exit == 0:
		ex  = Get_Exon(str,start)
		if ex == "null":
			exit = 1
		if len(ex) < 6:
			exit = 1
		ORF.append(ex)	
		start = Stop_Codon(str,start)
		if start >= (last-3):
			exit = 1
		start += 3
		
	return ORF
fa = open("Exons.txt","wb")
sw = ",".join(Get_ORF(fasta_file,1))
sw = ( "Reading Frame One\n") + sw

fa.write(sw)
sw1 = ",".join(Get_ORF(fasta_file,2))
sw1 = ( "\nReading Frame Two\n") + sw1
fa.write(sw1)
sw2 = ",".join(Get_ORF(fasta_file,3))
sw2 = ( "\nReading Frame Three\n") + sw2
fa.write(sw2)

fasta_file2 = fasta_file[::-1]
 
bw = ",".join(Get_ORF(fasta_file2,1))
bw = ( "\nReading Frame Four\n") + bw
fa.write(bw)

bw2 = ",".join(Get_ORF(fasta_file2,2))
bw2 = ( "\nReading Frame Five\n") + bw2

fa.write(bw2)

bw3 = ",".join(Get_ORF(fasta_file2,3))
bw3 = ( "\nReading Frame Six\n") + bw3

fa.write(bw3)
  

fa.close()
