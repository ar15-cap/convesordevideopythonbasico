from os import *

def main():
	print("Starting...")
	char1 = input("digite o nome do arquivo")
	char2 = input("digite o formato do arquivo")
	if char2 == "mp3":
		system("ffmpeg -i {0} {0}.mp3".format(char1))
	if char2 == "mp4":
		system("ffmpeg -i {0} {0}.mp4".format(char1))
	if char2 == "mkv":
		system("ffmpeg -i {0} {0}.mkv".format(char1))
	if char2 == "avi":
		system("ffmpeg -i {0} {0}.avi".format(char1))

main()