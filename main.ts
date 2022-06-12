let following = 0
let distance = 0
basic.showLeds(`
    # . # . #
    # # # # #
    . . # . .
    . # . # .
    . # . # .
    `)
let tries = 0
basic.forever(function () {
    distance = Tinybit.Ultrasonic_Car()
    if (following == 1) {
        if (distance <= 100) {
            if (distance <= 30) {
                Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Back, 49)
            } else if (distance >= 66) {
                Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 47)
            }
        } else {
            tries += 1
            basic.showString("" + (tries))
            if (tries >= 3) {
                music.playTone(262, music.beat(BeatFraction.Sixteenth))
                following = 0
            }
            Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Left, 49)
        }
    } else if (distance <= 30) {
        music.playTone(988, music.beat(BeatFraction.Sixteenth))
        following = 1
    } else {
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        tries = 0
    }
})
