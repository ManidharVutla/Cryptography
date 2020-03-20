#Name: Naga Vutla
#UID: 116352444

import sys


def caesar_str_enc(plaintext, K):
    ciphertext=""
    for ch in plaintext:
        encch = caesar_ch_enc(ch, K)
        ciphertext = ciphertext + encch   
    return ciphertext

def caesar_ch_enc(ch, K):
    
    # everything needed to map a char to its encoded char with K as the parameter
    if ch==' ':
        return ch
    encch=chr(ord(ch)+K % 26)
    return encch
    

def caesar_str_dec(ciphertext, K):
    plaintext = ""
    for ch in ciphertext:
        decch = caesar_ch_dec(ch, K)
        plaintext = plaintext + decch
        
    return plaintext

def caesar_ch_dec (ch, K):
    
    # ...
    if ch==' ':
        return ch
    decch=chr(ord(ch)-K % 26)
    return decch


def test_module():
    K = int(sys.argv[1])
    input_str = sys.argv[2]
    
    
    
    
    print(input_str)
    encstr = caesar_str_enc(input_str, K)
    print(encstr)
    decstr = caesar_str_dec(encstr, K)
    print(decstr)
    
    
if __name__=="__main__":
    test_module()