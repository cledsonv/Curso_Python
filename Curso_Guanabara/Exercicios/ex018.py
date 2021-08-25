from math import radians, sin, cos, tan

num = float(input('Digite o angulo: '))

radiano = radians(num)
seno = sin(radiano)
cos = cos(radiano)
tangente = tan(radiano)

print(f"""Seno: {seno:.2f}
Cosceno: {cos:.2f}
Tangente: {tangente:.2} 
""")