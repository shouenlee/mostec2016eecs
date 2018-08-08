import RPi.GPIO as GPIO
import pygame
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set up pins
inputs = [23,24,25,12]
#for each pin set it as an input!
for x in inputs:
    GPIO.setup(x,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#song list
songs = ['genghis_khan','shake_off','wash_side','queen_janelle','yes']
song_loc = '/home/pi/music/'
pygame.mixer.init()



current_song = 0 #used to count through songs!
play_pause_state = False #True is playing, #False is not playing

#create list...initialize with whatever values:
old_switch_states= [True,True,True,True]

#initialize switch state values!
for x in range(len(inputs)):
    #print(inputs[x])
    old_switch_states[x] = GPIO.input(inputs[x])

#preload a song, play it, immediately pause it!
pygame.mixer.music.load(song_loc+songs[current_song]+'.mp3')
pygame.mixer.music.play()
pygame.mixer.music.pause()

def unpause():
    global play_pause_state #global allows to change variable inside function
    play_pause_state = True
    #your code here

def pause():
    global play_pause_state
    play_pause_state = False

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
    #your code here

def volume(inc_dec):
    pass
    #your code here

def readInputs(new_readings,old_readings):
    change = []
    for x in range(len(inputs)):
        if old_readings[x]==True and new_readings[x] == False:
            change.append(True)
        else:
            change.append(False)
    if change[3]:
        return 'next_song'
    if change[2]:
        return 'pause_unpause'
    if change[0]:
        return 'volup'
    if change[1]:
        return 'voldown'

try:
    while True:
        new_switch_states = []
        for x in inputs:
            new_switch_states.append(GPIO.input(x))
        output = readInputs(new_switch_states,old_switch_states)
        old_switch_states=new_switch_states
        if output != None:
            print(output)
        if output == 'pause_unpause' and not play_pause_state:
            unpause()
        elif output == 'pause_unpause' and play_pause_state:
            pause()
        elif output == 'next_song':
            next_song()
        elif output == 'volup':
            volume(True)
        elif output == 'voldown':
            volume(False)
        time.sleep(0.1)
except KeyboardInterrupt:
    pygame.mixer.music.stop()
    GPIO.cleanup()
