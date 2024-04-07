import os



# 실행 프로그램의 경로
program_path = os.path.abspath(__file__)
# 프로그램의 디렉터리
program_directory = os.path.dirname(program_path)
# \\ -> / 변환
path = program_directory.replace("\\", "/")


print("현재 작업 디렉토리의 경로:", program_directory)
print("현재 작업 디렉토리의 경로:", program_path)
print("현재 작업 디렉토리의 경로:", path)
