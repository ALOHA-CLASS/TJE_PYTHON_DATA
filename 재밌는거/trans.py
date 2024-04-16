from googletrans import Translator
import os
# 현재 실행 파일 경로 가져오고, 입력파일 지정하기
program_path = os.path.abspath(__file__)
path = os.path.dirname(program_path)

def translate_text(input_file, output_file, source_lang='en', target_lang='ko'):
    # Googletrans Translator 객체 생성
    translator = Translator()

    # 입력 파일 열기
    with open(input_file, 'r', encoding='utf-8') as file:
        input_text = file.read()

    # 영어에서 한글로 번역
    translated_text = translator.translate(input_text, src=source_lang, dest=target_lang)

    # 번역 결과를 출력 파일에 쓰기
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text.text)

if __name__ == "__main__":
    input_file = path + '/' + input('입력 파일 : ')
    output_file = path + '/' + input('출력 파일 : ')

    # 번역 실행
    translate_text(input_file, output_file)

    print('번역이 완료되었습니다.')
