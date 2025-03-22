import os
import subprocess

def ffmp_get(path):
    os.environ["PATH"] =  f'{path};' + os.environ["PATH"]
    subprocess.run(["ffmpeg", "-version"])
