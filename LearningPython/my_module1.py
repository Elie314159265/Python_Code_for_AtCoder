# -*- coding: utf-8 -*-
class Student:
    def __init__(self,name,math,english,japanese,science,society):
        self.name=name
        self.math=math
        self.english=english
        self.japanese=japanese
        self.science=science
        self.society=society
    def average_score(self):
        ave=(self.math+self.english+self.japanese+self.science+self.society)/5
        return ave