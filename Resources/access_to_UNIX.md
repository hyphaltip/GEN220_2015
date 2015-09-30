Access to UNIX
==============

There are several ways to get access to UNIX environment. It depends
on what kind of computer you have.  It boils down to accessing a UNIX
environment directly on your machine or remotely connecting to a
machine that is running UNIX.

Apple - OSX
-----------

Apple's OSX is built on a UNIX _kernel_ which is effectively we call
an operating system. It is based on a flavor of Linux called
[FreeBSD](http://freebsd.org). Some info on [UNIX for
OSX](https://www.apple.com/media/us/osx/2012/docs/OSX_for_UNIX_Users_TB_July2011.pdf)
is provided by Apple.

Importantly you can access the UNIX command line interface on your
Apple machine using the Terminal which is located in the Utilities
folders or simply search for Terminal in the Spotlight search
menu. Some other guides about starting a command line session on OSX
[here](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line). Note
that you can customize many things about how the Terminal looks,
including colors, fonts, and open multiple windows at once which is
really useful to support doing more than one thing (e.g. running a
program and running an editor) at a time.

I also really prefer a tools called [iTerm](https://www.iterm2.com/) for my UNIX
environment. It is a replacement for Terminal and provides many
features that are helpful for customization and overall experience.


You may not find you are able to understand what the differences
between these tools right at the beginning - that's fine - use
whatever gets you working on the command line as soon as possible and
as you become more of an expert you may enjoy the additional features
you can find in other programs.

You should also make sure and install X11 to support running graphical
programs on any remote host. This allows you to login to a remote
host, have that host draw something which will show up on your
screen. For example, read a PDF that is located on the remote server
but show the file on your screen on your laptop. On OSX this is called
[X11 Quartz](http://xquartz.macosforge.org/landing/).

Tools to connect to the remote server (e.g. pigeon.bioinfo.ucr.edu)
are already built into the system. The main tool you will use is
```ssh```. One thing we reccomend is when you connect you use the -X
option which will turn on forwarding of X11 info, so that graphical
drawing will work ```ssh -X login@pigeon.bioinfo.ucr.edu```.

Apple - iOS & iPad
----

It is possible to run a secure login shell onto a remote UNIX computer
on the iPad or your iPhone. This is not ideal but it will give you
access to the shell in the same way. However switching between editor
and the command line interface will be problematic in the small amount
of screen space you will have.

Windows PC
----------

There are a several ways to access UNIX from your PC. The easiest I
think is to install one of the free SSH tools for Windows. One of the
easiest to use is [PuTTY](http://www.putty.org/).

A second option to run UNIX on your PC is to install a UNIX-like
environment on your PC. This is provided by a package called
[Cygwin](http://www.cygwin.com).

In both cases you may want to also install an X11 client for your
windows computer so that graphical display from the remote server can
be displayed. I am not sure of the best tools but I believe
[Xming](http://sourceforge.net/projects/xming/) is free and
reliable. If you install Cygwin then [Cygwin/X](http://x.cygwin.com/)
is probably the best way to go to get X11 capabilities.

There are some other options, like installing what is called a _Virtual Machine_ on
your Windows computer which will allow you to run a program which will
let you build and run what looks like another computer within your
environment. This is most easily done with several tools but probably
the best to try is [Virtual Box](https://www.virtualbox.org/). This is
not completely straightforward as you are of course installing another
operating system and administering a UNIX/Linux computer is outside
the scope of the class.

Also an advanced user (and if you are, you would have done this
already probably) could also install another operating system directly
on your computer (not virtually) and then it is possible to setup a
dual-boot computer at startup you can go into Windows or Linux. I
won't include instructions here but it is something that can be done
relatively easily now with current versions of operating systems but
still would require knowledge outside the scope of this class.



