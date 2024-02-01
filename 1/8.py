# import PyPDF2

# reader = PyPDF2.PdfReader('example.pdf')

# # print(reader.pages[0].extract_text())

# text = reader.extract_text()
# print(text)

import re
from PyPDF2 import PdfReader


reader = PdfReader("example2.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()


text2 = re.findall(r'', text)

print(text2)