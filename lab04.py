import RPi.GPIO as GPIO
import pygame
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set up pins
inputs = [23,24,25,12]
for x in inputs:
    GPIO.setup(x,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#song list
songs = ['ham_title','genghis_khan','shake_off','wash_side','queen_janelle','yes','my_shot']
song_loc = '/home/pi/music/'
pygame.mixer.init()


TIMEOUT = 0.5 #how long you wait for the second click!

current_song = 0 #used to count through songs!
play_pause_state = False #True is playing, #False is not playing



#preload a song, play it, immediately pause it!
pygame.mixer.music.load(song_loc+songs[current_song]+'.mp3')
pygame.mixer.music.play()
pygame.mixer.music.pause()


#unpause, pause, and next_song cand be copy/pasted from your working lab03.py
def unpause():
    global play_pause_state #global allows to change variable inside function
    play_pause_state = True
    pygame.mixer.music.unpause()
    #your code here

def pause():
    global play_pause_state
    play_pause_state = False
    pygame.mixer.music.pause()
    #your code here (same from lab3)

def next_song():
    global current_song
    if current_song == len(songs)-1:
        current_song = 0
        pygame.mixer.music.load(song_loc+songs[current_song]+'.mp3')
        pygame.mixer.music.play()
    else:
        current_song += 1
        pygame.mixer.music.load(song_loc+songs[current_song]+'.mp3')
        pygame.mixer.music.play()
    #your code here (same from lab3)

def click_getter():
    if GPIO.input(25) == False:
        firstpress = time.time()
        time.sleep(.1)
        if GPIO.input(25) == True:
            time.sleep(.1)
            while time.time() - firstpress < TIMEOUT:
                if GPIO.input(25) == False:
                    while time.time() - firstpress < TIMEOUT:
                        if GPIO.input(25) == True:
                            return 2
                            time.sleep(.1)
                
                else:
                    return 1
            
    #your code here NEW CODE!
    if GPIO.input(12) == False:
        two = time.time()
        while time.time() - two < TIMEOUT:
            if GPIO.input(12) == True:
                pass
        return 5
    

try:
    while True:
        output = click_getter()
        if output != None:
            print(output) #do nothing
        if output == 1 and not play_pause_state:
            unpause()
        elif output == 1 and play_pause_state:
            pause()
        elif output == 2:
            next_song()
except KeyboardInterrupt:
    pygame.mixer.music.stop()
    GPIO.cleanup()
