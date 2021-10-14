import string 

def Encrypt(string_text, int_key): 
    '''Caesar-encrypts string using specified key.''' 
    result = ""
    for i in range(len(string_text)):
      char = string_text[i]
      if(char.isupper()):
        result += chr((ord(char) + int_key - 65) % 26 + 65)
      elif(char.islower()):
        result += chr((ord(char) + int_key - 97) % 26 + 97)
      else:
        result += char
    return result

def Decrypt(string_text, int_key): 
  ''' Decrypts Caesar-encrypted string with specified key. ''' 
  result = ""
  for i in range(len(string_text)):
    char = string_text[i]
    if(char.isupper()):
      result += chr((ord(char) - int_key - 65) % 26 + 65)
    elif(char.islower()):
      result += chr((ord(char) - int_key - 97) % 26 + 97)
    else:
      result += char
  return result
 
def Print_menu():
  '''Prints menu. No user interaction. '''
  print("Main Menu")
  print("1). Encode a String")
  print("2). Decode a String")
  print("Q).Quit")
  print("Enter your selection ==>",end='')

choice = 1

def main(): 
  while choice !=3:
    Print_menu() 
    Choice = input()
    if Choice == '1': 
      Plaintext = input("Enter (brief) text to encrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Ciphertext = Encrypt(Plaintext, Key)
      print("Encrypted:", Ciphertext)
      print()
    elif Choice == '2': 
      Ciphertext = input("Enter (brief) text to decrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Plaintext = Decrypt(Ciphertext, Key)
      print("Decrypted:", Plaintext)
      print() 
    else: 
      print("Have an ordinary day.")

# our entire program: 
main() 
