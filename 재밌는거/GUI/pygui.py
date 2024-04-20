#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from pyguiui import PyGUITestUI


class PyGUITest(PyGUITestUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = PyGUITest()
    app.run()
