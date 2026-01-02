# 🧠 Why this is exactly right
“How does this program think?”
"What is this program even trying to accomoplish?"
### main idea 
  Well, I figured I would do a little experiment to see if i can get chatgpt help me code a little UI
  for the pimoroni pico explorer.

  I paired this device up with a raspberry pi pico W. Since the day I purchased this little device I knew that the
 demos given on the website werent enough. 

 I was in luck. This is the perfect device for that. I am really stoked to have one (my own money)

 I want to make a little UI that can let you navigate through a menu play a game or two and maybe more one day.
 (If My AHDH doesnt lock in on something before i finish this)

 Anyways all of that being said I will be leaving a whole bunch of comments within the code
 so if anyone could suggest me how to code better ...??...

 This is going to be "one of the fist" projects i do before i clean my github

# this is going to be the very first section always in python
 
### Imports / Dependencies
 This section is where you declare what your program is allowed to use.
 Nothing runs here.
 Nothing happens to the hardware.
 You are simply saying:
 “This program depends on time, hardware pins, graphics, and buttons.”
 If something isn’t imported here, it does not exist to the rest of the file.
 That’s why this always lives at the very top.
 

# this is this 2nd section from the top
 
### Hardware Objects
 This section is where you bind software names to physical things.
 Each variable here represents a real object on the board:
 the display
 each button
 later: buzzers, LEDs, sensors, etc.
 After this section:
 You never think about pin numbers again
 You talk to objects, not wires
 This is the layer that separates electronics from program logic.
 

# at this point i am not sure if this takes a specific place in the code's structure
 
### Program State (Single Source of Truth)
 This section defines what the program believes is happening right now.
 The state variable is not a screen.
 It is not a button.
 It is the authoritative answer to the question:
 “What mode is the system currently in?”
 Every part of the program must read this value.
 Only controlled logic is allowed to change it.
 This is what prevents:
 multiple screens drawing at once
 buttons doing random things
 logic fighting itself If the system ever feels “confused,” the bug will live here.



 
### Button history
 Used to detect transitions (pressed/released) instead of
 continuous button holds


# the main loop 
## this loop needs to only live in the main.py

it is not entirely clear to me why at this point but i will update soon

