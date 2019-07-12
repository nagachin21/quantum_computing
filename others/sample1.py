from wildqat import *

a = opt()

a.J = [
[0,1,0,1,0],
[0,0,1,0,0],
[0,0,0,1,1],
[0,0,0,0,1],
[0,0,0,0,0]
]

print(a.run())
