#ord.py

message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 'PATO'

lenght = len(message) - 1
key_lenght = len(key)

codes = []
key_codes = []

for i in range(0, key_lenght):
	key_codes.append(ord(key[i]))

for i in range(0,lenght):
	print(message[i])
	print(ord(message[i]))
	codes.append(ord(message[i]))
	if message[i] in key:
		continue
	key_codes.append(ord(message[i]))

print(codes)
print(key_codes)
