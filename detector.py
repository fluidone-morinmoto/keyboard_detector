import keyboard

device = '/dev/input/event13'

codes = [
    29,  #left control
    42,  #left shift
    56,  #alt
    100, #alt gr
    97,  #right control
    54,  #right shift
    58,  #caps lock
    69   #num lock
]

def _detect_key(event):
    if event.device == device:
        if event.scan_code in codes:
            msg = "Pressed '{}' with keycode {} on ther right keyboard"
            print(msg.format(event.name, event.scan_code))

## Hook the function for key detection on key release
keyboard.on_release(_detect_key)

## Wait a key is released (like while True:)
keyboard.wait()
