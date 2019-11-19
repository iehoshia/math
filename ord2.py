key = 'NOPQRSTUVWXYZ'
base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = 'MENSAJE'

print(key)
print(base)
print(message)

base_lenght = len(base) - 1
key_lenght = len(key) - 1
message_lenght = len(message) - 1

codes = []
key_codes = []
message_codes = []
reverse_codes = []

for i in range(0, key_lenght):
	key_codes.append(ord(key[i]))

for i in range(0, base_lenght):
	codes.append(ord(base[i]))
	if base[i] in key:
		continue
	key_codes.append(ord(base[i]))

print(codes)
print(key_codes)

def get_index(key, array):
	i = 0
	while i < len(array):
		if key == array[i]:
			return i
		i += 1
reverse_message = ''

i = 0
while i <= message_lenght:
	current_key = message[i]
	if current_key in base:
		current_code = ord(current_key)
		index = get_index(current_code, codes)
		if index is not None:
			message_codes.append(key_codes[index])
			reverse_message += chr(key_codes[index])
	i += 1

print(reverse_message)

print(message_codes)
reverse_roth = ''
i = 0
while i <= message_lenght:
	current_key = message_codes[i]
	if current_key in key_codes:
		index = get_index(current_key, key_codes)
		if index is not None:
			reverse_codes.append(codes[index])
			reverse_roth += chr(codes[index])
	i += 1

print(reverse_codes)
print(reverse_roth)