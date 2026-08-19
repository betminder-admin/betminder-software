import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Configuración de la página web
st.set_page_config(page_title="Calculador Geométrico Total", layout="wide")

st.title("📐 Generador y Calculador Geométrico Integral")
st.write("Calculá superficies, perímetros, volúmenes y propiedades topológicas con renderizado sólido.")

# --- MENÚ PRINCIPAL POR PESTAÑAS ---
tab2d, tab3d = st.tabs(["📐 Figuras Geométricas (2D)", "📦 Cuerpos Geométricos (3D)"])

# ==========================================
# 📐 SECCIÓN: FIGURAS GEOMÉTRICAS (2D)
# ==========================================
with tab2d:
    # Los controles solo aparecen si la pestaña 2D está activa
    st.sidebar.markdown("### 🔧 Configuración 2D")
    figura_2d = st.sidebar.selectbox(
        "Seleccione la Figura:", 
        ["Triángulo Equilátero", "Cuadrado", "Rectángulo", "Pentágono Regular", "Hexágono Regular", "Círculo"],
        key="sel_2d"
    )
    
    perimetro, superficie = 0.0, 0.0
    fig_2d, ax_2d = plt.subplots(figsize=(4, 4))
    
    if figura_2d == "Triángulo Equilátero":
        lado = st.sidebar.number_input("Lado (l):", min_value=0.1, value=5.0, key="tri_l")
        perimetro = 3 * lado
        superficie = (np.sqrt(3) / 4) * (lado ** 2)
        h = lado * np.sqrt(3) / 2
        puntos = np.array([[0, 0], [lado, 0], [lado/2, h], [0, 0]])
        ax_2d.plot(puntos[:,0], puntos[:,1], 'r-')
        ax_2d.fill(puntos[:,0], puntos[:,1], 'red', alpha=0.3)
        
    elif figura_2d == "Cuadrado":
        lado = st.sidebar.number_input("Lado (l):", min_value=0.1, value=5.0, key="cua_l")
        perimetro = 4 * lado
        superficie = lado ** 2
        puntos = np.array([[0, 0], [lado, 0], [lado, lado], [0, lado], [0, 0]])
        ax_2d.plot(puntos[:,0], puntos[:,1], 'b-')
        ax_2d.fill(puntos[:,0], puntos[:,1], 'blue', alpha=0.3)
        
    elif figura_2d == "Rectángulo":
        base = st.sidebar.number_input("Base (b):", min_value=0.1, value=6.0, key="rec_b")
        altura = st.sidebar.number_input("Altura (h):", min_value=0.1, value=4.0, key="rec_h")
        perimetro = 2 * (base + altura)
        superficie = base * altura
        puntos = np.array([[0, 0], [base, 0], [base, altura], [0, altura], [0, 0]])
        ax_2d.plot(puntos[:,0], puntos[:,1], 'g-')
        ax_2d.fill(puntos[:,0], puntos[:,1], 'green', alpha=0.3)
        
    elif figura_2d in ["Pentágono Regular", "Hexágono Regular"]:
        n_lados = 5 if figura_2d == "Pentágono Regular" else 6
        lado = st.sidebar.number_input("Lado (l):", min_value=0.1, value=4.0, key="poly_l")
        radio = lado / (2 * np.sin(np.pi / n_lados))
        apotema = lado / (2 * np.tan(np.pi / n_lados))
        perimetro = n_lados * lado
        superficie = (perimetro * apotema) / 2
        angulos = np.linspace(0, 2*np.pi, n_lados + 1)
        x = radio * np.cos(angulos)
        y = radio * np.sin(angulos)
        ax_2d.plot(x, y, 'm-')
        ax_2d.fill(x, y, 'magenta', alpha=0.3)
        
    elif figura_2d == "Círculo":
        radio = st.sidebar.number_input("Radio (r):", min_value=0.1, value=3.0, key="cir_r")
        perimetro = 2 * np.pi * radio
        superficie = np.pi * (radio ** 2)
        angulos = np.linspace(0, 2*np.pi, 100)
        x = radio * np.cos(angulos)
        y = radio * np.sin(angulos)
        ax_2d.plot(x, y, 'orange')
        ax_2d.fill(x, y, 'orange', alpha=0.3)

    ax_2d.set_aspect('equal')
    ax_2d.axis('off')

    col1_2d, col2_2d = st.columns(2)
    with col1_2d:
        st.subheader("📊 Resultados Métricos (2D)")
        st.metric(label="Perímetro", value=f"{perimetro:.2f} u")
        st.metric(label="Superficie (Área)", value=f"{superficie:.2f} u²")
    with col2_2d:
        st.subheader("🖼️ Representación 2D")
        st.pyplot(fig_2d)

# ==========================================
# 📦 SECCIÓN: CUERPOS GEOMÉTRICOS (3D)
# ==========================================
with tab3d:
    st.sidebar.markdown("### 🔧 Configuración 3D")
    cuerpo_3d = st.sidebar.selectbox(
        "Seleccione el Cuerpo:", 
        ["Cubo", "Prisma Rectangular", "Pirámide Cuadrangular", "Cilindro", "Cono", "Esfera"],
        key="sel_3d"
    )
    
    sup_3d, vol_3d = 0.0, 0.0
    caras, aristas, vertices = 0, 0, 0
    fig_3d = plt.figure(figsize=(5, 5))
    ax_3d = fig_3d.add_subplot(111, projection='3d')
    
    if cuerpo_3d == "Cubo":
        lado = st.sidebar.number_input("Lado:", min_value=0.1, value=5.0, key="cub_l")
        sup_3d = 6 * (lado ** 2)
        vol_3d = lado ** 3
        caras, aristas, vertices = 6, 12, 8
        
        r = [0, lado]
        xx, yy = np.meshgrid(r, r)
        ax_3d.plot_surface(xx, yy, np.atleast_2d(0), alpha=0.4, color='cyan')
        ax_3d.plot_surface(xx, yy, np.atleast_2d(lado), alpha=0.4, color='cyan')
        ax_3d.plot_surface(xx, np.atleast_2d(0), yy, alpha=0.4, color='cyan')
        ax_3d.plot_surface(xx, np.atleast_2d(lado), yy, alpha=0.4, color='cyan')
        ax_3d.plot_surface(np.atleast_2d(0), xx, yy, alpha=0.4, color='cyan')
        ax_3d.plot_surface(np.atleast_2d(lado), xx, yy, alpha=0.4, color='cyan')

    elif cuerpo_3d == "Prisma Rectangular":
        a = st.sidebar.number_input("Ancho (X):", min_value=0.1, value=4.0, key="pr_a")
        b = st.sidebar.number_input("Largo (Y):", min_value=0.1, value=6.0, key="pr_b")
        c = st.sidebar.number_input("Alto (Z):", min_value=0.1, value=3.0, key="pr_c")
        sup_3d = 2 * (a*b + b*c + a*c)
        vol_3d = a * b * c
        caras, aristas, vertices = 6, 12, 8
        
        # Dibujar caras del prisma de forma sólida
        x_m, y_m = np.meshgrid([0, a], [0, b])
        ax_3d.plot_surface(x_m, y_m, np.atleast_2d(0), alpha=0.4, color='royalblue')
        ax_3d.plot_surface(x_m, y_m, np.atleast_2d(c), alpha=0.4, color='royalblue')
        x_m, z_m = np.meshgrid([0, a], [0, c])
        ax_3d.plot_surface(x_m, np.atleast_2d(0), z_m, alpha=0.4, color='royalblue')
        ax_3d.plot_surface(x_m, np.atleast_2d(b), z_m, alpha=0.4, color='royalblue')

    elif cuerpo_3d == "Pirámide Cuadrangular":
        base_l = st.sidebar.number_input("Lado de la Base:", min_value=0.1, value=4.0, key="pi_b")
        h_pir = st.sidebar.number_input("Altura Pirámide:", min_value=0.1, value=6.0, key="pi_h")
        ap_reg = np.sqrt((base_l/2)**2 + h_pir**2)
        sup_3d = (base_l ** 2) + 2 * base_l * ap_reg
        vol_3d = (base_l ** 2) * h_pir / 3
        caras, aristas, vertices = 5, 8, 5
        
        # Definición de los 5 vértices reales
        p0 = [0, 0, 0]
        p1 = [base_l, 0, 0]
        p2 = [base_l, base_l, 0]
        p3 = [0, base_l, 0]
        p4 = [base_l/2, base_l/2, h_pir] # Cúspide
        
        # Unimos los vértices para formar los polígonos de las 5 caras
        caras_poligono = [
            [p0, p1, p2, p3], # Base cuadrangular
            [p0, p1, p4],     # Cara frontal
            [p1, p2, p4],     # Cara derecha
            [p2, p3, p4],     # Cara trasera
            [p3, p0, p4]      # Cara izquierda
        ]
        # Agregamos la colección 3D con relleno rojo traslúcido
        ax_3d.add_collection3d(Poly3DCollection(caras_poligono, facecolors='red', linewidths=1, edgecolors='darkred', alpha=0.4))
        
        # Ajustar límites de visualización manualmente para la pirámide
        ax_3d.set_xlim(0, base_l)
        ax_3d.set_ylim(0, base_l)
        ax_3d.set_zlim(0, h_pir)

    elif cuerpo_3d == "Cilindro":
        radio = st.sidebar.number_input("Radio:", min_value=0.1, value=3.0, key="cil_r")
        altura = st.sidebar.number_input("Altura:", min_value=0.1, value=7.0, key="cil_h")
        sup_3d = 2 * np.pi * radio * (radio + altura)
        vol_3d = np.pi * (radio ** 2) * altura
        caras, aristas, vertices = 3, 2, 0
        
        z = np.linspace(0, altura, 20)
        theta = np.linspace(0, 2*np.pi, 20)
        theta_grid, z_grid = np.meshgrid(theta, z)
        ax_3d.plot_surface(radio*np.cos(theta_grid), radio*np.sin(theta_grid), z_grid, alpha=0.4, color='orange')

    elif cuerpo_3d == "Cono":
        radio = st.sidebar.number_input("Radio Base:", min_value=0.1, value=3.0, key="con_r")
        altura = st.sidebar.number_input("Altura Cono:", min_value=0.1, value=6.0, key="con_h")
        g = np.sqrt(radio**2 + altura**2)
        sup_3d = np.pi * radio * (radio + g)
        vol_3d = (np.pi * (radio**2) * altura) / 3
        caras, aristas, vertices = 2, 1, 1
        
        z = np.linspace(0, altura, 20)
        theta = np.linspace(0, 2*np.pi, 20)
        theta_g, z_g = np.meshgrid(theta, z)
        r_dinamico = radio * (1 - z_g/altura)
        ax_3d.plot_surface(r_dinamico*np.cos(theta_g), r_dinamico*np.sin(theta_g), z_g, alpha=0.4, color='purple')

    elif cuerpo_3d == "Esfera":
        radio = st.sidebar.number_input("Radio:", min_value=0.1, value=4.0, key="esf_r")
        sup_3d = 4 * np.pi * (radio ** 2)
        vol_3d = (4/3) * np.pi * (radio ** 3)
        caras, aristas, vertices = 1, 0, 0
        
        u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:30j]
        ax_3d.plot_surface(radio*np.cos(u)*np.sin(v), radio*np.sin(u)*np.sin(v), radio*np.cos(v), alpha=0.4, color='lightgreen')

    ax_3d.set_xlabel('Eje X')
    ax_3d.set_ylabel('Eje Y')
    ax_3d.set_zlabel('Eje Z')

    col1_3d, col2_3d = st.columns(2)
    with col1_3d:
        st.subheader("📊 Análisis del Cuerpo (3D)")
        st.metric(label="Superficie Total", value=f"{sup_3d:.2f} u²")
        st.metric(label="Volumen", value=f"{vol_3d:.2f} u³")
        st.markdown("---")
        st.write(f"• **Caras:** {caras} | • **Aristas:** {aristas} | • **Vértices:** {vertices}")
    with col2_3d:
        st.subheader("📦 Renderizado 3D")
        st.pyplot(fig_3d)
