from docx import Document
from docx.shared import Mm

class Test():
    def Word(self):
        self.documents = Document()
        self.documents.add_heading("Goods", 5)
        self.documents.add_paragraph("Hello world!!!")
        self.documents.save("demo.docx")

Test().Word()