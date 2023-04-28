class mat(list):
   def add(self, b):
      f = lambda x,y: [xi+yi for xi,yi in zip(x,y)]
      return mat(f(self,b))

import re

meugab = 'A E D D A E C B B E C B D D B A C B B A E E B A E B E D B D B B A A E C C D E E E C B E A B E A B D C D B A C B C C D B E D A D E A E C B'
gab = \
'''1 - A 2 - E 3 - C 4 - D 5 - A  
6 - A 7 - E 8 - B 9 - B 10 - D  
11 - A 12 - D 13 - B 14 - E 15 - D 
16 - A 17 - E 18 - B 19 - B 20 - D  
21 - A 22 - D 23 - E 24- B 25 - A  
26 - A 27 - C 28 - E 29 - D 30 - C  
31 - B 32 - B 33 - C 34 - A 35 - E  
36 - E 37 - D 38 - B 39 - C 40 - B  
41 - C 42 - B 43 - D 44 - C 45 - C  
46 - A 47 - E 48 - D 49 - B 50 - E  
51 - E 52 - A 53 - D 54 - C 55 - A  
56 - E 57 - B 58 - E 59 - D 60 - D  
61 - B 62 - D 63 - A 64 - B 65 - A  
66 - A 67 - A 68 - E 69 - D 70 - E'''
gab = re.findall('[A-E]', gab)
print(gab)
comp = lambda x, y: [xi==yi for xi,yi in zip(x,y)]
pesos = mat([1.5 for i in range(70)])
contrapesos = mat([-0.5 if i>=20 and i<25 else 0 for i in range(70)])
contrapesos = contrapesos + mat([-0.5 if i>=10 and i<15 else 0 for i in range(70)])
pesos = pesos+contrapesos
certas = comp(meugab.split(' '), gab)
print(certas)
nota = sum([xi*yi for xi,yi in zip(certas, pesos)])
print(nota)
