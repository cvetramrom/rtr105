from numpy import * # Importe skaitlisko metožu bibliotēkas funkcijas
x = linspace(0,7,70) # Trešais arguments ir ģenerējamo elementu skaits
y=cos(x**2)

legend = []

from matplotlib import pyplot as plt
#print(plt.plot._doc_)
plt.grid()
plt.xlabel('osj x')
plt.ylabel('osj y')
plt.title('Funkcijas $cos(x)$')
plt.plot(x,y)
legend.append("$cos(x**2)$-linija")
#print(legend)
plt.show()
