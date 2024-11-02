import streamlit as st
from random import choice
from time import sleep

# Título do app
st.title("Pedra.Papel. Tesoura")

# Inicializa contadores de vitórias, derrotas e rodadas no estado da sessão, se ainda não existirem
if 'c' not in st.session_state:
    st.session_state.c = 0  # Contador de vitórias
if 'd' not in st.session_state:
    st.session_state.d = 0  # Contador de derrotas
if 'r' not in st.session_state:
    st.session_state.r = 0  # Contador de rodadas
if st.sidebar.button('Resetar rodadas'):
    st.session_state.c = 0
    st.session_state.d = 0
    st.session_state.r = 0
# Define as opções que o jogador pode escolher
opcoes = ['Pedra', 'Papel', 'Tesoura']
# Cria um seletor para o jogador escolher sua opção
jogador = st.selectbox('Opções', opcoes)

# Exibe a imagem correspondente à escolha do jogador
if jogador == 'Pedra':
    st.image('assets/pedra.png', caption='Pedra', width=150) 
elif jogador == 'Papel':
    st.image('assets/papel.png', caption='Papel', width=150)  # Exibe a imagem de Papel
else:
    st.image('assets/mao.png', caption='Tesoura', width=150)  # Exibe a imagem de Tesoura

# O computador escolhe aleatoriamente uma das opções
computador = choice(opcoes)

# Cria um botão que inicia o jogo
if st.button('Jogar'):
    st.write('Pedra...')  # Mensagem inicial do jogo
    sleep(1)  # Pausa de 1 segundo para aumentar a expectativa
    st.write('Papel...')  # Mensagem intermediária
    sleep(1)  # Pausa
    st.write('Tesoura!!')  # Mensagem final
    st.write('-=-' * 20)  # Separador visual
    st.write(f'O jogador jogou: {jogador}')  # Exibe a escolha do jogador
    st.write(f'O computador jogou: {computador}')  # Exibe a escolha do computador
    st.write('-=-' * 20)  # Outro separador visual
    
    # Verifica quem venceu a partida
    if jogador == computador:
        st.warning('Empate')  # Se as escolhas forem iguais, exibe mensagem de empate
    elif (jogador == 'Pedra' and computador == 'Tesoura') or \
         (jogador == 'Papel' and computador == 'Pedra') or \
         (jogador == 'Tesoura' and computador == 'Papel'):
        st.success('O jogador Venceu!!')  # Mensagem de vitória do jogador
        st.session_state.c += 1  # Incrementa o contador de vitórias do jogador
    else:
        st.error('O computador venceu')  # Mensagem de derrota do jogador
        st.session_state.d += 1  # Incrementa o contador de derrotas do jogador

    st.session_state.r += 1  # Incrementa o contador de rodadas após cada partida

# Exibe o número de rodadas, vitórias e derrotas na barra lateral
st.sidebar.title('Rodadas')  # Título da barra lateral
st.sidebar.warning(f'Rodadas: {st.session_state.r}')  # Exibe o número de rodadas jogadas
st.sidebar.success(f'Vitórias: {st.session_state.c}')  # Exibe o número de vitórias
st.sidebar.error(f'Derrotas: {st.session_state.d}')  # Exibe o número de derrotas

