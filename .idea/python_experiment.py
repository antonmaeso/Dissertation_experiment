from psychopy import visual, core, event
import pygame
import psychopy
from random import randint
#create a window
window = visual.Window(
        size=(1440, 900), fullscr=False, screen=0,
        allowGUI=False, allowStencil=False,
        monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
        blendMode='avg', useFBO=True)

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
trialClock = core.Clock()

# Setup the Window
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()
list_of_words = u"position heat seashore attack trucks doctor sugar purpose ducks authority distribution furniture dinner moon sofa morning change hydrant".split(' ')

list_of_sound = u"1.wav 1.wav 1.wav 1.wav 1.wav 1.wav 1.wav 1.wav 1.wav 1.wav".split(' ')
list_of_sound2 =u"sittin.wav sittin.wav sittin.wav sittin.wav sittin.wav sittin.wav sittin.wav sittin.wav sittin.wav sittin.wav sittin.wav sittin.wav sittin.wav".split(' ')
# draw the stimuli and update the window

def encoding_trial(list_of_sound, list_of_words, win , number_of_stimuli):
    text = visual.TextStim(win=window, name='text', font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                           color=u'white', colorSpace='rgb', opacity=1, depth=-1.0, text=list_of_words[0])
    sound = pygame.mixer.Sound(list_of_sound[0])
    number_of_stimuli += 1
    c_t = 0
    trialClock.reset()
    while True:  # this creates a never-ending loop
        if c_t == number_of_stimuli:
            sound.stop()
            win.flip()
            break
        text.draw(win)
        sound.play()
        win.flip()
        if trialClock.getTime() >= 2.0:
            c_t += 1
            trialClock.reset()
            sound.stop()
            sound = pygame.mixer.Sound(list_of_sound[c_t])
            text.setText(list_of_words[c_t])
        event.clearEvents()

def recall(win):
    text = visual.TextStim(win=window, name='text', font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                           color=u'white', colorSpace='rgb', opacity=1, depth=-1.0, text=list_of_words[0])
    current_stim = 0
    current_stim = play_sound(list_of_sound=list_of_sound2, current_stim=current_stim)

    continueRoutine = True
    inputText = ''
    char = ''
    while continueRoutine:
        try:
            char = event.getKeys()[0]
            print char
        except:
            pass

        text.setText(inputText)
        if len(char) == 1:
            inputText += char
            char = ''
        elif char == 'space':
            inputText += ' '
            char = ''
        elif char == 'escape':
            break
        elif char == 'backspace':
            inputText = inputText[:-1]
            char = ''
        elif char == 'return':
            # record final string
            number_of_stimuli = 4
            char = ''
            inputText = ''
            text.setText('')
            win.flip()
            if current_stim == number_of_stimuli:
                break
            else:
                current_stim = play_sound(list_of_sound=list_of_sound2, current_stim=current_stim)
        text.draw(win)
        win.flip()

def play_sound(list_of_sound, current_stim):
    sound = pygame.mixer.Sound(list_of_sound[current_stim])
    trialClock.reset()
    while True:
        sound.play()
        if trialClock.getTime() >= 2.0:
            sound.stop()
            return current_stim + 1

def pause(silence = 1.0):
    trialClock.reset()
    while trialClock.getTime() <= silence:
        pass


def distractor_task(win):

    text = visual.TextStim(win=window, name='text', font=u'Arial', pos=(0, -0.3), height=0.1, wrapWidth=None, ori=0,
                           color=u'white', colorSpace='rgb', opacity=1, depth=-1.0, text=list_of_words[0])
    question = visual.TextStim(win=window, name='text', font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                               color=u'white', colorSpace='rgb', opacity=1, depth=-1.0, text=list_of_words[0])
    current_stim = 0

    inputText = ''
    char = ''
    number_of_stimuli = 4
    while True:
        question.setText(str(randint(1, 100)) + ' + ' + str(randint(1, 100)))
        continueRoutine = True
        if current_stim == number_of_stimuli:
            text.setText('')
            text.draw(win)
            question.setText('')
            question.draw(win)
            win.flip()
            break
        current_stim = text_input(char, continueRoutine, current_stim, inputText, question, text, win)


def text_input(char, continueRoutine, current_stim, inputText, question, text, win):
    while continueRoutine:
        question.draw(win)
        try:
            char = event.getKeys()[0]
            print char
        except:
            pass
        text.setText(inputText)
        if len(char) == 1:
            inputText += char
            char = ''
        elif char == 'space':
            inputText += ' '
            char = ''
        elif char == 'escape':
            break
        elif char == 'backspace':
            inputText = inputText[:-1]
            char = ''
        elif char == 'return':
            current_stim = current_stim + 1
            char = ''
            inputText = ''
            continueRoutine = False
        text.draw(win)

        win.flip()
    return current_stim


def instructions(win, inst):
    instruction= visual.TextStim(win=window, name='text', font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                           color=u'white', colorSpace='rgb', opacity=1, depth=-1.0, text=list_of_words[0])
    char = ''
    while True:
        try:
            char = event.getKeys()[0]
            print char
        except:
            pass
        instruction.setText(inst + '\nPress enter to continue')
        instruction.draw(win)
        win.flip()
        if char == 'return':
            break
def retreival_two(win, words = ['one', 'two', 'three']):


    sound_box = {}
    for word in words:
        sound_box[word] =[psychopy.visual.ShapeStim(win, fillColorSpace='rgb',
                                  vertices=((0.1, 0.1), (-0.1, 0.1), (-0.1, -0.1), (0.1, -0.1)), pos=(0, .5)), list_of_sound2]

    clickable = visual.TextStim(win=window, name='text', font=u'Arial', pos=(0, .5), height=0.1, wrapWidth=None, ori=0,
                           color=u'white', colorSpace='rgb', opacity=1, depth=-1.0, text='firs word')

    poly = psychopy.visual.ShapeStim(win, fillColorSpace='rgb',vertices=((0.1, 0.1),(-0.1, 0.1),(-0.1, -0.1), (0.1, -0.1)), pos=(0, .5))

    text = visual.TextStim(win=window, name='text', font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                           color=u'white', colorSpace='rgb', opacity=1, depth=-1.0, text=list_of_words[0])


    continueRoutine = True
    inputText = ''
    char = ''
    m = event.Mouse(newPos=0, win=win)
    mouse_pos = []
    while continueRoutine:
        clickable.draw(win)
        poly.draw(win)
        if m.isPressedIn(poly):
            play_sound(list_of_sound=list_of_sound2, current_stim=0)


        if event.getKeys('space'):
            print m.getPos()

        # if m.getPos()[0] >= -0.11666667 and  m.getPos()[0] <= 0.11527778 and m.getPos()[1] <= 0.54444444 and m.getPos()[1] >= 0.45333333:
        #     play_sound(list_of_sound=list_of_sound2, current_stim=0)



        text.draw(win)
        win.flip()



def expreiment_flow():
    retreival_two(window)
    # print globalClock.getTime()
    # instructions(window, 'Thank you for participating in this study. Please follow the instructions to the best of your ability.')
    # instructions(window, 'You will a song and a word at the same time. Please remember as many of the words as possible.')
    # pause()
    # encoding_trial(list_of_sound2, list_of_words, window, 4)
    # print globalClock.getTime()
    # instructions(window, 'Please answer these additions as best you can.')
    # pause()
    # distractor_task(window)
    # instructions(window, 'Please give the word associated with the song.')
    # pause()
    # recall(window)
    # pause()
    # distractor_task(window)
    # print globalClock.getTime()
    # pause()
    # encoding_trial(list_of_sound, list_of_words, window, 4)
    # pause()
    # distractor_task(window)
    # pause()
    # recall(window)
    # pause()
    # print globalClock.getTime()

expreiment_flow()
window.close()
core.quit()