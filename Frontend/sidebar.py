import streamlit as st

def create_sidebar():
    # CSS pour le sidebar
    st.markdown("""
        <style>
        .sidebar-title {
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            color: #1f77b4;
            margin-bottom: 1.5rem;
        }
        .nav-link {
            display: block;
            padding: 12px 20px;
            margin: 8px 0;
            background-color: #f0f2f6;
            border-radius: 8px;
            text-decoration: none;
            color: #333;
            transition: all 0.3s ease;
            border-left: 4px solid transparent;
        }
        .nav-link:hover {
            background-color: #1f77b4;
            color: white;
            border-left: 4px solid #0d47a1;
            transform: translateX(5px);
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            text-decoration: none;
        }
        .nav-link.active {
            background-color: #1f77b4;
            color: white;
            border-left: 4px solid #0d47a1;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown('<div class="sidebar-title">Navigation Menu</div>', unsafe_allow_html=True)
        
        # Navigation
        if st.button("🏠 Home", use_container_width=True):
           st.switch_page("Home.py")
        if st.button("📊 Discover your mental state", use_container_width=True):
         st.switch_page("pages/classification.py")

        if st.button("📈 Predict your Academic Pressure", use_container_width=True):
            st.switch_page("pages/predict.py")
            
        if st.button("📊✨ Performance des modèles", use_container_width=True):
            st.switch_page("pages/classification.py")
      
      

      
         #st.markdown("---")
        # st.markdown("### ⚙️ Paramètres")
         #st.checkbox("Mode sombre", value=False)
        # st.selectbox("Langue", ["Français", "English", "العربية"])