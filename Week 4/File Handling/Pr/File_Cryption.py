import sys

def decrypt(In):
    decimal,Return=0,""
    for i in range(len(In)):
        decimal+=int(In[len(In)-1-i])*(2**i)
    if len(In)==8:
        ASCII=decimal
        Return+=str(chr(ASCII))
    elif len(In)<=5:
        if decimal==0:
            ASCII=32
        else:
            ASCII=decimal+96
        Return+=str(chr(ASCII))
    else:
        Return+="\"unknown encrypted element\""
    return Return

def encrypt (In, byte_size):
    byte,Return="",""
    while (True):
        bit = In%2
        byte+=str(bit)
        if In == 0:
            break
        In=int(In/2)
    if len(byte)<byte_size:
        byte+=(byte_size-len(byte))*"0"
    for i in range(-1*byte_size,0):
        Return+=byte[-len(byte)-i-1]
    Return+=" "
    return Return

def encryption_58(Input, Filed):            
    Return =""
    num_of_bits=input("Encrytion size (in bits): ")
    num_of_bits = int(num_of_bits) if (len(num_of_bits)!=0) else 8
    if num_of_bits>8 or num_of_bits<3:
        print("Input Error: Max Encryption Size: 8-bits!\n"+13*" "+"Min Encryption Size: 3-bit!")
        sys.exit()
    for i in range(len(Input)):
        ASCII = ord(Input[i])
        Return+=encrypt (ASCII, num_of_bits)
    return Return

def decryption_58(Input):
    Return=""
    Input=Input.split()
    for i in range(len(Input)):
        Return+=decrypt (Input[i])
    return Return
