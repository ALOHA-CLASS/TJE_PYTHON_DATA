# 텍스트를 음성으로 변환하는 라이브러리
# gtts
# TTS : Text To Speach
# STT : Speach To Text
# pip install gtts
from gtts import gTTS
import os

# 텍스트를 음성으로 변환
text = "집에 갈 시간입니다. 파이썬 엑셀 데이터 분석 시간입니다."
tts = gTTS(text=text, lang='ko')

# 음성mp3 파일 저장
tts.save('test.mp3')

# mp3 재생
os.system("test.mp3")


