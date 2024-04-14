# logitechNumlock

A basic python script that turns the numlock (and caps an scroll lock) rgb on and off depending on the state\
I made this because of Logitech's dumb desicion TO NOT PUT A NUM LOCK INDICATOR ON THE KEYBOARD LIKE WHAT THE FUCK

## features
- one color
- num lock indication (and the others)

## how to use 
- intall python
- install Logitch G Hub
- in `/logipyover/logi_led.py` line 260 make sure it points at the right file (by default `C:\Program Files\LGHUB\sdks\sdk_legacy_led_{bitness}.dll`)
- in `numlock.py` change the RGB values to your favorite color (by default `0,255,255`)
- run `python numlcok.py`