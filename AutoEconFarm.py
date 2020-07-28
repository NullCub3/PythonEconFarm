import time
import keyboard
import pyautogui

# Setting Variables
i = 0
spacing = 0.1
wait = 60*10

fee = 40
split = 0.25

auto_dep = False

# Recipients list, with added characters to prevent automated spamming of our usernames.
safe_recipients = ["N@u@l@l@C@u@b@e@#@2@3@3@4@", "P@o@s@s@i@b@l@y@_@C@a@n@o@n@#@4@8@0@9@"]
recipients_num = len(safe_recipients)
recipients = safe_recipients

# Makes the safe_recipients list usable
while i < recipients_num:
    recipients[i] = recipients[i].replace("@", "")
    i += 1

# Message box alerting user that the program is running.
pyautogui.alert("Running!")

# Setting first wait_time so that it doesn't have an infinite loop.
wait_time = wait + time.mktime(time.localtime())

while True:  # Main loop
    current_time = time.mktime(time.localtime())  # Getting the current time.

    if keyboard.is_pressed('esc'):  # Allows stopping of program by the esc key
        pyautogui.alert("Stopped!")
        break

    elif keyboard.is_pressed('q'):  # checks if the Q key has been pressed.
        auto_dep = not auto_dep  # Toggles the boolean auto_dep
        pyautogui.press('backspace')  # Removes the Q from the chat box

        pyautogui.alert("AutoDep is " + ("off", "on")[auto_dep] + "!")  # message box with the status of AutoDep

    elif current_time > wait_time:  # Checking if it is at or past the special wait_time
        pyautogui.write('\n+work\n')  # Presses enter to clear the box types "+work" and presses enter again

        if auto_dep:  # Checks to see if auto_dep is enabled.
            pyautogui.write('+dep all\n')  # Typing in "+dep all" and presses enter
            pyautogui.write('+with ' + str(fee) + '\n')

        # Sends the fee to the recipients
        pyautogui.write('+give ' + recipients[0] + ' ' + str(fee * (1 - split)) + '\n')
        pyautogui.write('+give ' + recipients[1] + ' ' + str(fee * split) + '\n')

        wait_time = wait + current_time  # Sets a new wait_time
        time.sleep(spacing)  # Waits for spacing seconds to prevent bad stuff
