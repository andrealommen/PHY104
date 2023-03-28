---
layout: page
author: Andrea Lommen
title: Project 
permalink: /project/
---

You design the final lab of this course.  It’s an individual project. If something brought you to this course that we haven’t talked about yet, please consider designing your project around that.

### Project proposal (due soon after spring break – see grid):
Your project proposal will just be a paragraph (a few sentences) saying:
1) What data set(s) you'll be using.
2) What question you'll be answering using them.

### The Project 
(presented the last week of class, rough draft of slides due about a week 
week beforehand - see grid):

**The TALK**

It'll be 3 slides long:
* Slide 1: Introduction to your data set (where you got it, why you're interested in it, what question you hope to answer, why you think other people would be interested in this question.)
* Slide 2: An interesting challenge your data presented. You might show a little (a very little!) bit of code here, but the main point is to describe the challenge, and the overview of how you solved it.
* Slide 3: Conclusion and graph or graphs.

Not a lot of words on slides, please. 

For your draft due on 10 April (a couple weeks before the end of the semester), you could make a draft of a final plot, or you could describe what you think the plot will look like, or even sketch it on a piece of paper, and put a photograph of it into your slide.
I find that even just making a sketch of what I think the plot (or plots) look like help me think about how to make them.

If you have multiple graphs, the conclusion "slide" could be multiple slides.  But remember that this isn't a PhD thesis, so you really don't need more than 1 or maybe 2 figures.


**Your project must include**:
*	Background about why this question is important.
*	A conclusion drawn from data or simulations.  In other words, it has to answer a question and you have decide what question that is.
*	A collection of at least three tests that your code passes (call it a `test suite' if you will). See my note below for more help/hints/suggestions for this.  
*	Documentation. (Your code must be commented).

**Your project must incorporate 5 of the following 10 elements:**
*	Reading in a public data set 
*	Simulating a data set (see my note below)
*	Plotting one parameter vs another 
*	Modeling the data (e.g. fitting a curve), or doing some numerical analysis such as a correlation analysis 
*	Assessing the validity of your model using residuals 
*	Using only a subset of the data that meet some criterion (e.g. just some rows from your table using the "loc" method or np.where)
*	Aggregating Data (e.g. combining all the different entries for cities in Pennsylvania into one combined entry for Pennsylvania) (Also see my note below)
*	Dictionaries
*	Numerical integration
* 	Use object-oriented programming to accomplish any of the above (e.g. a class and a method)

**Test Suite**

These can be simple tests that your code is working correctly.  Your code must pass them.  One of the tests must involve you feeding some data into your code, data in which you know what the answer should be. 

The options I suggest often:

(1) Create a CSV file that's a fake version of your real file, and show that your code behaves as expected. It can be really small.  For example, if you are trying to show that there's a linear between the price of apples and the year, you could create a csv with two columns "price" and "year".  And you could make a csv that looks like this:

year, price\
2000, 1.0\
2001, 1.10\
2002, 1.20\
2003, 1.30\
2004, 1.40

It's simple, but it's a nice check of your code.  You should be able to run your code on that file just like you did on your real data, and it should show a correlation coeffient of 1.0. 


(2) Same as above, but instead of creating a correlation, use random numbers for the price.  Now it should show close to zero correlation. You should use numpy's random number generator to create the file.

(3) If you're project involves making a histogram, make a histogram over a short version of your file, perhaps just the top 10 rows.  You'll be able to tell by looking if it's making the histogram correctly.

(4) If you're creating a dictionary out of a long file, check on several things you think it should pair, to make sure it paired the right things. 

(5) If you're doing a calculation, make sure the answers are in the range you expected. Hint: you'll have to come up with some other way of determining the range you expected.

(6) If you're eliminating missing data, make sure the plots before and after you took care of the missing data look te way you expected them to.

(7) If you're doing a calculation, do one of the calculations by hand to make sure it matches what you think it should be.

(8) Invent some other test your code should pass, and make sure it passes. 

**Aggregating Data**

Aggregating data is taking multiple entries and making them into one entry.  It could be a sum, an average, ...

**Simulating Data**

This is an option for people who don't want to read in a CSV at all, but actually want to write code that mimics a physical situation, and have that code produce a set of data for them.  For example, I could simulate the random walk of a photon out of the center of the sun.  Every 100th of a second I could have my photon make a turn in a random direction.  I could let my photon travel for a couple thousand years and collect data on its position.  That's simulated data.  Then I could do my project on those data. 

**There are many public data sets.**  See here for a list: https://www.forbes.com/sites/bernardmarr/2016/02/12/big-data-35-brilliant-and-free-data-sources-for-2016/#6a2e0b72b54d

### How is this graded?
This is the 5th lab so it's part of your lab grade. 
It’s graded on the 9 (4 + 5) required elements above (3 points for each), plus I add one criteria that’s just basic awesomeness (did you get into it?) and creativity (did you use your skills to make it cool?) (combined for 3 more points) for a total of 30 points.

### 3-slide powerpoint presentations
*	The main product of the project is the 3-slide powerpoint that you’ll show to the 
rest of the class during the last week of classes.   You'll also turn in the notebook
that shows you completed the items above.

## THE FINAL WEEK

Please sign-up for a presentation day [here:](
https://docs.google.com/spreadsheets/d/1fHfmumgC68f5EPQWtYbUrSy2-SnyMsVxRIW-YTa7VNw/edit#gid=0).

During the final two weeks of class you will do two things:
1) present your work (about 5 minutes)
2) listen to your class mates present their work and ask them questions (10 minutes of questions allotted for
each project).

You have an assignment to do while your classmates are presenting:
[Template for Q and A](https://docs.google.com/document/d/13B8gXVWKjKFlbleTWplkWegASVQh81IayDm8HNuUzMk/edit?usp=sharing)

At the end of the week you'll submit four things via Moodle:
* your responses to the template above to a pdf file 
* your presentation slides (in pptx or pdf)
* your Jupyter notebook (file -> download as -> an ipynb file)
* your data (usually as a CSV file, but it may be in a different format)

The Jupyter notebook should contain the following labels so that I can
easily see you've satisfied the criteria of the project
* Test1
* Test2
* Test2
* Element1
* Element2
* Element3
* Element4
* Element5


