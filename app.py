import streamlit as st
import cv2
import numpy as np


st.title("Mis Pruebas")
image = cv2.imread("./images/wonka.png", cv2.IMREAD_UNCHANGED)
st.image(image, channels="BGR", width=500)

