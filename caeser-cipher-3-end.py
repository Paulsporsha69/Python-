character =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z']

def caeser(text,shift,direction) :
    cipher_text =""
    if direction == "decode":
        shift = shift * -1
    for char in text:
      if char in character:
          position = character.index(char)
          new_pos = position + shift
          if new_pos >25 :
            new_pos = new_pos -26
          elif new_pos < 0:
            new_pos = new_pos + 26
          new_message = character[new_pos]
          cipher_text += new_message
      else :
          cipher_text += char
    print (f"The {direction}d message is : {cipher_text}")



shoul_end =False
while not shoul_end:
    direction = input("Type 'encode' to encrypt ,type 'decode' to decrypt :  \n")
    text = input("Type your message :").lower()
    shift = int(input("The number that you want to shift :"))
    shift =shift %26
    caeser(text, shift, direction)

    restart = input("Do you want to start again?")
    if restart =="No":
        shoul_end=True
        print("End Game")








