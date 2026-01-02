# (Always at the top in python)
# 1
# Imports  /  Dependencies
import time
from machine import Pin, PWM
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER
from pimoroni import Button

# 2
# Hardware_Objects
# idk if i am supposed to add anything gpio/related in this section
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
WIDTH, HEIGHT = display.get_bounds()
display.set_font("bitmap8")

button_a = Button(12)    # EACH piece of hardware must be defined / where it interacts with board
button_b = Button(13)
button_y = Button(15)
button_x = Button(14)


# Program_State
# single source of truth for which screen/mode is active

state = "CLOCK"    # current screen/mode



# Memory
# Am I being pressed right now?

prev_a = False  # false means not in use
prev_b = False
prev_x = False
prev_y = False

# Trigger
# current is true and prev is false
# buttons are only allowed to report facts
# # 1. Read inputs
    # 2. Detect edges
    # 3. Change state
    # 4. Draw based on state
    # 5. Update memory
    # 6. Sleep (frame pacing)


# this function is the ONLY place that touches the screen.
# It recieves the truth (state) and renders accordingly.

def draw_state(current_state):
    
    display.clear()

    if current_state == "CLOCK":
        display.text("CLOCK SCREEN", 10,10, scale =2)

    elif current_state == "MENU":
        display.text("MENU SCREEN", 10, 10, scale=2)

    else:
        display.text("UNKNOWN STATE", 10, 10, scale=2)

    display.update()


while True:   # Keeps the Pico alive, Creates “frames”, Lets us add logic incrementally without crashes

    # 1. Read raw button states
    a_now = button_a.read()
    b_now = button_b.read()
    x_now = button_x.read()
    y_now = button_y.read()

    # 2. detect rising edges (press events)

    a_pressed = a_now and not prev_a
    b_pressed = b_now and not prev_b
    x_pressed = x_now and not prev_x
    y_pressed = y_now and not prev_y

    # 3. state changes (placeholder)
    # if a_pressed:
    #    state = "MENU"

    # 4.draw based on state (placeholder)
    # draw_clock()
    # draw_menu()

    # 5. update memory (MUST happen every frame)

    prev_a = a_now
    prev_b = b_now
    prev_x = x_now
    prev_y = y_now
    # 6. sleep (frame pacing)

    time.sleep(0.05)  # 20fps

