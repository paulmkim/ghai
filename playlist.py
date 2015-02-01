import subprocess
import time

def invalidSong(song):
    if song in songinfo.keys():
        return False
    else:
        return True

songinfo = {"shakeitoff": 241,
            "uptownfunk": 270,
            "centuries": 231,
            "Iseethelight": 241,
            "happy": 234}

while True:
    path = "C:\Users\Alvin\Desktop\ghai\songs.txt"

    songString=""
    with open (path, "r") as myfile:
        songString=myfile.read()
    open(path, 'w').close()
    content = []
    buffer = ""
    for i in range(len(songString)):
        if songString[i] != ';':
            buffer = buffer + songString[i]
        else:
            content.append(buffer)
            buffer = ""

    for i in range(len(content)):
        content[i] = content[i].replace(" ", "")

    for i in range(len(content)):
        if invalidSong(content[i]):
            continue

        script = "start C:\Users\Alvin\Desktop\ghai\SongsToPlay\\" + content[i] + ".mp3"

        fo = open("C:\Users\Alvin\Desktop\ghai\play.bat", 'w')
        fo.write(script)
        fo.close()

        filepath="C:/Users/Alvin/Desktop/ghai/play.bat"
        p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

        stdout, stderr = p.communicate()
        print p.returncode

        pause = songinfo[content[i]]
        time.sleep(pause)
