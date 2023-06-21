def on_button_pressed_a():
    basic.clear_screen()
    radio.send_string("smile")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    if receivedString == "smile":
        basic.show_icon(IconNames.HAPPY)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    basic.clear_screen()
    radio.send_string("frown")
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(2)