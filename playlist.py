import subprocess
import time

songinfo = {"ShakeItOff": 241,
			"UptownFunk": 270
			"Centuries": 231}
		
while True:
	path = "C:\Users\Allison\Documents\GitHub\ghai\songs.txt"
	content = []
	content = [line.strip() for line in open(path)
	
	playlist = content.reverse()
	
	for i in range(len(playlist)):
		script = "start C:\Users\Allison\Documents\GitHub\ghai\Songs\\" + playlist[i] + ".mp3"
		
		fo = open("C:\Users\Allison\Documents\GitHub\ghai\play.bat", 'w')
		fo.write(script)
		fo.close()
		
		filepath="C:/Users/Allison/Documents/GitHub/ghai/play.bat"
		p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

		stdout, stderr = p.communicate()
		print p.returncode
		
		with open(path, 'r') as fin:
			data = fin.read().splitlines(True)
		with open(path, 'w') as fout:
			fout.writelines(data[:-1])
					
		pause = songinfo[playlist[i]]
		time.sleep(pause)






