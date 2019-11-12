#inverse_string.py

message = 'This message will be reversed'

translated = '' # REVERSE

i = len(message) - 1
print(i)

while i >= 0:
	translated = translated + message[i]
	print(translated)
	i = i - 1

str_translated = translated

i = len(str_translated)-1
while i >= 0:
	str_translated = str_translated[:i]
	print(str_translated)
	i = i - 1


i = len(translated) -1
message = ''
while i >= 0:
	message = message + translated[i]
	print(message)
	i = i - 1
print("The cipher text is :", translated)
print("The message is :", message)

print()
print("****************")
print()

def encrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text

      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
      return result
#check the above function
text = "CEASER CIPHER DEMO"
s = 4

print( "Plain Text : " + text)
print( "Shift pattern : " + str(s))
res = encrypt(text,s)
print( "Cipher: " + encrypt(text,s))

message = res #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      else:
         translated = translated + symbol
print('Hacking key #%s: %s' % (key, translated))

