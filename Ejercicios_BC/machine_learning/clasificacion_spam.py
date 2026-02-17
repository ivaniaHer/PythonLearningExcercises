import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# Se guardan los datos en un Dataframe
dataSpam = {
    'clasificacion_real':[1,1,1,0,0,0,0,1,0,1],
    'prediccion': [1,0,1,0,0,1,0,1,0,0]
}

dataFraude = {
    'clasificacion_real': [0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0],
    'prediccion': [0,1,1,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0],
}

df_spam = pd.DataFrame(dataSpam)
df_fraude = pd.DataFrame(dataFraude)

# condicion dentro de df[] = Solo se quedan las filas donde la condicion es true
# len() cuenta cuantas filas quedaron después del filtro
# se encarga de analizar el dataframe y extraer las variables importantes para el calculo
def extraer_variables(df):
    verdadero_positivo  = len(df[(df['clasificacion_real'] == 1) & (df['prediccion']) == 1])
    verdadero_negativo = len(df[(df['clasificacion_real'] == 0) & (df['prediccion'] == 0)])
    falso_positivo = len(df[(df['clasificacion_real'] == 0) & (df['prediccion'] == 1)])
    falso_negativo = len(df[(df['clasificacion_real'] == 1) & (df['prediccion'] == 0)])
    return verdadero_positivo, verdadero_negativo, falso_positivo, falso_negativo

def calcular_metricas(vp,vn,fp,fn):
    acc = (vp+vn)/(vp+vn+fp+fn)
    pre = vp/(vp+fp)
    rec = vp/(vp+fn)
    f_sc = (pre*rec)/(pre+rec)*2
    return  acc, pre, rec, f_sc

def calculos_sklearn(true,pred):
    acc_skl = accuracy_score(true,pred)
    prec_skl = precision_score(true,pred)
    rec_skl = recall_score(true, pred)
    f_sc_skl = f1_score(true,pred)
    return acc_skl, prec_skl, rec_skl, f_sc_skl

def imprimir_resultados(accuracy, precision, recall, f_score):
    print(f'Accuracy: {accuracy} = {accuracy*100}%')
    print(f'Precision: {precision:.2f} = {precision*100:.2f}%')
    print(f'Recall: {recall:.2f} = {recall*100:.2f}%')
    print(f'F-Score: {f_score:.2f} = {f_score*100:.2f}%')

print('EJERCICIO 1: CLASIFICACIÓN DE SPAM')
VP,VN,FP,FN = extraer_variables(df_spam)
print(f'VP: {VP}\nVN: {VN}\nFP: {FP}\nFN: {FN}')
accuracy, precision, recall, f_score = calcular_metricas(VP,VN,FP,FN)
print(f'\nRESULTADO DE MÉTRICAS')
imprimir_resultados(accuracy,precision, recall, f_score)

# USO DE SKLEARN
y_true = df_spam['clasificacion_real']
y_pred = df_spam['prediccion']

accuracy_skl, precision_skl, recall_skl, f_score_skl = calculos_sklearn(y_true, y_pred)
print(f'\nResultados con SKLEARN')
imprimir_resultados(accuracy_skl,precision_skl, recall_skl, f_score_skl)

resumen = {
    'Manual': [accuracy, precision,recall,f_score],
    'SkLearn': [accuracy_skl, precision_skl, recall_skl, f_score_skl]
}
resumen_df = pd.DataFrame(resumen)
print('\nCOMPARATIVA DE MÉTODOS\n',resumen_df)

# Gráfica con matplotlib
plt.figure(figsize=(10,6))
metricas = ['Exactitud', 'Precision','Recall','F1_Score']
valores = [accuracy,precision,recall,f_score]
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


# Ejemplo 2: fraudes

print('\n----------------------------------------------------------------------')
print('\nEJEMPLO 2: CLASIFICACION DE FRAUDE\n')
VP,VN,FP,FN = extraer_variables(df_fraude)
print(f'VP: {VP}\nVN: {VN}\nFP: {FP}\nFN: {FN}')
accuracy, precision, recall, f_score = calcular_metricas(VP,VN,FP,FN)
print('\nRESULTADO DE MÉTRICAS')
imprimir_resultados(accuracy,precision, recall, f_score)

# SKlearn
y_true_f = df_fraude['clasificacion_real']
y_pred_f = df_fraude['prediccion']

accuracy_skl, precision_skl, recall_skl, f_score_skl = calculos_sklearn(y_true_f, y_pred_f)
print(f'\nResultados con SKLEARN')
imprimir_resultados(accuracy_skl,precision_skl, recall_skl, f_score_skl)

resumen = {
    'Manual': [accuracy, precision,recall,f_score],
    'SkLearn': [accuracy_skl, precision_skl, recall_skl, f_score_skl]
}
resumen_df = pd.DataFrame(resumen)
print('\nCOMPARATIVA DE MÉTODOS\n',resumen_df)


