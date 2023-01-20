let RPS = 0
input.onButtonPressed(Button.A, function () {
    RPS = randint(1, 3)
    if (RPS == 1) {
        basic.showString("R")
    } else if (RPS == 2) {
        basic.showString("P")
    } else {
        basic.showString("S")
    }
})
basic.forever(function () {
	
})
