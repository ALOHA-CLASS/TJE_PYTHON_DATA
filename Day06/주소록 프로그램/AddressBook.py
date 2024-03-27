'''
    주소록 프로그램 만들기
    김조은,010-1234-1234,인천시 부평구

    [기능]
    1. 새로운 주소 등록하기
    2. 기존 주소 삭제하기
    3. 기존 주소 수정하기
    4. 특정 주소 검색하기
    5. 전체 주소 출력하기
    6. 주소록 정보를 파일로 관리하기

    [객체]
    📗 AddressBook  - 주소록 객체
    👩‍💼 Person       - 사람 객체

    [주소록 정보]
    📋 AddressBook.csv 파일로 관리
    💎 이름, 전화번호, 주소 정보를 저장

    [함수]
    file_reader()           : AddressBook.csv 파일 읽기
    file_generator()        : AddressBook.csv 파일 생성
    menu()                  : 메뉴 소개 및 입력
    exit()                  : 프로그램 종료
    run()                   : 프로그램 실행
    insert()                : 추가
    update()                : 수정
    search()                : 검색
    print_all()             : 전체 출력
    
    __init__()              : 생성자 - 주소록 리스트, 파일객체 초기화

'''

# 사람 : Person 클래스
# ✅ 생성자  
#   - 변수 : name, phone, addr
# ✅ 메소드
#     - info() 
#       : 이름, 전화번호, 주소를 문자열 템플릿으로 출력하는 기능


# 주소록 : AddressBook 클래스
# ✅ 변수 : 주소록 리스트 - address_list
# ✅ 생성자
# ✅ 메소드
#     - file_reader()           : AddressBook.csv 파일 읽기
#     - file_generator()        : AddressBook.csv 파일 생성
#     - menu()                  : 메뉴 소개 및 입력
#     - exit()                  : 프로그램 종료
#     - run()                   : 프로그램 실행
#     - insert()                : 추가
#     - update()                : 수정
#     - search()                : 검색
#     - print_all()             : 전체 출력


# --------------------------------------------------------
import sys


# 사람
class Person:
    # 생성자
    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr
        
    # info()
    def info(self):
        print('{}, {}, {}'.format(self.name, self.phone, self.addr))

# 주소록
class AddressBook:

    # 생성자
    def __init__(self):
        self.address_list = []
        self.file_reader()

    # csv 파일 읽기
    def file_reader(self):
        try:
            # 예외 발생 가능성 코드
            file = open('AddressBook.csv', 'rt', encoding='UTF-8')
        except:
            # 예외 처리 
            print('AddressBook.csv 파일이 없습니다.')
        else:
            # 예외 미발생 시, 파일 입력(AddressBook.csv --> address_list)
            while True:
                buffer = file.readline()    # 한 줄씩 데이터 읽기
                if not buffer:
                    break
                # 김조은,010-1234-1234,인천시 부평구(\n)
                name = buffer.split(',')[0]
                phone = buffer.split(',')[1]
                addr = buffer.split(',')[2].rstrip('\n')
                # rstrip(문자) : 지정한 문자를 문자열 오른쪽에서 제거
                # Person 객체 생성
                person = Person(name, phone, addr)
                # 가져온 연락처 정보를 address_list 에 추가
                self.address_list.append(person)

            print('AddressBook.csv 파일을 읽어왔습니다.')
            file.close()

    # csv 파일 생성
    def file_generator(self):
        try:
            file = open('AddressBook.csv', 'wt', encoding='UTF-8')
        except:
            print('AddressBook.csv 파일을 생성할 수 없습니다.')
        else:
            # address_list 를 모두 반복하여, 모든 연락처를 csv 파일에 출력
            for person in self.address_list:
                file.write('{},{},{}\n'.format(person.name, person.phone, person.addr))
            file.close()


    # 메뉴
    def menu():
        print('-' * 30)
        print('1. 주소 등록하기')
        print('2. 주소 삭제하기')
        print('3. 주소 수정하기')
        print('4. 주소 검색하기')
        print('5. 모든 주소 출력하기')
        print('0. 프로그램 종료')
        print('-' * 30)
        choice = int( input('메뉴 번호 : '))
        return choice

    # 프로그램 종료
    def exit(self):
        print('프로그램을 종료합니다.')
        sys.exit()      # 자동 임포트 : ctrl + . (quick fix) 


    # 프로그램 실행
    def run(self):
        
        while True:
            choice = AddressBook.menu()
            if choice == 0: self.exit()         # 종료
            elif choice == 1: self.insert()     # 추가
            elif choice == 2: self.delete()     # 삭제
            elif choice == 3: self.update()     # 조회
            elif choice == 4: self.search()     # 검색
            elif choice == 5: self.print_all()  # 전체출력
            else: print('(0~5) 사이의 메뉴번호를 입력해주세요.')
        

    # 주소록 추가 
    def insert(self):
        print('----- 연락처 추가 -----')
        name = input('이름 : ')
        phone = input('전화번호 : ')
        addr = input('주소 : ')
        
        # 유효성 검사
        if name and phone and addr:
            person = Person(name, phone, addr)
            self.address_list.append(person)
            # csv 파일에 연락처 목록을 생성(overwrite)
            self.file_generator()
            print('새 연락처가 등록되었습니다!')
        else:
            print('누락된 입력값이 있어 등록되지 않았습니다.')

    # 주소록 삭제 
    def delete(self):
        print('----- 기존 연락처 삭제 -----')
        name = input('삭제할 이름 : ')
        if not name:
            print('이름이 입력되지 않아 삭제를 취소합니다.')
            return
        # 삭제 여부
        deleted = False

        for i, person in enumerate(self.address_list):
            # 입력한 이름이 연락처에 존재하면,
            if name == self.address_list[i].name:
                phone = self.address_list[i].phone
                print('검색한 전화번호 : {}'.format(phone))
                if input('삭제할까요? (Y/N)').upper() == 'N':
                    continue

                self.address_list.pop(i)    # 해당 연락처 삭제
                deleted = True
                print('{} 의 정보를 삭제하였습니다.'.format(name))
                self.file_generator()       # AddressBook.csv 갱신
                # break

        if not deleted:
            print('{}의 정보가 삭제되지 않았습니다.'.format(name))


    # 주소록 수정
    def update(self):
        print('----- 기존 연락처 수정 -----')
        # 1. 수정할 이름 입력
        name = input('수정할 이름 : ')
        
        # 2. 입력여부 체크
        if not name:
            print('이름이 입력되지 않아 수정을 취소합니다.')
            return

        # 3. 수정 여부 확인 (Y/N)
        updated = False

        for i, person in enumerate(self.address_list):
            if name == self.address_list[i].name:
                phone = self.address_list[i].phone
                print('수정할 전화번호 : {}'.format(phone))
                if input('수정할까요? (Y/N)').upper() == 'N':
                    continue
                    
                # 해당 연락처 수정
                option = input('이름, 전화번호, 주소 중 무엇을 수정하시겠습니까? (이름, 전화번호, 주소)')
                if option == '이름':
                    name = input('수정할 이름을 입력하세요: ')
                    self.address_list[i].name = name
                elif option == '전화번호':
                    phone = input('수정할 전화번호을 입력하세요: ')
                    self.address_list[i].phone = phone
                elif option == '주소':
                    addr = input('수정할 주소를 입력하세요: ')
                    self.address_list[i].addr = addr
                else:
                    print('잘못 입력하셨습니다.')
                    break

                updated = True
                print('주소록이 수정되었습니다!')
                print('수정된 주소록 정보')
                self.address_list[i].info()
                self.file_generator()           # 주소록 갱신
                break
            
        if not updated:
            print('{} 의 정보가 수정되지 않았습니다.'.format(name))    
        # 6. csv 파일 갱신


    # 주소록 조회 
    def search(self):
        # 리스트에서 검색할 연락처 정보를 이름으로 찾아서 출력
        name = input('검색할 이름 : ')
        if not name: 
            print('이름이 입력되지 않아서 조회할 수 없습니다.')
            return      # 메소드 종료
        
        print('----- 조회된 연락처 정보 -----')

        # 검색 여부
        searched = False
        # (0, person1)
        for i, person in enumerate(self.address_list):
            # (입력 받은 이름) == (리스트에 있는 이름)  --> 조회 성공-> 출력
            if name == self.address_list[i].name:
                person.info()   
                searched = True

        if not searched:
            print('조회된 연락처 없습니다.')


    # 전체 출력 
    def print_all(self):
        print('----- 전체 연락처 출력 -----')
        for person in self.address_list:
            person.info()

        list_count = len(self.address_list)
        print('총 {}개의 연락처가 있습니다.'.format(list_count))

# AddressBook 클래스 끝
    
# 객체 생성
my_app = AddressBook()

# 프로그램 실행 - run()
my_app.run()
