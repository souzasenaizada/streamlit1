import streamlit as st

st.set_page_config(page_title="Atendimento Escola", page_icon="🎓")
st.title("Atendimento Virtual - Escola")

# Histórico do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Perguntas e respostas pré-definidas
faq = {
    "Qual o horário de atendimento?": "Nosso horário de atendimento é de segunda a sexta, das 08:00 às 18:00.",
    "Como faço matrícula?": "Para matrícula, acesse o formulário no nosso site ou vá até a secretaria da escola.",
    "Quais cursos são oferecidos?": "Oferecemos cursos de Ensino Fundamental, Médio, além de cursos extracurriculares de idiomas e tecnologia.",
    "Onde a escola está localizada?": "Estamos localizados na Rua Exemplo, 123, Centro.",
    "Falar com atendente": "Você pode falar diretamente com um atendente pelo WhatsApp clicando no botão abaixo."
}

# Mostrar histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Campo de input
pergunta = st.chat_input("Digite sua pergunta ou escolha uma das sugestões abaixo:")

# Botões de sugestões
for key in faq.keys():
    if st.button(key):
        pergunta = key

# Responder usuário
if pergunta:
    resposta = faq.get(pergunta, "Desculpe, não tenho uma resposta para isso no momento.")

    st.session_state.messages.append({"role": "user", "content": pergunta})
    st.session_state.messages.append({"role": "assistant", "content": resposta})

    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
        st.markdown(resposta)

    # Se for para falar com atendente
    if pergunta == "Falar com atendente":
        whatsapp_url = "https://wa.me/5561982885767"  # Substituir pelo número da escola
        st.markdown(f"[Clique aqui para falar no WhatsApp]({whatsapp_url})")