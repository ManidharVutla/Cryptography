#Name: Naga Vutla
#UID: 116352444


import numpy as np

def vigenere_enc(keyword, plaintext):
    
    plaintext=plaintext.replace(" ","");
    
    # Keyword Construction
    keyword= keyword * ((len(plaintext)/len(keyword)) + 1)
    keyword= keyword [0:len(plaintext)]
    
    # Encryption with the Keyword
    c=""
    for i in range(len(plaintext)):
        c = c + chr( (((ord(plaintext[i]) - 97)+ (ord(keyword[i]) - 97)) % 26) + 97 )
    return c
    

def vigenere_dec(keyword, ciphertext):
    # Keyword Construction
    keyword= keyword * ((len(ciphertext)/len(keyword)) + 1)
    keyword= keyword [0:len(ciphertext)]
    
    # Decryption with the Keyword
    p=""
    for i in range(len(ciphertext)):
        p = p + chr( (((ord(ciphertext[i]) - 97) - (ord(keyword[i]) - 97)) % 26) + 97 )
    return p

    
def hill_enc(M, plaintext):
    global length
    length=len(plaintext)
    while (len(plaintext)%3!=0):
        plaintext= plaintext + 'x' 
    # List of characters (0-26)
    s_ind_list = [ord(c)-97 for c in plaintext]
    c=""
    for i in range(0,len(s_ind_list),3):  # it means integers from 0 to len(char_list)-1 with step 3
        sublist = s_ind_list[i:i+3]
        mul=np.dot(M,sublist) % 26
        c = c + ''.join([chr(j+97) for j in mul])
    return c

def matrixinvmod26(M):
    Minv = np.linalg.inv(M)
    Mdet = np.linalg.det(M)

    Mod26invTable = {}
    for m in range(26):
        for n in range(26):
            if (m*n)%26==1:
                Mod26invTable[m] = n
    # Let's find Mdet26 and Mdetinv26
    Mdet26 = Mdet%26
    if Mdet26 in Mod26invTable:
        Mdetinv26 = Mod26invTable[Mdet26]
    else:
        Mdetinv26 = None 

    Madj = Mdet*Minv
    Madj26 = Madj%26
    Minv26 = (Mdetinv26*Madj26)%26
    Minv26 = np.matrix.round(Minv26, 0)%26

    return Minv26

def hill_dec(M, ciphertext):
    
    Minv = matrixinvmod26(M)
    # List of characters (0-26)
    s_ind_list = [ord(c)-97 for c in ciphertext]
    p=""
    for i in range(0,len(s_ind_list),3):  # it means integers from 0 to len(char_list)-1 with step 3
        sublist = s_ind_list[i:i+3]
        mul=np.dot(Minv,sublist) % 26
        p = p + ''.join([chr((int)(j+97)) for j in mul])
    return p[0:length]




