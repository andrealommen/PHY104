---
layout: page
author: Andrea Lommen
title: The Git Repository 
permalink: /git/
---

(These instructions don't work yet for submitting your work, but they will get you the first lab, so you can start working on it!)

Go to [https://github.com/INTRO104] and click on the lab you want to start, e.g. lab1. (I don't think you have to have a git account - I tested that.) 

Click "clone or download", a green button over on the right. You'll see a box with a URL in it, e.g. https://github.com/INTRO104/lab1.git. Copy that.

Right click on that URL and then choose "copy" from the pop-up list.

* On the home screen of your Jupyter hub account you have an option on the top right for "new" -> "terminal." That will open up a terminal window on the hub.

> git clone \<paste the name of the repository that you found by going to the link
at the top of this document\>, 

e.g. 

> git clone https://github.com/INTRO104/lab1.git

To paste you can either right click and choose paste or type ctrl-v. Let me know if you need help.  These instructions work in H204, but they may not work at home.

* Go back to the home screen of your Jupyter hub, and you should see a new
directory with the same name as the repository (i.e. "lab1"). Click on that directory
and then open up the file you downloaded, i.e. click
on lab1.ipynb.
* Do the lab and save your work. IMPORTANT: please save it as \<firstnamelastname\>_lab\<labnumber\>, e.g. janesmith_lab1

Open up a terminal window again (at the Jupyter home screen "new"-> "terminal")

-----This is the part that's untested, so don't do this yet----

Two things you have to do only once:
* Tell git your email address:
> git config --global user.email "Put your email address here"
for example
> git config --global user.email "jana.smith@haverford.edu"
* Tell git your name
> git config --global user.name "Put your name here"
for example..
> git config --global user.name "Jana Smith"

* Open up a terminal window again, navigate to the directory, and type "git add <filename>" e.g. git add tedsmith_lab1.ipynb.
* > git commit -m "I am turning in my lab."
* > git push
