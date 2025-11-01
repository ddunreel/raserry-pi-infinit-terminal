import subprocess
import time

def main():
    print("Opening a new terminal window...")

    # Use your preferred terminal here
    subprocess.run(['lxterminal', '-e', 'bash -c "echo and another one !; exec bash"'])
    
    time.sleep(0.0)  # Shorter delay of 0.1 seconds

if __name__ == "__main__":
    while True:  # Infinite loop
        main()


