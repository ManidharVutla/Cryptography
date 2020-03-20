 
import hmac
import hashlib
import random

def xor(byteseq1, byteseq2):
    # First we convert each byte to its int value
    l1 = [b for b in byteseq1]
    l2 = [b for b in byteseq2]
    l1xorl2 = [bytes([elem1^elem2]) for elem1,elem2 in zip(l1,l2)]
    result = b''.join(l1xorl2)

    return result


def F(byteseq, k):
    # create a hmac sha1 
    h = hmac.new(k, byteseq, hashlib.sha1)
    # Return first 8 bytes of the calculated hmac sha1 hash
    return h.digest()[:8]


# main block processing
def feistel_block(LE_inp, RE_inp, k):
    
    mid_fun=F(RE_inp,k)
    
    RE_out=xor(mid_fun, LE_inp)
    
    LE_out= RE_inp
    
    return LE_out, RE_out
    
    
def gen_keylist(keylenbytes, numkeys, seed):
    # We need to generate numkeys keys each being keylen bytes long
    keylist = []
    random.seed(seed)

    for i in range(0, numkeys):
        keylist.append(random.randint(123, 999).to_bytes(keylenbytes, 'little'))
    
    return keylist


def feistel_enc(inputblock, num_rounds, seed):
  
    keylist = gen_keylist(8, num_rounds, seed)
    
    for key in keylist:    
        le,re=feistel_block(inputblock[:4], inputblock[4:], key)
        inputblock=le+re
    
    cipherblock= inputblock[4:] + inputblock[:4]
    
    return cipherblock

    
def feistel_enc_test(input_fname, seed, num_rounds, output_fname):
    
    # First read the contents of the input file as a byte sequence
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    
    
    inpbyteseq=bytearray(inpbyteseq)
    cipherbyteseq=bytearray()
    #print(inpbyteseq)
    blocklist=[]
    for block in range(0, len(inpbyteseq), 8):
        blocklist.append(inpbyteseq[block:block+8])
    
    if len(blocklist[-1])<8: 
        blocklist[-1]= blocklist[-1] + b' '*(8 - len(blocklist[-1]))
    
    
    for seq in blocklist:
        cipherbyteseq+= feistel_enc(seq, 16, 30)
    
    #print(cipherbyteseq)
    fout = open(output_fname, 'wb')
    fout.write(cipherbyteseq)
    fout.close()
    
    
def feistel_dec(inputblock, num_rounds, seed):
    keylist = gen_keylist(8, num_rounds, seed)
    
    for key in reversed(keylist):    
        le,re=feistel_block(inputblock[:4], inputblock[4:], key)
        inputblock=le+re
    
    plainblock= inputblock[4:] + inputblock[:4]
    
    return plainblock

def feistel_dec_test(input_fname, seed, num_rounds, output_fname):
    
    # First read the contents of the input file as a byte sequence
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    
    inpbyteseq=bytearray(inpbyteseq)
    plainbyteseq=bytearray()
  
    blocklist=[]
    for block in range(0, len(inpbyteseq), 8):
        blocklist.append(inpbyteseq[block:block+8])
    
    
    for seq in blocklist:
        plainbyteseq+= feistel_dec(seq, 16, 30)
    
    fout = open(output_fname, 'wb')
    fout.write(plainbyteseq.decode("utf-8").rstrip().encode())
    fout.close()
    


