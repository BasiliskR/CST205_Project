__author__ = 'alexandre'

import sdl2
import audioread
import OpenGL
import tkinter.filedialog

def main():

    filepath = tkinter.filedialog.askopenfile(mode="r").name
    print("Filepath = " , filepath)
    audiofile = audioread.audio_open(filepath)
    print("Lenght = " ,  audiofile.duration)


main()


