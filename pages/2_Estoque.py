import streamlit as st
import pandas as pd

st.sidebar.markdown("Desenvolvido por [Éaco Rocha](https://github.com/Rxz1Eaco)")
# Função para mapear o status para emojis e cores
def status_to_emoji(status):
    if status == 'Boa':
        return '✅'
    elif status == 'Regular':
        return '🟨'
    elif status == 'Ruim':
        return '❌'
    else:
        return '⬜'

# Dados de exemplo para o Kanban 5S
data = {
    'Conceito': ['Utilização', 'Organização', 'Limpeza', 'Asseio', 'Disciplina'],
    'Segunda': ['Boa', 'Boa', 'Boa', 'Boa', 'Boa'],
    'Terça': ['Ruim', 'Ruim', 'Boa', 'Ruim', 'Boa'],
    'Quarta': ['Boa', 'Boa', 'Boa', 'Boa', 'Boa'],
    'Quinta': ['Regular', 'Boa', 'Boa', 'Regular', 'Boa'],
    'Sexta': ['Regular', 'Ruim', 'Ruim', 'Boa', 'Boa'],
    'Sábado': ['-', '-', '-', '-', '-']
}

df = pd.DataFrame(data)

st.title('KANBAN DO 5S 📋')
st.subheader('Setor - Estoque')
st.write('Como está nossa área:')

for conceito in df['Conceito']:
    st.write(f"### {conceito}")
    cols = st.columns(len(df.columns) - 1)
    for i, col in enumerate(df.columns[1:]):
        with cols[i]:
            key = f'{conceito}_{col}'  # Gera uma chave única para cada selectbox
            status = st.selectbox(f'{col}', ['Boa', 'Regular', 'Ruim', '-'], index=['Boa', 'Regular', 'Ruim', '-'].index(df.loc[df['Conceito'] == conceito, col].values[0]), key=key)
            df.loc[df['Conceito'] == conceito, col] = status_to_emoji(status)

st.table(df)

# Salvar o DataFrame em um arquivo Excel
file_name = 'kanban_5s_Estoque.xlsx'
df.to_excel(file_name, index=False)

# Instrução para mover manualmente o arquivo para a pasta desejada
st.markdown("""
Para mover o arquivo baixado para a pasta 'Database':
1. Clique no botão 'Baixar tabela em Excel'.
2. Após o download, localize o arquivo 'kanban_5s_Estoque.xlsx' em sua pasta de downloads.
3. Mova o arquivo para a pasta 'Database' manualmente.
""")

# Criar um botão de download para o arquivo Excel
with open(file_name, 'rb') as f:
    st.download_button(
        label='Baixar tabela em Excel',
        data=f,
        file_name=file_name,
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
