import streamlit as st
st.image("logo.png", width=150)

st.set_page_config(page_title="BetMinder Pro", page_icon="📊")
st.title("📊 BetMinder: Gestión de Riesgo para Apostadores")
st.write("Calculá tu apuesta óptima y protegé tu capital de las rachas de pérdidas.")

st.header("🧮 Calculadora Matemática Gratuita")
bankroll = st.number_input("Ingresá tu capital actual ($):", min_value=10.0, value=500.0, step=10.0)
cuota = st.number_input("Cuota del evento (Ej: 1.85):", min_value=1.01, value=1.85, step=0.05)

if cuota > 1:
    stake_sugerido = (bankroll * 0.03) / (cuota - 1)
    st.info(f"Monto máximo sugerido para esta apuesta: **${stake_sugerido:.2f} USD**")
else:
    st.warning("Introduce una cuota válida.")

st.markdown("---")
st.subheader("🚨 Desbloqueá la Protección Avanzada Anti-Racha (Pro)")
st.write("Con la cuenta Premium, el sistema registra tus operaciones y te bloquea el acceso si entrás en pérdida descontrolada.")
st.button("🔥 Activar Plan Inicial ($5/mes)", disabled=True)
st.caption("Módulo de pago en proceso de configuración.")
