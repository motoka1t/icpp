import datetime

class Person(object):

    def __init__(self, name):
        """「人間」を生成する"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
    
    def getName(self):
        """selfの名前（フルネーム）を返す"""
        return self.name
    
    def getLastName(self):
        """selfの姓を返す"""
        return self.lastName
    
    def setBirthday(self, birthdate):
        """birthdateをdatetime.date型とする
        selfの生年月日をbirthdateと設定する"""
        self.birthday = birthdate

    def getAge(self):
        """selfの現在の年齢を日単位で返す"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        """selfの名前がotherの名前に比べて
        アルファベット順で前ならばTrueを
        そうでなければFalseを返す
        比較は、姓について行われるが
        姓が同じであれば名前（フルネーム）が比較される"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    def __str__(self):
        """selfの名前（フルネーム）を返す"""
        return self.name
    


