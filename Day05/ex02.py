class Student:

    def __init__(self, no, name, major):
        self.no = no
        self.name = name
        self.major = major
        
    # 특수한 이름의 메소드
    # __(이름)__ 형태의 특수한 이름의 메소드들이 있다.
    # : 미리 정의된 이름이며, 특수한 상황해서 호출되도록 정의되어있다.
    
    # __str__  : str(객체) 함수를 호출할 때, 자동으로 실행되는 메소드
    def __str__(self):
        return '{} / {} / {}'.format(self.no, self.name, self.major)
    
    # __eq__, __ne__ 등의 메소드를 정의하지 않으면,
    # ==, != 자체는 인스턴스를 비교합니다.
    # 객체의 정보가 같은지 확인하는 메소드
    def __eq__(self, obj):
        return self.no == obj.no
    
    # 객체의 정보가 다른지 확인하는 메소드
    def __ne__(self, obj):
        return self.no != obj.no
        
    
# 객체 리스트
students = [ 
            Student(101, '한성호', '컴퓨터공학과'),
            Student(102, '이효리', '방송연예과'),
            Student(103, '손석구', '연극영화과'),
            Student(101, '한성호', '컴퓨터공학과'),
        ]

for student in students:
    # str(객체) : 해당 객체의 __str__ 메소드를 호출하는 메소드
    print( str(student) )
    
# == 기호를 이용하여 두 객체를 비교하면, 
# 해당 객체의 __eq__ 메소드가 호출된다.    
print( students[0] == students[1] )
print( students[0] == students[3] )

# != 기호를 이용하여 두 객체를 비교하면, 
# 해당 객체의 __ne__ 메소드가 호출된다.    
print( students[0] != students[1] )
print( students[0] != students[3] )

    

s1 = Student(101, 'ALOHA', '컴퓨터공학과')
s2 = Student(101, 'ALOHA', '컴퓨터공학과')

print( s1 == s2 )