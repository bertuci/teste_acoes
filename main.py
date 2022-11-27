
import streamlit as st
import pandas as pd



st.title('Melhores Resultados da Bolsa')


df = pd.read_excel('resultado.xlsx')


df['% entrada']  = df['% entrada'] * 100
df['% entrada'] = df['% entrada'].astype(str)
df['% entrada'] = df['% entrada'].str[:5]
df['% entrada'] = df['% entrada'].astype(str) + '%'



df['RESULTADO']  = df['RESULTADO'] * 100
df['RESULTADO'] = df['RESULTADO'].astype(str)
df['RESULTADO'] = df['RESULTADO'].str[:5]
df['RESULTADO'] = df['RESULTADO'].astype(str) + '%'


df['MEDIA']  = df['MEDIA'] * 100
df['MEDIA'] = df['MEDIA'].astype(str)
df['MEDIA'] = df['MEDIA'].str[:5]
df['MEDIA'] = df['MEDIA'].astype(str) + '%'


df['GAIN %']  = df['GAIN %'] * 100
df['GAIN %'] = df['GAIN %'].astype(str)
df['GAIN %'] = df['GAIN %'].str[:5]
df['GAIN %'] = df['GAIN %'].astype(str) + '%'

df['LOSS %']  = df['LOSS %'] * 100
df['LOSS %'] = df['LOSS %'].astype(str)
df['LOSS %'] = df['LOSS %'].str[:5]
df['LOSS %'] = df['LOSS %'].astype(str) + '%'


df['MAIOR LOSS']  = df['MAIOR LOSS'] * 100
df['MAIOR LOSS'] = df['MAIOR LOSS'].astype(str)
df['MAIOR LOSS'] = df['MAIOR LOSS'].str[:5]
df['MAIOR LOSS'] = df['MAIOR LOSS'].astype(str) + '%'


df['MAIOR GAIN']  = df['MAIOR GAIN'] * 100
df['MAIOR GAIN'] = df['MAIOR GAIN'].astype(str)
df['MAIOR GAIN'] = df['MAIOR GAIN'].str[:5]
df['MAIOR GAIN'] = df['MAIOR GAIN'].astype(str) + '%'

#st.dataframe(df)



with st.sidebar:
    option = st.selectbox(
        'Filtro de Gain',
        ('Maior que 70%', 'Menor que 70%'))





if option == 'Maior que 70%':
    df = df[df['GAIN %'] >= '70%']
    st.dataframe(df)

if  option == 'Menor que 70%':
    df = df[df['GAIN %'] <= '70%']
    st.dataframe(df)







@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='resultado.xlsx',
    mime='text/csv',
)
#if st.checkbox('WordCloud'):
#    st.dataframe(df_teste)





