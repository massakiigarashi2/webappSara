# myFirstStreamlitApp.py
#import the library
import streamlit as st
from re import L
import scipy.optimize as optimize

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Programa Exprimental - Sara Gatti")
# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
# st.subheader("Bem vindos!")
# Use st.write("") para adicionar um texto ao seu Web app

#SUGESTÃO DE MODIFICAÇÃO:

def objetivo(x):
  h, c, l = x
  volume_total = h * c * l
  volume_transformadores = sum([vt[i] for i in range(n)])
  espaco_livre = volume_total - volume_transformadores
  return espaco_livre

def penalizacao(x):
  peso_total = sum([pt[i] for i in range(n)])
  tempo_total = sum([tt[i] for i in range(n)])
  penalizacao = 0
  if peso_total > peso_maximo:
    penalizacao += peso_total - peso_maximo
  if tempo_total > tempo_maximo:
    penalizacao += (tempo_total - tempo_maximo) * 10
  return penalizacao

# variáveis de entrada
#n = int(input('Número de REC: '))
#h = int(input('Altura de REC: '))
#c = int(input('Comprimento de REC: '))
#l = int(input('Largura de REC: '))
n = st.text_input('Número de REC: ')
st.write("ALTURA REC (em metros):")
h = []
for i in range(0, n):
	eleH = int(st.text_input('Digite valor: '))
	# adding the element
	h.append(eleH)
print("h= ")
print(h)

#c = float(input('Comprimento de REC: '))
st.write('Comprimento de REC (em metros): ')
c = []
for i in range(0, n):
	eleC = int(st.text_input('Digite valor: '))
	# adding the element
	c.append(eleC)
st.write("c = ")
print(c)

#l = float(input('Largura de REC: '))
st.write('Largura de REC (em metros): ')
l = []
for i in range(0, n):
	eleL = int(st.text_input('Digite valor: '))
	# adding the element
	l.append(eleL)
st.write("l = ")
st.write(l)

vt = [h[i]*c[i]*l[i] for i in range(n)]  # volume de cada transformador

#pt = int(input('Peso de cada REC: '))
st.write('Peso de cada REC (em Kg): ')
pt = []
for i in range(0, n):
	elePT = int(st.text_input('Digite valor: '))
	# adding the element
	pt.append(elePT)
st.write("pt = ")
st.write(pt)

#tt = int(input('Tempo que cada REC deve permanecer na estufa: '))
st.write('Tempo que cada REC deve permanecer na estufa (em minutos): ')
tt = []
for i in range(0, n):
	eleTT = int(st.text_input('Digite valor: '))
	# adding the element
	tt.append(eleTT)
st.write("tt = ")
st.write(tt)

# restrições das variáveis
peso_maximo = 100
tempo_maximo = 50
h_minimo = 1
h_maximo = 10
c_minimo = 1
c_maximo = 10
l_minimo = 1
l_maximo = 10

# Utiliza a biblioteca scipy.optimize para encontrar a solução ótima
x0 = [5, 5, 5]  # valores iniciais das variáveis
bounds = [(h_minimo, h_maximo), (c_minimo, c_maximo), (l_minimo, l_maximo)]  # limites das variáveis
minimizer_kwargs = {"method": "SLSQP", "bounds": bounds}  # método de otimização e limites das variáveis
res = optimize.minimize(lambda x: objetivo(x) + penalizacao(x), x0, **minimizer_kwargs)

# Exibe o resultado
st.write(res)
