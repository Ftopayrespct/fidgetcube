def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . # . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . .
    """)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_ab():
    basic.show_leds("""
        . # # # .
                . # . # .
                . . # # .
                . . . . .
                . . # . .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . # . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    while True:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . # . .
        """)
        basic.show_leds("""
            . . . # .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . #
        """)
        basic.show_leds("""
            . . # . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . # . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . # . . .
                        . . . . .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . # .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . #
    """)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

basic.show_leds("""
    # . . . #
        # . . . #
        # # # # #
        # . . . #
        # . . . #
""")
basic.show_leds("""
    . . # . .
        . . . . .
        . . # . .
        . . # . .
        . . # . .
""")

def on_forever():
    pass
basic.forever(on_forever)
