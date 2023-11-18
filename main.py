def Verloren(bool2: bool):
    global ik_hoor_geluid
    SpelVoorbereiding(True)
    ik_hoor_geluid = 0
    basic.show_number(ik_hoor_geluid)
    music.play(music.string_playable("F E D C C C C C ", 252),
        music.PlaybackMode.UNTIL_DONE)
def StartSpel(bool22: bool):
    global teller, pauze
    basic.show_string(start_zin)
    for index in range(3):
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_number(teller)
        teller = teller - 1
    basic.pause(250)
    music.play(music.tone_playable(988, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_number(ik_hoor_geluid)
    pauze = 0
def Gewonnen(bool3: bool):
    global pauze
    SpelVoorbereiding(True)
    pauze = 1
    music.play(music.string_playable("A F E F D G E F ", 120),
        music.PlaybackMode.IN_BACKGROUND)
    for index2 in range(3):
        basic.show_icon(IconNames.SQUARE)
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    music.stop_melody(MelodyStopOptions.ALL)

def on_button_pressed_a():
    global ik_hoor_geluid
    if pauze == 0:
        ik_hoor_geluid = ik_hoor_geluid - 1
        basic.show_number(ik_hoor_geluid)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global ik_hoor_geluid
    if pauze != 1:
        ik_hoor_geluid = ik_hoor_geluid + 10
        basic.show_number(ik_hoor_geluid)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    SpelVoorbereiding(True)
    StartSpel(True)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_gesture_tilt_right():
    global ik_hoor_geluid
    if pauze != 1:
        ik_hoor_geluid = ik_hoor_geluid + 2
        basic.show_number(ik_hoor_geluid)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_button_pressed_b():
    global ik_hoor_geluid
    if pauze != 1:
        ik_hoor_geluid = ik_hoor_geluid + 1
        basic.show_number(ik_hoor_geluid)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_sound_loud():
    global ik_hoor_geluid
    if pauze != 1:
        ik_hoor_geluid = ik_hoor_geluid + randint(-5, 5)
        basic.show_number(ik_hoor_geluid)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_gesture_tilt_left():
    global ik_hoor_geluid
    if pauze != 1:
        ik_hoor_geluid = ik_hoor_geluid - 2
        basic.show_number(ik_hoor_geluid)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def SpelVoorbereiding(bool32: bool):
    global pauze, tijd, punten, ik_hoor_geluid, teller, start_zin
    pauze = 1
    tijd = randint(50, 100)
    punten = randint(25, 75)
    ik_hoor_geluid = 0
    teller = 3
    start_zin = "" + str(tijd) + " sec. voor " + str(punten) + " punten"
seconde = 0
punten = 0
tijd = 0
pauze = 0
teller = 0
start_zin = ""
ik_hoor_geluid = 0
SpelVoorbereiding(True)
StartSpel(True)

def on_forever():
    global seconde
    if pauze == 0:
        seconde = seconde + 1
        basic.pause(1000)
    else:
        seconde = 0
basic.forever(on_forever)

def on_forever2():
    if pauze == 0:
        if ik_hoor_geluid == punten:
            Gewonnen(True)
            StartSpel(True)
basic.forever(on_forever2)

def on_forever3():
    if pauze == 0:
        if seconde == tijd:
            Verloren(True)
            StartSpel(True)
basic.forever(on_forever3)
