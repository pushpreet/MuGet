import sys
import re
import shutil
import os

if  len(sys.argv) != 2:
    sys.exit("ERROR : No file specified")

playlistName = sys.argv[1]

if not playlistName.endswith(('.wpl', '.zpl')):
    sys.exit("ERROR : Wrong file specified")

if not os.path.isfile(playlistName):
    sys.exit("ERROR : File not found")

playlistFile =  open(playlistName, "r")

playlistName = playlistName.replace('.wpl', '')
playlistName = playlistName.replace('.zpl', '')

print("Playlist Name :", playlistName)

for line in playlistFile.readlines():
    m = re.compile('src="(.*?)"', re.DOTALL).findall(line)
    if m:
        if not os.path.exists(playlistName):
            os.makedirs(playlistName)
        
        try:
            shutil.copy(m[0], playlistName)
        except EnvironmentError:
            continue
        else:
            print('Copied ' + m[0])

playlistFile.close()