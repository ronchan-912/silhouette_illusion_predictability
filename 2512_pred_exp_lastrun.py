#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on 月  1/ 5 18:14:38 2026
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.1.4')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = '2512_pred_exp'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/rondenkouhei/study_multiperception/psychopy/experiment_github_pages/2512_pred_exp_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1710, 1112], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='smallMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='event')

# Initialize components for Routine "introduction1"
introduction1Clock = core.Clock()
key_resp_instruction_2 = keyboard.Keyboard()
img_inst1 = visual.ImageStim(
    win=win,
    name='img_inst1', units='pix', 
    image='png/inst1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1000, 528),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "mihon"
mihonClock = core.Clock()
movie = visual.MovieStim3(
    win=win, name='movie', units='pix',
    noAudio = False,
    filename='mp4/catch_demo.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    size=(1420, 800),
    depth=0.0,
    )
key_resp_mihon = keyboard.Keyboard()
finish_judge_2 = keyboard.Keyboard()
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='pix', 
    size=(25, 25),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -0.2235, -0.4431], fillColor=[1.0000, -0.2235, -0.4431],
    opacity=None, depth=-3.0, interpolate=True)

# Initialize components for Routine "introduction2"
introduction2Clock = core.Clock()
key_resp_instruction = keyboard.Keyboard()
img_inst2 = visual.ImageStim(
    win=win,
    name='img_inst2', units='pix', 
    image='png/inst2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1000, 528),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "demo"
demoClock = core.Clock()
finish_judge = keyboard.Keyboard()
key_resp_demo = keyboard.Keyboard()
key_resp_selection = keyboard.Keyboard()
# Set experiment start values for variable component opa_cw
opa_cw = 1.0
opa_cwContainer = []
# Set experiment start values for variable component opa_ccw
opa_ccw = 1.0
opa_ccwContainer = []
mov = visual.MovieStim3(
    win=win, name='mov', units='pix',
    noAudio = False,
    filename='mp4/demo/taisoufuku_demo_120sec.mp4',
    ori=0.0, pos=(0, 0), opacity=1.0,
    loop=True, anchor='center',
    size=(1450, 870),
    depth=-5.0,
    )
polygon_6 = visual.ShapeStim(
    win=win, name='polygon_6', vertices='cross',units='pix', 
    size=(25, 25),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -0.2235, -0.4431], fillColor=[1.0000, -0.2235, -0.4431],
    opacity=None, depth=-6.0, interpolate=True)
mask_cw = visual.ImageStim(
    win=win,
    name='mask_cw', units='pix', 
    image='png/mask_l.png', mask=None, anchor='center',
    ori=0.0, pos=(-480, 0), size=(480, 800),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
mask_ccw = visual.ImageStim(
    win=win,
    name='mask_ccw', units='pix', 
    image='png/mask_r.png', mask=None, anchor='center',
    ori=0.0, pos=(480, 0), size=(480, 800),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)

# Initialize components for Routine "introduction3"
introduction3Clock = core.Clock()
img_inst3 = visual.ImageStim(
    win=win,
    name='img_inst3', units='pix', 
    image='png/inst3.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1000, 687),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_instruction_3 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
key_resp = keyboard.Keyboard()
trialCounter = 0
strCounter = str(trialCounter)
nRestTrial = 6
finish_judge_3 = keyboard.Keyboard()
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',units='pix', 
    size=(25, 25),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -0.2235, -0.4431], fillColor=[1.0000, -0.2235, -0.4431],
    opacity=None, depth=-4.0, interpolate=True)

# Initialize components for Routine "breakt"
breaktClock = core.Clock()
key_resp_breaktime_2 = keyboard.Keyboard()
finish_judge_4 = keyboard.Keyboard()
polygon = visual.Rect(
    win=win, name='polygon',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.8824, 0.8039, 0.0980], fillColor=[0.8824, 0.8039, 0.0980],
    opacity=None, depth=-2.0, interpolate=True)
img_inst4 = visual.ImageStim(
    win=win,
    name='img_inst4', units='pix', 
    image='png/inst4.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1000, 352),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
text_shintyoku = visual.TextStim(win=win, name='text_shintyoku',
    text='',
    font='Open Sans',
    units='norm', pos=(0.9, 0.9), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "catch_trial"
catch_trialClock = core.Clock()
key_resp_catch = keyboard.Keyboard()
fixation_catch = visual.ShapeStim(
    win=win, name='fixation_catch', vertices='cross',units='pix', 
    size=(25, 25),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -0.2235, -0.4431], fillColor=[1.0000, -0.2235, -0.4431],
    opacity=None, depth=-2.0, interpolate=True)

# Initialize components for Routine "breakt"
breaktClock = core.Clock()
key_resp_breaktime_2 = keyboard.Keyboard()
finish_judge_4 = keyboard.Keyboard()
polygon = visual.Rect(
    win=win, name='polygon',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.8824, 0.8039, 0.0980], fillColor=[0.8824, 0.8039, 0.0980],
    opacity=None, depth=-2.0, interpolate=True)
img_inst4 = visual.ImageStim(
    win=win,
    name='img_inst4', units='pix', 
    image='png/inst4.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1000, 352),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
text_shintyoku = visual.TextStim(win=win, name='text_shintyoku',
    text='',
    font='Open Sans',
    units='norm', pos=(0.9, 0.9), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
key_resp = keyboard.Keyboard()
trialCounter = 0
strCounter = str(trialCounter)
nRestTrial = 6
finish_judge_3 = keyboard.Keyboard()
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',units='pix', 
    size=(25, 25),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -0.2235, -0.4431], fillColor=[1.0000, -0.2235, -0.4431],
    opacity=None, depth=-4.0, interpolate=True)

# Initialize components for Routine "breakt"
breaktClock = core.Clock()
key_resp_breaktime_2 = keyboard.Keyboard()
finish_judge_4 = keyboard.Keyboard()
polygon = visual.Rect(
    win=win, name='polygon',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.8824, 0.8039, 0.0980], fillColor=[0.8824, 0.8039, 0.0980],
    opacity=None, depth=-2.0, interpolate=True)
img_inst4 = visual.ImageStim(
    win=win,
    name='img_inst4', units='pix', 
    image='png/inst4.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1000, 352),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
text_shintyoku = visual.TextStim(win=win, name='text_shintyoku',
    text='',
    font='Open Sans',
    units='norm', pos=(0.9, 0.9), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "outro"
outroClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thank you.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_instruction_2.keys = []
key_resp_instruction_2.rt = []
_key_resp_instruction_2_allKeys = []
# keep track of which components have finished
introduction1Components = [key_resp_instruction_2, img_inst1]
for thisComponent in introduction1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction1"-------
while continueRoutine:
    # get current time
    t = introduction1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_instruction_2* updates
    waitOnFlip = False
    if key_resp_instruction_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instruction_2.frameNStart = frameN  # exact frame index
        key_resp_instruction_2.tStart = t  # local t and not account for scr refresh
        key_resp_instruction_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instruction_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_instruction_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instruction_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instruction_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instruction_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instruction_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_instruction_2_allKeys.extend(theseKeys)
        if len(_key_resp_instruction_2_allKeys):
            key_resp_instruction_2.keys = _key_resp_instruction_2_allKeys[-1].name  # just the last key pressed
            key_resp_instruction_2.rt = _key_resp_instruction_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *img_inst1* updates
    if img_inst1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        img_inst1.frameNStart = frameN  # exact frame index
        img_inst1.tStart = t  # local t and not account for scr refresh
        img_inst1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(img_inst1, 'tStartRefresh')  # time at next scr refresh
        img_inst1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction1"-------
for thisComponent in introduction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "mihon"-------
continueRoutine = True
routineTimer.add(60.000000)
# update component parameters for each repeat
key_resp_mihon.keys = []
key_resp_mihon.rt = []
_key_resp_mihon_allKeys = []
finish_judge_2.keys = []
finish_judge_2.rt = []
_finish_judge_2_allKeys = []
# keep track of which components have finished
mihonComponents = [movie, key_resp_mihon, finish_judge_2, fixation_2]
for thisComponent in mihonComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
mihonClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "mihon"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = mihonClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=mihonClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie* updates
    if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie.frameNStart = frameN  # exact frame index
        movie.tStart = t  # local t and not account for scr refresh
        movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
        movie.setAutoDraw(True)
    if movie.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > movie.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            movie.tStop = t  # not accounting for scr refresh
            movie.frameNStop = frameN  # exact frame index
            win.timeOnFlip(movie, 'tStopRefresh')  # time at next scr refresh
            movie.setAutoDraw(False)
    
    # *key_resp_mihon* updates
    waitOnFlip = False
    if key_resp_mihon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_mihon.frameNStart = frameN  # exact frame index
        key_resp_mihon.tStart = t  # local t and not account for scr refresh
        key_resp_mihon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_mihon, 'tStartRefresh')  # time at next scr refresh
        key_resp_mihon.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_mihon.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_mihon.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_mihon.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_mihon.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_mihon.tStop = t  # not accounting for scr refresh
            key_resp_mihon.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_mihon, 'tStopRefresh')  # time at next scr refresh
            key_resp_mihon.status = FINISHED
    if key_resp_mihon.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_mihon.getKeys(keyList=['f', 'j', 'space'], waitRelease=False)
        _key_resp_mihon_allKeys.extend(theseKeys)
        if len(_key_resp_mihon_allKeys):
            key_resp_mihon.keys = [key.name for key in _key_resp_mihon_allKeys]  # storing all keys
            key_resp_mihon.rt = [key.rt for key in _key_resp_mihon_allKeys]
    
    # *finish_judge_2* updates
    waitOnFlip = False
    if finish_judge_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finish_judge_2.frameNStart = frameN  # exact frame index
        finish_judge_2.tStart = t  # local t and not account for scr refresh
        finish_judge_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish_judge_2, 'tStartRefresh')  # time at next scr refresh
        finish_judge_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(finish_judge_2.clock.reset)  # t=0 on next screen flip
    if finish_judge_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finish_judge_2.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            finish_judge_2.tStop = t  # not accounting for scr refresh
            finish_judge_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finish_judge_2, 'tStopRefresh')  # time at next scr refresh
            finish_judge_2.status = FINISHED
    if finish_judge_2.status == STARTED and not waitOnFlip:
        theseKeys = finish_judge_2.getKeys(keyList=['q'], waitRelease=False)
        _finish_judge_2_allKeys.extend(theseKeys)
        if len(_finish_judge_2_allKeys):
            finish_judge_2.keys = _finish_judge_2_allKeys[-1].name  # just the last key pressed
            finish_judge_2.rt = _finish_judge_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mihonComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mihon"-------
for thisComponent in mihonComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
movie.stop()
# check responses
if key_resp_mihon.keys in ['', [], None]:  # No response was made
    key_resp_mihon.keys = None
thisExp.addData('key_resp_mihon.keys',key_resp_mihon.keys)
if key_resp_mihon.keys != None:  # we had a response
    thisExp.addData('key_resp_mihon.rt', key_resp_mihon.rt)
thisExp.addData('key_resp_mihon.started', key_resp_mihon.tStartRefresh)
thisExp.addData('key_resp_mihon.stopped', key_resp_mihon.tStopRefresh)
thisExp.nextEntry()
# check responses
if finish_judge_2.keys in ['', [], None]:  # No response was made
    finish_judge_2.keys = None
thisExp.addData('finish_judge_2.keys',finish_judge_2.keys)
if finish_judge_2.keys != None:  # we had a response
    thisExp.addData('finish_judge_2.rt', finish_judge_2.rt)
thisExp.nextEntry()
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)

# ------Prepare to start Routine "introduction2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_instruction.keys = []
key_resp_instruction.rt = []
_key_resp_instruction_allKeys = []
# keep track of which components have finished
introduction2Components = [key_resp_instruction, img_inst2]
for thisComponent in introduction2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction2"-------
while continueRoutine:
    # get current time
    t = introduction2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_instruction* updates
    waitOnFlip = False
    if key_resp_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instruction.frameNStart = frameN  # exact frame index
        key_resp_instruction.tStart = t  # local t and not account for scr refresh
        key_resp_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instruction, 'tStartRefresh')  # time at next scr refresh
        key_resp_instruction.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instruction.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instruction.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instruction.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instruction.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_instruction_allKeys.extend(theseKeys)
        if len(_key_resp_instruction_allKeys):
            key_resp_instruction.keys = _key_resp_instruction_allKeys[-1].name  # just the last key pressed
            key_resp_instruction.rt = _key_resp_instruction_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *img_inst2* updates
    if img_inst2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        img_inst2.frameNStart = frameN  # exact frame index
        img_inst2.tStart = t  # local t and not account for scr refresh
        img_inst2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(img_inst2, 'tStartRefresh')  # time at next scr refresh
        img_inst2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction2"-------
for thisComponent in introduction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo"-------
continueRoutine = True
routineTimer.add(120.000000)
# update component parameters for each repeat
finish_judge.keys = []
finish_judge.rt = []
_finish_judge_allKeys = []
key_resp_demo.keys = []
key_resp_demo.rt = []
_key_resp_demo_allKeys = []
key_resp_selection.keys = []
key_resp_selection.rt = []
_key_resp_selection_allKeys = []
opa_cw = 0  # Set routine start values for opa_cw
opa_ccw = 1.0  # Set routine start values for opa_ccw
# keep track of which components have finished
demoComponents = [finish_judge, key_resp_demo, key_resp_selection, mov, polygon_6, mask_cw, mask_ccw]
for thisComponent in demoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demo"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finish_judge* updates
    waitOnFlip = False
    if finish_judge.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finish_judge.frameNStart = frameN  # exact frame index
        finish_judge.tStart = t  # local t and not account for scr refresh
        finish_judge.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish_judge, 'tStartRefresh')  # time at next scr refresh
        finish_judge.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(finish_judge.clock.reset)  # t=0 on next screen flip
    if finish_judge.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finish_judge.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            finish_judge.tStop = t  # not accounting for scr refresh
            finish_judge.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finish_judge, 'tStopRefresh')  # time at next scr refresh
            finish_judge.status = FINISHED
    if finish_judge.status == STARTED and not waitOnFlip:
        theseKeys = finish_judge.getKeys(keyList=['q'], waitRelease=False)
        _finish_judge_allKeys.extend(theseKeys)
        if len(_finish_judge_allKeys):
            finish_judge.keys = _finish_judge_allKeys[-1].name  # just the last key pressed
            finish_judge.rt = _finish_judge_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *key_resp_demo* updates
    waitOnFlip = False
    if key_resp_demo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_demo.frameNStart = frameN  # exact frame index
        key_resp_demo.tStart = t  # local t and not account for scr refresh
        key_resp_demo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_demo, 'tStartRefresh')  # time at next scr refresh
        key_resp_demo.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_demo.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_demo.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_demo.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_demo.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_demo.tStop = t  # not accounting for scr refresh
            key_resp_demo.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_demo, 'tStopRefresh')  # time at next scr refresh
            key_resp_demo.status = FINISHED
    if key_resp_demo.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_demo.getKeys(keyList=['f', 'j', 'space'], waitRelease=False)
        _key_resp_demo_allKeys.extend(theseKeys)
        if len(_key_resp_demo_allKeys):
            key_resp_demo.keys = [key.name for key in _key_resp_demo_allKeys]  # storing all keys
            key_resp_demo.rt = [key.rt for key in _key_resp_demo_allKeys]
    
    # *key_resp_selection* updates
    waitOnFlip = False
    if key_resp_selection.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_selection.frameNStart = frameN  # exact frame index
        key_resp_selection.tStart = t  # local t and not account for scr refresh
        key_resp_selection.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_selection, 'tStartRefresh')  # time at next scr refresh
        key_resp_selection.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_selection.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_selection.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_selection.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_selection.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_selection.tStop = t  # not accounting for scr refresh
            key_resp_selection.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_selection, 'tStopRefresh')  # time at next scr refresh
            key_resp_selection.status = FINISHED
    if key_resp_selection.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_selection.getKeys(keyList=['l','r','b'], waitRelease=False)
        _key_resp_selection_allKeys.extend(theseKeys)
        if len(_key_resp_selection_allKeys):
            key_resp_selection.keys = _key_resp_selection_allKeys[-1].name  # just the last key pressed
            key_resp_selection.rt = _key_resp_selection_allKeys[-1].rt
    
    # *mov* updates
    if mov.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mov.frameNStart = frameN  # exact frame index
        mov.tStart = t  # local t and not account for scr refresh
        mov.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mov, 'tStartRefresh')  # time at next scr refresh
        mov.setAutoDraw(True)
    if mov.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mov.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            mov.tStop = t  # not accounting for scr refresh
            mov.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mov, 'tStopRefresh')  # time at next scr refresh
            mov.setAutoDraw(False)
    if mov.status == STARTED:  # only update if being drawn
        mov.setOpacity(1.0, log=False)
    
    # *polygon_6* updates
    if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_6.frameNStart = frameN  # exact frame index
        polygon_6.tStart = t  # local t and not account for scr refresh
        polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
        polygon_6.setAutoDraw(True)
    if polygon_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_6.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            polygon_6.tStop = t  # not accounting for scr refresh
            polygon_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_6, 'tStopRefresh')  # time at next scr refresh
            polygon_6.setAutoDraw(False)
    val = key_resp_selection.keys
    
    # opacity 0 means movie appearing
    # opacity 1 means movie disappearing
    if val == 'l':
        opa_cw = 0.0
        opa_ccw = 1.0
    elif val == 'r':
        opa_cw = 1.0
        opa_ccw = 0.0
    else:
        opa_cw = 1.0
        opa_ccw = 1.0
    
    
    # *mask_cw* updates
    if mask_cw.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mask_cw.frameNStart = frameN  # exact frame index
        mask_cw.tStart = t  # local t and not account for scr refresh
        mask_cw.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mask_cw, 'tStartRefresh')  # time at next scr refresh
        mask_cw.setAutoDraw(True)
    if mask_cw.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mask_cw.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            mask_cw.tStop = t  # not accounting for scr refresh
            mask_cw.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mask_cw, 'tStopRefresh')  # time at next scr refresh
            mask_cw.setAutoDraw(False)
    if mask_cw.status == STARTED:  # only update if drawing
        mask_cw.setOpacity(opa_cw, log=False)
    
    # *mask_ccw* updates
    if mask_ccw.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mask_ccw.frameNStart = frameN  # exact frame index
        mask_ccw.tStart = t  # local t and not account for scr refresh
        mask_ccw.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mask_ccw, 'tStartRefresh')  # time at next scr refresh
        mask_ccw.setAutoDraw(True)
    if mask_ccw.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mask_ccw.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            mask_ccw.tStop = t  # not accounting for scr refresh
            mask_ccw.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mask_ccw, 'tStopRefresh')  # time at next scr refresh
            mask_ccw.setAutoDraw(False)
    if mask_ccw.status == STARTED:  # only update if drawing
        mask_ccw.setOpacity(opa_ccw, log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo"-------
for thisComponent in demoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if finish_judge.keys in ['', [], None]:  # No response was made
    finish_judge.keys = None
thisExp.addData('finish_judge.keys',finish_judge.keys)
if finish_judge.keys != None:  # we had a response
    thisExp.addData('finish_judge.rt', finish_judge.rt)
thisExp.nextEntry()
# check responses
if key_resp_demo.keys in ['', [], None]:  # No response was made
    key_resp_demo.keys = None
thisExp.addData('key_resp_demo.keys',key_resp_demo.keys)
if key_resp_demo.keys != None:  # we had a response
    thisExp.addData('key_resp_demo.rt', key_resp_demo.rt)
thisExp.addData('key_resp_demo.started', key_resp_demo.tStartRefresh)
thisExp.addData('key_resp_demo.stopped', key_resp_demo.tStopRefresh)
thisExp.nextEntry()
mov.stop()

# ------Prepare to start Routine "introduction3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_instruction_3.keys = []
key_resp_instruction_3.rt = []
_key_resp_instruction_3_allKeys = []
# keep track of which components have finished
introduction3Components = [img_inst3, key_resp_instruction_3]
for thisComponent in introduction3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction3"-------
while continueRoutine:
    # get current time
    t = introduction3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *img_inst3* updates
    if img_inst3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        img_inst3.frameNStart = frameN  # exact frame index
        img_inst3.tStart = t  # local t and not account for scr refresh
        img_inst3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(img_inst3, 'tStartRefresh')  # time at next scr refresh
        img_inst3.setAutoDraw(True)
    
    # *key_resp_instruction_3* updates
    waitOnFlip = False
    if key_resp_instruction_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instruction_3.frameNStart = frameN  # exact frame index
        key_resp_instruction_3.tStart = t  # local t and not account for scr refresh
        key_resp_instruction_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instruction_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_instruction_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instruction_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instruction_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instruction_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instruction_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_instruction_3_allKeys.extend(theseKeys)
        if len(_key_resp_instruction_3_allKeys):
            key_resp_instruction_3.keys = _key_resp_instruction_3_allKeys[-1].name  # just the last key pressed
            key_resp_instruction_3.rt = _key_resp_instruction_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction3"-------
for thisComponent in introduction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_exp2512.xlsx'),
    seed=sum([ord(c) for c in expInfo['participant']]) + 100, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    mov00 = visual.MovieStim3(
        win=win, name='mov00', units='pix',
        noAudio = False,
        filename=movItems,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=True, anchor='center',
        size=(1120, 896),
        depth=-1.0,
        )
    trialCounter = trialCounter + 1
    
    if trialCounter % nRestTrial == 0:
        isRest = 0
    else:
        isRest = 1
    
    finish_judge_3.keys = []
    finish_judge_3.rt = []
    _finish_judge_3_allKeys = []
    # keep track of which components have finished
    trialComponents = [key_resp, mov00, finish_judge_3, fixation]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['f', 'j', 'space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                key_resp.rt = [key.rt for key in _key_resp_allKeys]
        
        # *mov00* updates
        if mov00.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mov00.frameNStart = frameN  # exact frame index
            mov00.tStart = t  # local t and not account for scr refresh
            mov00.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mov00, 'tStartRefresh')  # time at next scr refresh
            mov00.setAutoDraw(True)
        if mov00.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mov00.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                mov00.tStop = t  # not accounting for scr refresh
                mov00.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mov00, 'tStopRefresh')  # time at next scr refresh
                mov00.setAutoDraw(False)
        
        # *finish_judge_3* updates
        waitOnFlip = False
        if finish_judge_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_judge_3.frameNStart = frameN  # exact frame index
            finish_judge_3.tStart = t  # local t and not account for scr refresh
            finish_judge_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_judge_3, 'tStartRefresh')  # time at next scr refresh
            finish_judge_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(finish_judge_3.clock.reset)  # t=0 on next screen flip
        if finish_judge_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finish_judge_3.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                finish_judge_3.tStop = t  # not accounting for scr refresh
                finish_judge_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finish_judge_3, 'tStopRefresh')  # time at next scr refresh
                finish_judge_3.status = FINISHED
        if finish_judge_3.status == STARTED and not waitOnFlip:
            theseKeys = finish_judge_3.getKeys(keyList=['q'], waitRelease=False)
            _finish_judge_3_allKeys.extend(theseKeys)
            if len(_finish_judge_3_allKeys):
                finish_judge_3.keys = _finish_judge_3_allKeys[-1].name  # just the last key pressed
                finish_judge_3.rt = _finish_judge_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_2.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_2.addData('key_resp.rt', key_resp.rt)
    trials_2.addData('key_resp.started', key_resp.tStartRefresh)
    trials_2.addData('key_resp.stopped', key_resp.tStopRefresh)
    mov00.stop()
    strCounter = str(trialCounter)
    
    # check responses
    if finish_judge_3.keys in ['', [], None]:  # No response was made
        finish_judge_3.keys = None
    trials_2.addData('finish_judge_3.keys',finish_judge_3.keys)
    if finish_judge_3.keys != None:  # we had a response
        trials_2.addData('finish_judge_3.rt', finish_judge_3.rt)
    trials_2.addData('fixation.started', fixation.tStartRefresh)
    trials_2.addData('fixation.stopped', fixation.tStopRefresh)
    
    # ------Prepare to start Routine "breakt"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_breaktime_2.keys = []
    key_resp_breaktime_2.rt = []
    _key_resp_breaktime_2_allKeys = []
    finish_judge_4.keys = []
    finish_judge_4.rt = []
    _finish_judge_4_allKeys = []
    text_shintyoku.setText(strCounter + '/6')
    # keep track of which components have finished
    breaktComponents = [key_resp_breaktime_2, finish_judge_4, polygon, img_inst4, text_shintyoku]
    for thisComponent in breaktComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    breaktClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "breakt"-------
    while continueRoutine:
        # get current time
        t = breaktClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=breaktClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_breaktime_2* updates
        waitOnFlip = False
        if key_resp_breaktime_2.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            key_resp_breaktime_2.frameNStart = frameN  # exact frame index
            key_resp_breaktime_2.tStart = t  # local t and not account for scr refresh
            key_resp_breaktime_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_breaktime_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_breaktime_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_breaktime_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_breaktime_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_breaktime_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_breaktime_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_breaktime_2_allKeys.extend(theseKeys)
            if len(_key_resp_breaktime_2_allKeys):
                key_resp_breaktime_2.keys = _key_resp_breaktime_2_allKeys[-1].name  # just the last key pressed
                key_resp_breaktime_2.rt = _key_resp_breaktime_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *finish_judge_4* updates
        waitOnFlip = False
        if finish_judge_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_judge_4.frameNStart = frameN  # exact frame index
            finish_judge_4.tStart = t  # local t and not account for scr refresh
            finish_judge_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_judge_4, 'tStartRefresh')  # time at next scr refresh
            finish_judge_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(finish_judge_4.clock.reset)  # t=0 on next screen flip
        if finish_judge_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finish_judge_4.tStartRefresh + 120-frameTolerance:
                # keep track of stop time/frame for later
                finish_judge_4.tStop = t  # not accounting for scr refresh
                finish_judge_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finish_judge_4, 'tStopRefresh')  # time at next scr refresh
                finish_judge_4.status = FINISHED
        if finish_judge_4.status == STARTED and not waitOnFlip:
            theseKeys = finish_judge_4.getKeys(keyList=['q'], waitRelease=False)
            _finish_judge_4_allKeys.extend(theseKeys)
            if len(_finish_judge_4_allKeys):
                finish_judge_4.keys = _finish_judge_4_allKeys[-1].name  # just the last key pressed
                finish_judge_4.rt = _finish_judge_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        if polygon.status == STARTED:  # only update if drawing
            polygon.setPos((-5*t, -250), log=False)
            polygon.setSize((600-10*t, 50), log=False)
        
        # *img_inst4* updates
        if img_inst4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img_inst4.frameNStart = frameN  # exact frame index
            img_inst4.tStart = t  # local t and not account for scr refresh
            img_inst4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_inst4, 'tStartRefresh')  # time at next scr refresh
            img_inst4.setAutoDraw(True)
        
        # *text_shintyoku* updates
        if text_shintyoku.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_shintyoku.frameNStart = frameN  # exact frame index
            text_shintyoku.tStart = t  # local t and not account for scr refresh
            text_shintyoku.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_shintyoku, 'tStartRefresh')  # time at next scr refresh
            text_shintyoku.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breaktComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "breakt"-------
    for thisComponent in breaktComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_breaktime_2.keys in ['', [], None]:  # No response was made
        key_resp_breaktime_2.keys = None
    trials_2.addData('key_resp_breaktime_2.keys',key_resp_breaktime_2.keys)
    if key_resp_breaktime_2.keys != None:  # we had a response
        trials_2.addData('key_resp_breaktime_2.rt', key_resp_breaktime_2.rt)
    trials_2.addData('key_resp_breaktime_2.started', key_resp_breaktime_2.tStartRefresh)
    trials_2.addData('key_resp_breaktime_2.stopped', key_resp_breaktime_2.tStopRefresh)
    # check responses
    if finish_judge_4.keys in ['', [], None]:  # No response was made
        finish_judge_4.keys = None
    trials_2.addData('finish_judge_4.keys',finish_judge_4.keys)
    if finish_judge_4.keys != None:  # we had a response
        trials_2.addData('finish_judge_4.rt', finish_judge_4.rt)
    # the Routine "breakt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "catch_trial"-------
continueRoutine = True
routineTimer.add(60.000000)
# update component parameters for each repeat
key_resp_catch.keys = []
key_resp_catch.rt = []
_key_resp_catch_allKeys = []
mov_catch = visual.MovieStim3(
    win=win, name='mov_catch', units='pix',
    noAudio = False,
    filename='mp4/catch.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=True, anchor='center',
    size=(1120, 896),
    depth=-1.0,
    )
# keep track of which components have finished
catch_trialComponents = [key_resp_catch, mov_catch, fixation_catch]
for thisComponent in catch_trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
catch_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "catch_trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = catch_trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=catch_trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_catch* updates
    waitOnFlip = False
    if key_resp_catch.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_catch.frameNStart = frameN  # exact frame index
        key_resp_catch.tStart = t  # local t and not account for scr refresh
        key_resp_catch.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_catch, 'tStartRefresh')  # time at next scr refresh
        key_resp_catch.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_catch.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_catch.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_catch.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_catch.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_catch.tStop = t  # not accounting for scr refresh
            key_resp_catch.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_catch, 'tStopRefresh')  # time at next scr refresh
            key_resp_catch.status = FINISHED
    if key_resp_catch.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_catch.getKeys(keyList=['f', 'j', 'space'], waitRelease=False)
        _key_resp_catch_allKeys.extend(theseKeys)
        if len(_key_resp_catch_allKeys):
            key_resp_catch.keys = [key.name for key in _key_resp_catch_allKeys]  # storing all keys
            key_resp_catch.rt = [key.rt for key in _key_resp_catch_allKeys]
    
    # *mov_catch* updates
    if mov_catch.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mov_catch.frameNStart = frameN  # exact frame index
        mov_catch.tStart = t  # local t and not account for scr refresh
        mov_catch.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mov_catch, 'tStartRefresh')  # time at next scr refresh
        mov_catch.setAutoDraw(True)
    if mov_catch.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mov_catch.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            mov_catch.tStop = t  # not accounting for scr refresh
            mov_catch.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mov_catch, 'tStopRefresh')  # time at next scr refresh
            mov_catch.setAutoDraw(False)
    
    # *fixation_catch* updates
    if fixation_catch.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_catch.frameNStart = frameN  # exact frame index
        fixation_catch.tStart = t  # local t and not account for scr refresh
        fixation_catch.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_catch, 'tStartRefresh')  # time at next scr refresh
        fixation_catch.setAutoDraw(True)
    if fixation_catch.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_catch.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            fixation_catch.tStop = t  # not accounting for scr refresh
            fixation_catch.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_catch, 'tStopRefresh')  # time at next scr refresh
            fixation_catch.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in catch_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "catch_trial"-------
for thisComponent in catch_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_catch.keys in ['', [], None]:  # No response was made
    key_resp_catch.keys = None
thisExp.addData('key_resp_catch.keys',key_resp_catch.keys)
if key_resp_catch.keys != None:  # we had a response
    thisExp.addData('key_resp_catch.rt', key_resp_catch.rt)
thisExp.addData('key_resp_catch.started', key_resp_catch.tStartRefresh)
thisExp.addData('key_resp_catch.stopped', key_resp_catch.tStopRefresh)
thisExp.nextEntry()
mov_catch.stop()

# ------Prepare to start Routine "breakt"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_breaktime_2.keys = []
key_resp_breaktime_2.rt = []
_key_resp_breaktime_2_allKeys = []
finish_judge_4.keys = []
finish_judge_4.rt = []
_finish_judge_4_allKeys = []
text_shintyoku.setText(strCounter + '/6')
# keep track of which components have finished
breaktComponents = [key_resp_breaktime_2, finish_judge_4, polygon, img_inst4, text_shintyoku]
for thisComponent in breaktComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
breaktClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "breakt"-------
while continueRoutine:
    # get current time
    t = breaktClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=breaktClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_breaktime_2* updates
    waitOnFlip = False
    if key_resp_breaktime_2.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
        # keep track of start time/frame for later
        key_resp_breaktime_2.frameNStart = frameN  # exact frame index
        key_resp_breaktime_2.tStart = t  # local t and not account for scr refresh
        key_resp_breaktime_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_breaktime_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_breaktime_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_breaktime_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_breaktime_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_breaktime_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_breaktime_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_breaktime_2_allKeys.extend(theseKeys)
        if len(_key_resp_breaktime_2_allKeys):
            key_resp_breaktime_2.keys = _key_resp_breaktime_2_allKeys[-1].name  # just the last key pressed
            key_resp_breaktime_2.rt = _key_resp_breaktime_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *finish_judge_4* updates
    waitOnFlip = False
    if finish_judge_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finish_judge_4.frameNStart = frameN  # exact frame index
        finish_judge_4.tStart = t  # local t and not account for scr refresh
        finish_judge_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish_judge_4, 'tStartRefresh')  # time at next scr refresh
        finish_judge_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(finish_judge_4.clock.reset)  # t=0 on next screen flip
    if finish_judge_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finish_judge_4.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            finish_judge_4.tStop = t  # not accounting for scr refresh
            finish_judge_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finish_judge_4, 'tStopRefresh')  # time at next scr refresh
            finish_judge_4.status = FINISHED
    if finish_judge_4.status == STARTED and not waitOnFlip:
        theseKeys = finish_judge_4.getKeys(keyList=['q'], waitRelease=False)
        _finish_judge_4_allKeys.extend(theseKeys)
        if len(_finish_judge_4_allKeys):
            finish_judge_4.keys = _finish_judge_4_allKeys[-1].name  # just the last key pressed
            finish_judge_4.rt = _finish_judge_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if polygon.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            polygon.tStop = t  # not accounting for scr refresh
            polygon.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
            polygon.setAutoDraw(False)
    if polygon.status == STARTED:  # only update if drawing
        polygon.setPos((-5*t, -250), log=False)
        polygon.setSize((600-10*t, 50), log=False)
    
    # *img_inst4* updates
    if img_inst4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        img_inst4.frameNStart = frameN  # exact frame index
        img_inst4.tStart = t  # local t and not account for scr refresh
        img_inst4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(img_inst4, 'tStartRefresh')  # time at next scr refresh
        img_inst4.setAutoDraw(True)
    
    # *text_shintyoku* updates
    if text_shintyoku.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_shintyoku.frameNStart = frameN  # exact frame index
        text_shintyoku.tStart = t  # local t and not account for scr refresh
        text_shintyoku.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_shintyoku, 'tStartRefresh')  # time at next scr refresh
        text_shintyoku.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in breaktComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "breakt"-------
for thisComponent in breaktComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_breaktime_2.keys in ['', [], None]:  # No response was made
    key_resp_breaktime_2.keys = None
thisExp.addData('key_resp_breaktime_2.keys',key_resp_breaktime_2.keys)
if key_resp_breaktime_2.keys != None:  # we had a response
    thisExp.addData('key_resp_breaktime_2.rt', key_resp_breaktime_2.rt)
thisExp.addData('key_resp_breaktime_2.started', key_resp_breaktime_2.tStartRefresh)
thisExp.addData('key_resp_breaktime_2.stopped', key_resp_breaktime_2.tStopRefresh)
thisExp.nextEntry()
# check responses
if finish_judge_4.keys in ['', [], None]:  # No response was made
    finish_judge_4.keys = None
thisExp.addData('finish_judge_4.keys',finish_judge_4.keys)
if finish_judge_4.keys != None:  # we had a response
    thisExp.addData('finish_judge_4.rt', finish_judge_4.rt)
thisExp.nextEntry()
# the Routine "breakt" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_exp2512.xlsx'),
    seed=sum([ord(c) for c in expInfo['participant']]), name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    mov00 = visual.MovieStim3(
        win=win, name='mov00', units='pix',
        noAudio = False,
        filename=movItems,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=True, anchor='center',
        size=(1120, 896),
        depth=-1.0,
        )
    trialCounter = trialCounter + 1
    
    if trialCounter % nRestTrial == 0:
        isRest = 0
    else:
        isRest = 1
    
    finish_judge_3.keys = []
    finish_judge_3.rt = []
    _finish_judge_3_allKeys = []
    # keep track of which components have finished
    trialComponents = [key_resp, mov00, finish_judge_3, fixation]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['f', 'j', 'space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                key_resp.rt = [key.rt for key in _key_resp_allKeys]
        
        # *mov00* updates
        if mov00.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mov00.frameNStart = frameN  # exact frame index
            mov00.tStart = t  # local t and not account for scr refresh
            mov00.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mov00, 'tStartRefresh')  # time at next scr refresh
            mov00.setAutoDraw(True)
        if mov00.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mov00.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                mov00.tStop = t  # not accounting for scr refresh
                mov00.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mov00, 'tStopRefresh')  # time at next scr refresh
                mov00.setAutoDraw(False)
        
        # *finish_judge_3* updates
        waitOnFlip = False
        if finish_judge_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_judge_3.frameNStart = frameN  # exact frame index
            finish_judge_3.tStart = t  # local t and not account for scr refresh
            finish_judge_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_judge_3, 'tStartRefresh')  # time at next scr refresh
            finish_judge_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(finish_judge_3.clock.reset)  # t=0 on next screen flip
        if finish_judge_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finish_judge_3.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                finish_judge_3.tStop = t  # not accounting for scr refresh
                finish_judge_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finish_judge_3, 'tStopRefresh')  # time at next scr refresh
                finish_judge_3.status = FINISHED
        if finish_judge_3.status == STARTED and not waitOnFlip:
            theseKeys = finish_judge_3.getKeys(keyList=['q'], waitRelease=False)
            _finish_judge_3_allKeys.extend(theseKeys)
            if len(_finish_judge_3_allKeys):
                finish_judge_3.keys = _finish_judge_3_allKeys[-1].name  # just the last key pressed
                finish_judge_3.rt = _finish_judge_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    mov00.stop()
    strCounter = str(trialCounter)
    
    # check responses
    if finish_judge_3.keys in ['', [], None]:  # No response was made
        finish_judge_3.keys = None
    trials.addData('finish_judge_3.keys',finish_judge_3.keys)
    if finish_judge_3.keys != None:  # we had a response
        trials.addData('finish_judge_3.rt', finish_judge_3.rt)
    trials.addData('fixation.started', fixation.tStartRefresh)
    trials.addData('fixation.stopped', fixation.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    restOrNot = data.TrialHandler(nReps=isRest, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='restOrNot')
    thisExp.addLoop(restOrNot)  # add the loop to the experiment
    thisRestOrNot = restOrNot.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRestOrNot.rgb)
    if thisRestOrNot != None:
        for paramName in thisRestOrNot:
            exec('{} = thisRestOrNot[paramName]'.format(paramName))
    
    for thisRestOrNot in restOrNot:
        currentLoop = restOrNot
        # abbreviate parameter names if possible (e.g. rgb = thisRestOrNot.rgb)
        if thisRestOrNot != None:
            for paramName in thisRestOrNot:
                exec('{} = thisRestOrNot[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "breakt"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_breaktime_2.keys = []
        key_resp_breaktime_2.rt = []
        _key_resp_breaktime_2_allKeys = []
        finish_judge_4.keys = []
        finish_judge_4.rt = []
        _finish_judge_4_allKeys = []
        text_shintyoku.setText(strCounter + '/6')
        # keep track of which components have finished
        breaktComponents = [key_resp_breaktime_2, finish_judge_4, polygon, img_inst4, text_shintyoku]
        for thisComponent in breaktComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        breaktClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "breakt"-------
        while continueRoutine:
            # get current time
            t = breaktClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=breaktClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_breaktime_2* updates
            waitOnFlip = False
            if key_resp_breaktime_2.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
                # keep track of start time/frame for later
                key_resp_breaktime_2.frameNStart = frameN  # exact frame index
                key_resp_breaktime_2.tStart = t  # local t and not account for scr refresh
                key_resp_breaktime_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_breaktime_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_breaktime_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_breaktime_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_breaktime_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_breaktime_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_breaktime_2.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_breaktime_2_allKeys.extend(theseKeys)
                if len(_key_resp_breaktime_2_allKeys):
                    key_resp_breaktime_2.keys = _key_resp_breaktime_2_allKeys[-1].name  # just the last key pressed
                    key_resp_breaktime_2.rt = _key_resp_breaktime_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *finish_judge_4* updates
            waitOnFlip = False
            if finish_judge_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                finish_judge_4.frameNStart = frameN  # exact frame index
                finish_judge_4.tStart = t  # local t and not account for scr refresh
                finish_judge_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(finish_judge_4, 'tStartRefresh')  # time at next scr refresh
                finish_judge_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(finish_judge_4.clock.reset)  # t=0 on next screen flip
            if finish_judge_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > finish_judge_4.tStartRefresh + 120-frameTolerance:
                    # keep track of stop time/frame for later
                    finish_judge_4.tStop = t  # not accounting for scr refresh
                    finish_judge_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(finish_judge_4, 'tStopRefresh')  # time at next scr refresh
                    finish_judge_4.status = FINISHED
            if finish_judge_4.status == STARTED and not waitOnFlip:
                theseKeys = finish_judge_4.getKeys(keyList=['q'], waitRelease=False)
                _finish_judge_4_allKeys.extend(theseKeys)
                if len(_finish_judge_4_allKeys):
                    finish_judge_4.keys = _finish_judge_4_allKeys[-1].name  # just the last key pressed
                    finish_judge_4.rt = _finish_judge_4_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 60-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            if polygon.status == STARTED:  # only update if drawing
                polygon.setPos((-5*t, -250), log=False)
                polygon.setSize((600-10*t, 50), log=False)
            
            # *img_inst4* updates
            if img_inst4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img_inst4.frameNStart = frameN  # exact frame index
                img_inst4.tStart = t  # local t and not account for scr refresh
                img_inst4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img_inst4, 'tStartRefresh')  # time at next scr refresh
                img_inst4.setAutoDraw(True)
            
            # *text_shintyoku* updates
            if text_shintyoku.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_shintyoku.frameNStart = frameN  # exact frame index
                text_shintyoku.tStart = t  # local t and not account for scr refresh
                text_shintyoku.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_shintyoku, 'tStartRefresh')  # time at next scr refresh
                text_shintyoku.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in breaktComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "breakt"-------
        for thisComponent in breaktComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_breaktime_2.keys in ['', [], None]:  # No response was made
            key_resp_breaktime_2.keys = None
        restOrNot.addData('key_resp_breaktime_2.keys',key_resp_breaktime_2.keys)
        if key_resp_breaktime_2.keys != None:  # we had a response
            restOrNot.addData('key_resp_breaktime_2.rt', key_resp_breaktime_2.rt)
        restOrNot.addData('key_resp_breaktime_2.started', key_resp_breaktime_2.tStartRefresh)
        restOrNot.addData('key_resp_breaktime_2.stopped', key_resp_breaktime_2.tStopRefresh)
        # check responses
        if finish_judge_4.keys in ['', [], None]:  # No response was made
            finish_judge_4.keys = None
        restOrNot.addData('finish_judge_4.keys',finish_judge_4.keys)
        if finish_judge_4.keys != None:  # we had a response
            restOrNot.addData('finish_judge_4.rt', finish_judge_4.rt)
        # the Routine "breakt" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed isRest repeats of 'restOrNot'
    
    # get names of stimulus parameters
    if restOrNot.trialList in ([], [None], None):
        params = []
    else:
        params = restOrNot.trialList[0].keys()
    # save data for this loop
    restOrNot.saveAsText(filename + 'restOrNot.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "outro"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
outroComponents = [text]
for thisComponent in outroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
outroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "outro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = outroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=outroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in outroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "outro"-------
for thisComponent in outroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
