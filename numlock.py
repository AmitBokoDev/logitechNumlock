import logipyover.logi_led as led
import time
import ctypes

R=0
G=255
B=255

def get_key_state(vk):
    """ Return True if the key is active (NumLock, CapsLock, etc.). """
    return bool(ctypes.windll.user32.GetKeyState(vk))

def main():
    # Initialize the LED SDK
    if not led.logi_led_init():
        print("Failed to initialize Logi LED SDK.")
        return
    
    time.sleep(1)  # Give the SDK a second to initialize

    led.logi_led_set_lighting(R,G,B)
    NUM_LOCK_HID_CODE = 0x53  # HID code for NumLock
    CAPS_LOCK_HID_CODE = 0x39  # HID code for Caps Lock
    SCROLL_LOCK_HID_CODE = 0x47  # HID code for Scroll Lock

    try:
        while True:
            numlock_active = get_key_state(0x90)  # Virtual-Key code for NumLock
            capslock_active = get_key_state(0x14)  # Virtual-Key code for Caps Lock
            scrolllock_active = get_key_state(0x91)  # Virtual-Key code for Scroll Lock

            # Control the Num Lock LED based on its active state
            if numlock_active:
                led.logi_led_set_lighting_for_key_with_hid_code(NUM_LOCK_HID_CODE,R,G,B)
            else:
                led.logi_led_set_lighting_for_key_with_hid_code(NUM_LOCK_HID_CODE, 0, 0, 0)
            
            # Control the Caps Lock LED based on its active state
            if capslock_active:
                led.logi_led_set_lighting_for_key_with_hid_code(CAPS_LOCK_HID_CODE,R,G,B)
            else:
                led.logi_led_set_lighting_for_key_with_hid_code(CAPS_LOCK_HID_CODE, 0, 0, 0)

            # Control the Scroll Lock LED based on its active state
            if scrolllock_active:
                led.logi_led_set_lighting_for_key_with_hid_code(SCROLL_LOCK_HID_CODE,R,G,B)
            else:
                led.logi_led_set_lighting_for_key_with_hid_code(SCROLL_LOCK_HID_CODE, 0, 0, 0)
            
            time.sleep(0.1)  # Update state every 100ms
    finally:
        # Shut down the LED SDK when ending the program
        led.logi_led_shutdown()

if __name__ == "__main__":
    main()
