import pyautogui
import keyboard
import threading
import time

clicking = False
click_speed = 0.01  # Default click speed (10ms delay)

def clicker():
    """Runs the auto-clicker in a separate thread."""
    global clicking, click_speed
    while True:
        if clicking:
            pyautogui.click()
            time.sleep(click_speed)
        else:
            time.sleep(0.1)  # Reduce CPU usage when paused

def main():
    global clicking, click_speed

    print("=== Python Auto Clicker ===")
    print("Press 's' to start clicking.")
    print("Press 'p' to pause clicking.")
    print("Press 'q' to quit the program.")
    print("Press '+' to increase click speed.")
    print("Press '-' to decrease click speed.")

    # Start the auto-clicker in a separate thread
    threading.Thread(target=clicker, daemon=True).start()

    try:
        while True:
            # Start clicking
            if keyboard.is_pressed('s'):
                if not clicking:
                    clicking = True
                    print(f"Auto clicking started! (Speed: {click_speed:.3f} sec)")
                    time.sleep(0.5)

            # Pause clicking
            if keyboard.is_pressed('p'):
                if clicking:
                    clicking = False
                    print("Auto clicking paused!")
                    time.sleep(0.5)

            # Increase click speed
            if keyboard.is_pressed('+'):
                if click_speed > 0.001:  # Minimum delay is 1ms
                    click_speed -= 0.001
                    print(f"Click speed increased! (New speed: {click_speed:.3f} sec)")
                    time.sleep(0.3)

            # Decrease click speed
            if keyboard.is_pressed('-'):
                if click_speed < 1.0:  # Maximum delay is 1 second
                    click_speed += 0.001
                    print(f"Click speed decreased! (New speed: {click_speed:.3f} sec)")
                    time.sleep(0.3)

            # Quit the program
            if keyboard.is_pressed('q'):
                print("Quitting auto clicker. Goodbye!")
                clicking = False
                break

            time.sleep(0.1)  # Small delay to reduce CPU usage
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")

if __name__ == '__main__':
    main()
