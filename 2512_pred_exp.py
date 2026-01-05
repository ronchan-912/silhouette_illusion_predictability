#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on 火 12/16 14:34:58 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

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

import psychopy.iohub as io
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
    originPath='/Users/rondenkouhei/study_multiperception/psychopy/experiment_exp2/2512_pred_exp.py',
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
    monitor='newMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
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

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "introduction"
introductionClock = core.Clock()
key_resp_instruction = keyboard.Keyboard()
text_instruction = visual.TextStim(win=win, name='text_instruction',
    text="You will see a spinning girl.\nClockwise → [f]\nCounter-clockwise → [j].\nSwitching every half turn → [space].\nYou don't know which direction → [enter].\n\nPlease press [space] to continue the experiment.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win,
    name='image', units='pix', 
    image='/Users/rondenkouhei/study_multiperception/stimulus/arrow_cwccw_x.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -400), size=(600, 150),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
key_resp = keyboard.Keyboard()
trialCounter = 0
strCounter = str(trialCounter)
nRestTrial = 27
fixation_below_2 = visual.TextStim(win=win, name='fixation_below_2',
    text='+',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color=[1.0000, -0.3000, -0.3000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "breakt"
breaktClock = core.Clock()
text_break_17 = visual.TextStim(win=win, name='text_break_17',
    text="It's breaktime.\nPlease wait at least 60 seconds.\nThen, press [space] to continue the experiment.\n\nClockwise → [f]\nCounter-clockwise → [j].\nSwitching every half turn → [space].\nYou don't know which direction → [enter].",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_4 = visual.ImageStim(
    win=win,
    name='image_4', units='pix', 
    image='/Users/rondenkouhei/study_multiperception/stimulus/arrow_cwccw_x.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -400), size=(600, 150),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_breaktime_2 = keyboard.Keyboard()
polygon = visual.Rect(
    win=win, name='polygon',units='norm', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(-0.5, -0.55), anchor='center-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.8824, 0.8039, 0.0980], fillColor=[0.8824, 0.8039, 0.0980],
    opacity=None, depth=-3.0, interpolate=True)
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

# ------Prepare to start Routine "introduction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_instruction.keys = []
key_resp_instruction.rt = []
_key_resp_instruction_allKeys = []
# keep track of which components have finished
introductionComponents = [key_resp_instruction, text_instruction, image]
for thisComponent in introductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction"-------
while continueRoutine:
    # get current time
    t = introductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introductionClock)
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
        theseKeys = key_resp_instruction.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_instruction_allKeys.extend(theseKeys)
        if len(_key_resp_instruction_allKeys):
            key_resp_instruction.keys = _key_resp_instruction_allKeys[-1].name  # just the last key pressed
            key_resp_instruction.rt = _key_resp_instruction_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_instruction* updates
    if text_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instruction.frameNStart = frameN  # exact frame index
        text_instruction.tStart = t  # local t and not account for scr refresh
        text_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instruction, 'tStartRefresh')  # time at next scr refresh
        text_instruction.setAutoDraw(True)
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction"-------
for thisComponent in introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_exp2512.xlsx'),
    seed=80, name='trials')
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
        size=(1600, 900),
        depth=-1.0,
        )
    trialCounter = trialCounter + 1
    
    if trialCounter % nRestTrial == 0:
        isRest = 0
    else:
        isRest = 1
    
    # keep track of which components have finished
    trialComponents = [key_resp, mov00, fixation_below_2]
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
            theseKeys = key_resp.getKeys(keyList=['f', 'j', 'return', 'space'], waitRelease=False)
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
        
        # *fixation_below_2* updates
        if fixation_below_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_below_2.frameNStart = frameN  # exact frame index
            fixation_below_2.tStart = t  # local t and not account for scr refresh
            fixation_below_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_below_2, 'tStartRefresh')  # time at next scr refresh
            fixation_below_2.setAutoDraw(True)
        if fixation_below_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_below_2.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                fixation_below_2.tStop = t  # not accounting for scr refresh
                fixation_below_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_below_2, 'tStopRefresh')  # time at next scr refresh
                fixation_below_2.setAutoDraw(False)
        
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
        text_shintyoku.setText(strCounter + '/27')
        # keep track of which components have finished
        breaktComponents = [text_break_17, image_4, key_resp_breaktime_2, polygon, text_shintyoku]
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
            
            # *text_break_17* updates
            if text_break_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_break_17.frameNStart = frameN  # exact frame index
                text_break_17.tStart = t  # local t and not account for scr refresh
                text_break_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_break_17, 'tStartRefresh')  # time at next scr refresh
                text_break_17.setAutoDraw(True)
            
            # *image_4* updates
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                image_4.setAutoDraw(True)
            
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
                polygon.setSize(((60-t)/60, 0.1), log=False)
            
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
        restOrNot.addData('text_shintyoku.started', text_shintyoku.tStartRefresh)
        restOrNot.addData('text_shintyoku.stopped', text_shintyoku.tStopRefresh)
        # the Routine "breakt" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed isRest repeats of 'restOrNot'
    
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'trials'


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
