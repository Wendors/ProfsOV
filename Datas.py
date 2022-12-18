# -*- coding: utf-8 -*-

import sys
import os
import time

class Dat():
    mun = 0
    year = 0
    def Daetes(self):
        self.monslist = ["січень", "лютий", "березень", "квітень",
                         "травень", "червень", "липень", "серпень",
                         "вересень", "жовтень", "листопад", "грудень"]
        self.chemon = int(time.strftime('%m')) % 2
        if self.chemon == 0:
            self.inmon = 31
            if int(time.strftime('%m')) > 9:
                self.inmon = 30
        else:
            self.inmon = 30
            if int(time.strftime('%m')) == 1:
                self.inmon = 28
            if int(time.strftime('%m')) == 7:
                self.inmon = 31
        if 12 == int(time.strftime('%m')):
            self.neztm = int(time.strftime('%m')) + 1
            if self.neztm == 13:
                self.neztm = 1
                self.mone = self.monslist[self.neztm - 1]
                self.years = int(time.strftime('%Y'))
            for self.i in range(0, len(self.monslist)):
                if self.i + 1 == int(time.strftime("%m")):
                    self.mun = self.monslist[self.i]
        else:
            self.mone = int(time.strftime('%m')) + 1
            self.years = int(time.strftime('%Y'))
            for self.i in range(0, len(self.monslist)):
                if self.i + 1 == int(time.strftime("%m")):
                    self.mun = self.monslist[self.i]
        return self.mun, self.years

    def Spis_profs(self):
        self.listprof = {"Злодіїв в законі": "п. 1 <З>",
                         "Авторитет": "п. 1 <А>",
                         "Лідер ОЗГ": "п. 1  <Л>",
                         "Широкий резонанс": "п. 2",
                         "Проти основ національної безпеки": "п. 3",
                         "Вбивство на замовлення": "п. 4",
                         "Бандитизм": "п. 5",
                         "Наркоділки з міжрегіональними звязками": "п. 6",
                         "Шахрайство": "п. 7",
                         "Службові злочини": "п. 8",
                         "Нецільове використання бюджетних коштів": "п. 9",
                         "Ухилення від сплати податків": "п. 10",
                         "Зловживання владою або службовим становищем": "п. 11",
                         "Хабарр": "п. 12",
                         "Тероризм": "п. 13",
                         "Вступили в незаконні бандитські угрупування": "п. 14",
                         "Масові заворушення": "п. 15",
                         "У сфері державної таємниці": "п. 16",
                         "Розв'язування війни": "п. 17",
                         "Злочинний вплив": "п. 18",
                         "Напад":"п.19",
                         "Дії що дезорганізують роботу установи": "п. 18",
                         "Вживання наркотичних речовин": "п. 21",
                         "Телефонні шахраї": "п.22"}
        return self.listprof