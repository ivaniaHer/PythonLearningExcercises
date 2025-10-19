# Requisito: Antes de ejecutar, instala las librerías necesarias.
# Abre tu terminal o command prompt y ejecuta:
# pip install scikit-learn pandas numpy joblib
#
# Para ejecutar el script, guarda este código como 'clasificador_gastos.py'
# y luego ejecuta en tu terminal:
# python clasificador_gastos.py

import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# Constantes para la generación de datos
CATEGORIAS = [
    "comida", "transporte", "renta", "entretenimiento", "salud", "educacion", "compras", "ahorro",
    "viajes", "mascotas", "servicios", "donaciones", "regalos", "hogar", "ropa", "tecnologia", "imprevistos"
]
METODOS = ["efectivo", "debito", "credito", "transferencia", "billetera"]
DIAS = ["lun", "mar", "mie", "jue", "vie", "sab", "dom"]
MERCHANTS = {
    "comida": ["Rest. El Sabor", "Taquería Centro", "Café UNAB"],
    "transporte": ["Bus El Centro", "Uber", "Gasolinera SV"],
    "renta": ["Inmobiliaria López"], "entretenimiento": ["Cine Metro", "GameZone", "Concierto Plaza"],
    "salud": ["Farmacia Salud+", "Clínica Central", "Laboratorio Plus"],
    "educacion": ["Librería Estudio", "UNAB", "Cursos Online"],
    "compras": ["Tienda Mega", "ElectroSV", "Mercado Central"], "ahorro": ["Transferencia Ahorros", "Bco Ahorros"],
    "viajes": ["Aerolínea SV", "Hotel Pacífico", "Agencia Viajes"], "mascotas": ["Vet Amigos", "PetShop Centro"],
    "servicios": ["ANDA", "AES", "Tigo", "Claro"], "donaciones": ["Fundación SV", "Iglesia Central"],
    "regalos": ["Regalitos SV", "Joyería Luna"], "hogar": ["Ferretería Casa", "Mantenimiento SRL"],
    "ropa": ["Moda Express", "Outlet Centro"], "tecnologia": ["TechZone", "CompuSV"],
    "imprevistos": ["Gastos Varios", "Emergencias SV"]
}
WEIGHTS_CAT = [18, 12, 10, 10, 8, 8, 15, 8, 6, 5, 9, 3, 4, 7, 7, 6, 6]
THRESH_ELEVADO = 150.0
THRESH_MEDIO = 40.0


def monto_categoria(cat):
    """Genera un monto aleatorio basado en la categoría."""
    if cat == "renta":
        mu, sigma = 250, 40
    elif cat == "ahorro":
        mu, sigma = -75, 25
    elif cat == "compras":
        mu, sigma = 65, 35
    elif cat == "comida":
        mu, sigma = 20, 12
    elif cat == "transporte":
        mu, sigma = 8, 5
    elif cat == "salud":
        mu, sigma = 45, 30
    elif cat == "educacion":
        mu, sigma = 80, 40
    elif cat == "entretenimiento":
        mu, sigma = 30, 20
    elif cat == "viajes":
        mu, sigma = 180, 110
    elif cat == "mascotas":
        mu, sigma = 35, 20
    elif cat == "servicios":
        mu, sigma = 45, 25
    elif cat == "donaciones":
        mu, sigma = 20, 20
    elif cat == "regalos":
        mu, sigma = 50, 30
    elif cat == "hogar":
        mu, sigma = 70, 60
    elif cat == "ropa":
        mu, sigma = 45, 35
    elif cat == "tecnologia":
        mu, sigma = 120, 100
    elif cat == "imprevistos":
        mu, sigma = 60, 90
    else:
        mu, sigma = 25, 20
    val = np.random.normal(mu, sigma)
    if cat == "ahorro":
        val = -abs(val)
    else:
        val = abs(val)
    if np.random.rand() < 0.03 and cat != "ahorro": val *= np.random.choice([2.5, 3.0])
    return float(np.round(val, 2))


def generar_transaccion():
    """Crea un diccionario representando una transacción."""
    cat = random.choices(CATEGORIAS, weights=WEIGHTS_CAT, k=1)[0]
    metodo = random.choices(METODOS, weights=[25, 25, 30, 15, 5], k=1)[0]
    dia = random.choices(DIAS, weights=[15, 15, 15, 15, 15, 15, 10], k=1)[0]
    hora = int(np.clip(np.random.normal(14, 4), 0, 23))
    mes = int(np.clip(np.random.normal(7, 3), 1, 12))
    monto = monto_categoria(cat)
    comercio = random.choice(MERCHANTS[cat])
    return {"monto": monto, "categoria": cat, "metodo": metodo, "dia_semana": dia, "hora": hora, "mes": mes,
            "comercio": comercio}


def etiquetar(txn):
    """Aplica una etiqueta a una transacción basada en reglas."""
    if txn["categoria"] == "ahorro" or txn["monto"] < 0: return "ahorro"
    if txn["monto"] >= THRESH_ELEVADO: return "elevado"
    if txn["monto"] >= THRESH_MEDIO: return "medio"
    return "otros"


# 3. FUNCIÓN PARA CLASIFICAR USANDO UN MODELO YA ENTRENADO Y GUARDADO
def clasificar_con_modelo_cargado(transaccion: dict, model_path: str) -> str:
    """
    Carga un pipeline de modelo desde un archivo y lo usa para clasificar
    una nueva transacción.
    """
    if not os.path.exists(model_path):
        return f"Error: No se encontró el archivo del modelo en '{model_path}'"
    pipeline_cargado = joblib.load(model_path)
    sample = pd.DataFrame([transaccion])
    pred = pipeline_cargado.predict(sample)[0]

    if pred in {"elevado", "medio", "ahorro", "otros"}:
        return pred
    else:
        return "otros"


if __name__ == "__main__":
    print(" PASO 1: Generando dataset de gastos...")
    random.seed(42)
    np.random.seed(42)
    N = 6000
    rows = [generar_transaccion() for _ in range(N)]
    df = pd.DataFrame(rows)
    df["etiqueta"] = df.apply(etiquetar, axis=1)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    csv_path = "dataset_gastos.csv"
    df.to_csv(csv_path, index=False, encoding="utf-8")
    print(f" -> Dataset de {N} filas guardado en: '{csv_path}'")
    print(" -> Distribución de clases generadas:")
    print(df["etiqueta"].value_counts())
    print("-" * 40)

    print("\n PASO 2: Entrenando el modelo Perceptrón (una sola neurona)...")
    X = df.drop(columns=["etiqueta"])
    y = df["etiqueta"]

    num_cols = ["monto", "hora", "mes"]
    cat_cols = ["categoria", "metodo", "dia_semana", "comercio"]

    preprocesador = ColumnTransformer([
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
    ])

    pipeline = Pipeline([
        ("prep", preprocesador),
        ("perceptron", Perceptron(max_iter=1000, tol=1e-3, random_state=42))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f" -> Accuracy en el conjunto de prueba: {acc:.4f}\n")
    print(" -> Reporte de clasificación:")
    print(classification_report(y_test, y_pred, zero_division=0))
    print("-" * 40)

    print("\n PASO 3: Guardando el pipeline del modelo entrenado...")
    model_path = "pipeline_gastos_perceptron.joblib"
    joblib.dump(pipeline, model_path)
    print(f" -> Modelo guardado en: '{model_path}'")
    print("-" * 40)

    print("\n PASO 4: Probando la clasificación con una nueva transacción...")

    # Define aquí la transacción que quieres clasificar
    # ¡Puedes cambiar estos valores para probar!
    transaccion_a_probar = {
        "monto": 275.0,
        "categoria": "compras",
        "metodo": "debito",
        "dia_semana": "vie",
        "hora": 15,
        "mes": 10,
        "comercio": "Tienda Mega"
    }

    print(f"\nTransacción de prueba: {transaccion_a_probar}")

    etiqueta_predicha = clasificar_con_modelo_cargado(transaccion_a_probar, model_path)

    print(f"  -> Etiqueta Predicha: {etiqueta_predicha.upper()}")

    transaccion_otros = {
        "monto": 15.75,
        "categoria": "mascotas",
        "metodo": "efectivo",
        "dia_semana": "mar",
        "hora": 17,
        "mes": 4,
        "comercio": "PetShop Centro"
    }
    print(f"\nTransacción de prueba: {transaccion_otros}")
    etiqueta_predicha_2 = clasificar_con_modelo_cargado(transaccion_otros, model_path)
    print(f"  -> Etiqueta Predicha: {etiqueta_predicha_2.upper()}")