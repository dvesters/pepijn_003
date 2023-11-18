function Verloren (bool: boolean) {
    SpelVoorbereiding(true)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(247, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(220, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(196, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(175, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(165, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(131, music.beat(BeatFraction.Breve)), music.PlaybackMode.UntilDone)
    scoren = 0
    basic.showNumber(scoren)
}
input.onGesture(Gesture.LogoDown, function () {
    actie("-", 10)
})
function StartSpel (bool2: boolean) {
    basic.showString(start_zin)
    for (let index = 0; index < 3; index++) {
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        basic.showNumber(teller)
        teller = teller - 1
    }
    basic.pause(250)
    music.play(music.tonePlayable(988, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    seconde = 0
    basic.showNumber(scoren)
    pauze = 0
}
function Gewonnen (bool: boolean) {
    SpelVoorbereiding(true)
    pauze = 1
    music.play(music.stringPlayable("E F F G C5 B C5 C5 ", 451), music.PlaybackMode.LoopingInBackground)
    for (let index = 0; index < 3; index++) {
        basic.showIcon(IconNames.Square)
        basic.showIcon(IconNames.SmallSquare)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    }
    music.stopMelody(MelodyStopOptions.All)
}
input.onButtonPressed(Button.A, function () {
    actie("-", 1)
})
input.onGesture(Gesture.Shake, function () {
    actie("?", 5)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    SpelVoorbereiding(true)
    pauze = 0
    StartSpel(true)
})
input.onGesture(Gesture.TiltRight, function () {
    actie("+", 2)
})
input.onGesture(Gesture.LogoUp, function () {
    actie("+", 10)
})
input.onButtonPressed(Button.B, function () {
    actie("+", 1)
})
input.onSound(DetectedSound.Loud, function () {
    actie("?", 10)
})
input.onGesture(Gesture.TiltLeft, function () {
    actie("-", 2)
})
function actie (som: string, num: number) {
    if (som == "+") {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        scoren = scoren + num
    } else if (som == "-") {
        music.play(music.tonePlayable(185, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        scoren = scoren - num
    } else {
        actie(tekstlijst._pickRandom(), randint(0 - num, num))
    }
    music.stopAllSounds()
    basic.showNumber(scoren)
    if (pauze != 1) {
    	
    }
}
function SpelVoorbereiding (bool3: boolean) {
    pauze = 1
    led.plotBarGraph(
    2,
    9
    )
    tekstlijst = ["+", "="]
    music.setVolume(35)
    tijd = randint(25, 99)
    punten = randint(25, 99)
    scoren = 0
    teller = 3
    start_zin = "" + tijd + " sec. voor " + punten + " punten"
}
let punten = 0
let tijd = 0
let tekstlijst: string[] = []
let pauze = 0
let seconde = 0
let teller = 0
let start_zin = ""
let scoren = 0
SpelVoorbereiding(true)
StartSpel(true)
loops.everyInterval(1000, function () {
    if (pauze == 0) {
        seconde = seconde + 1
    }
})
basic.forever(function () {
    if (pauze == 0) {
        if (scoren == punten) {
            Gewonnen(true)
            StartSpel(true)
        }
    }
})
basic.forever(function () {
    if (pauze == 0) {
        if (seconde == tijd) {
            Verloren(true)
            StartSpel(true)
        }
    }
})
