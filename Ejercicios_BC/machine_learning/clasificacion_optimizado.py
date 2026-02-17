import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import numpy as np
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

def metricas_manual(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    acc = (tp + tn) / (tp + tn + fp + fn)
    prec = tp / (tp + fp) if (tp + fp) != 0 else 0
    rec = tp / (tp + fn) if (tp + fn) != 0 else 0
    f1 = 2 * (prec * rec) / (prec + rec) if (prec + rec) != 0 else 0

    return {
        "Accuracy": acc,
        "Precision": prec,
        "Recall": rec,
        "F1": f1}

def metricas_sklearn(y_true, y_pred):
    return {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred),
        "Recall": recall_score(y_true, y_pred),
        "F1": f1_score(y_true, y_pred)
    }

def evaluar(df, nombre):
    print(f"\n===== {nombre} =====")

    y_true = df['clasificacion_real']
    y_pred = df['prediccion']

    manual = metricas_manual(y_true, y_pred)
    skl = metricas_sklearn(y_true, y_pred)

    resumen = pd.DataFrame({
        "Manual": manual,
        "Sklearn": skl
    })

    print(resumen)
    return resumen

evaluar(df_spam, "CLASIFICACIÓN SPAM")

#Grafica

y_true_f = df_fraude['clasificacion_real']
y_pred_f = df_fraude['prediccion']

y_true_s = df_spam['clasificacion_real']
y_pred_s = df_spam['prediccion']

metricas1 = metricas_sklearn(y_true_f, y_pred_f)
valores1 = list(metricas1.values())

metricas2 = metricas_sklearn(y_true_s, y_pred_s)
valores2 = list(metricas2.values())

nombres = list(metricas1.keys())

colores = ['#690C34','#BB165E','#E9448B','#F396BE']
x = np.arange(len(nombres))
width = 0.35

plt.figure(figsize=(10,6))

plt.bar(x - width/2, valores1, width, label='SPAM')
plt.bar(x + width/2, valores2, width, label='NUEVO')

plt.xticks(x, nombres)
plt.ylim(0,1)
plt.ylabel("Puntaje")
plt.title("Comparación de Métricas entre Datasets")
plt.axhline(y=0.7, linestyle='--', alpha=0.5)

plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
evaluar(df_fraude, "CLASIFICACIÓN FRAUDE")


