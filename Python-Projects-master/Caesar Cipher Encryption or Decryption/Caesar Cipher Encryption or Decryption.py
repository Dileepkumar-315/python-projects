import string
alphabet=list(string.ascii_lowercase)
def encryption(plain_text,shift_key):
    chiper_text=""
    for char in plain_text:
        position=alphabet.index(char)
        new_position=(position+shift_key)%26
        chiper_text+=alphabet[new_position]
    print("here's the text after encryption:",chiper_text)
def decryption(s,n):
    chiper_text=""
    for char in s:
        position = alphabet.index(char)
        new_position = (position - n) % 26
        chiper_text += alphabet[new_position]
    print("here's the text after decryption:", chiper_text)
wanna_do=False
while not wanna_do:
    what_to_do=input("type 'encrypt' for encryption,type 'decrypt' for decryption:\n").lower()
    s=input("Type your message:\n").lower()
    n=int(input("Type the shift number:\n"))
    li=list(string.ascii_lowercase)
    if what_to_do=="encrypt":
        encryption(plain_text=s,shift_key=n)
    elif what_to_do=="decrypt":
        decryption(s,n)
    m=input("enter yes to continue and no to end:")
    if m=="no":
        wanna_do=True
        print("Have a nice day!bye")
