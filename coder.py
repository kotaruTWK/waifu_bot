def coder(message, word="default"):
    coded = ""
    lenW = len(word)
    
    for letter in message:
        if letter.lower() in word.lower():
            letter = letter
        else:
            if letter.isupper() == True:
                cap = True
                letter = letter.lower()
            else:
            	cap = False
            letter = trans(letter)
            if cap == True:
            	letter = letter.upper()
            while letter.lower() in word:
                letter = trans(letter)
            else:
                letter = letter
        coded += letter
    return coded
	
def trans(letter):
    
	letter = letter.translate(bytes.maketrans(b"abcdefghijklmnopqrstuvwxyz",b"bcdefghijklmnopqrstuvwxyza"))
	return letter


def decoder(message, word="default"):
    decoded = ""
    lenW = len(word)
    
    for letter in message:
        if letter.lower() in word.lower():
            letter = letter
        else:
            if letter.isupper() == True:
                cap = True
                letter = letter.lower()
            else:
            	cap = False
            letter = detrans(letter)
            if cap == True:
            	letter = letter.upper()
            while letter.lower() in word:
                letter = detrans(letter)
            else:
                letter = letter
        decoded += letter
    return decoded
	
def detrans(letter):
	letter = letter.translate(bytes.maketrans(b"bcdefghijklmnopqrstuvwxyza",b"abcdefghijklmnopqrstuvwxyz"))
	return letter
