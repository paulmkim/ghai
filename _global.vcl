# Global voice commands
# ctrl+w = good if using notepad++
# alt+f4 = good if notepad++ not open

openSongFile() := RunProgram(notepad++) WaitForWindow(notepad++) {ctrl+o} Wait(300) 
                  " C:\Users\Alvin\Desktop\ghai\songs.txt" {enter};
closeSongFile() := Wait(200) {ctrl+s}{alt+f4};

play <_anything> = openSongFile() $1 ";" closeSongFile();
