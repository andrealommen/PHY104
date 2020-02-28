---
layout: page
author: Andrea Lommen
title: The Git Repository 
permalink: /git/
---

The first lab:
[https://classroom.github.com/a/lGS1MyW6](https://classroom.github.com/a/lGS1MyW6)

The second lab:
[https://classroom.github.com/a/lOVABn5T](https://classroom.github.com/a/lOVABn5T)

The third lab:
[https://classroom.github.com/a/-nRrjo07](https://classroom.github.com/a/-nRrjo07)

Note that the second lab has a funny name: Lab2-2ndTry because the first one I created was causing problems in downloading.

------------------------------------------------------------------------------
I think now that you've done the stuff below once already, you can clik the link above and skip down to "accepting" my assignment.

------------------------------------------------------------------------------

Click on that link and it will ask you to create an account. You do indeed need a git account
to turn in your lab. The "free" option is just fine for you.

When it asks you to create a repository name you can call that
anything you want.  I'd probably call it "104". Choose "Private." You can skip the "initialize repository" step. You actually won't use
this repository for anything, because you'll be using the
classroom repository. (You may be able to skip this step as long as you've created a github
account.)

Clink on the link above one more time, and now that you have a github account it should tell you that github classroom wants access to your account, which you should grant.

-----------------------------------------------------------
**Skip to here if you already have done this once. **

-----------------------------------------------------------

After clicking one of the links above you'll have the opportunity to "accept" my assignment. Please accept it.

Click "clone or download", a green button over on the right. You'll see a box with a URL in it, e.g. https://github.com/INTRO104/lab1.git. Copy that.

Right click on that URL and then choose "copy" from the pop-up list.

* On the home screen of your Jupyter hub account you have an option on the top right for "new" -> "terminal." That will open up a terminal window on the hub. Type the following and then press "return".

> git clone \<paste the name of the repository that you found by going to the link
at the top of this document\>, 

e.g. mine looked like this:

> git clone https://github.com/INTRO104/lab1-andrealommen.git

(Yours will magically have your git account name tagged onto the end of it.)

To paste you can either right click and choose paste or type ctrl-v. Let me know if you need help.  These instructions work in H204, but they may not work at home.

* Go back to the home screen of your Jupyter hub, and you should see a new
directory with the same name as the repository (i.e. "lab1-yourname"). Click on that directory
and then open up the file you downloaded, i.e. click
on Lab1_2020.ipynb.

--------Special instructions that only apply to Lab1 which we started in a different directory ----------- <br>
I believe you all already have Lab1_2020.ipynb in a folder called "lab1" 
on your Jupyter desktop.  That's the version you've been doing some work on.  
You should download (from notebook.kinsc.etc) and upload (to github) this version 
rather than the one you've just downloaded into lab1-yourname.  Bottom line - it doesn't
matter which one you work on, as long the one you eventually upload to github is the
one with your work in it!
---------------------------------------------------------------------------------------------------------

Complete the lab in the Jupyter hub. When you've finished say "Restart and run all" and make
sure that everything runs correctly.

Go to "File" -> "Download as " -> "Notebook(ipynb)"
This will download your completed file as an ipython notebook (that's what ipynb stands for).
Open up a web page on your github account (github.com) and use the "upload" button to upload
your completed lab.  Where it says "Add an optional extended description" you could say "I'm 
turning in my first python lab!" .
The "commit directly to the master branch" will be checked.  That's fine.
Press "commit". You've just turned in your first lab!
