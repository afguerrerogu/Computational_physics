#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

# Walk . py Random walk with graph
import visual 
import visual.graph 
import random

random.seed(None)  # Seed generator , None => system c lo c k
jmax = 20
x = 0.; y = 0.  # Start at origin


graph1 = gdisplay(width =500 , height =500 ,title = 'Random Walk' , xtitle = 'x' ,ytitle = 'y' )
pts = gcurve( color = color.yellow )

for i in range( 0 , jmax + 1 ):
    pts.plot( pos = ( x , y ) )
    x += ( random.random( ) - 0.5 ) * 2.
    y += ( random.random( ) - 0.5 ) * 2.
    pts.plot( pos = ( x , y ) )
    rate (100)