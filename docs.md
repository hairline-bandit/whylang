As this is just a fronted for Python, I will just list off each character that corresponds to a Python thing and also some tricks...

F = if

E = else

I = elif

q = ==

M = >

L = <

m = >=

l = <=

n = in

o = not

a = =

p = (

P = )

b = \[

B = \]

d = and

r = or

u = +

i = -

v = /

k = *

K = %

w = int

W = str

O = float

h = list

H = set

t = True

f = False

N = None

c = ,

z = " " (a space)

s = += 

x = -=

U = "

T = print

D = def

g = input

y = for

Y = range

j = len

J = :

V = ignore all above encodings (write as is until the next V)

1234567890. = What they are (nothing changes for these)

**Note that anything that would need a colon after it in Python (def, if, else, elif, for) does not need one here**

Here's a trick:

If you want to write to the file with regular Python, say you want to use a Python built in or import, surround it with V

i.e. Vimport randomV
