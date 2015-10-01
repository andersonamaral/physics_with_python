# Example of Thomson's Hydron Atom Model

print "Assumindo que ha apenas um eletron de carga -e dentro de uma regiao esferica de carga postiva uniforme 'ro' (Tipico Atomo de Hidrogenio de Thomson, vamos mostrar que seu movimento, se tem energia cinetica, pode ser uma simples oscilacao harmonica em relacao ao centro da esfera " 


import math 

e = 1.6*(10**(-19))
r = 1.0*(10**(-10))
ro = (e)/((4.0/3.0)*math.pi*(r**3))
Eta0 = 8.854187*(10**(-12))
k = (ro*e)/(3*Eta0)
m = 9.11*(10**(-31))

print " Dados  e = 1.6*(10**(-19)), r = 1.0*(10**(-10)),ro = (e)/((4.0/3.0)*math.pi*(r**3)),Eta0 = 8.854187*(10**(-12)) e k = (ro*e)/(3*Eta0) " 


print " O valor da forca constante k sera: " 

print k ,  "nt/m" 

print " ... e o valor da frequencia do eletron sera: " 


f =( 1.0/(2.0*math.pi))*math.sqrt(k/m)

print f , "Hz"  




 
