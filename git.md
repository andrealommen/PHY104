---
layout: page
author: Andrea Lommen
title: The Git Repository 
permalink: /git/
---

For each of the 5 lab assignments you will need to do the following steps:

* Clone the repository to your computer.
* Modify the files and commit changes to complete your solution.
* Push/sync the changes up to GitHub.

That probably all looks like hogwash to you at the moment, because it's early in
the semester.  Here are more explicit instructions.

Go to [https://github.com/INTRO104] and click on the lab you want to start, e.g. lab1. 

Click "clone or download", a green button over on the right. You'll see a box with a URL in it, e.g. https://github.com/INTRO104/lab1.git. Copy that.

* On the home screen of your Jupyter hub account you have an option on the top right for "new" -> "terminal." That will open up a terminal window on the hub.
* Make a new directory for this assignment using "cd" ie.
> mkdir lab1
* change into that directory (cd = change directory)
> cd lab1
* clone the repository
> git \<paste the name of the repository that you found by going to the link
at the top of this document\>, e.g. git https://github.com/INTRO104/lab1.git
* Go back to the home screen of your Jupyter hub, and you should be able to click
on the directory you just created.  Then open up the file you downloaded, i.e. click
on lab1.ipynb.
* Do the lab and save your work. IMPORTANT: please save it as \<firstnamelastname\>_lab\<labnumber\>, e.g. janesmith_lab1
* Open up a terminal window again, navigate to the directory, and type "git add <filename>" e.g. git add tedsmith_lab1.ipynb.
* > git commit -m "I am turning in my lab."
* > git push
