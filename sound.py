import subprocess

from subprocess import Popen

#Is used to generate the music
def play(sound_path,meth=0):
    return Popen(["aplay","-q",sound_path])

#Kills the subprocess
def kill(process):
    process.kill()

