#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "test.ui"           # 파일명.ui 
RESOURCE_PATHS = [PROJECT_PATH]


class PyGUITestUI:
    def __init__(self, master=None):
        self.builder = pygubu.Builder()
        self.builder.add_resource_paths(RESOURCE_PATHS)
        self.builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow: tk.Toplevel = self.builder.get_object(
            "main_window", master)              # TopLevel id 지정
        self.builder.connect_callbacks(self)

    
    # 콜백 함수 정의
    def action_select(self):
        print("조회 버튼 클릭!")

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = PyGUITestUI()
    app.run()
