import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Calculador Geométrico 3D", layout="wide")

st.title("📐 Generador y Calculador Geométrico 3D")
st.write("Selecciona un cuerpo geométrico, ingresa sus dimensiones y obtén sus propiedades topológicas y métricas.")

# --- BARRA LATERAL: CONTROLES ---
st.sidebar.header("Configuración del Cuerpo")
cuerpo = st.sidebar.selectbox("Seleccione el Cuerpo:", ["Cubo", "Cilindro", "Esfera"])

# Inicialización de variables de cálculo
sup, vol = 0.0, 0.0
caras, aristas, vertices = 0, 0, 0

# Crear la figura 3D de Matplotlib
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

# --- LÓGICA POR CUERPO ---
if cuerpo == "Cubo":
    lado = st.sidebar.number_input("Lado:", min_value=0.1, value=5.0, step=0.5)
    
    # Cálculos
    sup = 6 * (lado ** 2)
    vol = lado ** 3
    caras, aristas, vertices = 6, 12, 8
    
    # Gráfico
    r = [0, lado]
    X, Y, Z = np.meshgrid(r, r, r)
    ax.scatter(X, Y, Z, alpha=0)
    xx, yy = np.meshgrid(r, r)
    ax.plot_surface(xx, yy, np.atleast_2d(0), alpha=0.4, color='cyan')
    ax.plot_surface(xx, yy, np.atleast_2d(lado), alpha=0.4, color='cyan')
    ax.plot_surface(xx, np.atleast_2d(0), yy, alpha=0.4, color='cyan')
    ax.plot_surface(xx, np.atleast_2d(lado), yy, alpha=0.4, color='cyan')
    ax.plot_surface(np.atleast_2d(0), xx, yy, alpha=0.4, color='cyan')
    ax.plot_surface(np.atleast_2d(lado), xx, yy, alpha=0.4, color='cyan')

elif cuerpo == "Cilindro":
    radio = st.sidebar.number_input("Radio:", min_value=0.1, value=3.0, step=0.5)
    altura = st.sidebar.number_input("Altura:", min_value=0.1, value=7.0, step=0.5)
    
    # Cálculos
    sup = 2 * np.pi * radio * (radio + altura)
    vol = np.pi * (radio ** 2) * altura
    caras, aristas, vertices = 3, 2, 0
    
    # Gráfico
    z = np.linspace(0, altura, 20)
    theta = np.linspace(0, 2*np.pi, 20)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radio * np.cos(theta_grid)
    y_grid = radio * np.sin(theta_grid)
    ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.4, color='orange')
    r_tapa, th_tapa = np.meshgrid(np.linspace(0, radio, 10), theta)
    ax.plot_surface(r_tapa*np.cos(th_tapa), r_tapa*np.sin(th_tapa), np.atleast_2d(0), alpha=0.5, color='orange')
    ax.plot_surface(r_tapa*np.cos(th_tapa), r_tapa*np.sin(th_tapa), np.atleast_2d(altura), alpha=0.5, color='orange')

elif cuerpo == "Esfera":
    radio = st.sidebar.number_input("Radio:", min_value=0.1, value=4.0, step=0.5)
    
    # Cálculos
    sup = 4 * np.pi * (radio ** 2)
    vol = (4/3) * np.pi * (radio ** 3)
    caras, aristas, vertices = 1, 0, 0
    
    # Gráfico
    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = radio * np.outer(np.cos(u), np.sin(v))
    y = radio * np.outer(np.sin(u), np.sin(v))
    z = radio * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, alpha=0.4, color='gainsboro', edgecolor='blue', lw=0.3)

# Ajustes visuales de la gráfica
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title(f"Visualización de {cuerpo}")

# --- DISTRIBUCIÓN EN PANTALLA ---
col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("📊 Resultados de Análisis")
    
    # Métricas principales
    st.metric(label="Superficie Total", value=f"{sup:.2f} u²")
    st.metric(label="Volumen", value=f"{vol:.2f} u³")
    
    st.markdown("---")
    st.markdown("**Propiedades del Poliedro:**")
    st.write(f"• **Caras:** {caras}")
    st.write(f"• **Aristas:** {aristas}")
    st.write(f"• **Vértices:** {vertices}")
    
    # --- INTEGRACIÓN COMPONENTES DE MONETIZACIÓN (Ejemplo Lemon Squeezy) ---
    st.markdown("---")
    st.subheader("⭐ Versión Premium")
    st.write("Desbloquea exportación en PDF, CAD y soporte para figuras complejas.")
    # Link directo al checkout creado en tu panel de Lemon Squeezy
    st.markdown("[🚀 Comprar Acceso Premium](https://lemonsqueezy.com)", unsafe_allow_html=True)

with col2:
    st.subheader("📦 Renderizado 3D Interactivo")
    # Mostrar el gráfico de Matplotlib en la app web
    st.pyplot(fig)
