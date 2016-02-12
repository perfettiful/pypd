# before we start... #
  * you should have already Pure Data installed on your machine. check how to install it on:
    * mac osx (http://en.flossmanuals.net/PureData/InstallingOSX)
    * windows (http://en.flossmanuals.net/PureData/InstallingWindows)
    * linux (ubuntu) (http://en.flossmanuals.net/PureData/InstallingUbuntu)

  * you should be able to run it via command line. you can see how to achieve it here (http://en.flossmanuals.net/PureData/StartingPD).


# getting started! #

it's very easy to use pyPd. this tutorial will show how to get started with it, step by step...

## 1 - download... ##
to download pypd, you need to check out it from svn.

**OSX/Linux**

  1. open a terminal.
  1. make or change into the directory where you want the pypd sourcecode.
  1. run the following command to download pypd from the svn repository:
> > `svn checkout http://pypd.googlecode.com/svn/trunk/ pypd-read-only`

**Windows**

you will need an svn client, like Tortoise (http://tortoisesvn.tigris.org/).

## 2 - configure... ##
after that, you have to configure pypd. for that you must:
  1. among the downloaded files, open the "communication\_class" directory.
  1. open the "communication.py" file.
  1. in the beggining of it, you will two important variables (PD\_DIR, SERVER\_DIR). the first stores where your original pd application is (that one you are able to run using a terminal). the second stores where the file server.pd (that were already downloaded with the source through svn) is. update its values (you must put the entire path!!!) and run the "_example.py_" file that is inside "_communication\_class_" directory. if you have no errors, everything should be fine and configured!

## 3 - ... and run! ##
now, everything should be fine and you can try pyPd without problems!
unhapilly, i still don't have a great documentation to guide new users, but there are some well comment files inside pypd directory, called 