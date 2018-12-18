Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /home/user/dgr.mmdd-2018.linki1 ==================

Warning (from warnings module):
  File "/usr/lib/python2.7/dist-packages/matplotlib/font_manager.py", line 273
    warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')
UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.

Traceback (most recent call last):
  File "/home/user/dgr.mmdd-2018.linki1", line 62, in <module>
    plt.legend(legend, loc = 3, fancybox=True, framealpha=0.5, facecolor="green")
  File "/usr/lib/python2.7/dist-packages/matplotlib/pyplot.py", line 3553, in legend
    ret = gca().legend(*args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_axes.py", line 538, in legend
    self.legend_ = mlegend.Legend(self, handles, labels, **kwargs)
TypeError: __init__() got an unexpected keyword argument 'facecolor'
>>> 
================== RESTART: /home/user/dgr.mmdd-2018.linki1 ==================

Traceback (most recent call last):
  File "/home/user/dgr.mmdd-2018.linki1", line 63, in <module>
    plt.legend(legend, loc = 3, fancybox=True, framealpha=0.5, facecolor="green")
  File "/usr/lib/python2.7/dist-packages/matplotlib/pyplot.py", line 3553, in legend
    ret = gca().legend(*args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_axes.py", line 538, in legend
    self.legend_ = mlegend.Legend(self, handles, labels, **kwargs)
TypeError: __init__() got an unexpected keyword argument 'facecolor'
>>> 
================== RESTART: /home/user/dgr.mmdd-2018.linki1 ==================
>>> 
================ RESTART: /home/user/dgr_mmdd-2018_linki1.py ================
>>> 
================ RESTART: /home/user/dgr_mmdd-2018_linki2.py ================

Traceback (most recent call last):
  File "/home/user/dgr_mmdd-2018_linki2.py", line 64, in <module>
    plt.legend(legend, loc = 3, fancybox=True, framealpha=0.5, facecolor="green")
  File "/usr/lib/python2.7/dist-packages/matplotlib/pyplot.py", line 3553, in legend
    ret = gca().legend(*args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/matplotlib/axes/_axes.py", line 538, in legend
    self.legend_ = mlegend.Legend(self, handles, labels, **kwargs)
TypeError: __init__() got an unexpected keyword argument 'facecolor'
>>> 
================ RESTART: /home/user/dgr_mmdd-2018_linki2.py ================

Traceback (most recent call last):
  File "/home/user/dgr_mmdd-2018_linki2.py", line 4, in <module>
    legend.append("$sin(x)$ - default - viss ir savienots ar taisnaam liinijaam")
NameError: name 'legend' is not defined
>>> 
