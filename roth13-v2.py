def rot13(phrase):
   abc = "abcdefghijklmnopqrstuvwxyz"
   out_phrase = ""
   for char in phrase:
       out_phrase += abc[(abc.find(char)+13)%26]
   return out_phrase

phrase = "mensaje"
print(phrase)
print(rot13(phrase))
# kgurkehffvnafknerkpbzvat
print(rot13(rot13(phrase)))
# What's the output?