class IntSet(object):
    """intSetは整数型の集合である"""
    #ここに実装に関する情報を書く（抽象化の情報ではない）
    #集合は、int型の要素からなるリストself.valsによって表される
    #int型の要素はそれぞれ、リストself.valsにちょうど一度だけ現れる

    def __init__(self):
        """整数の空集合を生成する"""
        self.vals = []
    
    def insert(self, e):
        """eをint型とし、eをselfに挿入する"""
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        """eをint型とする
        eがselfにあればTrueを、なければFalseを返す"""
        return e in self.vals
    
    def remove(self, e):
        """eをint型とし、eをselfから削除する
        eがselfになければ例外ValueErrorを発生させる"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    
    def getMembers(self):
        """selfが含む要素を持つリストを返す
        要素の順序に関しては何も約束できない"""
        return self.vals[:]
    
    def __str__(self):
        """selfの文字列表現を返す"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}' #-1としたのは最後のカンマを省くため 

    