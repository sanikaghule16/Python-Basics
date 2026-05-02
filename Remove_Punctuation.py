import string
text = input("Enter A String:")
result = "".join(ch for ch in text if ch not in string.punctuation)
print("String Without Punctuation:",result)
print("\n--------------------------------------------------")
