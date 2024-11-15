alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
plain_text=''
def encryption(plain_text,shift_key):
    cipher_text=''
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text=alphabet[new_position]
        else:
            cipher_text+=char
    print(f'{cipher_text}')
def decryption (cipher_text,shift_key):
    plain_text=''
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position=(position-shift_key)%26
            plain_text=alphabet[new_position]
        else:
            plain_text+=char
    print(f'{plain_text}')
want_to_end = False
while not want_to_end:
    what_to_do=input('enter encrypt for encryption and decrypt for decryption')
    text=input('enter message')
    shift=int(input('how many times do you want to shift?'))
    if what_to_do == 'encrypt':
        encryption(plain_text = text,shift_key=shift)
    else:
        decryption(cipher_text = text,shift_key=shift)
    again=input('do you want to play again?')
    if again=='yes':
        want_to_end= False
    else:
        want_to_end= True
        print('bye')
    