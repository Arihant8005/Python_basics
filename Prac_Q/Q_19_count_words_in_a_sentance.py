# #Count Words in a Sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))

#or
sentance = [str(x) for x in input("Enter the sentence: ").split()]
print(len(sentance))