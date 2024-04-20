# 설치
# pip install tk
# pip install pygubu
# 디자이너 시작
# --> pygubu-designer
# gui_gubu.py
import tkinter as tk
import pygubu


class PyGuiTest:
    
    def __init__(self):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('layout.ui')

        #3: Create the mainwindow
        self.mainwindow = builder.get_object('main_window')
        
    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = PyGuiTest()
    app.run()