# 부모 클래스 - Robot
class Robot:
    
    # 생성자
    def __init__(self, name, power, battery):
        self.name = name
        self.power = power
        self.battery = battery
        
    # 메소드 - 전원, 이동, 충전
    def power(self, power):
        self.power = power
        print('power : ', power)
        
    def move(self, direction):
        print('{} (으/)로 이동합니다.'.format(direction))
        
    def charge(self):
        self.battery = 100
        print('충전이 완료되었습니다.')
        

# 자식 클래스 - DroneRobot, CleanRobot
# 상속 정의 : class 클래스명(부모클래스):

# 드론
class DroneRobot(Robot):
    # 부모 클래스의 변수와 메소드를 모두 재사용한다.
    # 단, 프라이빗 멤버는 상속되지 않음
    
    # 최대 높이
    max_height = 50
    
    # super() : 자식 클래스의 생성자에서 부모클래스의 생성자를 호출하는 메소드
    def __init__(self, name, power, battery, height):
        # self.name = name
        # self.power = power
        # self.battery = battery
        super().__init__(name, power, battery)
        self.height = height
        
        
    # 오버라이딩
    # : 부모 클래스의 메소드를 자식 클래스에서 재정의하는 것
    def move(self, direction, height):
        if height > DroneRobot.max_height:
            print('{}m 이상으로는 비행할 수 없습니다'.format(DroneRobot.max_height))
            return
            
        self.height = height
        print('고도 : {}'.format(height))
        print('{} (으/)로 방향으로 비행합니다.'.format(direction))
        
        
# 로봇 청소기
class CleanRobot(Robot):
    max_bin = 50
    
    # 생성자
    def __init__(self, name, power, battery, bin):
        super().__init__(name, power, battery)
        self.bin = bin
        
    # 메소드 오버라이딩
    def move(self, direction):
        print('{} 으(/로) 이동하여 청소합니다.'.format(direction))
        self.bin += 1            # 먼지 흡입
        
    def mapping(self):
        print('청소할 영역을 기억합니다.')
        
        
    # 먼지통 비우기
    def vacate(self):
        self.bin = 0
        print('먼지통을 비웁니다.')
        

# 객체 생성
print('# Robot #')
robot = Robot('휴먼로봇', 'ON', 100)
robot.move('왼쪽')      # 위쪽, 아래쪽, 왼쪽, 오른쪽
robot.charge()

print('# DroneRotbot #')
drone = DroneRobot('드론로봇', 'ON', 100, 10)
drone.move('앞쪽', 50)

print('# CleanRobot #')
cleanRobot = CleanRobot('로봇청소기', 'ON', 100, 0)
cleanRobot.mapping()
cleanRobot.move('앞쪽')
cleanRobot.vacate()