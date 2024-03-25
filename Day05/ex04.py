# getter, setter
# - getter : 변수의 값를 가져오는 메소드
# - setter : 변수의 값을 지정하는 메소드

class Person:
    
    # getter
    def get_name(self):
        return self.name
    
    # setter
    def set_name(self, value):
        if len(value) >= 2:
            self.name = value
        else:
            print('이름은 2글자 이상이어야합니다.')

p = Person()

p.name = 'ALOHA'
p.set_name('ALOHA')
print('p - name : {}'.format( p.get_name() ))

p.set_name('김')