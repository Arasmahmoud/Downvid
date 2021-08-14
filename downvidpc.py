import os
os.system ("clear")

from pytube import YouTube

print ('\033[1;31m _   _    _     _   _   _       ')
print ('\033[1;31m| | / /  | |   / / | | | |      ')
print ('\033[1;31m| |/ /   | |  / /  | |_| |      ')
print ('\033[1;31m| |\ \   | | / /   \___  |      ')
print ('\033[1;31m| | \ \  | |/ /        | |      ')
print ('\033[1;31m|_|  \_\ |___/         |_| KV4 ')      
print ('      ') 
print ('Website ==> aras21.tk') 
print ('Instagram ==> almcompany6') 
print ('Linkedin ==> almcompany') 
print ('Udemy ==> Arasmahmoud\033[1;37m .')
print ('               ') 

link = input ("link vîdeo  ji bo em daxin ? ")

yt = YouTube(link)

videos = yt.streams.all()

i = 1

for stream in videos:
    print (str(i) + " - " + str (stream))
    i += 1

stream_number = int (input ("jimarkê helbjêra jibo daxstinê>>> "))


video = videos [stream_number - 1]

video.download ("downvid")

print ('           ') 
print ("\033[1;31m¡¡¡¡  ^_^ [+] video te daket serxêrebe [+] ^_^ ¡¡¡¡")


print ('\033[1;31m _   _    _     _   _   _       ')
print ('\033[1;31m| | / /  | |   / / | | | |      ')
print ('\033[1;31m| |/ /   | |  / /  | |_| |      ')
print ('\033[1;31m| |\ \   | | / /   \___  |      ')
print ('\033[1;31m| | \ \  | |/ /        | |      ')
print ('\033[1;31m|_|  \_\ |___/         |_| KV4\033[1;37m. ')      


print ('     ') 



print ('     ') 


