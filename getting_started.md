# Getting Started 

This page has some useful tips and tricks for getting started running jobs on the Coma cluster.


## Using Modules
 
Modules are a simple way to use different versions of software packages. These versions are often different from the default ones installed on coma, and have additional functionality. For instance, the default version of python is 2.6.6, but there is a module for python 2.7.4. To use this version, simply type:

```console
user@local:~$ module load python27
user@local:~$ python --version
    Python 2.7.4
```

Note that this changes the version of python invoked at the prompt. For instance:

The module version of python also include numpy, scipy, and many other packages useful for scientific computing. For the new intel-v3 nodes, load the python27-extras module to use numpy and scipy.

In order to see which modules you currently have loaded, type:

```console
user@local:~$ module list
``` 

To see which modules are available for loading, type:

```console
user@local:~$ module avail
```

You can load or unload a specific module using the load/unload commands:
 
```console
user@local:~$ module load gcc-4.7.3
```

Modules can be used to load versions of compilers, such as gcc and icc. The main exception to this is when using the ifort compiler. In this case, one must source the configuration file directly:

 
```console
user@local:~$ source /opt/intel/.composer_xe_2013_sp1.0.080/bin/compilervars.sh intel64
user@local:~$ ifort --version
    ifort (IFORT) 14.0.0 20130728
    Copyright (C) 1985-2013 Intel Corporation.  All rights reserved.
```
 
The loading of module files can be placed in `.bashrc` file in one's home directory (/home/username/ or ~/) so it is done automatically at login. Note that this must be done again at the start of a slurm job, so make sure the module loading is in your job script. See [Scheduling Tips]() on how to write a slurm script in order to submit your job to the queue.


## Installing Python

If the available Python module(s) do not suit your needs, you can install Python from source locally or instakll python using Anaconda! 


### From Source

Start by creating a directory like 'usr' in your home directory, i.e., `/home/yourusername/usr/`.  Next cd into this directory.  Download the source code for Python by going to [https://www.python.org](https://www.python.org), navigating to the download menu--source.  Select the Python version you would like, e.g. 'Latest Python 2 Release - Python 2.7.14'.  Then right click the link for the 'compressed source tarball' and copy the link.  Then in your new directory, `/home/yourusername/usr/` type:

 
```console
user@local:~$ wget (paste link for source here)
user@local:~$ tar -xvf Python-2.7.14.tar.xz 
``` 

Navigate into this python directory.   

```console
user@local:~$ ./configure --prefix=/home/yourusername/usr
user@local:~$ make 
```

Don't worry if you get the following message:

```console
Python build finished, but the necessary bits
to build these modules were not found:
    bsddb185 
    dl
    gdbm            
    imageop
    sunaudiodev 
```

These are not important--nothing to see here--move along. Next install python by typing:

 
```console
user@local:~$ make install
 ```

You now need to make sure this python in your path (before the system python). In your .bashrc file in your home directory, you can add this line:

```
export PATH=$HOME/usr/bin/:$PATH.
```
 
You will probably also want to install pip by following the installation instructions on [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).


### Anaconda

[need instructions]
 