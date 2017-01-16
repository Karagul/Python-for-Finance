# -*- coding: utf-8 -*-
"""
"""

from __future__ import division
from scipy.stats import kendalltau, pearsonr, spearmanr
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pandas_datareader import data, wb
from scipy.integrate import quad
from scipy.optimize import fmin
import sys
import statistics as st
from scipy.interpolate import interp1d
from ambhas.copula import Copula
import statistics
from scipy.stats import norm
plt.style.use('ggplot')

def generateDat():
    global x,y
    returns1 = data.DataReader('AAPL', 'yahoo', '2005-1-1', '2010-1-1')
    returns2 = data.DataReader('GOOG', 'yahoo', '2005-1-1', '2010-1-1')
    x = returns1['Adj Close']
    x.plot()
    y = returns2['Adj Close']
    y.plot()
    plt.title('Valores de Retornos')
    plt.show()
# Data and histograms
def plotDat():
    global x,y
    plt.figure(1)
    plt.hist(x,bins=100,color='red',alpha=0.8,align='mid')
    plt.title('Retornos de Apple')
    
    plt.figure(2)
    plt.hist(y,bins=100,orientation='horizontal',color='blue',alpha=0.8,align='mid')
    plt.title('Retornos de Google')
    
    plt.figure(3)
    plt.scatter(x,y,marker="o",color='green')
    plt.title('Apple-Google')
    plt.show()
    
def generateCopulas():
    global x,y
    plt.figure(4)
    frank = Copula(x,y,family='frank')
    uf,vf = frank.generate_uv(1000)
    plt.scatter(uf,vf,marker='.',color='magenta')
    plt.ylim(0,1)
    plt.xlim(0,1)
    plt.title('Apple-Google (Frank)')
       
    plt.figure(5)
    clayton = Copula(x,y,family='clayton')
    uc,vc = clayton.generate_uv(1000)
    plt.scatter(uc,vc,marker='.',color='black')
    plt.ylim(0,1)
    plt.xlim(0,1)
    plt.title('Apple-Google (Clayton)')
    plt.show()
    
    plt.figure(6)
    gumbel = Copula(x,y,family='gumbel')
    ug,vg = gumbel.generate_uv(1000)
    plt.scatter(ug,vg,marker='.',color='orange')
    plt.ylim(0,1)
    plt.xlim(0,1)
    plt.title('Apple-Google (Gumbel)')
    plt.show()
        
    foo = Copula(x, y, family='frank')
    print("Tau Frank ="), foo.tau
    print("Pearson Frank ="), foo.pr
    print("Spearman Frank ="), foo.sr
    print("Theta Frank ="), foo.theta

    foo2 = Copula(x, y, family='clayton')
    print("Tau Clayton ="), foo2.tau
    print("Pearson Clayton ="), foo2.pr
    print("Spearman Clayton ="), foo2.sr
    print("Theta Clayton ="), foo2.theta

    foo3 = Copula(x, y, family='gumbel')
    print("Tau Gumbel ="), foo3.tau
    print("Pearson Gumbel ="), foo3.pr
    print("Spearman Gumbel ="), foo3.sr
    print("Theta Gumbel ="), foo3.theta

# Run the functions
generateDat()
plotDat()
generateCopulas()