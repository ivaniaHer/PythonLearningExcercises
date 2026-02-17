import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from wcwidth import center

datos_real = [1,0,1,1,0,1,0,0,1,0]
datos_pred = [1,0,0,1,0,1,0,0,0,0]

accuracy = accuracy_score(datos_real, datos_pred)
precision = precision_score(datos_real, datos_pred)
recall = recall_score(datos_real, datos_pred)
f1_score = f1_score(datos_real, datos_pred)

plt.figure(figsize=(10,6))
metricas = ['Exactitud', 'Precision','Recall','F1_Score']
valores = [accuracy,precision,recall,f1_score]
colores = ['#FEE685','#B9F8CF','#74D4FF','#C68AFF']

barras = plt.bar(metricas, valores, color=colores, edgecolor = 'black', linewidth = 1.5)
plt.ylim(0,1)
plt.ylabel('Puntaje', fontsize = 12)
plt.title('Métricas de evaluación de modelos', fontsize = 14, fontweight = 'bold', pad=20)
plt.axhline(y=0.7, color='#ED124C', linestyle='--', alpha = 0.5, label='Umbral 0.7')

for barra, valor, in zip(barras, valores):
    altura = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura + 0.01, f'{valor:.3f}',
        ha='center',
        va = 'bottom',
        fontweight='bold')
plt.legend()
plt.grid(axis='y', alpha = 0.3)
plt.tight_layout()
plt.show()

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1-Score: {f1_score}')