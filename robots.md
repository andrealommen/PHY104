---
layout: page
author: Andrea Lommen
title:  Robots 
permalink: /robots/
---


## Robots assignments and due dates<br>
Before each date listed below, ask a TA or an instructor to 
verify that you've completed the task.  The hope is that you can often get the items checked off during your lab period.  If not, there are plenty of TA hours.

### By Sunday February 9 <br>
Upgrade your robot with the new motors.  Demonstrate that you can get it to move.

### By Friday February 14 <br>
Write a function that makes your robot drive straight for any distance you desire.  The distance should be an argument of the function, and it should be in units you can measure, e.g. cm. 
The TA/instructor will name a distance, and your robot should go that distance. 

### By Friday February 21 <br>
Write a function that makes your robot turn any number of degrees you specify. The number of degrees should be the argument of the function.  If the number is positive it should turn to the right.  If negative it should turn to the left. The TA/instructor will give you a number of degrees, and your robot should turn that number of degrees.

### Nothing due by Friday February 28 <br>
Since homework2 is due this week, we wanted to give you some time in lab to ask questions about it during your lab period.

### By Friday March 7 <br>
Combine your two functions to get your robot to follow one of the paths laid out in masking tape by the TAs. 

### Nothing due by Friday Mar 14, spring break <br>

### By Sunday Mar 23 <br>
Implement Infrared Navigation

[Infrared Navigation Tutorials here](https://learn.parallax.com/courses/infrared-light-navigation-for-the-cyberbot/)

You don't need all of them.  Here are the ones you need:

*	Infrared Light Signals (just skim for background)
*	Build the IR circuits
*	Test the IR Object Detectors
*	(skip several things here)
*	Faster IR Navigation (You might want to play around with where the IR sensors are aimed.  I found them pointed away from each other slightly and down slightly to be helpful. ). Instead of using their script. Use mine: [ir_navigation.py](./ir_navigation.py) 

To get checked off on this lab you have to 
*	Explain to the TA/Suzanne how the code works. 
*	Make a list of situations in which the robot gets stuck. (We’ll see if we can fix one or more of them next week) 

### By Sunday Mar 30 <br>
Adding contingencies. Your robot responds to one set of sensors now (infrared) which is very cool.  In order to make it more robust and reliable (i.e. not get stuck) add code to get your robot out of sticky situations and demonstrate to your TAs that it works at least part of the time. (From my humble experience over break, you have to be realistic here.  You're not going to be able  to write code that will let the robot roam forever the floor of your dorm without stopping.   
Here are some ideas.  You can do one of these or invent something else.  Your choice.  In all cases the challenge will be combining your existing infrared code with if’s and else’s (or try's and except's) etc such that your new code improves the situation.
*	I wrote some code to detect whether a wheel has stopped [here](./stall_check.py). This didn’t work so well because when it gets stuck the wheels don’t stop (they often spin).  It did work part of the time.
*	Add the [whiskers](https://learn.parallax.com/courses/touch-navigation-for-the-cyberbot/) so that if actually bumps into something it’ll back up. Don't forget that you have to combine the infrared sensor and the whiskers in one program to make your robot smarter.   
*	Add code that detects when the infrared light readings haven’t changed in awhile. If they haven't, perhaps your robot is stuck in one place, and you should have it back up.  
*	There’s an accelerometer  on the microbit.  You could use that to detect that it’s not moving. (Disclaimer, I have not tried this.) 
*	There’s an optical light sensor that you can install as well.  There’s a [parallax tutorial for this](https://learn.parallax.com/courses/visible-light-navigation-for-the-cyberbot/).  Don’t forget you have to combine the infrared sensor and the optical sensor information in your program.
o	If it gets into a corner it can get caught going back and forward forever.  Make it back out of the corner in that situation. I'm thinking of a clever "if" loop that somehow keeps track of whether it’s repeating itself.  I didn’t actually try this one.

To get checked off you have to explain your code to Suzanne or a TA, and demonstrate that without your code, the robot gets stuck in a particular situation, but with your code it succeeds!

### No more robot assignments until mid-April, because I want you to have a chance to work on your project and Homework4

### Last Robot assignment: Due April 28 (but please start by the 14th)
[Roaming robot with ultrasonic ping](https://learn.parallax.com/courses/cyberbot-roaming-with-the-ping/)

### Other optional robot projects in case you want to do something besides
the cyberbot roaming with the ping  

### Add the capability to avoid drop-offs 
(so you can put your robot on a table).
I updated the infrared-light-detection code for you to reflect the new servos you installed, but you'll have to update the code yourself for this project. You'll notice the sugggested code says things like ``bot(18).servo_speed(75)`` rather than ``drive.speed(37,37)`` like it should. [This page tells you how to do that.](https://learn.parallax.com/courses/upgrade-your-cyberbot-with-feedback-360-servos/lessons/how-to-update-scripts-for-feedback-360-servos/)
*	[Drop-off Detector](https://learn.parallax.com/courses/infrared-light-navigation-for-the-cyberbot/lessons/drop-off-detector/)
*	[Simulate a drop-off](https://learn.parallax.com/courses/infrared-light-navigation-for-the-cyberbot/lessons/simulate-a-drop-off-with-poster-board/)
*	[Avoid Drop-offs](https://learn.parallax.com/courses/infrared-light-navigation-for-the-cyberbot/lessons/avoid-drop-offs/)	

### Using another board as a controller

* Watch the little video here just to see what we're trying to do. [tilt control](https://learn.parallax.com/courses/cybersecurity-radio-tilt-control_makecode/)
* Some instructions will appear here...hopefully in time for you to follow them.

