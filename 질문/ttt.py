class Person:
    
    def __init__(self):
        self.name = '이름없음'

    # getter
    def get_name(self):
        return self.name
    
    # setter
    def set_name(self, value):
        if len(value) >= 2:
            self.name = value
        else:
            print('이름은 2글자 이상이어야 합니다.')


q = Person()
# q.name = '김조은'
q.set_name('김')
print('q - name : {}'.format( q.get_name() ))