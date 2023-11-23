import Caesar 
import utils
from Hill import Hill


text = "paymoremoney"

hill = Hill()
crypt = hill.cipher(text)
print(crypt)
plain = hill.decipher(crypt)
print(plain)




# crypt = Caesar.Caesar(text, k=8)

# print(crypt)

# plain = Caesar.decipher(crypt)
# print(plain)


# file_content = ""
# with open("books/hemingwaye-oldmanandthesea.txt", "r") as file:
#     file_content = file.read()
# file_content = file_content.replace('\n', '')
# utils.statics(file_content, "plaintext")

