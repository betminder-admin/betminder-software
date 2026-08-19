import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página web
st.set_page_config(page_title="Calculador Geométrico Total", layout="wide")

st.title("📐 Generador y Calculador Geométrico Integral")
st.write("Calculá superficies, perímetros, volúmenes y propiedades topológicas de figuras 2D y cuerpos 3D.")

# --- MENÚ PRINCIPAL POR PESTAÑAS ---
tab2d, tab3d = st.tabs(["平面 Figuras Geométricas (2D)", "📦 Cuerpos Geométricos (3D)"])

# ==========================================
# 📐 SECCIÓN: FIGURAS GEOMÉTRICAS (2D)
# ==========================================
with tab2d:
    st.sidebar.header("Configuración 2D")
    figura_2d = st.sidebar.selectbox(
        "Seleccione la Figura:", 
        ["Triángulo Equilátero", "Cuadrado", "Rectángulo", "Pentágono Regular", "Hexágono Regular", "Círculo"]
    )
    
    perimetro, superficie = 0.0, 0.0
    fig_2d, ax_2d = plt.subplots(figsize=(4, 4))
    
    if figura_2d == "Triángulo Equilátero":
        lado = st.sidebar.number_input("Lado (l):", min_value=0.1, value=5.0, key="tri_l")
        perimetro = 3 * lado
        superficie = (np.sqrt(3) / 4) * (lado ** 2)
        # Gráfico
        h = lado * np.sqrt(3) / 2
        puntos = np.array([[0, 0], [lado, 0], [lado/2, h], [0, 0]])
        ax_2d.plot(puntos[:,0], puntos[:,1], 'r-')
        ax_2d.fill(puntos[:,0], puntos[:,1], 'red', alpha=0.3)
        
    elif figura_2d == "Cuadrado":
        lado = st.sidebar.number_input("Lado (l):", min_value=0.1, value=5.0, key="cua_l")
        perimetro = 4 * lado
        superficie = lado ** 2
        # Gráfico
        puntos = np.array([[0, 0], [lado, 0], [lado, lado], [0, lado], [0, 0]])
        ax_2d.plot(puntos[:,0], puntos[:,1], 'b-')
        ax_2d.fill(puntos[:,0], puntos[:,1], 'blue', alpha=0.3)
        
    elif figura_2d == "Rectángulo":
        base = st.sidebar.number_input("Base (b):", min_value=0.1, value=6.0)
        altura = st.sidebar.number_input("Altura (h):", min_value=0.1, value=4.0)
        perimetro = 2 * (base + altura)
        superficie = base * altura
        # Gráfico
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
        # Gráfico
        angulos = np.linspace(0, 2*np.pi, n_lados + 1)
        x = radio * np.cos(angulos)
        y = radio * np.sin(angulos)
        ax_2d.plot(x, y, 'm-')
        ax_2d.fill(x, y, 'magenta', alpha=0.3)
        
    elif figura_2d == "Círculo":
        radio = st.sidebar.number_input("Radio (r):", min_value=0.1, value=3.0, key="cir_r")
        perimetro = 2 * np.pi * radio
        superficie = np.pi * (radio ** 2)
        # Gráfico
        angulos = np.linspace(0, 2*np.pi, 100)
        x = radio * np.cos(angulos)
        y = radio * np.sin(angulos)
        ax_2d.plot(x, y, 'orange')
        ax_2d.fill(x, y, 'orange', alpha=0.3)

    ax_2d.set_aspect('equal')
    ax_2d.axis('off')

    # Despliegue en pantalla 2D
    col1_2d, col2_2d = st.columns(2)
    with col1_2d:
        st.subheader("📊 Resultados Métricos")
        st.metric(label="Perímetro", value=f"{perimetro:.2f} u")
        st.metric(label="Superficie (Área)", value=f"{superficie:.2f} u²")
    with col2_2d:
        st.subheader("🖼️ Representación 2D")
        st.pyplot(fig_2d)

# ==========================================
# 📦 SECCIÓN: CUERPOS GEOMÉTRICOS (3D)
# ==========================================
with tab3d:
    st.sidebar.header("Configuración 3D")
    cuerpo_3d = st.sidebar.selectbox(
        "Seleccione el Cuerpo:", 
        ["Cubo", "Prisma Rectangular", "Pirámide Cuadrangular", "Cilindro", "Cono", "Esfera"]
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
        X, Y, Z = np.meshgrid(r, r, r)
        ax_3d.scatter(X, Y, Z, alpha=0)
        xx, yy = np.meshgrid(r, r)
        ax_3d.plot_surface(xx, yy, np.atleast_2d(0), alpha=0.4, color='cyan')
        ax_3d.plot_surface(xx, yy, np.atleast_2d(lado), alpha=0.4, color='cyan')
        ax_3d.plot_surface(xx, np.atleast_2d(0), yy, alpha=0.4, color='cyan')
        ax_3d.plot_surface(xx, np.atleast_2d(lado), yy, alpha=0.4, color='cyan')

    elif cuerpo_3d == "Prisma Rectangular":
        a = st.sidebar.number_input("Ancho (a):", min_value=0.1, value=4.0)
        b = st.sidebar.number_input("Largo (b):", min_value=0.1, value=6.0)
        c = st.sidebar.number_input("Alto (c):", min_value=0.1, value=3.0)
        sup_3d = 2 * (a*b + b*c + a*c)
        vol_3d = a * b * c
        caras, aristas, vertices = 6, 12, 8
        # Esqueleto básico representativo
        X, Y, Z = np.meshgrid([0, a], [0, b], [0, c])
        ax_3d.scatter(X, Y, Z, color='blue')

    elif cuerpo_3d == "Pirámide Cuadrangular":
        base_l = st.sidebar.number_input("Lado de la Base:", min_value=0.1, value=4.0)
        h_pir = st.sidebar.number_input("Altura Pirámide:", min_value=0.1, value=6.0)
        ap_reg = np.sqrt((base_l/2)**2 + h_pir**2)
        sup_3d = (base_l ** 2) + 2 * base_l * ap_reg
        vol_3d = (base_l ** 2) * h_pir / 3
        caras, aristas, vertices = 5, 8, 5
        # Coordenadas vértices
        v = np.array([[0,0,0], [base_l,0,0], [base_l,base_l,0], [0,base_l,0], [base_l/2,base_l/2,h_pir]])
        ax_3d.scatter(v[:,0], v[:,1], v[:,2], color='red')

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
        # Generación visual básica
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

    # Despliegue en pantalla 3D
    col1_3d, col2_3d = st.columns(2)
    with col1_3d:
        st.subheader("📊 Análisis del Cuerpo")
        st.metric(label="Superficie Total", value=f"{sup_3d:.2f} u²")
        st.metric(label="Volumen", value=f"{vol_3d:.2f} u³")
        st.markdown("---")
        st.write(f"• **Caras:** {caras} | • **Aristas:** {aristas} | • **Vértices:** {vertices}")
    with col2_3d:
        st.subheader("📦 Renderizado 3D")
        st.pyplot(fig_3d)
