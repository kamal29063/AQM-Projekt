


def run_currency_analytics(language_index):
    import streamlit as st
    import Currency_Converter
    import Currency_Evolution


    # Erstelle eine dicke Linie Funktion (Sidebar)
    def draw_line_sidebar(width):
        st.sidebar.markdown(f"<hr style='border: {width}px dashed #009999;'>",
                            unsafe_allow_html=True)

    # Erstelle eine dicke Linie Funktion
    def draw_line_centred_sidebar_title(groesse):
        st.sidebar.markdown(f"<hr style='border: {groesse}px dotted black;margin-bottom: 0;'>", unsafe_allow_html=True)
        st.sidebar.markdown(f"<hr style='border: {groesse}px dotted #009999;margin: 0;'>", unsafe_allow_html=True)
        st.sidebar.write('')
        st.sidebar.write('')


    # Logo sidebar
    st.sidebar.image("Images/FinGraph Logo.png",
                     use_column_width=True)

    # Draw Line for the sidebar (3 Pixel)
    draw_line_sidebar(3)

    # Tabs Bar erstellen
    currency_sidebar_tab = st.sidebar.selectbox("Wähle Tab",
                                              ['⌨ Currency Converter', '⇱⇲ Currency Evolution'],
                                              key='currency_sidebar_tab')

    # darw six pixel dashed line
    draw_line_centred_sidebar_title(6)


    if currency_sidebar_tab == '⌨ Currency Converter':
        Currency_Converter.run_currency_converter(language_index)
        st.sidebar.write('')
        st.sidebar.write('')
        st.sidebar.write('')
        st.sidebar.write('')
        # Foto Sidebar Stocks API
        st.sidebar.image("Images/Currency Converter.png",
                         use_column_width=True)

    if currency_sidebar_tab == '⇱⇲ Currency Evolution':
        Currency_Evolution.run_currency_evolution(language_index)
        st.sidebar.write('')
        st.sidebar.write('')
        st.sidebar.write('')
        st.sidebar.write('')
        # Foto Sidebar Stocks API
        st.sidebar.image("Images/Currency Evolution.png",
                         use_column_width=True)
