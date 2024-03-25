'''
-클래스 선언

    class 클래스명:
        클래스 내용
        
        # 생성자
        # : 객체가 생성될 때, 실행되는 메소드
        def __init__(self, 매개변수):
            생성자 내용
            
        # self : 객체 자신을 가리키는 키워드(딕셔너리)
        # self.(변수),  self.(메소드)
        
        # 소멸자
        # : 객체가 소멸될 때, 실행되는 메소드
        def __del__(self):
            소멸자 내용
            
        # 메소드
        # : 클래스가 정의된 함수
        def 메소드명(self, 매개변수):
            메소드 내용
            
'''

'''
    # 객체 생성
    # 객체 변수명 = 클래스명( )         # 클래스명( )  --> 생성자 함수
    # 인스턴스 : 클래스를 통하여 생성된 객체
    
'''

# Person  클래스 선언
class Person:

    # 클래스 변수 선언
    # name = '이름없음'
    # age = 0
    # tel = '010-0000-0000'

    # 생성자
    def __init__(self, name=None, age=None, tel=None):
        self.name = name
        self.age = age
        self.tel = tel
        print('Person 객체 생성...')
        
        # pass : 아무런 동작도 수행하지 않는 키워드
        #        함수 정의 등에서 구체적인 기능 구현을 나중으로 미룰 때 주로 사용                
    
    # 소멸자
    def __del__(self):
        print('Person({}) 객체 소멸...'.format(self.name))

    # 메소드
    def show_info(self):
        print('이름 : {}, 나이 : {}, 전화번호 : {}'.format(self.name, self.age, self.tel))


# Person 객체 생성
person = Person('김조은', 20, '010-1234-1234')
person.show_info()

person2 = Person('박조은', 30, '010-1111-2222')
person2.show_info()

# 객체의 변수 접근
print('이름 : {}'.format( person.name ))
print('나이 : {}'.format( person.age ))
print('전화번호 : {}'.format( person.tel ))



# 생성자를 디폴트 매개변수로 지정하면, 
# 인자의 개수를 가변적으로 사용가능
person3 = Person('이조은')
person3.show_info()

person4 = Person('권조은', 10)
person4.show_info()

person4.tel = '010-2222-3333'
print('person4 추가된 전화번호 : {}'.format(person4.tel))


print( person )