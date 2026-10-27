import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Imagem como matriz: Bandeira da Itália")

bandeira = np.zeros((12, 18, 3), dtype=np.uint8)
bandeira[:] = (255, 255, 255)          
bandeira[:, :6] = (0, 146, 70)          
bandeira[:, 12:] = (206, 43, 55)       
st.image(ampliar(bandeira))