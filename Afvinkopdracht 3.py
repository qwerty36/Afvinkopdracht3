###################################################################################################################################
##Python application to determine whether or not a restriction enzyme cuts the sequence, and if differences will be shown or not.##
##Made by: Richard Jansen, Student at HAN University of applied sciences, Nijmegen, The Netherlands.###############################
##Date: 29-11-2014 ################################################################################################################
###################################################################################################################################



#############################################################
##Assignment of the variables and references to other files##
#############################################################

artwork = open ("artwork.txt")
bestand = open ("enzymen.txt")
x = open ("sikkel_seq.txt")
y = open ("normaal_seq.txt")
sikkel_seq = str(x.readlines())
normaal_seq = str(y.readlines())

###########################################################################
##A "for" loop to check if restriction enzymes will cut the sequence#######
##and if so, will there be a difference between the two given sequences?###
###########################################################################

for regel in bestand:
    enzym, seq = regel.split()
    seq = seq.replace("^","")
    if sikkel_seq.find(seq) ^ normaal_seq.find(seq):
        print (len(sikkel_seq.split(seq)))
        if len(sikkel_seq.split(seq)) != len(normaal_seq.split(seq)):
            print ("Using "+enzym, "deviations in the sequences CAN be shown ")
        else:
            print ("using "+enzym, "deviations in the sequences CAN NOT be shown ")
    else:
        print ("Enzyme "+enzym, "Cuts either both sequences resulting in equal length or does not cut at all")



############################################################################
##A little bit of a bonus that tends not to work.....  dammit!##############
############################################################################

#for regel in artwork:
	#print (regel)
