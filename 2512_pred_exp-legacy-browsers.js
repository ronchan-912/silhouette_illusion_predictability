/********************** 
 * 2512_Pred_Exp Test *
 **********************/


// store info about the experiment session:
let expName = '2512_pred_exp';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(introduction1RoutineBegin());
flowScheduler.add(introduction1RoutineEachFrame());
flowScheduler.add(introduction1RoutineEnd());
flowScheduler.add(mihonRoutineBegin());
flowScheduler.add(mihonRoutineEachFrame());
flowScheduler.add(mihonRoutineEnd());
flowScheduler.add(introduction2RoutineBegin());
flowScheduler.add(introduction2RoutineEachFrame());
flowScheduler.add(introduction2RoutineEnd());
flowScheduler.add(demoRoutineBegin());
flowScheduler.add(demoRoutineEachFrame());
flowScheduler.add(demoRoutineEnd());
flowScheduler.add(introduction3RoutineBegin());
flowScheduler.add(introduction3RoutineEachFrame());
flowScheduler.add(introduction3RoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(catch_trialRoutineBegin());
flowScheduler.add(catch_trialRoutineEachFrame());
flowScheduler.add(catch_trialRoutineEnd());
flowScheduler.add(breaktRoutineBegin());
flowScheduler.add(breaktRoutineEachFrame());
flowScheduler.add(breaktRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(outroRoutineBegin());
flowScheduler.add(outroRoutineEachFrame());
flowScheduler.add(outroRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'mp4/catch.mp4', 'path': 'mp4/catch.mp4'},
    {'name': 'png/mask_l.png', 'path': 'png/mask_l.png'},
    {'name': 'png/arrow_cwccw_x.png', 'path': 'png/arrow_cwccw_x.png'},
    {'name': 'png/arrow_cwccw_y.png', 'path': 'png/arrow_cwccw_y.png'},
    {'name': 'mp4/dance_nonrigid.mp4', 'path': 'mp4/dance_nonrigid.mp4'},
    {'name': 'png/inst4.png', 'path': 'png/inst4.png'},
    {'name': 'mp4/catch_demo.mp4', 'path': 'mp4/catch_demo.mp4'},
    {'name': 'png/mask_r.png', 'path': 'png/mask_r.png'},
    {'name': 'png/inst3.png', 'path': 'png/inst3.png'},
    {'name': 'mp4/demo/taisoufuku_demo_120sec.mp4', 'path': 'mp4/demo/taisoufuku_demo_120sec.mp4'},
    {'name': 'mp4/dance_rigid_mask_shuffle.mp4', 'path': 'mp4/dance_rigid_mask_shuffle.mp4'},
    {'name': 'png/inst1.png', 'path': 'png/inst1.png'},
    {'name': 'mp4/dance_rigid.mp4', 'path': 'mp4/dance_rigid.mp4'},
    {'name': 'conditions_exp2512.xlsx', 'path': 'conditions_exp2512.xlsx'},
    {'name': 'png/inst2.png', 'path': 'png/inst2.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.1.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var introduction1Clock;
var key_resp_instruction_2;
var img_inst1;
var mihonClock;
var movieClock;
var movie;
var key_resp_mihon;
var finish_judge_2;
var fixation_2;
var introduction2Clock;
var key_resp_instruction;
var img_inst2;
var demoClock;
var finish_judge;
var key_resp_demo;
var key_resp_selection;
var movClock;
var mov;
var polygon_6;
var mask_cw;
var mask_ccw;
var introduction3Clock;
var img_inst3;
var key_resp_instruction_3;
var trialClock;
var key_resp;
var trialCounter;
var strCounter;
var nRestTrial;
var finish_judge_3;
var fixation;
var breaktClock;
var key_resp_breaktime_2;
var polygon;
var img_inst4;
var text_shintyoku;
var catch_trialClock;
var key_resp_catch;
var fixation_catch;
var outroClock;
var text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "introduction1"
  introduction1Clock = new util.Clock();
  key_resp_instruction_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  img_inst1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img_inst1', units : 'pix', 
    image : 'png/inst1.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1000, 528],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "mihon"
  mihonClock = new util.Clock();
  movieClock = new util.Clock();
  movie = new visual.MovieStim({
    win: psychoJS.window,
    name: 'movie',
    units: 'pix',
    movie: 'mp4/catch_demo.mp4',
    pos: [0, 0],
    size: [1420, 800],
    ori: 0.0,
    opacity: undefined,
    loop: false,
    noAudio: false,
    });
  key_resp_mihon = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  finish_judge_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  fixation_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_2', units : 'pix', 
    vertices: 'cross', size:[25, 25],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color([1.0, (- 0.2235), (- 0.4431)]),
    fillColor: new util.Color([1.0, (- 0.2235), (- 0.4431)]),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  // Initialize components for Routine "introduction2"
  introduction2Clock = new util.Clock();
  key_resp_instruction = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  img_inst2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img_inst2', units : 'pix', 
    image : 'png/inst2.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1000, 528],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "demo"
  demoClock = new util.Clock();
  finish_judge = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  key_resp_demo = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  key_resp_selection = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  movClock = new util.Clock();
  mov = new visual.MovieStim({
    win: psychoJS.window,
    name: 'mov',
    units: 'pix',
    movie: 'mp4/demo/taisoufuku_demo_120sec.mp4',
    pos: [0, 0],
    size: [1450, 870],
    ori: 0.0,
    opacity: 1.0,
    loop: true,
    noAudio: false,
    });
  polygon_6 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'polygon_6', units : 'pix', 
    vertices: 'cross', size:[25, 25],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color([1.0, (- 0.2235), (- 0.4431)]),
    fillColor: new util.Color([1.0, (- 0.2235), (- 0.4431)]),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  mask_cw = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mask_cw', units : 'pix', 
    image : 'png/mask_l.png', mask : undefined,
    ori : 0.0, pos : [(- 480), 0], size : [480, 800],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  mask_ccw = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mask_ccw', units : 'pix', 
    image : 'png/mask_r.png', mask : undefined,
    ori : 0.0, pos : [480, 0], size : [480, 800],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  // Initialize components for Routine "introduction3"
  introduction3Clock = new util.Clock();
  img_inst3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img_inst3', units : 'pix', 
    image : 'png/inst3.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1000, 687],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_instruction_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  trialCounter = 0;
  strCounter = trialCounter.toString();
  nRestTrial = 6;
  
  finish_judge_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  fixation = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation', units : 'pix', 
    vertices: 'cross', size:[25, 25],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color([1.0, (- 0.2235), (- 0.4431)]),
    fillColor: new util.Color([1.0, (- 0.2235), (- 0.4431)]),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  // Initialize components for Routine "breakt"
  breaktClock = new util.Clock();
  key_resp_breaktime_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  polygon = new visual.Rect ({
    win: psychoJS.window, name: 'polygon', units : 'pix', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color([0.8824, 0.8039, 0.098]),
    fillColor: new util.Color([0.8824, 0.8039, 0.098]),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  img_inst4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img_inst4', units : 'pix', 
    image : 'png/inst4.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1000, 352],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  text_shintyoku = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_shintyoku',
    text: '',
    font: 'Open Sans',
    units: 'norm', 
    pos: [0.9, 0.9], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "catch_trial"
  catch_trialClock = new util.Clock();
  key_resp_catch = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  fixation_catch = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_catch', units : 'pix', 
    vertices: 'cross', size:[25, 25],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color([1.0, (- 0.2235), (- 0.4431)]),
    fillColor: new util.Color([1.0, (- 0.2235), (- 0.4431)]),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "outro"
  outroClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Thank you.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_instruction_2_allKeys;
var introduction1Components;
function introduction1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'introduction1'-------
    t = 0;
    introduction1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_instruction_2.keys = undefined;
    key_resp_instruction_2.rt = undefined;
    _key_resp_instruction_2_allKeys = [];
    // keep track of which components have finished
    introduction1Components = [];
    introduction1Components.push(key_resp_instruction_2);
    introduction1Components.push(img_inst1);
    
    introduction1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function introduction1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'introduction1'-------
    // get current time
    t = introduction1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_instruction_2* updates
    if (t >= 0.0 && key_resp_instruction_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_instruction_2.tStart = t;  // (not accounting for frame time here)
      key_resp_instruction_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_instruction_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_instruction_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_instruction_2.clearEvents(); });
    }

    if (key_resp_instruction_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_instruction_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_instruction_2_allKeys = _key_resp_instruction_2_allKeys.concat(theseKeys);
      if (_key_resp_instruction_2_allKeys.length > 0) {
        key_resp_instruction_2.keys = _key_resp_instruction_2_allKeys[_key_resp_instruction_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_instruction_2.rt = _key_resp_instruction_2_allKeys[_key_resp_instruction_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *img_inst1* updates
    if (t >= 0.0 && img_inst1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      img_inst1.tStart = t;  // (not accounting for frame time here)
      img_inst1.frameNStart = frameN;  // exact frame index
      
      img_inst1.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    introduction1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introduction1RoutineEnd() {
  return async function () {
    //------Ending Routine 'introduction1'-------
    introduction1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_resp_instruction_2.stop();
    // the Routine "introduction1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_mihon_allKeys;
var _finish_judge_2_allKeys;
var mihonComponents;
function mihonRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'mihon'-------
    t = 0;
    mihonClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(60.000000);
    // update component parameters for each repeat
    key_resp_mihon.keys = undefined;
    key_resp_mihon.rt = undefined;
    _key_resp_mihon_allKeys = [];
    finish_judge_2.keys = undefined;
    finish_judge_2.rt = undefined;
    _finish_judge_2_allKeys = [];
    // keep track of which components have finished
    mihonComponents = [];
    mihonComponents.push(movie);
    mihonComponents.push(key_resp_mihon);
    mihonComponents.push(finish_judge_2);
    mihonComponents.push(fixation_2);
    
    mihonComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function mihonRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'mihon'-------
    // get current time
    t = mihonClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *movie* updates
    if (t >= 0.0 && movie.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movie.tStart = t;  // (not accounting for frame time here)
      movie.frameNStart = frameN;  // exact frame index
      
      movie.setAutoDraw(true);
      movie.play();
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (movie.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      movie.setAutoDraw(false);
    }

    
    // *key_resp_mihon* updates
    if (t >= 0.0 && key_resp_mihon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_mihon.tStart = t;  // (not accounting for frame time here)
      key_resp_mihon.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_mihon.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_mihon.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_mihon.clearEvents(); });
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_mihon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_mihon.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_mihon.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_mihon.getKeys({keyList: ['f', 'j', 'space'], waitRelease: false});
      _key_resp_mihon_allKeys = _key_resp_mihon_allKeys.concat(theseKeys);
      if (_key_resp_mihon_allKeys.length > 0) {
        key_resp_mihon.keys = _key_resp_mihon_allKeys.map((key) => key.name);  // storing all keys
        key_resp_mihon.rt = _key_resp_mihon_allKeys.map((key) => key.rt);
      }
    }
    
    
    // *finish_judge_2* updates
    if (t >= 0.0 && finish_judge_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      finish_judge_2.tStart = t;  // (not accounting for frame time here)
      finish_judge_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { finish_judge_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { finish_judge_2.start(); }); // start on screen flip
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (finish_judge_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      finish_judge_2.status = PsychoJS.Status.FINISHED;
  }

    if (finish_judge_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = finish_judge_2.getKeys({keyList: ['q'], waitRelease: false});
      _finish_judge_2_allKeys = _finish_judge_2_allKeys.concat(theseKeys);
      if (_finish_judge_2_allKeys.length > 0) {
        finish_judge_2.keys = _finish_judge_2_allKeys[_finish_judge_2_allKeys.length - 1].name;  // just the last key pressed
        finish_judge_2.rt = _finish_judge_2_allKeys[_finish_judge_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *fixation_2* updates
    if (t >= 0.0 && fixation_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_2.tStart = t;  // (not accounting for frame time here)
      fixation_2.frameNStart = frameN;  // exact frame index
      
      fixation_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    mihonComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function mihonRoutineEnd() {
  return async function () {
    //------Ending Routine 'mihon'-------
    mihonComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    movie.stop();
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(key_resp_mihon.corr, level);
    }
    psychoJS.experiment.addData('key_resp_mihon.keys', key_resp_mihon.keys);
    if (typeof key_resp_mihon.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_mihon.rt', key_resp_mihon.rt);
        }
    
    key_resp_mihon.stop();
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(finish_judge_2.corr, level);
    }
    psychoJS.experiment.addData('finish_judge_2.keys', finish_judge_2.keys);
    if (typeof finish_judge_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('finish_judge_2.rt', finish_judge_2.rt);
        routineTimer.reset();
        }
    
    finish_judge_2.stop();
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_instruction_allKeys;
var introduction2Components;
function introduction2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'introduction2'-------
    t = 0;
    introduction2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_instruction.keys = undefined;
    key_resp_instruction.rt = undefined;
    _key_resp_instruction_allKeys = [];
    // keep track of which components have finished
    introduction2Components = [];
    introduction2Components.push(key_resp_instruction);
    introduction2Components.push(img_inst2);
    
    introduction2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function introduction2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'introduction2'-------
    // get current time
    t = introduction2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_instruction* updates
    if (t >= 0.0 && key_resp_instruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_instruction.tStart = t;  // (not accounting for frame time here)
      key_resp_instruction.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_instruction.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_instruction.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_instruction.clearEvents(); });
    }

    if (key_resp_instruction.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_instruction.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_instruction_allKeys = _key_resp_instruction_allKeys.concat(theseKeys);
      if (_key_resp_instruction_allKeys.length > 0) {
        key_resp_instruction.keys = _key_resp_instruction_allKeys[_key_resp_instruction_allKeys.length - 1].name;  // just the last key pressed
        key_resp_instruction.rt = _key_resp_instruction_allKeys[_key_resp_instruction_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *img_inst2* updates
    if (t >= 0.0 && img_inst2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      img_inst2.tStart = t;  // (not accounting for frame time here)
      img_inst2.frameNStart = frameN;  // exact frame index
      
      img_inst2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    introduction2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introduction2RoutineEnd() {
  return async function () {
    //------Ending Routine 'introduction2'-------
    introduction2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_resp_instruction.stop();
    // the Routine "introduction2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _finish_judge_allKeys;
var _key_resp_demo_allKeys;
var _key_resp_selection_allKeys;
var demoComponents;
function demoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'demo'-------
    t = 0;
    demoClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(120.000000);
    // update component parameters for each repeat
    finish_judge.keys = undefined;
    finish_judge.rt = undefined;
    _finish_judge_allKeys = [];
    key_resp_demo.keys = undefined;
    key_resp_demo.rt = undefined;
    _key_resp_demo_allKeys = [];
    key_resp_selection.keys = undefined;
    key_resp_selection.rt = undefined;
    _key_resp_selection_allKeys = [];
    // keep track of which components have finished
    demoComponents = [];
    demoComponents.push(finish_judge);
    demoComponents.push(key_resp_demo);
    demoComponents.push(key_resp_selection);
    demoComponents.push(mov);
    demoComponents.push(polygon_6);
    demoComponents.push(mask_cw);
    demoComponents.push(mask_ccw);
    
    demoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var val;
var opa_cw;
var opa_ccw;
function demoRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'demo'-------
    // get current time
    t = demoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *finish_judge* updates
    if (t >= 0.0 && finish_judge.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      finish_judge.tStart = t;  // (not accounting for frame time here)
      finish_judge.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { finish_judge.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { finish_judge.start(); }); // start on screen flip
    }

    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (finish_judge.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      finish_judge.status = PsychoJS.Status.FINISHED;
  }

    if (finish_judge.status === PsychoJS.Status.STARTED) {
      let theseKeys = finish_judge.getKeys({keyList: ['q'], waitRelease: false});
      _finish_judge_allKeys = _finish_judge_allKeys.concat(theseKeys);
      if (_finish_judge_allKeys.length > 0) {
        finish_judge.keys = _finish_judge_allKeys[_finish_judge_allKeys.length - 1].name;  // just the last key pressed
        finish_judge.rt = _finish_judge_allKeys[_finish_judge_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *key_resp_demo* updates
    if (t >= 0.0 && key_resp_demo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_demo.tStart = t;  // (not accounting for frame time here)
      key_resp_demo.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_demo.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_demo.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_demo.clearEvents(); });
    }

    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_demo.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_demo.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_demo.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_demo.getKeys({keyList: ['f', 'j', 'space'], waitRelease: false});
      _key_resp_demo_allKeys = _key_resp_demo_allKeys.concat(theseKeys);
      if (_key_resp_demo_allKeys.length > 0) {
        key_resp_demo.keys = _key_resp_demo_allKeys.map((key) => key.name);  // storing all keys
        key_resp_demo.rt = _key_resp_demo_allKeys.map((key) => key.rt);
      }
    }
    
    
    // *key_resp_selection* updates
    if (t >= 0.0 && key_resp_selection.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_selection.tStart = t;  // (not accounting for frame time here)
      key_resp_selection.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_selection.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_selection.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_selection.clearEvents(); });
    }

    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_selection.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_selection.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_selection.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_selection.getKeys({keyList: ['l', 'r', 'b'], waitRelease: false});
      _key_resp_selection_allKeys = _key_resp_selection_allKeys.concat(theseKeys);
      if (_key_resp_selection_allKeys.length > 0) {
        key_resp_selection.keys = _key_resp_selection_allKeys[_key_resp_selection_allKeys.length - 1].name;  // just the last key pressed
        key_resp_selection.rt = _key_resp_selection_allKeys[_key_resp_selection_allKeys.length - 1].rt;
      }
    }
    
    
    // *mov* updates
    if (t >= 0.0 && mov.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mov.tStart = t;  // (not accounting for frame time here)
      mov.frameNStart = frameN;  // exact frame index
      
      mov.setAutoDraw(true);
      mov.play();
    }

    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mov.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mov.setAutoDraw(false);
    }

    if (mov.status === PsychoJS.Status.STARTED)  {  // only update if being drawn
      mov.setOpacity(1.0, false);
    }
    
    // *polygon_6* updates
    if (t >= 0.0 && polygon_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_6.tStart = t;  // (not accounting for frame time here)
      polygon_6.frameNStart = frameN;  // exact frame index
      
      polygon_6.setAutoDraw(true);
    }

    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygon_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon_6.setAutoDraw(false);
    }
    val = key_resp_selection.keys;
    if ((val === "l")) {
        opa_cw = 0.0;
        opa_ccw = 1.0;
    } else {
        if ((val === "r")) {
            opa_cw = 1.0;
            opa_ccw = 0.0;
        } else {
            opa_cw = 1.0;
            opa_ccw = 1.0;
        }
    }
    
    
    // *mask_cw* updates
    if (t >= 0.0 && mask_cw.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mask_cw.tStart = t;  // (not accounting for frame time here)
      mask_cw.frameNStart = frameN;  // exact frame index
      
      mask_cw.setAutoDraw(true);
    }

    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mask_cw.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mask_cw.setAutoDraw(false);
    }
    
    if (mask_cw.status === PsychoJS.Status.STARTED){ // only update if being drawn
      mask_cw.setOpacity(opa_cw, false);
    }
    
    // *mask_ccw* updates
    if (t >= 0.0 && mask_ccw.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mask_ccw.tStart = t;  // (not accounting for frame time here)
      mask_ccw.frameNStart = frameN;  // exact frame index
      
      mask_ccw.setAutoDraw(true);
    }

    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mask_ccw.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mask_ccw.setAutoDraw(false);
    }
    
    if (mask_ccw.status === PsychoJS.Status.STARTED){ // only update if being drawn
      mask_ccw.setOpacity(opa_ccw, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    demoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demoRoutineEnd() {
  return async function () {
    //------Ending Routine 'demo'-------
    demoComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(finish_judge.corr, level);
    }
    psychoJS.experiment.addData('finish_judge.keys', finish_judge.keys);
    if (typeof finish_judge.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('finish_judge.rt', finish_judge.rt);
        routineTimer.reset();
        }
    
    finish_judge.stop();
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(key_resp_demo.corr, level);
    }
    psychoJS.experiment.addData('key_resp_demo.keys', key_resp_demo.keys);
    if (typeof key_resp_demo.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_demo.rt', key_resp_demo.rt);
        }
    
    key_resp_demo.stop();
    key_resp_selection.stop();
    mov.stop();
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_instruction_3_allKeys;
var introduction3Components;
function introduction3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'introduction3'-------
    t = 0;
    introduction3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_instruction_3.keys = undefined;
    key_resp_instruction_3.rt = undefined;
    _key_resp_instruction_3_allKeys = [];
    // keep track of which components have finished
    introduction3Components = [];
    introduction3Components.push(img_inst3);
    introduction3Components.push(key_resp_instruction_3);
    
    introduction3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function introduction3RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'introduction3'-------
    // get current time
    t = introduction3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *img_inst3* updates
    if (t >= 0.0 && img_inst3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      img_inst3.tStart = t;  // (not accounting for frame time here)
      img_inst3.frameNStart = frameN;  // exact frame index
      
      img_inst3.setAutoDraw(true);
    }

    
    // *key_resp_instruction_3* updates
    if (t >= 0.0 && key_resp_instruction_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_instruction_3.tStart = t;  // (not accounting for frame time here)
      key_resp_instruction_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_instruction_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_instruction_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_instruction_3.clearEvents(); });
    }

    if (key_resp_instruction_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_instruction_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_instruction_3_allKeys = _key_resp_instruction_3_allKeys.concat(theseKeys);
      if (_key_resp_instruction_3_allKeys.length > 0) {
        key_resp_instruction_3.keys = _key_resp_instruction_3_allKeys[_key_resp_instruction_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_instruction_3.rt = _key_resp_instruction_3_allKeys[_key_resp_instruction_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    introduction3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introduction3RoutineEnd() {
  return async function () {
    //------Ending Routine 'introduction3'-------
    introduction3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_resp_instruction_3.stop();
    // the Routine "introduction3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials_2;
var currentLoop;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions_exp2512.xlsx',
      seed: 10, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_2.forEach(function() {
      const snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(trialRoutineBegin(snapshot));
      trials_2LoopScheduler.add(trialRoutineEachFrame());
      trials_2LoopScheduler.add(trialRoutineEnd());
      trials_2LoopScheduler.add(breaktRoutineBegin(snapshot));
      trials_2LoopScheduler.add(breaktRoutineEachFrame());
      trials_2LoopScheduler.add(breaktRoutineEnd());
      trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions_exp2512.xlsx',
      seed: 80, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      const snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd());
      const restOrNotLoopScheduler = new Scheduler(psychoJS);
      trialsLoopScheduler.add(restOrNotLoopBegin(restOrNotLoopScheduler, snapshot));
      trialsLoopScheduler.add(restOrNotLoopScheduler);
      trialsLoopScheduler.add(restOrNotLoopEnd);
      trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var restOrNot;
function restOrNotLoopBegin(restOrNotLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    restOrNot = new TrialHandler({
      psychoJS: psychoJS,
      nReps: isRest, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'restOrNot'
    });
    psychoJS.experiment.addLoop(restOrNot); // add the loop to the experiment
    currentLoop = restOrNot;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    restOrNot.forEach(function() {
      const snapshot = restOrNot.getSnapshot();
    
      restOrNotLoopScheduler.add(importConditions(snapshot));
      restOrNotLoopScheduler.add(breaktRoutineBegin(snapshot));
      restOrNotLoopScheduler.add(breaktRoutineEachFrame());
      restOrNotLoopScheduler.add(breaktRoutineEnd());
      restOrNotLoopScheduler.add(endLoopIteration(restOrNotLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function restOrNotLoopEnd() {
  psychoJS.experiment.removeLoop(restOrNot);

  return Scheduler.Event.NEXT;
}


async function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var _key_resp_allKeys;
var mov00Clock;
var mov00;
var isRest;
var _finish_judge_3_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(60.000000);
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    mov00Clock = new util.Clock();
    mov00 = new visual.MovieStim({
      win: psychoJS.window,
      name: 'mov00',
      units: 'pix',
      movie: movItems,
      pos: [0, 0],
      size: [1120, 896],
      ori: 0.0,
      opacity: undefined,
      loop: true,
      noAudio: false,
      });
    trialCounter = (trialCounter + 1);
    if (((trialCounter % nRestTrial) === 0)) {
        isRest = 0;
    } else {
        isRest = 1;
    }
    
    finish_judge_3.keys = undefined;
    finish_judge_3.rt = undefined;
    _finish_judge_3_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(key_resp);
    trialComponents.push(mov00);
    trialComponents.push(finish_judge_3);
    trialComponents.push(fixation);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['f', 'j', 'space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys.map((key) => key.name);  // storing all keys
        key_resp.rt = _key_resp_allKeys.map((key) => key.rt);
      }
    }
    
    
    // *mov00* updates
    if (t >= 0.0 && mov00.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mov00.tStart = t;  // (not accounting for frame time here)
      mov00.frameNStart = frameN;  // exact frame index
      
      mov00.setAutoDraw(true);
      mov00.play();
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mov00.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mov00.setAutoDraw(false);
    }

    
    // *finish_judge_3* updates
    if (t >= 0.0 && finish_judge_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      finish_judge_3.tStart = t;  // (not accounting for frame time here)
      finish_judge_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { finish_judge_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { finish_judge_3.start(); }); // start on screen flip
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (finish_judge_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      finish_judge_3.status = PsychoJS.Status.FINISHED;
  }

    if (finish_judge_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = finish_judge_3.getKeys({keyList: ['q'], waitRelease: false});
      _finish_judge_3_allKeys = _finish_judge_3_allKeys.concat(theseKeys);
      if (_finish_judge_3_allKeys.length > 0) {
        finish_judge_3.keys = _finish_judge_3_allKeys[_finish_judge_3_allKeys.length - 1].name;  // just the last key pressed
        finish_judge_3.rt = _finish_judge_3_allKeys[_finish_judge_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *fixation* updates
    if (t >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        }
    
    key_resp.stop();
    mov00.stop();
    strCounter = trialCounter.toString();
    
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(finish_judge_3.corr, level);
    }
    psychoJS.experiment.addData('finish_judge_3.keys', finish_judge_3.keys);
    if (typeof finish_judge_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('finish_judge_3.rt', finish_judge_3.rt);
        routineTimer.reset();
        }
    
    finish_judge_3.stop();
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_breaktime_2_allKeys;
var breaktComponents;
function breaktRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'breakt'-------
    t = 0;
    breaktClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_breaktime_2.keys = undefined;
    key_resp_breaktime_2.rt = undefined;
    _key_resp_breaktime_2_allKeys = [];
    text_shintyoku.setText((strCounter + "/6"));
    // keep track of which components have finished
    breaktComponents = [];
    breaktComponents.push(key_resp_breaktime_2);
    breaktComponents.push(polygon);
    breaktComponents.push(img_inst4);
    breaktComponents.push(text_shintyoku);
    
    breaktComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function breaktRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'breakt'-------
    // get current time
    t = breaktClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_breaktime_2* updates
    if (t >= 60 && key_resp_breaktime_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_breaktime_2.tStart = t;  // (not accounting for frame time here)
      key_resp_breaktime_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_breaktime_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_breaktime_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_breaktime_2.clearEvents(); });
    }

    if (key_resp_breaktime_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_breaktime_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_breaktime_2_allKeys = _key_resp_breaktime_2_allKeys.concat(theseKeys);
      if (_key_resp_breaktime_2_allKeys.length > 0) {
        key_resp_breaktime_2.keys = _key_resp_breaktime_2_allKeys[_key_resp_breaktime_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_breaktime_2.rt = _key_resp_breaktime_2_allKeys[_key_resp_breaktime_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *polygon* updates
    if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon.setAutoDraw(false);
    }
    
    if (polygon.status === PsychoJS.Status.STARTED){ // only update if being drawn
      polygon.setPos([((- 5) * t), (- 250)], false);
      polygon.setSize([(600 - (10 * t)), 50], false);
    }
    
    // *img_inst4* updates
    if (t >= 0.0 && img_inst4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      img_inst4.tStart = t;  // (not accounting for frame time here)
      img_inst4.frameNStart = frameN;  // exact frame index
      
      img_inst4.setAutoDraw(true);
    }

    
    // *text_shintyoku* updates
    if (t >= 0.0 && text_shintyoku.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_shintyoku.tStart = t;  // (not accounting for frame time here)
      text_shintyoku.frameNStart = frameN;  // exact frame index
      
      text_shintyoku.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    breaktComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function breaktRoutineEnd() {
  return async function () {
    //------Ending Routine 'breakt'-------
    breaktComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(key_resp_breaktime_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_breaktime_2.keys', key_resp_breaktime_2.keys);
    if (typeof key_resp_breaktime_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_breaktime_2.rt', key_resp_breaktime_2.rt);
        routineTimer.reset();
        }
    
    key_resp_breaktime_2.stop();
    // the Routine "breakt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_catch_allKeys;
var mov_catchClock;
var mov_catch;
var catch_trialComponents;
function catch_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'catch_trial'-------
    t = 0;
    catch_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(60.000000);
    // update component parameters for each repeat
    key_resp_catch.keys = undefined;
    key_resp_catch.rt = undefined;
    _key_resp_catch_allKeys = [];
    mov_catchClock = new util.Clock();
    mov_catch = new visual.MovieStim({
      win: psychoJS.window,
      name: 'mov_catch',
      units: 'pix',
      movie: 'mp4/catch.mp4',
      pos: [0, 0],
      size: [1120, 896],
      ori: 0.0,
      opacity: undefined,
      loop: true,
      noAudio: false,
      });
    // keep track of which components have finished
    catch_trialComponents = [];
    catch_trialComponents.push(key_resp_catch);
    catch_trialComponents.push(mov_catch);
    catch_trialComponents.push(fixation_catch);
    
    catch_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function catch_trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'catch_trial'-------
    // get current time
    t = catch_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_catch* updates
    if (t >= 0.0 && key_resp_catch.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_catch.tStart = t;  // (not accounting for frame time here)
      key_resp_catch.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_catch.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_catch.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_catch.clearEvents(); });
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_catch.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_catch.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_catch.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_catch.getKeys({keyList: ['f', 'j', 'space'], waitRelease: false});
      _key_resp_catch_allKeys = _key_resp_catch_allKeys.concat(theseKeys);
      if (_key_resp_catch_allKeys.length > 0) {
        key_resp_catch.keys = _key_resp_catch_allKeys.map((key) => key.name);  // storing all keys
        key_resp_catch.rt = _key_resp_catch_allKeys.map((key) => key.rt);
      }
    }
    
    
    // *mov_catch* updates
    if (t >= 0.0 && mov_catch.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mov_catch.tStart = t;  // (not accounting for frame time here)
      mov_catch.frameNStart = frameN;  // exact frame index
      
      mov_catch.setAutoDraw(true);
      mov_catch.play();
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mov_catch.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mov_catch.setAutoDraw(false);
    }

    
    // *fixation_catch* updates
    if (t >= 0.0 && fixation_catch.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_catch.tStart = t;  // (not accounting for frame time here)
      fixation_catch.frameNStart = frameN;  // exact frame index
      
      fixation_catch.setAutoDraw(true);
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_catch.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_catch.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    catch_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function catch_trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'catch_trial'-------
    catch_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(key_resp_catch.corr, level);
    }
    psychoJS.experiment.addData('key_resp_catch.keys', key_resp_catch.keys);
    if (typeof key_resp_catch.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_catch.rt', key_resp_catch.rt);
        }
    
    key_resp_catch.stop();
    mov_catch.stop();
    return Scheduler.Event.NEXT;
  };
}


var outroComponents;
function outroRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'outro'-------
    t = 0;
    outroClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    outroComponents = [];
    outroComponents.push(text);
    
    outroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function outroRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'outro'-------
    // get current time
    t = outroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    outroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function outroRoutineEnd() {
  return async function () {
    //------Ending Routine 'outro'-------
    outroComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
