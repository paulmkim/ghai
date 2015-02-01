import subprocess
import time

def invalidSong(song):
	if content[i] != "shakeitoff" and content[i] != "uptownfunk" and content[i] != "centuries":
		return True
	
songinfo = {"shakeitoff": 241,
			"uptownfunk": 270,
			"centuries": 231}
		
while True:
	path = "C:\Users\Paul\Desktop\ghai\songs.txt"
	
	#content = [line.strip() for line in open(path)]
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
		#print content[i]
		
	#playlist = []
	#for i in range(len(content)):
	#	playlist.append(content[len(content) - i -1])
	
	for i in range(len(content)):
		if invalidSong(content[i]):
			continue
			
		script = "start C:\Users\Paul\Desktop\ghai\SongsToPlay\\" + content[i] + ".mp3"
		
		fo = open("C:\Users\Paul\Desktop\ghai\play.bat", 'w')
		fo.write(script)
		fo.close()
		
		filepath="C:/Users/Paul/Desktop/ghai/play.bat"
		p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

		stdout, stderr = p.communicate()
		print p.returncode
		
		"""with open(path, 'r') as fin:
			data = fin.read().splitlines(True)
		with open(path, 'w') as fout:
			fout.writelines(data[:-1])
		"""			
		pause = songinfo[content[i]]
		time.sleep(10)






