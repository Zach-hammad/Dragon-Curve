'''
D R E X E L   U N I V E R S I T Y
ENGR 131 Winter 2020-2021
Programming Project 2
The Harter-Heighway Dragon:  Plot module

DO NOT EDIT THIS SCRIPT!

Use it by invoking

from engr131_plot_module import make_2D_plot

in your script. Then you can call make_2D_plot() to make a plot!

Cameron F Abrams cfa22@drexel.edu
'''
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def make_2D_plot(S,fn='my_plot.png',color_map_name='viridis',axes=[]):
    # S[] is a list of 2D point class instances 
    #   with position attributes x and y
    color_map=cm.get_cmap(color_map_name)
    plt.figure(figsize=(8,8))
    if len(axes)==0: # autoscale and center
        xomax=max([p.x for p in S])
        xomin=min([p.x for p in S])
        yomax=max([p.y for p in S])
        yomin=min([p.y for p in S])
        xspan=xomax-xomin
        yspan=yomax-yomin
        xpad=xspan/10
        ypad=yspan/10
        xspan+=2*xpad
        yspan+=2*ypad
        xmax=xomax+xpad
        xmin=xomin-xpad
        ymax=yomax+ypad
        ymin=yomin-ypad
        if xspan>yspan:
            shft=(xmax-yomax)-0.5*(xmax-xmin-yomax+yomin)
            plt.xlim([xmin,xmax])
            plt.ylim([xmin,xmax])
        else: 
            shft=(ymax-xomax)-0.5*(ymax-ymin-xomax+xomin)
            plt.xlim([ymin-shft,ymax-shft])    
            plt.ylim([ymin,ymax])
    else:
        plt.xlim(axes[0])
        plt.ylim(axes[1])

    for i,(p,q) in enumerate(zip(S[:-1],S[1:])):
        plt.plot([p.x,q.x],[p.y,q.y],color=color_map(i/len(S)))

    plt.axis('off')
    plt.savefig(fn, bbox_inches='tight')