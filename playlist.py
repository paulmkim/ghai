import subprocess

songinfo = {"Happy": 234,
			"UptownFunk": 270}
		
while True:
	path = "C:\Users\Allison\Documents\GitHub\ghai\songs.txt"
	content = []
	content = [line.strip() for line in open(path)]


	for i in range(len(content)):
		filepath="C:/Users/Allison/Documents/GitHub/ghai/" + content[i] + ".bat"
		p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

		stdout, stderr = p.communicate()
		print p.returncode

		pause = songinfo[content[i]]
		time.sleep(pause)

		
