def run_forecasting(language_index):
    import streamlit as st
    import datetime
    import pandas as pd
    import yfinance as yf
    import Process_Button_Styling
    import App_Documentation
    import Select_Store_Location
    import Centred_Title
    import Background_Style
    Background_Style.run_background_styl()



    # Erstelle eine dicke Linie Funktion
    def draw_line(groesse):
        st.markdown(f"<hr style='border: {groesse}px solid black;'>", unsafe_allow_html=True)

    # Erstelle eine dicke Linie Funktion (Sidebar)
    def draw_line_sidebar(width):
        st.sidebar.markdown(f"<hr style='border: {width}px dashed #009999;'>",
                            unsafe_allow_html=True)






    def forecasting_forecast_data(forecasting_asset_type, selected_ticker, selected_interval, forecasting_tech_indicator_periods_count,interval_count):
        import logging
        logging.getLogger("prophet.plot").disabled = True
        from prophet import Prophet
        import pandas_ta as ta
        from dateutil.relativedelta import relativedelta

        selected_ticker_dummy = selected_ticker
        # Aktien
        if forecasting_asset_type == 'Aktien':
            selected_ticker = selected_ticker
            title = selected_ticker

        # Kryptowährungen
        elif forecasting_asset_type == 'Kryptowährungen':
            selected_ticker = str(selected_ticker).upper() + '-USD'
            title = selected_ticker_dummy + '-USD'

        # Währungen
        elif forecasting_asset_type == 'Währungen':
            selected_ticker = str(selected_ticker).upper() + 'USD=X'
            title = selected_ticker_dummy + ' / USD'

        # Rohstoffe
        elif forecasting_asset_type == 'Rohstoffe':
            selected_ticker = str(selected_ticker).upper() + '=F'
            title = selected_ticker_dummy + ' / USD'

        # Fonds
        elif forecasting_asset_type == 'Fonds':
            selected_ticker = str(selected_ticker).upper()
            title = selected_ticker_dummy + ' / USD'

        today = datetime.datetime.today().date()

        if selected_interval == '1mo':
            start_date = today - relativedelta(years=10)
        elif selected_interval == '1wk':
            start_date = today - relativedelta(years=2)
        elif selected_interval == '1d':
            start_date = today - relativedelta(years=1)
        elif selected_interval == '1h':
            start_date = today - relativedelta(months=1)
        elif selected_interval == '1m':
            start_date = today - relativedelta(days=1)


        end_date = today

        # Lade die Daten des aktuellen Tickers
        data = yf.download(tickers=selected_ticker,
                           interval=selected_interval,
                           start=start_date,
                           end=end_date)

        # Lösche die Ticker-Level aus den Daten
        data.columns = data.columns.droplevel(1)



        #  Index Spalte zurücksetzen
        data = data.reset_index()

        if selected_interval in ['1mo','1wk','1d']:
            # Umbennen der Spalte 'Date' zu 'Datetime'
            data = data.rename(columns={"Date": "Datetime"})


        # Datetime format anpasse
        data["Datetime"] = data["Datetime"].dt.tz_localize(None)

        if selected_interval == '1mo':
            selected_interval_fb_prophet = 'M'
        elif selected_interval == '1wk':
            selected_interval_fb_prophet = 'W'
        elif selected_interval == '1d':
            selected_interval_fb_prophet = 'D'
        elif selected_interval == '1h':
            selected_interval_fb_prophet = 'H'
        elif selected_interval == '1m':
            selected_interval_fb_prophet = 'T'

        # Erstelle ein leeres DataFrame für alle Vorhersageergebnisse
        forecasting_results = pd.DataFrame()

        # Iteriere über die Spalten (außer 'Datetime')
        for column_name in data.columns[1:]:
            # Erstelle das Eingabe-DataFrame für Prophet
            data_forecasting_input = pd.DataFrame({
                'ds': data["Datetime"].values,  # Umbenennung direkt hier
                'y': data[column_name]
            })



            # Erstelle und trainiere das Prophet-Modell
            model = Prophet(weekly_seasonality=True, yearly_seasonality=True)
            model.fit(data_forecasting_input)

            # Vorhersage erstellen
            future = model.make_future_dataframe(periods=interval_count, freq=selected_interval_fb_prophet)


            forecasting_result_dataframe = model.predict(future)
            forecasting_result_dataframe = forecasting_result_dataframe.rename(
                columns={'ds': 'Datetime', 'yhat': column_name})

            # Speichern der Vorhersageergebnisse im DataFrame
            if forecasting_results.empty:  # Wenn das DataFrame noch leer ist, initialisiere es mit der 'Datetime' Spalte
                forecasting_results['Datetime'] = forecasting_result_dataframe['Datetime']

            # Füge die Vorhersage-Spalte zum DataFrame hinzu
            forecasting_results[column_name] = forecasting_result_dataframe[column_name]

        # Das endgültige DataFrame enthält jetzt alle Vorhersagewerte in einer einzigen Struktur
        data = forecasting_results


        # Füge eine neue Spalte mit Tickernamen als erste Spalte im DataFrame
        data.insert(0, 'Ticker', selected_ticker)

        # Füge die 'Is Forecast' Spalte hinzu
        data['Is Forecast'] = data['Datetime'].apply(lambda x: 'Yes' if x > datetime.datetime.now() else 'No')

        data = data[data['Is Forecast'] == 'Yes']







        data["BarColor"] = data[["Open", "Close"]].apply(lambda o: "red" if o.Open > o.Close else "green",
                                                         axis=1)
        data["Date_Text"] = data["Datetime"].astype(str)
        talib_indicators = []

        try:
            tech_indicator_periods_length = 0
            if forecasting_tech_indicator_periods_count == 'Default':

                tech_indicator_periods_length = 14
            else:
                tech_indicator_periods_length = int(forecasting_tech_indicator_periods_count)


            # Berechnung des Simple Moving Average (SMA)
            data["SMA"] = ta.sma(data["Close"], length=tech_indicator_periods_length)

            # Simple Moving Average (SMA)
            data["SMA"] = ta.sma(data["Close"], length=tech_indicator_periods_length)

            # Exponential Moving Average (EMA)
            data["EMA"] = ta.ema(data["Close"], length=tech_indicator_periods_length)

            # Weighted Moving Average (WMA)
            data["WMA"] = ta.wma(data["Close"], length=tech_indicator_periods_length)

            # Relative Strength Index (RSI)
            data["RSI"] = ta.rsi(data["Close"], length=tech_indicator_periods_length)

            # Füge die Werte zur Idikatoren-Liste
            talib_indicators = talib_indicators + ["MA", "EMA", "SMA", "WMA", "RSI"]
        except:
            pass

        try:
            # Moving Average Convergence Divergence (MACD)
            macd = ta.macd(data["Close"], fast=12, slow=26, signal=9)
            data["MACD"] = macd["MACD_12_26_9"]
            data["Signal"] = macd["MACDs_12_26_9"]
            data["Histogram"] = macd["MACDh_12_26_9"]
            talib_indicators = talib_indicators + ["MACD", "Signal", "Histogram"]

        except:
            pass

        try:
            # Bollinger Bands
            tech_indicator_periods_length = 0
            if forecasting_tech_indicator_periods_count == 'Default':
                tech_indicator_periods_length = 20
            else:
                tech_indicator_periods_length = int(forecasting_tech_indicator_periods_count)

            bbands = ta.bbands(data["Close"], length=tech_indicator_periods_length, std=2)
            data["BB_upper"] = bbands["BBU_20_2.0"]
            data["BB_middle"] = bbands["BBM_20_2.0"]
            data["BB_lower"] = bbands["BBL_20_2.0"]
            talib_indicators = talib_indicators + ["BB_upper", "BB_middle", "BB_lower"]
        except:
            pass

        try:
            # Stochastic Oscillator
            stoch = ta.stoch(data["High"], data["Low"], data["Close"], k=14, d=3)
            data["Stoch_K"] = stoch["STOCHk_14_3_3"]
            data["Stoch_D"] = stoch["STOCHd_14_3_3"]
            talib_indicators = talib_indicators + ["Stoch_K", "Stoch_K"]
        except:
            pass

        try:
            # Average Directional Index (ADX)
            tech_indicator_periods_length = 0
            if forecasting_tech_indicator_periods_count == 'Default':
                tech_indicator_periods_length = 14
            else:
                tech_indicator_periods_length = int(forecasting_tech_indicator_periods_count)

            adx = ta.adx(data["High"],
                         data["Low"],
                         data["Close"],
                         length=tech_indicator_periods_length)
            data["ADX"] = adx["ADX_14"]
            talib_indicators = talib_indicators + ["ADX"]
        except:
            pass

        try:
            # Momentum (MOM)
            tech_indicator_periods_length = 0
            if forecasting_tech_indicator_periods_count == 'Default':
                tech_indicator_periods_length = 10
            else:
                tech_indicator_periods_length = int(forecasting_tech_indicator_periods_count)

            data["MOM"] = ta.mom(data["Close"],
                                 length=tech_indicator_periods_length)
            talib_indicators = talib_indicators + ["MOM"]
        except:
            pass

        try:
            # TRIX
            data["TRIX"] = ta.trix(data["Close"], length=15)
            talib_indicators = talib_indicators + ["TRIX"]
        except:
            pass

        try:
            # Commodity Channel Index (CCI)
            tech_indicator_periods_length = 0
            if forecasting_tech_indicator_periods_count == 'Default':
                tech_indicator_periods_length = 20
            else:
                tech_indicator_periods_length = int(forecasting_tech_indicator_periods_count)

            data["CCI"] = ta.cci(data["High"], data["Low"], data["Close"], length=tech_indicator_periods_length)
            talib_indicators = talib_indicators + ["CCI"]
        except:
            pass

        try:
            # Williams %R
            tech_indicator_periods_length = 0
            if forecasting_tech_indicator_periods_count == 'Default':
                tech_indicator_periods_length = 14
            else:
                tech_indicator_periods_length = int(forecasting_tech_indicator_periods_count)

            data["WilliamsR"] = ta.willr(data["High"],
                                         data["Low"],
                                         data["Close"],
                                         length=tech_indicator_periods_length)
            talib_indicators = talib_indicators + ["WilliamsR"]
        except:
            pass

        try:
            # Supertrend
            tech_indicator_periods_length = 0
            if forecasting_tech_indicator_periods_count == 'Default':
                tech_indicator_periods_length = 10
            else:
                tech_indicator_periods_length = int(forecasting_tech_indicator_periods_count)

            supertrend = ta.supertrend(data["High"],
                                       data["Low"],
                                       data["Close"],
                                       length=tech_indicator_periods_length,
                                       multiplier=3)

            data["Supertrend"] = supertrend["SUPERT_10_3.0"]
            talib_indicators = talib_indicators + ["Supertrend"]


        except:
            pass
        return data, talib_indicators, title





    def create_chart(title,df, close_price_line=False, open_price_line=False, low_price_line=False, high_price_line=False, indicators=[], selected_ticker='',indicator_colors=False):
        from bokeh.plotting import figure, column
        ## Candlestick Pattern Logic
        candle = figure(x_axis_type="datetime",
                        outer_height=500,
                        inner_height=500,
                        x_range=(df.Datetime.values[0], df.Datetime.values[-1]),
                        tooltips=[("Datetime", "@Date_Text"),
                                  ("Open", "@Open"),
                                  ("High", "@High"),
                                  ("Low", "@Low"),
                                  ("Close", "@Close")], )

        candle.segment("Datetime", "Low", "Datetime", "High", color="black", line_width=0.5, source=df)
        candle.segment("Datetime", "Open", "Datetime", "Close", line_color="BarColor", line_width=2 if len(df) > 100 else 6,
                       source=df)



        # Setze die Hintergrundfarbe
        candle.background_fill_color = '#eeeeee'  # Hier kannst du die Farbe ändern
        candle.border_fill_color = '#d5d5d5'  # Die Farbe des Rahmens (optional)


        # Diagramm Titel
        candle.title.text = f'{title} (Forecast)'
        candle.title_location = "above"  # Titel über dem Diagramm
        candle.title.align = "center"  # Zentriere den Titel horizontal

        # Achsen Beschriftung
        candle.xaxis.axis_label = "Datetime"
        candle.yaxis.axis_label = f"Price ($)"

        ## Close Price Line
        if close_price_line:
            candle.line("Datetime",
                        "Close",
                        color='#009999',
                        source=df,
                        legend_label='Close')

        ## Open Price Line
        if open_price_line:
            candle.line("Datetime",
                        "Open",
                        color='#FF6F61',
                        source=df,
                        legend_label='Open')

        ## Low Price Line
        if low_price_line:
            candle.line("Datetime",
                        "Low",
                        color='#6B5B95',
                        source=df,
                        legend_label='Low')

        ## High Price Line
        if high_price_line:
            candle.line("Datetime",
                        "High",
                        color='#88B04B',
                        source=df,
                        legend_label='High')

        for indicator in indicators:
            candle.line("Datetime", indicator, color=indicator_colors[indicator], line_width=2, source=df,
                        legend_label=indicator)

        return column(children=[candle], sizing_mode="scale_width")

    # Logo sidebar
    st.sidebar.image("Images/FinGraph Logo.png",
                     use_column_width=True)

    # Draw Line for the sidebar (3 Pixel)
    draw_line_sidebar(3)

    forecasting_asset_type_col, selected_ticker_col = st.sidebar.columns(2)
    with forecasting_asset_type_col:
        forecasting_asset_type_options = ['Aktien', 'Kryptowährungen', 'Währungen','Rohstoffe','Fonds']
        forecasting_asset_type = st.selectbox(label='Asset-Typ wählen:',
                                                       options=forecasting_asset_type_options)

    with selected_ticker_col:
        # Tickers importieren
        import Tickers as tic
        tickers, big_four_tickers = tic.run_tickers(asset_type=forecasting_asset_type)
        # Einfachauswahl für Ticker
        forecasting_selected_ticker = st.selectbox(
            label="Ticker:",
            options=tickers
        )

    selected_interval_col, count_of_periods_col,  = st.sidebar.columns(2)




    with selected_interval_col:
        # Liste der Intervalle für yfinance
        intervals = [

            "1h",  # 1 hour (alias for "60m")
            "1d",  # 1 day
            "1wk",  # 1 week
            "1mo",  # 1 month

        ]

        # Liste umkehren
        intervals.reverse()

        # Dropdown-Liste in Streamlit zur Auswahl des Intervalls
        selected_interval = st.selectbox("Intervall:",
                                     options= intervals,
                                     index=2
                                     )





    with count_of_periods_col:
        count_of_periods= st.number_input(label='Anzahl:',
                                          min_value=25,
                                          max_value=1000,
                                          key='_col')

    forecasting_close_price_line = False
    forecasting_open_price_line = False
    forecasting_low_price_line = False
    forecasting_high_price_line = False
    forecasting_volume_line_chart = False

    forecasting_included_kpis_options = ['Schlusskurs', 'Eröffnungskurs', 'Tiefstkurs', 'Höchstkurs', 'Handelsvolumen']

    forecasting_included_kpis = st.sidebar.multiselect(label="Kennzahlen:",
                                   options=forecasting_included_kpis_options,
                                   key='forecasting_included_kpis')

    if 'Schlusskurs' in forecasting_included_kpis:
        forecasting_close_price_line = True
        # st.write(forecasting_close_price_line)

    if 'Eröffnungskurs' in forecasting_included_kpis:
        forecasting_open_price_line = True
        # st.write(forecasting_open_price_line)

    if 'Tiefstkurs' in forecasting_included_kpis:
        forecasting_low_price_line = True
        # st.write(forecasting_low_price_line)

    if 'Höchstkurs' in forecasting_included_kpis:
        forecasting_high_price_line = True
        # st.write(forecasting_high_price_line)

    if 'Handelsvolumen' in forecasting_included_kpis:
        forecasting_volume_line_chart = True
        # st.write(forecasting_volume_line_chart)


    # Page Title
    Centred_Title.run_centred_title('Forecasting')
    if 'forecasting_tech_indicator_periods_count' not in st.session_state:
        st.session_state.forecasting_tech_indicator_periods_count = 'Default'

    forecasting_tech_indicator_periods_count = st.session_state.forecasting_tech_indicator_periods_count




    forecasting_data, forecasting_talib_indicators, title = forecasting_forecast_data(
        forecasting_asset_type=forecasting_asset_type,
        selected_ticker=forecasting_selected_ticker,
        selected_interval=selected_interval,
        forecasting_tech_indicator_periods_count=forecasting_tech_indicator_periods_count,
        interval_count=count_of_periods
        )

    forecasting_tech_indicators_col,forecasting_tech_indicator_periods_count_col= st.columns([10,1])

    with forecasting_tech_indicators_col:
        # Farbzuordnung für Indikatoren
        forecasting_indicator_colors = {
            "SMA": "#FF5733",  # Bright Orange
            "EMA": "#6A0DAD",  # Deep Purple
            "WMA": "#3498DB",  # Sky Blue
            "RSI": "#F1C40F",  # Vibrant Yellow
            "MOM": "#2C3E50",  # Dark Blue-Gray
            "DEMA": "#E74C3C",  # Bright Red
            "MA": "#16A085",  # Teal Green
            "TEMA": "#1ABC9C",  # Aqua
            "MACD": "#8E44AD",  # Purple
            "Signal": "#2ECC71",  # Green
            "Histogram": "#D35400",  # Orange
            "BB_upper": "#E67E22",  # Pumpkin Orange
            "BB_middle": "#BDC3C7",  # Light Gray
            "BB_lower": "#3498DB",  # Sky Blue
            "Stoch_K": "#9B59B6",  # Amethyst
            "Stoch_D": "#34495E",  # Wet Asphalt
            "ADX": "#F39C12",  # Yellow Orange
            "TRIX": "#C0392B",  # Red
            "CCI": "#2980B9",  # Belize Hole Blue
            "WilliamsR": "#27AE60",  # Emerald Green
            "Supertrend": "#1F618D"  # Dark Blue
        }


        forecasting_tech_indicators = st.multiselect(label="Technische Indikatoren:",
                                    options=forecasting_talib_indicators,
                                    key='forecasting_tech_indicators')


    with forecasting_tech_indicator_periods_count_col:

        forecasting_periods_count_list = ['Default']
        for i in range(2,51):
            forecasting_periods_count_list.append(i)
        forecasting_tech_indicator_periods_count = st.selectbox(label='Anzahl der Perioden:',
                                                               options=forecasting_periods_count_list,
                                                               key='forecasting_tech_indicator_periods_count')



    # Eine horizontale zwei Pixel Linie hinzufügen
    draw_line(2)


    st.bokeh_chart(create_chart(title,forecasting_data, forecasting_close_price_line,forecasting_open_price_line,forecasting_low_price_line,forecasting_high_price_line,  forecasting_tech_indicators, forecasting_selected_ticker,forecasting_indicator_colors), use_container_width=True)

    ## Volume Bars Logic
    if forecasting_volume_line_chart:

        # Eine horizontale zwei Pixel Linie hinzufügen
        draw_line(2)

        import plotly.express as px

        # Interaktives Liniendiagramm mit Plotly und Streamlit
        fig = px.line(forecasting_data,
                      x='Datetime',
                      y='Volume')

        # Hintergrund und Layout anpassen
        fig.update_layout(
            plot_bgcolor='#eeeeee',  # Hintergrundfarbe des Plots
            paper_bgcolor='#d5d5d5',  # Hintergrundfarbe der gesamten Figur
            font=dict(color='#009999'),  # Schriftfarbe
            title=dict(
                text=f'Handelsvolumen für {forecasting_selected_ticker} (Forecast)',
                # Titeltext
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

    # Eine horizontale zwei Pixel Linie hinzufügen
    draw_line(2)

    store_location_path = Select_Store_Location.run_select_store_location(language_index=language_index)

    # Eine horizontale drei Pixel Linie hinzufügen
    draw_line(3)
    # Daten speichern
    process_button_dummy_one, process_button, process_button_dummy_two = st.columns([1.5, 1, 1.5])
    with process_button_dummy_one:
        pass
    with process_button:
        Process_Button_Styling.run_process_button_style()
        if st.button("Daten lokal speichern"):
            if len(store_location_path) > 0:
                basics_columns = ['Datetime', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']
                store_columns = basics_columns + forecasting_tech_indicators
                forecasting_data = forecasting_data[store_columns]
                forecasting_data.insert(0,'Ticker',title)
                forecasting_data.to_excel(rf'{store_location_path}/Stocksdata.xlsx',
                              sheet_name='Stocks Data',
                              index=False)

                st.success('Alles geklappt')
            else:
                st.warning(
                    # "Please complete your details and check them for accuracy"
                    f'Bitte vervollständigen')
    with process_button_dummy_two:
        pass

        # Footer importieren
    import Footer as ft
    ft.run_footer(language_index=language_index,
                  doc_path='test_documentation.pdf')


