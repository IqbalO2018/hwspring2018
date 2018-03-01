#words = raw_input(",")("enter any amount of words, seperated by coommas")

s=raw_input("please enter any amount of words, seperated by commas")
lower = s.lower()
list = s.split(",")
numofwords = len(list)
word = list
word1 = word[0]
word2 = word[1]
word3 = word[2]
word4 = word[3]
word5 = word[4]


if(numofwords % 2 != 0):
	print("that is odd")
	if("llama" in lower):
			print(list)

if(len(word1) % 2 != 0):
	if(len(word2) % 2 != 0):
		if(len(word3) % 2 != 0):
			if(len(word4) % 2 != 0):
				if(len(word4) % 2 != 0):
					print("this is odd")
