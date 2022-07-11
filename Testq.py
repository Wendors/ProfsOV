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
        self.p2 = self.document.add_paragraph()
        self.rung = self.p2.add_run()
        self.rung.add_picture('{0}'.format(self.pathtemp + self.gnam), width=Cm(1.3), height=Cm(1.7))
        self.rung.add_break(break_type=WD_BREAK.LINE)
        self.run1 = self.p2.add_run()
        self.run1.add_text('МІНІСТЕРСТВО ЮСТИЦІЇ УКРАЇНИ')
        self.run1.font.name = 'Times New Roman'
        self.run1.font.size = Pt(16)
        self.run1.bold = True
        self.run1.add_break(break_type=WD_BREAK.LINE)
        self.run2 = self.p2.add_run()
        self.run2.add_text('ДЕРЖАВНА УСТАНОВА «ПОЛИЦЬКА ВИПРАВНА КОЛОНІЯ (№76)»')
        self.run2.font.name = 'Times New Roman'
        self.run2.font.size = Pt(14)
        self.run2.bold = True
        self.run2.add_break(break_type=WD_BREAK.LINE)
        self.run3 = self.p2.add_run()
        self.run3.add_text(' с. Іванчі Вараського району Рівненської  області, 34375тел. 2-53-24; 5-31-49,тел./факс 5-35-46')
        self.run3.font.name = 'Times New Roman'
        self.run3.add_break(break_type=WD_BREAK.LINE)
        self.run3.add_text('E-mail: pvk76@ukr.net Код ЄДРПОЧ 08564370')
        self.run3.font.size = Pt(11)
        self.run3.add_break(break_type=WD_BREAK.LINE)
        self.p2.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        self.p3 = self.document.add_paragraph()
        self.run4 = self.p3.add_run()
        self.run4.add_text('__________№___________                      	На №5к/вих.//7709 від 25.10.2021')
        self.run4.font.name = 'Times New Roman'
        self.run4.font.size = Pt(14)
        self.run4.add_break(break_type=WD_BREAK.LINE)
        self.p3.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY

        self.document.save('demo.docx')
Docxs()