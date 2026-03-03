# data types
num_int=1
num_float=2.3
num_complex=3+8j
string = 'Hello'
boolean = True
lista = [1,2,3,'cherry',3.2,3+2j]
t_tuple = ('Not','Modificable','lol',123)
t_set ={3,42,40.23,43,21,34,54}
t_dictionary = {
    'key':'value',
    'language':'python'
}
q1=2
p1=3
q2=10
p2=8
euclidean_distance=((q2-q1)**2)+(p2-p1)**2
print(f'''
{type(num_int)} = {num_int} 
{type(num_float)} = {num_float}
{type(num_complex)} = {num_complex}
{type(string)} = {string}
{type(boolean)} = {boolean}
{type(lista)} = {lista}
{type(t_tuple)} = {t_tuple}
{type(t_set)} = {t_set}
{type(t_dictionary)} = {t_dictionary}
Euclidean distance between ({q1},{p1}) and ({q2},{p2}) = {euclidean_distance**0.5:.2f})
''')
