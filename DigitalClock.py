import turtle
import time

# Set up the turtle window
window = turtle.Screen()
window.bgcolor("black")
window.setup(width=500, height=250)
window.title("DigitalClock")


turtle.hideturtle()
turtle.color("white")
turtle.goto(0, 0)
turtle.speed(0)

# Main loop to keep updating the time
while True:
    turtle.clear()  # Clear the previous time
    TehranTime = time.localtime()  # Get the local time (Tehran's time if your system is set to that timezone)

    # Format the time as HH:MM:SS
    current_time = f"{TehranTime.tm_hour:02}:{TehranTime.tm_min:02}:{TehranTime.tm_sec:02}"

    # Display the time on the screen
    turtle.write(current_time, align="center", font=("Arial", 50, "bold"))

    time.sleep(1)  # Pause for 1 second before updating again



