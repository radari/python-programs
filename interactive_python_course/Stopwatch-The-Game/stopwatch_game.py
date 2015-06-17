# "Stopwatch: The Game" mini-project
# author sturrion

import simplegui

# global variables
tenths = 0				# total time in tenths
interval = 100 			# 0.1 second
width = 350				# canvas width
height = 150			# canvas height
t_position = [50, 120]	# position of the timer in the canvas 
number_stops = 0		# number of stops
correct_stops = 0		# number of correct stops
s_position = [270, 30]  # position of the score in the canvas 
running = False			# variable to have where the stopwatch is running

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths_d = t % 10
    
    secs = int(t /10)
    minutes = int(secs/60)
    
    secs = secs % 60
    secs_b = int(secs / 10)
    secs_c = secs % 10
    
    return str(minutes) + ':' + str(secs_b) + str(secs_c) + '.' + str(tenths_d)

# function to evaluate the result of the stop
def evaluate_stop():
    global number_stops, correct_stops
    if running:
        number_stops += 1
        if tenths % 10 == 0:
            correct_stops += 1

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    global running
    timer.start()
    running = True

def stop_button():
    global running
    timer.stop()
    evaluate_stop()
    running = False
    

def reset_button():
    global running, tenths, number_stops, correct_stops
    timer.stop()
    running = False
    tenths, number_stops, correct_stops = 0, 0, 0

# define event handler for timer with 0.1 sec interval
def increment_tenths():
    global tenths
    tenths += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(tenths), t_position, 100, "Cyan")
    score = str(correct_stops) + ' / ' + str(number_stops)
    canvas.draw_text(score, s_position, 30, "Teal")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start_button, 125)
frame.add_button("Stop", stop_button, 125)
frame.add_button("Reset", reset_button, 125)

timer = simplegui.create_timer(interval, increment_tenths)


# start frame
frame.start()



