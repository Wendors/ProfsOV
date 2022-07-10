from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_BREAK
from docx.oxml.ns import qn
from docx.shared import Cm, Pt
import tempfile
#Створити вордовський файл для завантаженя контролю Який збережиний шаблон docx в ресурсі программи
class Docxs():
    gnam = "/gerb.png"
    pathtemp = tempfile.gettempdir() + "/Proftemp"
    def __init__(self):
        self.document = Document()
        """
        self.p1 = self.document.add_paragraph()
        self.rung = self.p1.add_run()
        self.rung.add_picture('{0}'.format(self.pathtemp + self.gnam),width=Cm(1.3), height=Cm(1.7))
        self.p1.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        """
        self.p2 = self.document.add_paragraph()
        self.rung = self.p2.add_run()
        self.rung.add_picture('{0}'.format("Gerb.png"), width=Cm(1.3), height=Cm(1.7))
        self.rung.add_break(break_type=WD_BREAK.LINE)
        self.run1 = self.p2.add_run()
        self.run1.add_text('\nМІНІСТЕРСТВО ЮСТИЦІЇ УКРАЇНИ')
        self.run1.font.name = 'Times New Roman'
        self.run1.font.size = Pt(16)
        self.run1.bold = True
        self.run1.add_break(break_type=WD_BREAK.LINE)
        self.run2 = self.p2.add_run()
        self.run2.add_text('ДЕРЖАВНА УСТАНОВА «ПОЛИЦЬКА ВИПРАВНА КОЛОНІЯ (№76)»')
        self.run2.font.name = 'Times New Roman'
        self.run2.font.size = Pt(14)
        self.run2.bold = True
        self.p2.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        self.document.add_page_break()

        self.document.save('demo.docx')
Docxs()