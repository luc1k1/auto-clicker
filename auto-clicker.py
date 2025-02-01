import pyautogui
import keyboard
import time

def main():
    print("=== Python Auto Clicker ===")
    print("Press 's' to start clicking.")
    print("Press 'p' to pause clicking.")
    print("Press 'q' to quit the program.")

    clicking = False

    try:
        while True:
            # Start auto clicking when 's' is pressed.
            if keyboard.is_pressed('s'):
                if not clicking:
                    clicking = True
                    print("Auto clicking started!")
                    # Debounce so that the start command isn't registered multiple times.
                    time.sleep(0.5)

            # Pause auto clicking when 'p' is pressed.
            if keyboard.is_pressed('p'):
                if clicking:
                    clicking = False
                    print("Auto clicking paused!")
                    time.sleep(0.5)

            # Exit the program when 'q' is pressed.
            if keyboard.is_pressed('q'):
                print("Quitting auto clicker. Goodbye!")
                break

            # If the auto clicker is active, simulate a mouse click.
            if clicking:
                pyautogui.click()
                # Adjust the sleep time to change the clicking speed.
                time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")

if __name__ == '__main__':
    main()
