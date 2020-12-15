def calc_encryption():
  en_message = []
  message = input("Message to encrypt: ")
  for x in range(len(message)):
    charValue = int(ord(message[x]))
    charValue = charValue + 2
    newChar = chr(charValue)
    en_message.append(str(newChar))
  print ("")
  print(''.join(str(x) for x in en_message))

calc_encryption()