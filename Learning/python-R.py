# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 19:39:45 2016

@author: Malek
"""
import rpy2

print(rpy2.__path__)
print(rpy2.__version__)

from rpy2.rinterface import R_VERSION_BUILD
print(R_VERSION_BUILD)

#docker run -it --rm -p 8888:8888 rpy2/rpy2:2.8.x ipython

#from rpy2.rinterface import R_VERSION_BUILD
#print(R_VERSION_BUILD)

#import rpy2.robjects as robjects

#r = robjects.r
#
#x = robjects.IntVector(range(10))
#y = r.rnorm(10)
#
#r.X11()
#
#r.layout(r.matrix(robjects.IntVector([1,2,3,2]), nrow=2, ncol=2))
#r.plot(r.runif(10), y, xlab="runif", ylab="foo/bar", col="red")