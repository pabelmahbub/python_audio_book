import pyttsx3
import PyPDF2


book = open('python.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

print(pages)


my_book = pyttsx3.init()

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()

    my_book.say(text)
    my_book.runAndWait()
