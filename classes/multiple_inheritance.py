class father:
    def __init__(self,fathername,fatherage):
        self.fathername=fathername
        self.fatherage=fatherage

    def showfathername(self):
        print(self.fathername)

    def age(self):
        print(self.fatherage)

class mother:
    def __init__(self,mothername):
        self.mothername=mothername

    def showmothername(self):
        return self.mothername

class son(father,mother):
    def __init__(self,sonname,fathername,fatherage,mothername):
        father.__init__(self,fathername,fatherage)
        mother.__init__(self,mothername)
        self.sonname = sonname

    def showsonname(self):
        print(self.sonname)

s=son(sonname='Allen',fathername="David",fatherage=50,mothername="Alexa")
s.showsonname()
s.showfathername()
print(s.showmothername())

