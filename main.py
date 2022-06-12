following = 0
distance = 0
basic.show_leds("""
    # . # . #
        # # # # #
        . . # . .
        . # . # .
        . # . # .
""")
Tinybit.RGB_Car_Big(Tinybit.enColor.OFF)
Tinybit.RGB_Car_Program().clear()
Tinybit.RGB_Car_Program().clear()

def on_forever():
    global distance, following
    distance = Tinybit.Ultrasonic_Car()
    if following == 1:
        if distance <= 50:
            if distance <= 30:
                Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_BACK, 60)
            else:
                Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 60)
        else:
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_LEFT, 20)
    else:
        if distance <= 20:
            following = 1
basic.forever(on_forever)

def on_forever2():
    if distance < 5:
        basic.show_arrow(ArrowNames.NORTH)
    elif distance > 5 and distance < 200:
        basic.show_arrow(ArrowNames.SOUTH)
    else:
        basic.clear_screen()
basic.forever(on_forever2)
