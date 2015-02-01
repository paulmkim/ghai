import subprocess

# assume we already have database of emotion

# if happy, will play upbeat, happy songs (fuck yeah! songs)
# if sad, either play slow, "sad" songs OR can play pick-me-up song
# if angry, either play "anger" song
# if calm = relaxed/normal state, play not sad song
# if nervous, play pumped-up songs OR relaxed music 

# 0 = low or negative, 1 = high or positive
# 0 = low&negative, 1 (01) = low&positive, 2 (10) = high&negative, 3 (11) = high&positive

intputText = "Happy"
playGenre = False
#satisfied = False
while True:
	
	filepath = "C:Users/Allison/Documents/GitHub/baemax/PlayingSong/" + inputText + ".bat"
	p=subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
	
	stdout, stderr = p.communicate()
	print p.returncode
	
	
	
	"""
		#sadfilepath="C:/Users/Allison/Documents/GitHub/baemax/PlayingSong/SadIntro.bat"
		sadfilepath="C:/Users/Paul/Desktop/baemax/PlayingSong/SadIntro.bat"
		o = subprocess.Popen(sadfilepath, shell=True, stdout = subprocess.PIPE)
		
		stdout, stderr = o.communicate()
		print o.returncode
		
		#filepath="path of the batch file"
		#filepath="C:/Users/Allison/Documents/GitHub/baemax/PlayingSong/SadSongs.bat"
		filepath="C:/Users/Paul/Desktop/baemax/PlayingSong/SadSongs.bat"
		p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

		stdout, stderr = p.communicate()
		print p.returncode 
		# 0 if success

	elif emotion == 1:
		
		#almfilepath="C:/Users/Allison/Documents/GitHub/baemax/PlayingSong/CalmIntro.bat"
		calmfilepath="C:/Users/Paul/Desktop/baemax/PlayingSong/CalmIntro.bat"
		o = subprocess.Popen(calmfilepath, shell=True, stdout = subprocess.PIPE)
		
		stdout, stderr = o.communicate()
		print o.returncode
		
		#filepath="C:/Users/Allison/Documents/GitHub/baemax/PlayingSong/CalmSongs.bat"
		filepath="C:/Users/Paul/Desktop/baemax/PlayingSong/CalmSongs.bat"
		p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

		stdout, stderr = p.communicate()
		print p.returncode 
		# 0 if success

	elif emotion == 2:
		
		#angryfilepath="C:/Users/Allison/Documents/GitHub/baemax/PlayingSong/AngryIntro.bat"
		angryfilepath="C:/Users/Paul/Desktop/baemax/PlayingSong/AngryIntro.bat"
		o = subprocess.Popen(angryfilepath, shell=True, stdout = subprocess.PIPE)
		
		stdout, stderr = o.communicate()
		print o.returncode
		
		#filepath="C:/Users/Allison/Documents/GitHub/baemax/PlayingSong/AngrySongs.bat"
		filepath="C:/Users/Paul/Desktop/baemax/PlayingSong/AngrySongs.bat"
		p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

		stdout, stderr = p.communicate()
		print p.returncode 
		# 0 if success
		
	elif emotion == 3:
		#happyfilepath="C:/Users/Allison/Documents/GitHub/baemax/PlayingSong/HappyIntro.bat"
		happyfilepath="C:/Users/Paul/Desktop/baemax/PlayingSong/HappyIntro.bat"
		o = subprocess.Popen(happyfilepath, shell=True, stdout = subprocess.PIPE)
		
		stdout, stderr = o.communicate()
		print o.returncode
	
	
		#filepath="C:/Users/Allison/Documents/GitHub/baemax/PlayingSong/HappySongs.bat"
		filepath="C:/Users/Paul/Desktop/baemax/PlayingSong/HappySongs.bat"
		p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

		stdout, stderr = p.communicate()
		print p.returncode 
			# 0 if success
		
	#newfilepath="C:/Users/Allison/Documents/GitHub/baemax/PlayingSong/satisfiedWithCare.bat"	
	newfilepath="C:/Users/Paul/Desktop/baemax/PlayingSong/satisfiedWithCare.bat"
	p = subprocess.Popen(newfilepath, shell=True, stdout = subprocess.PIPE)

	stdout, stderr = p.communicate()
	print p.returncode
	
	user_response = raw_input("Would you like to hear another song? ")
	response = user_response.lower()
	library = ["no thanks", "i don't want to", "not really", "nah", "no", "i hate you"]
	for word in library:
		if response == word:
			satisfied = True
			break
		
	if emotion != 3:
		emotion += 1
	else:
		emotion = 0"""
	
	