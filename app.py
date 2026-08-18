import streamlit as st

# Configuración visual de la aplicación web
st.set_page_config(page_title="BetMinder Pro", page_icon="📊", layout="centered")

# Muestra tu nuevo logotipo profesional
st.image("BetMinder.png", width=150)

st.title("📊 BetMinder: Gestión Automatizada de Riesgo")
st.write("Calculá tu stake matemático óptimo y protegé tu dinero de decisiones emocionales.")

# --- SECCIÓN GRATUITA (EL GANCHO) ---
st.header("🧮 Calculadora de Apuesta (Criterio Kelly)")

bankroll = st.number_input("Ingresá tu capital actual ($):", min_value=10.0, value=500.0, step=10.0)
cuota = st.number_input("Cuota del evento (Ej: 1.85):", min_value=1.01, value=1.85, step=0.05)

# Lógica matemática estricta y corregida
if cuota > 1.00:
    # Se sugiere arriesgar un 3% base ajustado por la cuota
    stake_sugerido = (bankroll * 0.03) / (cuota - 1.00)
    
    # Tope máximo de seguridad del 10%
    if stake_sugerido > (bankroll * 0.10): 
        stake_sugerido = bankroll * 0.10
        
    st.info(f"Monto máximo sugerido para esta apuesta: **${stake_sugerido:.2f} USD**")
else:
    st.warning("⚠️ La cuota introducida no es válida. Debe ser mayor a 1.00 para calcular el riesgo.")

# --- BARRERA DE PAGO (MONETIZACIÓN SaaS) ---
st.markdown("---") 
st.subheader("🚨 Desbloqueá la Protección Avanzada Anti-Racha (Pro)")
st.write("""
¿Sabías que el 95% de los apostadores pierden por no saber detenerse? 
Con la cuenta Premium, el sistema registra tus operaciones en tiempo real y te da acceso al panel avanzado de control para frenar tus pérdidas diarias antes de entrar en estado de ira (tilt).
""")

# URL provisional hasta que Lemon Squeezy te dé el alta oficial
url_pago_real = "https://lemonsqueezy.com"

st.link_button("🔥 Activar Plan Inicial ($5/mes por 3 meses)", url_pago_real, type="primary")
st.caption("🔒 Facturación segura. Luego de 3 meses, la suscripción pasa a $9/mes de forma automática. Cancela cuando quieras con un clic.")
