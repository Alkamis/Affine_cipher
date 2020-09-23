
#classical Affine cipher


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m





 # affine cipher encrytion function
def affine_encrypt(text, key):
    '''
    C = (k*P + b) % 26
    '''
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26)
                        + ord('A')) for t in text.upper().replace(' ', '')])


# affine cipher decryption function
def affine_decrypt(cipher, key):
    '''
    P = (k^-1 * (C - b)) % 26
    '''
    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1]))
                         % 26) + ord('A')) for c in cipher])


# Main function
def main():
   while True:
       try:
           text = input('Enter your text:')
           k = int(input("Enter value of K :"))
           b = int(input("Enter value of b :"))
           key = [k, b]
       except ValueError:
           print("Ooop your input is wrong ")
           break



       # calling encryption function
       affine_encrypted_text = affine_encrypt(text, key)

       print('Encrypted Text: {}'.format(affine_encrypted_text))

       # calling decryption function
       print('Decrypted Text: {}'.format
             (affine_decrypt(affine_encrypted_text, key)))
       break


if __name__ == '__main__':
    main()
