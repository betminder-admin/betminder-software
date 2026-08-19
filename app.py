import streamlit as st
import pandas as pd

# 1. ÓPTICA BASE: Configuración visual centrada de la app
st.set_page_config(page_title="BetMinder Pro", page_icon="📊", layout="centered")

# Muestra tu logotipo profesional de Canva
st.image("BetMinder.png", width=140)

st.title("📊 BetMinder: Gestión Automatizada de Riesgo")
st.write("Calculá tu stake matemático óptimo y protegé tu dinero de decisiones emocionales.")

# --- SECCIÓN GRATUITA (EL GANCHO) ---
st.markdown("### 🧮 Calculadora de Apuesta (Criterio Kelly)")

# Entradas numéricas integradas en dos columnas limpias
col_in1, col_in2 = st.columns(2)
with col_in1:
    bankroll = st.number_input("Ingresá tu capital actual ($):", min_value=10.0, value=500.0, step=10.0)
with col_in2:
    cuota = st.number_input("Cuota del evento (Ej: 1.85):", value=1.85, step=0.05, format="%.2f")

# Lógica matemática interna
if cuota > 1.00:
    stake_sugerido = (bankroll * 0.03) / (cuota - 1.00)
    # Tope máximo de seguridad del 10%
    if stake_sugerido > (bankroll * 0.10): 
        stake_sugerido = bankroll * 0.10
    
    # 🎨 ÓPTICA OPCIÓN 1: Tarjetas de Métricas Grandes e Impactantes
    st.markdown("#### 📈 Resultados del Análisis de Riesgo")
    m_col1, m_col2, m_col3 = st.columns(3)
    m_col1.metric(label="Banca a Proteger", value=f"${bankroll:.2f}")
    m_col2.metric(label="Inversión Máxima", value=f"${stake_sugerido:.2f}", delta="-3.0% Base")
    m_col3.metric(label="Nivel de Alerta", value="Seguro" if cuota > 1.5 else "Riesgoso")
    
    # 🎨 ÓPTICA OPCIÓN 2: Gráfico de Barras de Distribución de Capital
    st.markdown("#### 📊 Distribución Óptica de la Banca")
    datos_grafico = pd.DataFrame({
        'Categoría': ['Capital Seguro', 'Monto a Arriesgar'],
        'Monto ($)': [bankroll - stake_sugerido, stake_sugerido]
    })
    st.bar_chart(datos_grafico, x='Categoría', y='Monto ($)', color="#1E3A8A")

else:
    st.warning("⚠️ La cuota introducida no es válida. Debe ser mayor a 1.00 para calcular el riesgo.")

# --- BARRERA DE PAGO (MONETIZACIÓN SaaS) ---
st.markdown("---")

# 🎨 ÓPTICA OPCIÓN 3: Tarjeta Contenedora Estilizada con Bordes para el Plan Pro
with st.container(border=True):
    st.subheader("🚨 Desbloqueá la Protección Avanzada Anti-Racha (Pro)")
    st.write("""
    ¿Sabías que el 95% de los apostadores pierden por no saber detenerse? 
    Con la cuenta Premium, el sistema registra tus operaciones en tiempo real y te da acceso al panel avanzado de control para frenar tus pérdidas diarias antes de entrar en estado de ira (tilt).
    """)
    
    # Botón interactivo destacado que redirige a tu comunidad de Telegram
    url_comunidad = "https://t.me"
    st.link_button("🔥 Unirse al Canal y Activar Plan Pro", url_comunidad, type="primary", use_container_width=True)
    st.caption("🔒 Acceso seguro vía Telegram. Suscripción mensual administrada por soporte. Cancela cuando quieras.")
