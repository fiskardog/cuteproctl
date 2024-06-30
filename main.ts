bitcommander.onEvent(BCPins.Yellow, BCEvents.Down, function my_function() {
    radio.sendValue("cmd", 3)
    bitcommander.setLedColor(0xFFFF00)
})
bitcommander.onEvent(BCPins.Blue, BCEvents.Down, function my_function2() {
    radio.sendValue("cmd", 2)
    bitcommander.setLedColor(0x0080FF)
})
bitcommander.onEvent(BCPins.Green, BCEvents.Down, function my_function3() {
    radio.sendValue("cmd", 1)
    bitcommander.setLedColor(0x18E600)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendValue("cmd", 5)
    bitcommander.ledClear()
    basic.showIcon(IconNames.Cow)
})
bitcommander.onEvent(BCPins.Joystick, BCEvents.Down, function my_function4() {
    radio.sendValue("cmd", 5)
    bitcommander.ledClear()
})
bitcommander.onEvent(BCPins.Red, BCEvents.Down, function my_function5() {
    radio.sendValue("cmd", 0)
    bitcommander.setLedColor(0xFF0000)
})
/** 

Bit:Commander to send  numeric command based

on button pushed.

Stop everything on joystick button, or  button B.


 */
basic.showIcon(IconNames.TShirt)
bitcommander.ledBrightness(20)
radio.setGroup(1)
basic.forever(function on_forever() {
    
})
