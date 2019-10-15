number = input("Enter your Phone Number: ")
numbers_to_words = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero"
}
display = ""
for ch in number:
    display += numbers_to_words.get(ch) + " "
print(display)
