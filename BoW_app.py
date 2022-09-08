"""
Written by Collin Hoffman

4/7/2022 as part of Dr. Gang Shao's research.

BoW_app.py
"""

import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import BoW_network
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning())

#give app a name
st.title('Top 200 PURR Tags, with Links')

#call function from other file
BoW_network.simple_func()

#open HTML source code, create components
HtmlFile = open("BoW.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 900,width=900)

