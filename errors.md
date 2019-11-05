# Possible errors you may encounter

* 'Illegal instruction' error
The likely cause of this error is that you have code that was compiled on one computing architecture, and is ran on another one which does not 
support all the features. I.e. You compiled it on a new Intel CPU and try to run it on an AMD machine. A solution to this problem is to either
verify if you have some kind of compiled code that you are using that needs to be rebuilt using '-march=generic' instead of '-march=native' flags
or alternatively restrict the range of nodes that you use to run your code to either intel only, or intel_v1, intel_v4... etc 




