import time
from datetime import datetime

def run_timer(minutes):
    # Convert total minutes to seconds
    total_seconds = minutes * 60
    
    while total_seconds >= 0:
        # Get current date and time
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Calculate minutes and seconds remaining
        mins, secs = divmod(total_seconds, 60)
        
        # Format the timer string
        timer_display = f"{mins:02d}:{secs:02d}"
        
        # Print date and timer on the same line
        # end="\r" returns the cursor to the start of the line
        print(f"Date: {now} | Time Remaining: {timer_display}", end="\r")
        
        # Wait for 1 second
        time.sleep(1)
        
        # Decrease total seconds
        total_seconds -= 1

    print("\nTime's up!")

# Run the timer for 7 minutes
if __name__ == "__main__":
    run_timer(7)