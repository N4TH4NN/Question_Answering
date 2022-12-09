import streamlit as st

class ArchitecturePage:
    
    def scope(self):
        st.set_page_config(
            page_title="Ex-stream-ly Cool App",
            initial_sidebar_state="collapsed",
            page_icon="🧊",
            layout="wide",
            menu_items={
                'Get Help': 'https://www.extremelycoolapp.com/help',
                'Report a bug': "https://www.extremelycoolapp.com/bug",
                'About': "# This is a header. This is an *extremely* cool app!"
            }
            )   

