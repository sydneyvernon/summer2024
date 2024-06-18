#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 13:37:16 2024

@author: Sydney.Vernon
"""
import numpy as np
import scipy as sp

def lowpass(x, cut_freq):
    """
    Uses eighth-order Chebyshev type I filter to lowpass filter the cols of data
    matrix X, returning lowpass component X_LOWPASS. Curoff freq (measured in fractions
    of sampling rate) is given by input parameter cut_freq. If the data sequence is too 
    short for an eigth-order filter, the filter order is reduced. 
    
    Ported from lowpass.m in original Matlab code for global warming visualizations.
    Principal ideas taken from decimate.m
    """
    nrows = x.shape[0]
    nfilt = 8
    rip = 0.05
    b,a = sp.signal.cheby1(nfilt, rip, 2*cut_freq)
    
    # check filter order is adequate
#     while(np.abs(filtmag_db(b, a, 2*cut_freq) + rip) > 1e-6):
#         nfilt -= 1
#         if nfilt==0:
#             break
#         b,a = sp.signal.cheby1(nfilt, rip, 2*cut_freq)
#     if nfilt==0:
#         ## THROW ERROR HERE 'Bad Chebyshev design: cutoff frequency likely to be too small.'
#         pass

    return sp.signal.filtfilt(b,a,x)
    
    
    
    
# function x_lowpass = lowpass(x, cut_freq)


#     x_lowpass	= filtfilt(b, a, x);

# % ---------------------------------------------------------------------------
    
# function H = filtmag_db(b,a,f)
# %FILTMAG_DB Filter's magnitude response in decibels at given frequency.

#   nb  = length(b);
#   na  = length(a);
#   top = exp(-j*(0:nb-1)*pi*f)*b(:);
#   bot = exp(-j*(0:na-1)*pi*f)*a(:);
  
#   H   = 20*log10(abs(top/bot));
