import keyboard
import json
from pydub import AudioSegment
from pydub.playback import play


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

device = None
config = None
available_keys = []
mapped_sounds = {}

with open('./config.json') as file:
    config = json.load(file)
    mapped_sounds = config["mapped_sounds"]
    device = config["device"]
    # print("-------------------------")
    # print(mapped_sounds)
    # print("-------------------------")
    # print(available_keys)
    # print("-------------------------")

## Dedicated function for play sounds
def _play_sound(sound):
    msg = "Ready to play {}"
    print(msg.format(sound))

    ## This plays audio via ffmpeg
    song = None
    if sound.lower().endswith('.mp3'):
        song = AudioSegment.from_mp3(sound)
    if sound.lower().endswith(('.wav', 'wave')):
        song = AudioSegment.from_wav(sound)
    if song is not None:
        play(song)
    else:
        msg = "{} is not in a valid format. Only mp3 and wave are permitted"
        print(msg.format(sound))

## Detects if the pressed key come from the right device and is related to a
## command
def _detect_key(event):
    if event.device == device:
        scan_code = "{}".format(event.scan_code)
        if scan_code in mapped_sounds.keys():
            msg = "Pressed {} and play a sound".format(scan_code)
            print(msg)
            _play_sound(mapped_sounds[scan_code])
        else:
            print("{} is not in keys ".format(event.scan_code))
            print(mapped_sounds.keys())

## Hook the function for key detection on key release
keyboard.on_release(_detect_key)

## Wait a key is released (like while True:)
keyboard.wait()
