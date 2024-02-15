from Crypto.Cipher import AES

def xor_encrypt(data_block):
    for i in range(15):
        data_block[i+1] = data_block[i+1] ^ data_block[i]
    return data_block

def xor_decrypt(cipher_block):
    plain_text = []
    plain_text.append(cipher_block[0])
    for i in range(15):
        plain_text.append(cipher_block[i+1] ^ cipher_block[i])
    return plain_text 

def main():
    key = bytes.fromhex('50726573746964696769746174696f6e')
    cipher_text2 = bytes.fromhex('a0595e10eec5ffd64cf3569eac102451')
    cipher_text1 = bytes.fromhex('e1dbfd6826a14f279fafe76982333070')
    
    AES_cipher = AES.new(key, AES.MODE_ECB)
   
    AES_Out_Cipher1 = AES_cipher.decrypt(cipher_text1)
    AES_Out_Cipher2 = AES_cipher.decrypt(cipher_text2)
    
    flag = xor_decrypt(list(AES_Out_Cipher1))
    flag2 = xor_decrypt(list(AES_Out_Cipher2))

    for i in range(len(flag)):
        print(chr(flag[i]), end="")
    for i in range(len(flag2)):
        print(chr(flag2[i]), end="")

        
if __name__=="__main__":
    main()



