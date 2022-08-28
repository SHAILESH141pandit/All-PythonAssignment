# 5. Write a python script to print two given words in dictionary order.
FWord = input("Enter a first words:  ")
SWord = input("Enter a second words:  ")

if FWord>SWord:
    print("Dictionary order is",SWord,FWord)

else:
    print("Dictionary order is",FWord,SWord)