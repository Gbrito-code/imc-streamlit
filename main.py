import streamlit as st
import matplotlib.pyplot as plt  # Importa a biblioteca para criar gráficos

# Configuração de estilos com CSS para personalizar o fundo e fonte
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;  /* Fundo claro */
        font-family: Arial, sans-serif;  /* Fonte amigável */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar com informações explicativas
with st.sidebar:
    # Título da barra lateral
    st.title("Calculadora de IMC")
    # Explicação do que é IMC
    st.header("O que é IMC?")
    st.markdown("""
    O **Índice de Massa Corporal (IMC)** é uma medida usada para avaliar se uma pessoa está dentro de uma faixa de peso saudável com base na relação entre peso e altura.
    """)
    # Exibição das faixas de classificação
    st.write("""
    - **Abaixo do peso**: IMC menor que 18.5  
    - **Peso ideal**: IMC entre 18.5 e 24.9  
    - **Sobrepeso**: IMC entre 25 e 29.9  
    - **Obesidade**: IMC entre 30 e 39.9  
    - **Obesidade mórbida**: IMC acima de 40  
    """)

# Título principal da página
st.title("Calculadora de IMC")
st.subheader("Bem-vindo(a)! Descubra se seu peso está saudável.")

# Entradas do usuário
# Entrada para o peso em quilogramas, permitindo apenas valores positivos e com precisão de uma casa decimal
peso = st.number_input(label="Digite o seu peso (em kg):", min_value=0.0, step=0.1, format="%.1f")
# Entrada para a altura em metros, também com valores positivos e precisão de duas casas decimais
altura = st.number_input(label="Digite a sua altura (em metros):", min_value=0.0, step=0.01, format="%.2f")

# Botão para calcular o IMC
if st.button("Calcular"):
    # Verifica se o peso e a altura são maiores que zero para evitar divisões por zero
    if peso > 0 and altura > 0:
        # Calcula o IMC
        imc = peso / (altura ** 2)
        # Define o IMC ideal para comparação
        imc_ideal = 21.7
        # Calcula a diferença do IMC atual em relação ao ideal
        imc_delta = imc - imc_ideal

        # Determina a classificação do IMC
        if imc < 18.5:
            classe = 'Abaixo do peso'
            cor = "blue"  # Cor azul para representar essa classificação
        elif 18.5 <= imc < 25:
            classe = 'Peso ideal'
            cor = "green"  # Cor verde para indicar saúde
        elif 25 <= imc <= 30:
            classe = 'Sobrepeso'
            cor = "orange"  # Cor laranja para alerta
        elif imc <= 40:
            classe = 'Obesidade'
            cor = "red"  # Cor vermelha para risco moderado
        else:
            classe = 'Obesidade mórbida'
            cor = "darkred"  # Vermelho escuro para risco severo

        # Exibe o resultado com cores para destaque
        st.success("Cálculo realizado com sucesso!")
        st.markdown(f"<h2 style='color:{cor};'>Seu IMC: {imc:.2f} ({classe})</h2>", unsafe_allow_html=True)
        st.write(f"Comparação com o IMC ideal (21.7): **{imc_delta:.2f}**")

        # Adiciona um gráfico de barras para mostrar as categorias de IMC
        categorias = ["Abaixo do peso", "Peso ideal", "Sobrepeso", "Obesidade", "Obesidade mórbida"]
        valores = [18.5, 25, 30, 40, 45]  # Valores representando as faixas

        # Criação do gráfico com Matplotlib
        fig, ax = plt.subplots()
        # Barras coloridas para cada faixa
        ax.bar(categorias, valores, color=['blue', 'green', 'orange', 'red', 'darkred'], alpha=0.7)
        # Linha indicando o IMC do usuário
        ax.axhline(y=imc, color='black', linestyle='--', label=f'Seu IMC ({imc:.2f})')
        ax.legend()  # Legenda para a linha
        plt.xticks(rotation=45)  # Rotação dos rótulos das categorias
        plt.title("Classificação do IMC")  # Título do gráfico
        plt.ylabel("Valores de IMC")  # Rótulo do eixo Y

        # Exibe o gráfico na interface do Streamlit
        st.pyplot(fig)

        # Mensagens personalizadas de acordo com a classificação do IMC
        if classe == 'Abaixo do peso':
            st.info("Você está abaixo do peso. Consulte um nutricionista para ajustar sua dieta.")
        elif classe == 'Peso ideal':
            st.success("Parabéns! Você está com um peso saudável. Mantenha sua rotina!")
        elif classe == 'Sobrepeso':
            st.warning("Atenção! Considere consultar um profissional para manter sua saúde.")
        else:
            st.error("Recomenda-se acompanhamento médico para cuidar da sua saúde.")

        # Botão para reiniciar o aplicativo e permitir novo cálculo
        if st.button("Reiniciar"):
            st.experimental_rerun()
    else:
        # Mensagem de erro se os valores de peso ou altura forem inválidos
        st.error("Por favor, insira valores válidos para peso e altura!")
