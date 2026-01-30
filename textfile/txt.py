# open and read text file
with open("simple.txt", "r", encoding="utf-8") as file:
    text = file.read()

# print extracted text
print("Extracted Text:\n")
print(text)
