def Verloren(bool2: bool):
    global scoren
    SpelVoorbereiding(True)
    music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(247, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(220, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(196, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(175, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(165, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(131, music.beat(BeatFraction.BREVE)),
        music.PlaybackMode.UNTIL_DONE)
    scoren = 0
    basic.show_number(scoren)

def on_gesture_logo_down():
    actie("-", 10)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def StartSpel(bool22: bool):
    global teller, seconde, pauze
    basic.show_string(start_zin)
    for index in range(3):
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_number(teller)
        teller = teller - 1
    basic.pause(250)
    music.play(music.tone_playable(988, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    seconde = 0
    basic.show_number(scoren)
    pauze = 0
def Gewonnen(bool3: bool):
    global pauze
    SpelVoorbereiding(True)
    pauze = 1
    music.play(music.string_playable("E F F G C5 B C5 C5 ", 451),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
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
    actie("-", 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    actie("?", 5)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global pauze
    SpelVoorbereiding(True)
    pauze = 0
    StartSpel(True)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_gesture_tilt_right():
    actie("+", 2)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_up():
    actie("+", 10)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_b():
    actie("+", 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_sound_loud():
    actie("?", 10)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_gesture_tilt_left():
    actie("-", 2)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def actie(som: str, num: number):
    global scoren
    if som == "+":
        music.play(music.tone_playable(988, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        scoren = scoren + num
    elif som == "-":
        music.play(music.tone_playable(185, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        scoren = scoren - num
    else:
        actie(tekstlijst._pick_random(), randint(0 - num, num))
    music.stop_all_sounds()
    basic.show_number(scoren)
    if pauze != 1:
        pass
def SpelVoorbereiding(bool32: bool):
    global pauze, tekstlijst, tijd, punten, scoren, teller, start_zin
    pauze = 1
    led.plot_bar_graph(2, 9)
    tekstlijst = ["+", "="]
    music.set_volume(35)
    tijd = randint(25, 99)
    punten = randint(25, 99)
    scoren = 0
    teller = 3
    start_zin = "" + str(tijd) + " sec. voor " + str(punten) + " punten"
punten = 0
tijd = 0
tekstlijst: List[str] = []
pauze = 0
seconde = 0
teller = 0
start_zin = ""
scoren = 0
SpelVoorbereiding(True)
StartSpel(True)

def on_every_interval():
    global seconde
    if pauze == 0:
        seconde = seconde + 1
loops.every_interval(1000, on_every_interval)

def on_forever():
    if pauze == 0:
        if scoren == punten:
            Gewonnen(True)
            StartSpel(True)
basic.forever(on_forever)

def on_forever2():
    if pauze == 0:
        if seconde == tijd:
            Verloren(True)
            StartSpel(True)
basic.forever(on_forever2)
