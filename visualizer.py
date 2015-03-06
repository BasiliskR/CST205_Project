__author__ = 'alexandre'

import audioread
import OpenGL

def main():
    filepath = "test.wav"
    audioFile = audioread.audio_open(filepath)

