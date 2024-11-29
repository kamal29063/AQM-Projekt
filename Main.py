import streamlit as st
from streamlit_navigation_bar import st_navbar

import As_is_To_Be_Analysis
import Currency_Analytics
import Forecasting
import Portfolio_Performance_Optimization
import Sentiment_Analysis
import Terms_of_Use
import About_Us
import Market_Trends

translations_main = {
    0: [
        "Please confirm that you accept the terms and conditions.",  # Englisch
        "Bitte bestätigen Sie, dass Sie die Geschäftsbedingungen akzeptieren.",  # Deutsch
        "Si prega di confermare di accettare i termini e le condizioni.",  # Italienisch
        "Veuillez confirmer que vous acceptez les termes et conditions.",  # Französisch
        "Por favor, confirme que acepta los términos y condiciones.",  # Spanisch
        "Por favor, confirme que aceita os termos e condições.",  # Portugiesisch
        "Vänligen bekräfta att du accepterar villkoren.",  # Schwedisch
        "Vennligst bekreft at du godtar vilkårene.",  # Norwegisch
        "Bekræft venligst, at du accepterer betingelserne.",  # Dänisch
        "Proszę potwierdzić, że akceptujesz warunki.",  # Polnisch
        "Пожалуйста, подтвердите, что вы принимаете условия.",  # Russisch
        "Будь ласка, підтвердіть, що ви приймаєте умови."  # Ukrainisch
    ],
    1: [
        "Language",  # Englisch
        "Sprache",  # Deutsch
        "Lingua",  # Italienisch
        "Langue",  # Französisch
        "Idioma",  # Spanisch
        "Idioma",  # Portugiesisch
        "Språk",  # Schwedisch
        "Språk",  # Norwegisch
        "Sprog",  # Dänisch
        "Język",  # Polnisch
        "Язык",  # Russisch
        "Мова"  # Ukrainisch
    ],
    2: [
        "Terms of Use",  # Englisch
        "Nutzungsbedingungen",  # Deutsch
        "Termini di utilizzo",  # Italienisch
        "Conditions d'utilisation",  # Französisch
        "Términos de uso",  # Spanisch
        "Termos de uso",  # Portugiesisch
        "Användarvillkor",  # Schwedisch
        "Bruksvilkår",  # Norwegisch
        "Brugsvilkår",  # Dänisch
        "Warunki użytkowania",  # Polnisch
        "Условия использования",  # Russisch
        "Умови використання"  # Ukrainisch
    ],
    3: [
        "About us",  # Englisch
        "Über uns",  # Deutsch
        "Chi siamo",  # Italienisch
        "À propos de nous",  # Französisch
        "Sobre nosotros",  # Spanisch
        "Sobre nós",  # Portugiesisch
        "Om oss",  # Schwedisch
        "Om oss",  # Norwegisch
        "Om os",  # Dänisch
        "O nas",  # Polnisch
        "О нас",  # Russisch
        "Про нас"  # Ukrainisch
    ],

    4: [
        "Market Trends",  # Englisch
        "Markttrends",  # Deutsch
        "Tendenze di mercato",  # Italienisch
        "Tendances du marché",  # Französisch
        "Tendencias del mercado",  # Spanisch
        "Tendências de mercado",  # Portugiesisch
        "Marknadstrender",  # Schwedisch
        "Markedstrender",  # Norwegisch
        "Markedstendenser",  # Dänisch
        "Trendy rynkowe",  # Polnisch
        "Рыночные тенденции",  # Russisch
        "Ринкові тенденції"  # Ukrainisch
    ],

    5: [
        "Portfolio Optimization",  # Englisch
        "Portfolio-Optimierung",  # Deutsch
        "Ottimizzazione del portafoglio",  # Italienisch
        "Optimisation de portefeuille",  # Französisch
        "Optimización de cartera",  # Spanisch
        "Otimização de portfólio",  # Portugiesisch
        "Portföljoptimering",  # Schwedisch
        "Porteføljeoptimalisering",  # Norwegisch
        "Porteføljeoptimering",  # Dänisch
        "Optymalizacja portfela",  # Polnisch
        "Оптимизация портфеля",  # Russisch
        "Оптимізація портфеля"  # Ukrainisch
    ],

    6: [
        "Forecasting",  # Englisch
        "Prognose",  # Deutsch
        "Previsione",  # Italienisch
        "Prévision",  # Französisch
        "Pronóstico",  # Spanisch
        "Previsão",  # Portugiesisch
        "Prognos",  # Schwedisch
        "Prognose",  # Norwegisch
        "Prognose",  # Dänisch
        "Prognoza",  # Polnisch
        "Прогнозирование",  # Russisch
        "Прогнозування"  # Ukrainisch
    ],
    7: [
        "As-Is To-Be Analysis",  # Englisch
        "Ist-Zustand/Soll-Zustand-Analyse",  # Deutsch
        "Analisi dello stato attuale e futuro",  # Italienisch
        "Analyse de l'état actuel et futur",  # Französisch
        "Análisis del estado actual y futuro",  # Spanisch
        "Análise do estado atual e futuro",  # Portugiesisch
        "Analys av nuläge och framtid",  # Schwedisch
        "Analyse av nåværende og fremtidig tilstand",  # Norwegisch
        "Analyse af nuværende og fremtidig tilstand",  # Dänisch
        "Analiza stanu obecnego i przyszłego",  # Polnisch
        "Анализ текущего и целевого состояния",  # Russisch
        "Аналіз поточного та майбутнього стану"  # Ukrainisch
    ],
    8: [
        "Sentiment Analysis",  # Englisch
        "Stimmungsanalyse",  # Deutsch
        "Analisi del sentiment",  # Italienisch
        "Analyse de sentiment",  # Französisch
        "Análisis de sentimiento",  # Spanisch
        "Análise de sentimento",  # Portugiesisch
        "Sentimentanalys",  # Schwedisch
        "Sentimentanalyse",  # Norwegisch
        "Sentimentanalyse",  # Dänisch
        "Analiza nastrojów",  # Polnisch
        "Анализ настроений",  # Russisch
        "Аналіз настроїв"  # Ukrainisch
    ],

    9: [
        "Currency Analytics",  # Englisch
        "Währungsanalyse",  # Deutsch
        "Analisi delle valute",  # Italienisch
        "Analyse de devises",  # Französisch
        "Análisis de divisas",  # Spanisch
        "Análise de moedas",  # Portugiesisch
        "Valutaanalys",  # Schwedisch
        "Valutaanalyse",  # Norwegisch
        "Valutaanalyse",  # Dänisch
        "Analiza walut",  # Polnisch
        "Аналитика валют",  # Russisch
        "Аналіз валют"  # Ukrainisch
    ]
}

# Mache die Seite so breit wie möglich
st.set_page_config(page_title="FinGraph", layout="wide")

st.markdown(
    """
    <style>
    /*Side bar*/
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 100%;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 350px;
        margin-left: -400px;
    }

    """,
    unsafe_allow_html=True,
)

if 'language_index' not in st.session_state:
    st.session_state.language_index = 0

language_index = st.session_state.language_index

if 'language_value' not in st.session_state:
    st.session_state.language_value = 'English'

language_value = st.session_state.language_value

if 'top_nav_value' not in st.session_state:
    st.session_state.top_nav_value = translations_main.get(2)[language_index]

top_nav_value = st.session_state.top_nav_value

# Mach die Frabge von allen Text schwarz
# Define the CSS style for text color
st.markdown("""
    <style>
    /* Change text color of all elements */
    * {




    }
    </style>
    """, unsafe_allow_html=True)

# Side bar link Styling
st.markdown("""
    <style>
    .st-emotion-cache-6qob1r {
    background-color: #f3f5e9 !important;
    }   
    </style>
    """, unsafe_allow_html=True)

styles = {
    "nav": {
        "background-color": "#f3f5e9",
        "height": "3.25rem",

    },
    "div": {
        "max-width": "85.25rem",
        "font-size": "20px",
        "font-size": "20px",
        "padding": "1rem",

    },
    "span": {
        "color": "var(--text-color)",
        "border-radius": "0.3rem",
        "padding": "1rem",

    },
    "active": {
        "background-color": "#f7e48f",
        "padding": "1rem"
    },
    "hover": {
        "background-color": "#D3D3D3",
    },
}

options = {
    "show_menu": False,
    "show_sidebar": False,
}

pages = [
    f'{translations_main.get(2)[language_index]}',
    f'{translations_main.get(3)[language_index]}',
    f'{translations_main.get(4)[language_index]}',
    f'{translations_main.get(5)[language_index]}',
    f'{translations_main.get(6)[language_index]}',
    f'{translations_main.get(7)[language_index]}',
    f'{translations_main.get(8)[language_index]}',
    f'{translations_main.get(9)[language_index]}',
]


# navigation_bar_top


# Suche den Index des ausgewählten Begriffs in den Übersetzungen
def return_selected_page_translated(selected_term, target_language_index):
    for key, value in translations_main.items():
        if selected_term in value:
            return value[target_language_index]


selected_page_transalted = return_selected_page_translated(top_nav_value, language_index)

navigation_bar_top = st_navbar(pages=pages,
                               styles=styles,
                               options=options,
                               selected=selected_page_transalted)

############

# berechne die Index der ausgewählten Sprache
language_dict = {
    'English': 0,
    'Deutsch': 1,
    'Italiano': 2,
    'Français': 3,
    'Español': 4,
    'Português': 5,
    'Svenska': 6,
    'Norsk': 7,
    'Dansk': 8,
    'Polski': 9,
    'Русский': 10,
    'українська': 11

}

# Deine Styles hier
options = list(language_dict.keys())

# Navigationsleiste erstellen
logo_column, text_language_column, drop_down_language_column = st.columns([12.5, 1, 1.4])
with logo_column:
    # Logo
    hover_style = """
        <style>
        .logo {
            transition: opacity 0.8s ease;
            animation: umdrehen 3s infinite linear;
        }
        @keyframes umdrehen {
                0% {
        transform: scale(1, 1);
      }
      50% {
        transform: scale(1.6, 1.6);
      }
      100% {
        transform: scale(1, 1);
      }
        }

        </style>
    """

    # Apply the custom CSS
    st.markdown(hover_style, unsafe_allow_html=True)

    st.markdown(
        '<div style="text-align: left;"><img src="https://i.postimg.cc/XqV6vZdP/tigers.png" class="logo" width="100"></div>',
        unsafe_allow_html=True
    )

with text_language_column:
    st.write('')
    st.write('')
    st.write(f'**{translations_main.get(1)[language_index]}:** ')

with drop_down_language_column:
    selected_language = st.selectbox('',
                                     options=options)

# Session State überprüfen und neu laden
if 'language_index' not in st.session_state:
    st.session_state.language_index = language_dict.get(selected_language)

if st.session_state.language_index != language_dict.get(selected_language):
    st.session_state.language_index = language_dict.get(selected_language)
    st.experimental_rerun()

# Session State überprüfen und neu laden
if 'language_value' not in st.session_state:
    st.session_state.language_value = selected_language

if st.session_state.language_value != selected_language:
    st.session_state.language_value = selected_language
    st.experimental_rerun()

# Session State überprüfen und neu laden
if 'top_nav_value' not in st.session_state:
    st.session_state.top_nav_value = str(navigation_bar_top)

if st.session_state.top_nav_value != str(navigation_bar_top):
    st.session_state.top_nav_value = str(navigation_bar_top)
    st.experimental_rerun()

############


# Wenn es nicht akzeptiert wurde, zeige die Warnung
# Bei Terms of Use zeige es nicht
# get the Agreemen-Value from Terms of Use checkbox
if 'agree' not in st.session_state:
    agree = False
else:
    agree = st.session_state.agree

if not agree and str(navigation_bar_top) != f'{translations_main.get(2)[language_index]}':
    for i in range(50):
        st.write('')

    st.warning(f'{translations_main.get(0)[language_index]}')

else:
    # "Terms of Use"
    if navigation_bar_top == f'{translations_main.get(2)[language_index]}':
        Terms_of_Use.run_terms_of_use(language_index)

    # "About Us"
    if navigation_bar_top == f'{translations_main.get(3)[language_index]}':
        About_Us.run_about_us(language_index)

    # "Markt Trends"
    if navigation_bar_top == f'{translations_main.get(4)[language_index]}':
        Market_Trends.run_market_trends(language_index)

    # "Portfolio Performance Optimization"
    if navigation_bar_top == f'{translations_main.get(5)[language_index]}':
        Portfolio_Performance_Optimization.run_Portfolio_Performance_Optimization(language_index)

    # "Forecasting"
    if navigation_bar_top == f'{translations_main.get(6)[language_index]}':
        Forecasting.run_forecasting(language_index)

    # "As_is_To_Be_Analysis"
    if navigation_bar_top == f'{translations_main.get(7)[language_index]}':
        As_is_To_Be_Analysis.run_As_is_To_Be_Analysis(language_index)

    # "Sentiment Analysis"
    if navigation_bar_top == f'{translations_main.get(8)[language_index]}':
        Sentiment_Analysis.run_Sentiment_Analysis(language_index)

    # "Currency Analytics"
    if navigation_bar_top == f'{translations_main.get(9)[language_index]}':
        Currency_Analytics.run_currency_analytics(language_index)







