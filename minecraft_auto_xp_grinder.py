import pyautogui
import time
import random

def press_and_hold_mouse(duration):
    """
    Presses and holds the left mouse button for the specified duration.
    """
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()

def press_key(key):
    """
    Presses a specified keyboard key.
    """
    pyautogui.press(key)
    time.sleep(0.1)  # Small delay to ensure the key press is registered

def eat_food():
    """
    Switches to slot 7, holds right-click to eat food, and returns to the attack routine.
    """
    press_key('7')  # Switch to slot 7 (food)
    print("Swapped to food in slot 7")
    pyautogui.mouseDown(button='right')  # Start holding right-click
    print("Eating food...")
    time.sleep(5)  # Hold right-click for 5 seconds to eat
    pyautogui.mouseUp(button='right')  # Release right-click
    print("Finished eating food")
    press_key(str(current_sword_slot))  # Return to the last sword slot
    print(f"Swapped back to sword in slot {current_sword_slot}")

counter = 0
round_counter = 0
current_sword_slot = 1  # Start with slot 1
time.sleep(5)

while True:
    counter += 1
    round_counter += 1
    for i in range(12):
        deviation = random.uniform(-0.01, 0.01)  # Random deviation between -0.01 and 0.01 seconds
        press_and_hold_mouse(0.085 + deviation)
        print("Attack")
        click_rate_dev = random.uniform(-0.15, 0.15)  # Random deviation between -0.15 and 0.15 seconds
        time.sleep(0.75 + click_rate_dev)
    time.sleep(30)
    
    if round_counter >= 5:
        eat_food()
        round_counter = 0  # Reset the round counter after eating
    else:
        # Swap sword by pressing the current_sword_slot key
        press_key(str(current_sword_slot))
        print(f"Swapped to sword in slot {current_sword_slot}")
        
        # Update to the next sword slot (cycle from 1 to 6)
        current_sword_slot += 1
        if current_sword_slot > 5:
            current_sword_slot = 1
