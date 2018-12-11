Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
=================== RESTART: /home/user/dgr,mmdd.py-2018-7 ===================
Lietotāj,lūdzu ievādi argumentu (x): 4

Traceback (most recent call last):
  File "/home/user/dgr,mmdd.py-2018-7", line 13, in <module>
    y=sin(x)
NameError: name 'sin' is not defined
>>> 
=================== RESTART: /home/user/dgr,mmdd.py-2018-7 ===================
Lietotāj,lūdzu ievādi argumentu (x): 1
sin(1.00) =0.841471
a0=0.00 SO=0.00
a1=-0.17 S1=-0.17
a2=0.01 S2=-0.16
a3=-0.00 S3=-0.16
>>> 
=================== RESTART: /home/user/dgr,mmdd.py-2018-7 ===================
Lietotāj,lūdzu ievādi argumentu (x): 1

Traceback (most recent call last):
  File "/home/user/dgr,mmdd.py-2018-7", line 13, in <module>
    y=sin(x)
NameError: name 'sin' is not defined
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/dgr,mmdd.py-2018-7', '__package__': None, 'x': 1.0, '__name__': '__main__', '__doc__': None}
>>> from math import *
>>> vars()
{'exp': <built-in function exp>, 'pow': <built-in function pow>, 'fsum': <built-in function fsum>, 'cosh': <built-in function cosh>, 'ldexp': <built-in function ldexp>, 'hypot': <built-in function hypot>, 'acosh': <built-in function acosh>, 'tan': <built-in function tan>, 'asin': <built-in function asin>, 'isnan': <built-in function isnan>, 'log': <built-in function log>, 'fabs': <built-in function fabs>, 'floor': <built-in function floor>, 'atanh': <built-in function atanh>, 'sqrt': <built-in function sqrt>, '__package__': None, 'frexp': <built-in function frexp>, 'factorial': <built-in function factorial>, 'degrees': <built-in function degrees>, 'pi': 3.141592653589793, 'log10': <built-in function log10>, '__doc__': None, 'asinh': <built-in function asinh>, 'fmod': <built-in function fmod>, 'atan': <built-in function atan>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/dgr,mmdd.py-2018-7', 'copysign': <built-in function copysign>, 'cos': <built-in function cos>, 'ceil': <built-in function ceil>, 'atan2': <built-in function atan2>, 'isinf': <built-in function isinf>, 'sinh': <built-in function sinh>, '__name__': '__main__', 'trunc': <built-in function trunc>, 'expm1': <built-in function expm1>, 'e': 2.718281828459045, 'tanh': <built-in function tanh>, 'radians': <built-in function radians>, 'sin': <built-in function sin>, 'lgamma': <built-in function lgamma>, 'erf': <built-in function erf>, 'erfc': <built-in function erfc>, 'modf': <built-in function modf>, 'x': 1.0, 'acos': <built-in function acos>, 'log1p': <built-in function log1p>, 'gamma': <built-in function gamma>}
>>> 
=================== RESTART: /home/user/dgr,mmdd.py-2018-7 ===================
Lietotāj,lūdzu ievādi argumentu (x): 0.25
sin(0.25) =0.247404
a0=0.00 SO=0.00
a1=-0.00 S1=-0.00
a2=0.00 S2=-0.00
a3=-0.00 S3=-0.00
>>> 
=================== RESTART: /home/user/dgr.mmdd.py-2018-8 ===================
Lietotāj, lūdzu, ievadi agumentu (x):3
sin(3.00)=0.14

Traceback (most recent call last):
  File "/home/user/dgr.mmdd.py-2018-8", line 11, in <module>
    print("a0=%.2f S0="%(a0,S))
TypeError: not all arguments converted during string formatting
>>> 
=================== RESTART: /home/user/dgr.mmdd.py-2018-8 ===================
Lietotāj, lūdzu, ievadi agumentu (x):3
sin(3.00)=0.14

Traceback (most recent call last):
  File "/home/user/dgr.mmdd.py-2018-8", line 11, in <module>
    print("a0=%.2f S0=%"(a0,S))
TypeError: 'str' object is not callable
>>> 
=================== RESTART: /home/user/dgr.mmdd.py-2018-8 ===================
Lietotāj, lūdzu, ievadi agumentu (x):3
sin(3.00)=0.14

Traceback (most recent call last):
  File "/home/user/dgr.mmdd.py-2018-8", line 11, in <module>
    print("a0=%.2f S0=%.2f"(a0,S))
TypeError: 'str' object is not callable
>>> 
=================== RESTART: /home/user/dgr.mmdd.py-2018-8 ===================
Lietotāj, lūdzu, ievadi agumentu (x):3
sin(3.00)=0.14
a0=3.00 S0=3.00
a1=-4.50 S1=-1.50
a2+2.02 S2=0.52

Traceback (most recent call last):
  File "/home/user/dgr.mmdd.py-2018-8", line 29, in <module>
    print("a3+%.2f S3=%.2f"(a3,S))
TypeError: 'str' object is not callable
>>> 
=================== RESTART: /home/user/dgr.mmdd.py-2018-8 ===================
Lietotāj, lūdzu, ievadi agumentu (x):3
sin(3.00)=0.14
a0=3.00 S0=3.00
a1=-4.50 S1=-1.50
a2+2.02 S2=0.52
a3+-0.43 S3=0.09
>>> 
=================== RESTART: /home/user/dgr.mmdd.py-2018-9 ===================
Lietotāj,lūdzu, ievadi argumentu (x): 7
sin(7.00)=  0.66
a0=  7.00 S0=  7.00

Traceback (most recent call last):
  File "/home/user/dgr.mmdd.py-2018-9", line 19, in <module>
    print("a1=%6,2f S1=%6.2f"%(a,S))
ValueError: unsupported format character ',' (0x2c) at index 5
>>> 
=================== RESTART: /home/user/dgr.mmdd.py-2018-9 ===================
Lietotāj,lūdzu, ievadi argumentu (x): 7
sin(7.00)=  0.66
a0=  7.00 S0=  7.00
a1=-57.17 S1=-50.17
a2=140.06 S2= 89.89
a3=-163.40 S3=-73.51
>>> 

