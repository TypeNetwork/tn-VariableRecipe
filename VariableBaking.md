# Variable Font Baking

## Preparation

### Install libraries in the terminal

~~~Python
sudo sh install.sh
~~~

## Clone the repository

### By desktop application

* Download the desktop application from github.com
* Copy the repository path from github.com and clone the repository in a local folder.

![images/DesktopGitNobel.png](images/DesktopGitNobel.png)

### By terminal (faster for usage with ufo’s)

* Make a “git” folder on your desktop (or another place of storage).
* Copy the repository path from github.com and clone the repository in a local folder.

~~~ 
>>> cd ~/Desktop/git
>>> git clone <paste-repository-path-here>
~~~

### Committing changes 

* Change can be committed using the desktop application
* Or by using the terminal (faster for usage with ufo’s)

~~~
>>> cd ~/Desktop/git/<repository-name>
>>> git pull;git add *;git commit -m "Description of the committed changes";git pull;git push
~~~

These terminal instruction will synchornize all online and local changes.

**Note that a UFO font can contain hundreds or even thousands of files. Moving a UFO to another folder therefore creates a magnitude of changes in the git commit.

* Make sure not to move UFO’s around or rename them if not necessary.
* It is better to use the terminal-commit method, if there are thousands of changes, due to copying or moving UFO files.

## Open the repository 

Open the respository for editing by dragging the entire folder into Sublime (https://www.sublimetext.com). There are many other editors that allow the editing of file/folder trees, but Sublime also offers a nice interface for running the scripts from within the application (without the need for terminal or RoboFont).

## Collections of UFO masters

The UFO masters often are grouped together in a single folder. They not necessarily need to combine into a single Var-font, e.g. roman and italic UFO’s can be joined in the same folder. The design space file will define which masters are used for the various axes, sorting them out.

Masters that are inteneded to be used in a single Var-font must have matching glyph sets, matching points and matching component references. 

The compatibility of the masters can be checked and altered with the RoboFont->Compatibilizer tool.

## Edit design space files

Starting the baking of Var-fonts, we need to make one or more design space files that define the axes and how the master UFO’s are located. 

Several design space files can co-exist, to test the relation between indiviual axis groups.

The design space files should be named after the axes that they support. Separate the axis names by an underscore.

### Examples
~~~
Nobel-wght.designspace
Nobel-wdth.designspace
Nobel-wdth_wght.designspace
~~~

Design space files are XML documents with a relative simple structure.

* Definition of the axes
* Definition of the ufo masters and their axis location.

~~~
<designspace format="3">
	<axes>
		... (definition of axes here)
	</axes>
	<sources>
		... (definition of ufo-axis-locations here)
	</source>
</designspace>
~~~ 

A typical axis definition looks like this:

~~~
<axis 
	minimum="30" 
	default="90" 
	maximum="250" 
	name="Weight" 
	tag="wght">
</axis>
~~~

Although the values all relative, in the latest implementation of fonttools, they are more bound to the type of axis than before. For the [wght] axis it is adviced to use the stem of the capital-H as value. 

A typical source definition looks like this:

~~~
<source 
	familyname="Nobel" 
	filename="master_ufo3/Nobel-Regular.ufo" 
	name="Nobel-Regular.ufo" 
	stylename="Regular">
	<location>
		<dimension name="weight" xvalue="90" />
		<dimension name="width" xvalue="224" />
	</location>
</source>
~~~

Each location point on an axis (minimum value, default value and maximum value) should have exactly one master ufo defined.

The origin of the design space (often the Regular of the family) needs all axes defined in the <location> tags, where the value is equal to the default value of the axis.


