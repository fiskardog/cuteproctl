def my_function():
    radio.send_value("cmd", 3)
    bitcommander.set_led_color(0xFFFF00)
bitcommander.on_event(BCPins.YELLOW, BCEvents.DOWN, my_function)

def my_function2():
    radio.send_value("cmd", 2)
    bitcommander.set_led_color(0x0080FF)
bitcommander.on_event(BCPins.BLUE, BCEvents.DOWN, my_function2)

def my_function3():
    radio.send_value("cmd", 1)
    bitcommander.set_led_color(0x18E600)
bitcommander.on_event(BCPins.GREEN, BCEvents.DOWN, my_function3)

def on_button_pressed_b():
    radio.send_value("cmd", 5)
    bitcommander.led_clear()
    basic.show_icon(IconNames.COW)
input.on_button_pressed(Button.B, on_button_pressed_b)

def my_function4():
    radio.send_value("cmd", 5)
    bitcommander.led_clear()
bitcommander.on_event(BCPins.JOYSTICK, BCEvents.DOWN, my_function4)

def my_function5():
    radio.send_value("cmd", 0)
    bitcommander.set_led_color(0xFF0000)
bitcommander.on_event(BCPins.RED, BCEvents.DOWN, my_function5)

"""

Bit:Commander to send  numeric command based

on button pushed.

Stop everything on joystick button, or  button B.

"""
basic.show_icon(IconNames.TSHIRT)
bitcommander.led_brightness(20)
radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)
