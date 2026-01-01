# (AI)
# (
# Imports / Dependencies
# This section is where you declare what your program is allowed to use.
# Nothing runs here.
# Nothing happens to the hardware.
# You are simply saying:
# “This program depends on time, hardware pins, graphics, and buttons.”
# If something isn’t imported here, it does not exist to the rest of the file.
# That’s why this always lives at the very top.
# )

# Imports  /  Dependencies
import time
from machine import Pin, PWM
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER
from pimoroni import Button

# (AI)
# (
# Hardware Objects
# This section is where you bind software names to physical things.
# Each variable here represents a real object on the board:
# the display
# each button
# later: buzzers, LEDs, sensors, etc.
# After this section:
# You never think about pin numbers again
# You talk to objects, not wires
# This is the layer that separates electronics from program logic.
# )

# Hardware_Objects
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)

button_a = Button(12)    # EACH piece of hardware must be defined / where it interacts with board
button_b = Button(13)
button_y = Button(15)
button_x = Button(14)

# (AI)
# (
# Program State (Single Source of Truth)
# This section defines what the program believes is happening right now.
# The state variable is not a screen.
# It is not a button.
# It is the authoritative answer to the question:
# “What mode is the system currently in?”
# Every part of the program must read this value.
# Only controlled logic is allowed to change it.
# This is what prevents:
# multiple screens drawing at once
# buttons doing random things
# logic fighting itself
# If the system ever feels “confused,” the bug will live here.
# )

# Program_State
# single source of truth for which screen/mode is active

state = "CLOCK"    # current screen/mode


# (AI)
# (
# Button history
# Used to detect transitions (pressed/released) instead of
# continuous button holds
# )

# Memory
# Am I being pressed right now?

prev_a = False  # false means not in use
prev_b = False
prev_x = False
prev_y = False

# Trigger
# current is true and prev is false
# buttons are only allowed to report facts
 
while True:   # Keeps the Pico alive, Creates “frames”, Lets us add logic incrementally without crashes
    a_now = button_a.read()
    b_now = button_b.read()
    x_now = button_x.read()
    y_now = button_y.read()

    a_pressed = a_now and not prev_a
    b_pressed = b_now and not prev_b
    x_pressed = x_now and not prev_x
    y_pressed = y_now and not prev_y


    pass

