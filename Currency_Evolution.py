


def run_currency_evolution(language_index):
    import pandas as pd
    import Centred_Title
    import streamlit as st
    import Background_Style
    from datetime import datetime
    import plotly.express as px
    import matplotlib.pyplot as plt
    import seaborn as sns

    Background_Style.run_background_styl()


    if 'currency_changed' not in st.session_state:
        st.session_state.currency_changed = False

    currency_changed = st.session_state.currency_changed

    # Erstelle eine dicke Linie Funktion
    def draw_line(groesse):
        st.markdown(f"<hr style='border: {groesse}px solid black;'>", unsafe_allow_html=True)


    # Erstelle eine dicke Linie Funktion (Sidebar)
    def draw_line_sidebar(width):
        st.sidebar.markdown(f"<hr style='border: {width}px dashed #009999;'>",
                            unsafe_allow_html=True)

    # Erstelle eine dicke Linie Funktion
    def draw_line_curreny(groesse):
        st.markdown(
            f"<hr style='border: {groesse}px solid black; width: 100%; margin-left: auto; margin-right: auto;'>",
            unsafe_allow_html=True
        )

    # Währung Zeichen
    def make_metric(date, value, delta,first_currency,second_currency):


        if delta > 0:
            st.markdown(
                        f"""
                       <div style='border: 1px solid black; box-shadow: 0px 0px 25px 3px black; padding: 10px; background-color: #f8f8f8;'>
                           <h1 style='text-align: center; background-color:#d5d5d5;'>
                               {date}
                               ‎ ‎ ‎ <span style='color:green; background-color:#bdbdbd;'>↑{delta:.3f} %</span>
                           </h1>
                           <h1 style='text-align: center; background-color:#eeeeee;'>
                               <span style='color:#009999;'>{first_currency}‎/‎{second_currency}   ‎  {value:.5f}</span>
                           </h1>
                       </div>
                       """,unsafe_allow_html=True)

        else:


            st.markdown(
                        f"""
                       <div style='border: 1px solid black; box-shadow: 0px 0px 25px 3px black; padding: 10px; background-color: #f8f8f8;'>
                           <h1 style='text-align: center; background-color:#d5d5d5;'>
                               {date}
                               ‎ ‎ ‎ <span style='color:red; background-color:#bdbdbd;'>↓{delta:.3f} %</span>
                           </h1>
                           <h1 style='text-align: center; background-color:#eeeeee;'>
                               <span style='color:#009999;'>{first_currency}‎/‎{second_currency}   ‎  {value:.5f}</span>
                           </h1>
                       </div>
                       """, unsafe_allow_html=True)



    # Währungstrends mit yfinace
    st.cache
    def get_currency_trends_yfinace(first_currency, second_currency, exchange_date_from, exchange_date_to):

        import yfinance as yf
        from datetime import  timedelta


        def get_data(exchange_date_from,exchange_date_to):
            ticker = str(first_currency).upper() + str(second_currency).upper() + '=X'
            exchange_date_to_plus_one = exchange_date_to + timedelta(days=1)
            # Daten mit yfinance abrufen
            data = yf.download(ticker, start=exchange_date_from, end=exchange_date_to_plus_one)
            data = data.reset_index()
            # Lösche die Ticker-Level aus den Daten
            data.columns = data.columns.droplevel(1)
            return data

        # 1. Versuch
        data = get_data(exchange_date_from,exchange_date_to)


        if not data.empty:
            rates = data[['Date','Close']]
            return rates, exchange_date_from, exchange_date_to
        else:
            # 2. Versuch
            data = get_data(exchange_date_from,exchange_date_to)
            if not data.empty:
                rates = data[['Date','Close']]
                return rates, exchange_date_from, exchange_date_to
            else:
                # 3. Versuch
                data = get_data(exchange_date_from,exchange_date_to)
                if not data.empty:
                    rates = data[['Date','Close']]
                    return rates, exchange_date_from, exchange_date_to
                else:
                    # 4. Versuch
                    data = get_data(exchange_date_from,exchange_date_to)
                    if not data.empty:
                        rates = data[['Date','Close']]
                        return rates, exchange_date_from, exchange_date_to
                    else:
                        # 5. Versuch
                        data = get_data(exchange_date_from,exchange_date_to)
                        if not data.empty:
                            rates = data[['Date','Close']]
                            return rates, exchange_date_from, exchange_date_to
                        else:
                            # 6. Versuch
                            data = get_data(exchange_date_from,exchange_date_to)
                            if not data.empty:
                                rates = data[['Date','Close']]
                                return rates, exchange_date_from, exchange_date_to
                            else:
                                # 7. Versuch
                                data = get_data(exchange_date_from,exchange_date_to)
                                if not data.empty:
                                    rates = data[['Date','Close']]
                                    return rates, exchange_date_from,exchange_date_to
                                else:
                                    return 0,None

    currency_codes = [
        'USD', 'EUR', 'AFN', 'ALL', 'AMD', 'AOA', 'ARS', 'AWG', 'AZN', 'BAM',
        'BBD', 'BDT', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN',
        'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE',
        'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'FJD', 'FKP',
        'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL',
        'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK',
        'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD',
        'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD',
        'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MUR', 'MVR', 'MWK', 'MXN',
        'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB',
        'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PRB', 'PYG', 'QAR', 'RON', 'RSD',
        'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL',
        'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND',
        'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VEF',
        'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XOF', 'XPF', 'YER', 'ZAR'
    ]

    first_currency_evolution_col, second_currency_evolution_col = st.sidebar.columns(2)
    with first_currency_evolution_col:
        first_currency_evolution = st.selectbox(label='Erste Währung',
                                              options=currency_codes,
                                              key='first_currency_evolution',
                                              index=0)

    with second_currency_evolution_col:
        second_currency_evolution = st.selectbox(label='Zweite Währung',
                                               options=currency_codes,
                                               key='second_currency_evolution',
                                               index=1)

    exchange_date_from_currency_evolution_col, exchange_date_to_currency_evolution_col = st.sidebar.columns(2)
    today = datetime.today().date()
    from datetime import timedelta

    today_minus_seven_days = today - timedelta(days=7)
    with exchange_date_from_currency_evolution_col:
        exchange_date_from = st.date_input(label='Von:',
                                              value=today_minus_seven_days,
                                              max_value=today_minus_seven_days,
                                              key='exchange_date_from')

    exchange_date_from_plus_seven_days = exchange_date_from + timedelta(days=7)

    with exchange_date_to_currency_evolution_col:
        exchange_date_to = st.date_input(label='Bis',
                                          value=today,
                                          min_value=exchange_date_from_plus_seven_days,
                                          max_value=today,
                                          key='exchange_date_to')

    Centred_Title.run_centred_title('Currency Evolution')

    # CSS für zentrierten Button und Hover-Effekt
    st.markdown("""
                <style>
                /* Zentrierung des Buttons über Display-Flex in Streamlit */
                div.stButton > button {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin: 0 auto; 
                    background-color: #009999; 
                    color: white;
                    padding: 12px 24px;
                    font-size: 25px;
                    border: none;
                    border-radius: 8px;
                    transition: all 0.3s ease;
                }
                div.stButton > button:hover {
                    background-color: #959595; 
                    cursor: pointer;
                    transform: scale(1.50);
                }
                </style>
                """, unsafe_allow_html=True)

    # Button mit der Variable button_name zentriert anzeigen
    button_text = "⇆"

    if st.button(button_text, key="unique_button_key"):
        st.session_state.currency_changed = not currency_changed
        currency_changed = st.session_state.currency_changed

    first_currency_dummy = first_currency_evolution
    second_currency_dummy = second_currency_evolution

    if currency_changed:
        first_currency_evolution = second_currency_dummy
        second_currency_evolution = first_currency_dummy

    try:




        data_selected_date_from_to, data_selected_date_from, data_selected_date_to = get_currency_trends_yfinace(
            first_currency=first_currency_evolution,
            second_currency=second_currency_evolution,
            exchange_date_from=exchange_date_from,
            exchange_date_to=exchange_date_to)

        data_selected_date_from_to= data_selected_date_from_to.rename(columns={'Date':'date',
                                                                                          'Close':'value'})

        data_selected_date_from_to['date'] = data_selected_date_from_to['date'].dt.strftime('%Y-%m-%d')
        data_selected_date_from_to['first currency'] = first_currency_evolution
        data_selected_date_from_to['second currency'] = second_currency_evolution
        data_selected_date_from = data_selected_date_from_to['value'].iloc[0]
        data_selected_date_to = data_selected_date_from_to['value'].iloc[-1]



        delta_from_divide_to = ((data_selected_date_from - data_selected_date_to)/data_selected_date_from)*100
        delta_to_divide_from = ((data_selected_date_to - data_selected_date_from)/data_selected_date_to)*100




        data_selected_date_from_column, data_selected_date_to_column = st.columns(2)
        with data_selected_date_from_column:
            make_metric(exchange_date_from,
                        data_selected_date_from,
                        delta_from_divide_to,
                        first_currency_evolution,
                        second_currency_evolution)
            draw_line_curreny(3)
        with data_selected_date_to_column:
            make_metric(exchange_date_to,
                        data_selected_date_to,
                        delta_to_divide_from,
                        first_currency_evolution,
                        second_currency_evolution)
            draw_line_curreny(3)


        # Interaktives Liniendiagramm mit Plotly und Streamlit
        fig = px.line(data_selected_date_from_to,
                      x='date',
                      y='value')

        # Hintergrund und Layout anpassen
        fig.update_layout(
            plot_bgcolor='#eeeeee',  # Hintergrundfarbe des Plots
            paper_bgcolor='#d5d5d5',  # Hintergrundfarbe der gesamten Figur
            font=dict(color='#009999'),  # Schriftfarbe
            title=dict(
                text=f'Wechselkurse zwischen {exchange_date_from} und {exchange_date_to} ({first_currency_evolution} / {second_currency_evolution})',  # Titeltext
                x=0.5,  # Zentriert den Titel
                xanchor='center',  # Verankert den Titel in der Mitte
                font=dict(size=25)  # Schriftgröße des Titels
            )

        )

        # Achsenfarben anpassen
        fig.update_xaxes(title_font=dict(color='black'), tickfont=dict(color='black'))
        fig.update_yaxes(title_font=dict(color='black'), tickfont=dict(color='black'))

        # Change the line color
        fig.update_traces(line=dict(color='#009999'))

        # Diagramm in Streamlit anzeigen
        st.plotly_chart(fig, use_container_width=True)
    except:
        st.warning('Bitte wählen Sie andere Daten')

    # Eine horizontale drei Pixel Linie hinzufügen
    draw_line(3)

    # Footer importieren
    import Footer as ft
    ft.run_footer(language_index=language_index,
                  doc_path='test_documentation.pdf')
