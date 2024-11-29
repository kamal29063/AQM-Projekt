def run_Portfolio_Performance_Optimization(language_index):
    import streamlit as st
    import yfinance as yf
    import pandas as pd
    import numpy as np
    import scipy.optimize as sco
    import datetime
    from scipy.optimize import minimize
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

    def make_metric(ticker, weight, tickers_count, market_caps):
        distributed_weight = 1 / tickers_count

        market_cap = float(market_caps[market_caps['Ticker'] == ticker]['Market Cap'])
        # st.write(market_cap)

        # Zahl formatieren

        if market_cap >= (1000_000_000_000):  # Billionen
            market_cap = f"{market_cap / 1000_000_000_000:.2f} Bn"

        elif market_cap >= 1_000_000_000:  # Milliarden
            market_cap = f"{market_cap / 1_000_000_000:.2f} Md"


        elif market_cap >= 1_000_000:  # Millionen
            market_cap = f"{market_cap / 1_000_000:.2f} Mio"

        elif market_cap >= 1_000:  # Tausend
            market_cap = f"{market_cap / 1_000:.2f} Tsd"


        else:  # Weniger als Tausend
            market_cap = f"{market_cap:.2f}"

        # st.write(market_cap)

        weight = weight * 100
        distributed_weight = distributed_weight * 100

        if weight > distributed_weight:

            st.markdown(
                f"""
                <div style='border: 1px solid black; box-shadow: 0px 0px 25px 3px black; padding: 10px; background-color: #f8f8f8; height: 100%; display: flex; flex-direction: column; justify-content: center;'>
                     <h1 style='text-align: center; background-color:#d5d5d5; margin: 0; padding: 5px; height: 50%;'>{ticker}</h1>
                    <h1 style='text-align: center; background-color:#eeeeee; margin: 0; padding: 5px; height: 50%;'>
                        <span style='color:green; '>
                        <span style='color:green; '>↑ ‎ </span>
                        {weight:.1f} %
                        </span>
                    </h1>
                    <h1 style='text-align: center; background-color:#d5d5d5; margin: 0; padding: 5px; height: 50%;'>{market_cap}</h1>
                </div>
                """, unsafe_allow_html=True
            )
        elif weight == distributed_weight:
            st.markdown(
                f"""
                            <div style='border: 1px solid black; box-shadow: 0px 0px 25px 3px black; padding: 10px; background-color: #f8f8f8; height: 100%; display: flex; flex-direction: column; justify-content: center;'>
                                 <h1 style='text-align: center; background-color:#d5d5d5; margin: 0; padding: 5px; height: 50%;'>{ticker}</h1>
                                <h1 style='text-align: center; background-color:#eeeeee; margin: 0; padding: 5px; height: 50%;'>
                                    <span style='color:#FFDF00; '>
                                    <span style='color:#FFDF00; '>↔ ‎ </span>
                                    {weight:.1f} %
                                    </span>
                                </h1>
                                <h1 style='text-align: center; background-color:#d5d5d5; margin: 0; padding: 5px; height: 50%;'>{market_cap}</h1>
                            </div>
                            """, unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style='border: 1px solid black; box-shadow: 0px 0px 25px 3px black; padding: 10px; background-color: #f8f8f8; height: 100%; display: flex; flex-direction: column; justify-content: center;'>
                     <h1 style='text-align: center; background-color:#d5d5d5; margin: 0; padding: 5px; height: 50%;'>{ticker}</h1>
                    <h1 style='text-align: center; background-color:#eeeeee; margin: 0; padding: 5px; height: 50%;'>
                        <span style='color:red; '>
                        <span style='color:red; '>↓ ‎ </span>
                        {weight:.1f} %
                        </span>
                    </h1>
                    <h1 style='text-align: center; background-color:#d5d5d5; margin: 0; padding: 5px; height: 50%;'>{market_cap}</h1>
                </div>
                """, unsafe_allow_html=True
            )
        st.write('')
        st.write('')

    def calculate_performance_optimization(data, selected_optimization_method, market_caps=None):

        try:
            if selected_optimization_method == 'Mean-Variance Optimization':
                method_name, weights_df = mean_variance_optimization(data)

            if selected_optimization_method == 'Minimum Variance Portfolio':
                method_name, weights_df = minimum_variance_portfolio(data)

            if selected_optimization_method == 'Maximum Sharpe Ratio Portfolio':
                method_name, weights_df = maximum_sharpe_ratio(data)

            if selected_optimization_method == 'Equal Weight Portfolio':
                method_name, weights_df = equal_weight_portfolio(data)

            if selected_optimization_method == 'Risk Parity Portfolio':
                method_name, weights_df = risk_parity_portfolio(data)

            if selected_optimization_method == 'Inverse Variance Portfolio':
                method_name, weights_df = inverse_variance_portfolio(data)

            if selected_optimization_method == 'Maximum Diversification Portfolio':
                method_name, weights_df = maximum_diversification_portfolio(data)

            if selected_optimization_method == 'Maximum Decorrelation Portfolio':
                method_name, weights_df = maximum_decorrelation_portfolio(data)

            if selected_optimization_method == 'Black-Litterman Model Portfolio':
                method_name, weights_df = black_litterman_portfolio(data, market_caps)

            if selected_optimization_method == 'Hierarchical Risk Parity Portfolio':
                method_name, weights_df = hierarchical_risk_parity_portfolio(data)


        except Exception as e:
            method_name, weights_df = '', pd.DataFrame(columns=['Ticker', 'Weight'])

        return method_name, weights_df

    def create_pie_chart(data):
        import plotly.express as px

        # Erstellen des Kreisdiagramms mit Plotly
        fig = px.pie(data, values='Weight', names='Ticker',
                     title='Verteilung der Ticker-Gewichte',
                     color_discrete_sequence=px.colors.sequential.RdBu,
                     hole=0.3)  # Optional für einen Donut-Style

        # Layout des Diagramms anpassen (Titel zentrieren)
        fig.update_layout(
            height=600,  # Höhe des Diagramms
            title={
                'text': 'Verteilung der Ticker-Gewichte',
                'x': 0.5,  # Zentrieren des Titels (x=0.5 bedeutet mittig)
                'xanchor': 'center',
                'yanchor': 'top'
            },
            title_font_size=24,  # Titelgröße
            plot_bgcolor='#eeeeee',  # Hintergrundfarbe des Plots
            paper_bgcolor='#d5d5d5',  # Hintergrundfarbe der gesamten Figur
            font=dict(color='#009999'),
            margin=dict(l=50, r=50, t=100, b=50)  # Ränder anpassen
        )

        # Darstellung des Diagramms mit Streamlit
        st.plotly_chart(fig, use_container_width=True)

    def create_line_chart(data, portfolio_performacne_optimization_asset_type):
        import plotly.express as px
        import plotly.graph_objects as go
        import pandas as pd
        import streamlit as st

        data_selected_date_from_to = pd.DataFrame(data)

        # Layout und Grunddiagramm erstellen
        fig = go.Figure()

        # Schleife über alle Spalten außer 'date'
        for col in data_selected_date_from_to.columns:
            if col != 'Date':
                fig.add_trace(
                    go.Scatter(
                        x=data_selected_date_from_to['Date'],
                        y=data_selected_date_from_to[col],
                        mode='lines',
                        name=col
                    )
                )

        # Layout anpassen
        fig.update_layout(
            plot_bgcolor='#eeeeee',  # Hintergrundfarbe des Plots
            paper_bgcolor='#d5d5d5',  # Hintergrundfarbe der gesamten Figur
            font=dict(color='#009999'),  # Schriftfarbe
            title=dict(
                text=f'{portfolio_performacne_optimization_asset_type}-Kurse',  # Titeltext
                x=0.5,  # Zentriert den Titel
                xanchor='center',  # Verankert den Titel in der Mitte
                font=dict(size=25)  # Schriftgröße des Titels
            )
        )

        # Achsenfarben anpassen
        fig.update_xaxes(title_font=dict(color='black'), tickfont=dict(color='black'))
        fig.update_yaxes(title_font=dict(color='black'), tickfont=dict(color='black'))

        # Diagramm in Streamlit anzeigen
        st.plotly_chart(fig, use_container_width=True)

    # Daten abrufen
    st.cache

    def portfolio_performacne_fetch_data(tickers, start_date, end_date, portfolio_performacne_optimization_asset_type):
        try:
            selected_ticker_dummy = tickers
            selected_tickers = []
            # Aktien
            if portfolio_performacne_optimization_asset_type == 'Aktien':
                for ticker in tickers:
                    selected_tickers.append(ticker)


            # Kryptowährungen
            elif portfolio_performacne_optimization_asset_type == 'Kryptowährungen':
                for ticker in tickers:
                    selected_tickers.append(str(ticker).upper() + '-USD')

            # Währungen
            elif portfolio_performacne_optimization_asset_type == 'Währungen':
                for ticker in tickers:
                    selected_tickers.append(str(ticker).upper() + 'USD=X')

            # Rohstoffe
            elif portfolio_performacne_optimization_asset_type == 'Rohstoffe':
                for ticker in tickers:
                    selected_tickers.append(str(ticker).upper() + '=F')

            # Fonds
            elif portfolio_performacne_optimization_asset_type == 'Fonds':
                for ticker in tickers:
                    selected_tickers.append(str(ticker).upper())

            data = yf.download(selected_tickers,
                               start=start_date,
                               end=end_date,
                               interval='1d')['Adj Close']

            return data
        except:
            st.warning('Bitte andere Daten wählen')
            data = pd.DataFrame({'Date': [None],
                                 'None1': [None],
                                 'None2': [None]})

            return data

    # Marktkapitalisierung für Aktien
    def get_market_caps_stocks(tickers):
        market_caps = {}
        for ticker in tickers:
            stock = yf.Ticker(ticker)
            # Holen Sie die Marktkapitalisierung direkt ab und konvertieren Sie sie in einen float
            market_cap = stock.info.get("marketCap")

            # Überprüfen, ob die Marktkapitalisierung vorhanden ist und in eine Zahl konvertierbar ist
            if market_cap is not None:
                try:
                    market_caps[ticker] = float(market_cap)  # In float konvertieren
                except ValueError:
                    pass

        # Rückgabe als DataFrame für bessere Übersicht
        market_caps_df = pd.DataFrame(list(market_caps.items()), columns=["Ticker", "Market Cap"])
        return market_caps_df

    # Marktkapitalisierung für Fonds
    def get_market_caps_funds(tickers):
        """
        Holt die Marktkapitalisierungen für Fonds.
        """
        import yfinance as yf
        import pandas as pd

        market_caps = {}
        for ticker in tickers:
            fund = yf.Ticker(ticker)
            # Marktkapitalisierung aus den Informationen abrufen
            market_cap = fund.info.get("totalAssets")  # Für Fonds oft totalAssets
            if market_cap is not None:
                try:
                    market_caps[ticker] = float(market_cap)
                except ValueError:
                    pass

        # Rückgabe als DataFrame
        market_caps_df = pd.DataFrame(list(market_caps.items()), columns=["Ticker", "Market Cap"])
        return market_caps_df

    # Marktkapitalisierung für Währungen
    def get_exchange_rates(tickers):
        import yfinance as yf
        import pandas as pd
        exchange_rates = {}
        for ticker in tickers:
            currency_pair = yf.Ticker(ticker + 'USD=X')
            # Wechselkurs abrufen
            exchange_rate = currency_pair.history(period="1d").get("Close")  # Schlusskurs als Wechselkurs
            if not exchange_rate.empty:
                exchange_rates[ticker] = float(exchange_rate.iloc[-1])  # Neuesten Wert holen

        # Rückgabe als DataFrame
        # WICHTIG
        # Market Cap bezieht sich auf Exchange Rate
        exchange_rates_df = pd.DataFrame(list(exchange_rates.items()), columns=["Ticker", "Market Cap"])
        return exchange_rates_df

    # Marktkapitalisierung für Krypto-Währungen
    def get_market_caps_crypto(tickers):
        import yfinance as yf
        import pandas as pd
        market_caps = {}
        for ticker in tickers:
            crypto = yf.Ticker(ticker + '-USD')
            # Marktkapitalisierung für Kryptowährungen abrufen
            market_cap = crypto.info.get("marketCap")
            if market_cap is not None:
                try:
                    market_caps[ticker] = float(market_cap)
                except ValueError:
                    pass

        # Rückgabe als DataFrame
        market_caps_df = pd.DataFrame(list(market_caps.items()), columns=["Ticker", "Market Cap"])
        return market_caps_df

    # Marktkapitalisierung für Rohstoffe
    def get_commodity_prices(tickers):
        import yfinance as yf
        import pandas as pd

        commodity_prices = {}
        for ticker in tickers:
            commodity = yf.Ticker(ticker + '=F')

            price = commodity.history(period="1d").get("Close")
            if not price.empty:
                commodity_prices[ticker] = float(price.iloc[-1])  # Neuesten Schlusskurs holen

        # Rückgabe als DataFrame
        # Market Cap bezieht sich auf Price
        commodity_prices_df = pd.DataFrame(list(commodity_prices.items()), columns=["Ticker", "Market Cap"])
        return commodity_prices_df

    # Mean-Variance Optimization
    def mean_variance_optimization(df):
        returns = df.iloc[:, 1:].pct_change().dropna()
        cov_matrix = returns.cov()
        avg_returns = returns.mean()
        num_assets = len(avg_returns)

        def portfolio_volatility(weights):
            return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

        constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
        bounds = [(0, 1) for _ in range(num_assets)]
        initial_weights = np.array([1 / num_assets] * num_assets)

        result = minimize(portfolio_volatility, initial_weights, bounds=bounds, constraints=constraints)
        weights = result.x
        weight_df = pd.DataFrame({'Ticker': df.columns[1:], 'Weight': weights})

        return "Mean-Variance Optimization", weight_df

    # Minimum Variance Portfolio
    def minimum_variance_portfolio(df):
        returns = df.iloc[:, 1:].pct_change().dropna()
        cov_matrix = returns.cov()
        num_assets = len(cov_matrix)

        def portfolio_volatility(weights):
            return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

        constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
        bounds = [(0, 1) for _ in range(num_assets)]
        initial_weights = np.array([1 / num_assets] * num_assets)

        result = minimize(portfolio_volatility, initial_weights, bounds=bounds, constraints=constraints)
        weights = result.x
        weight_df = pd.DataFrame({'Ticker': df.columns[1:], 'Weight': weights})

        return "Minimum Variance Portfolio", weight_df

    # Maximum Sharpe Ratio Portfolio
    def maximum_sharpe_ratio(df, risk_free_rate=0.01):
        # Berechnung der täglichen Renditen
        returns = df.iloc[:, 1:].pct_change().dropna()
        cov_matrix = returns.cov()
        avg_returns = returns.mean()
        num_assets = len(avg_returns)

        # Zielfunktion: Negative Sharpe Ratio
        def negative_sharpe_ratio(weights):
            portfolio_return = np.dot(weights, avg_returns)
            portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            return -(portfolio_return - risk_free_rate) / portfolio_volatility

        # Constraints: Summe der Gewichte = 1
        constraints = [{'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}]

        # Zusatz: Mindestgewicht für Diversifikation
        min_weight = 0  # Mindestens 5% Gewicht pro Asset
        max_weight = 1  # Maximal 50% Gewicht pro Asset
        bounds = [(min_weight, max_weight) for _ in range(num_assets)]

        # Startwerte: Gleichgewichtetes Portfolio
        initial_weights = np.array([1 / num_assets] * num_assets)

        # Optimierung
        result = minimize(
            negative_sharpe_ratio,
            initial_weights,
            bounds=bounds,
            constraints=constraints
        )

        # Überprüfung, ob die Optimierung erfolgreich war
        if not result.success:
            raise ValueError("Die Optimierung ist fehlgeschlagen: " + result.message)

        # Ergebnis: Gewichte der Assets
        weights = result.x

        # Ausgabe als DataFrame
        weight_df = pd.DataFrame({'Ticker': df.columns[1:], 'Weight': weights})

        return "Maximum Sharpe Ratio Portfolio", weight_df

    # Equal Weight Portfolio
    def equal_weight_portfolio(df):
        num_assets = len(df.columns) - 1
        weights = np.full(num_assets, 1 / num_assets)
        weight_df = pd.DataFrame({'Ticker': df.columns[1:], 'Weight': weights})

        return "Equal Weight Portfolio", weight_df

    # Risk Parity Portfolio
    def risk_parity_portfolio(df):
        returns = df.iloc[:, 1:].pct_change().dropna()
        cov_matrix = returns.cov()
        inv_volatility = 1 / np.sqrt(np.diag(cov_matrix))
        weights = inv_volatility / np.sum(inv_volatility)
        weight_df = pd.DataFrame({'Ticker': df.columns[1:], 'Weight': weights})

        return "Risk Parity Portfolio", weight_df

    # Inverse Variance Portfolio
    def inverse_variance_portfolio(df):
        returns = df.iloc[:, 1:].pct_change().dropna()
        variances = returns.var()
        weights = 1 / variances
        weights /= weights.sum()
        weight_df = pd.DataFrame({'Ticker': df.columns[1:], 'Weight': weights})

        return "Inverse Variance Portfolio", weight_df

    # Maximum Diversification Portfolio
    def maximum_diversification_portfolio(df):
        returns = df.iloc[:, 1:].pct_change().dropna()
        cov_matrix = returns.cov()
        avg_returns = returns.mean()
        diversifications = np.abs(avg_returns) / np.sqrt(np.diag(cov_matrix))
        weights = diversifications / diversifications.sum()
        weight_df = pd.DataFrame({'Ticker': df.columns[1:], 'Weight': weights})

        return "Maximum Diversification Portfolio", weight_df

    # Maximum Decorrelation Portfolio
    def maximum_decorrelation_portfolio(df):
        returns = df.iloc[:, 1:].pct_change().dropna()
        corr_matrix = returns.corr()
        inv_correlation = 1 / np.abs(corr_matrix).sum()
        weights = inv_correlation / inv_correlation.sum()
        weight_df = pd.DataFrame({'Ticker': df.columns[1:], 'Weight': weights})

        return "Maximum Decorrelation Portfolio", weight_df

    # Black-Litterman Model Portfolio
    def black_litterman_portfolio(df, market_capitalizations, tau=0.025):
        # Berechnung der historischen Renditen (Änderungen über die Zeit für jede Spalte außer Datum)
        returns = df.iloc[:, 1:].pct_change().dropna()
        avg_returns = returns.mean()

        # Sicherstellen, dass die Ticker aus 'df' und 'market_capitalizations' übereinstimmen
        tickers = df.columns[1:]
        market_capitalizations = market_capitalizations.set_index('Ticker')

        # Überprüfen, ob die Tickers in beiden DataFrames übereinstimmen und ordnen
        market_caps = market_capitalizations.reindex(tickers)['Market Cap']

        # Fehlende Werte abfangen
        if market_caps.isnull().any():
            missing_tickers = market_caps[market_caps.isnull()].index.tolist()
            raise ValueError(f"Marktkapitalisierungen fehlen für folgende Ticker: {missing_tickers}")

        # Normalisierung der Gewichte aus den Marktkapitalisierungen
        weights = market_caps.values / market_caps.sum()

        # Black-Litterman-Anpassung der erwarteten Renditen
        adjusted_returns = tau * avg_returns + (1 - tau) * weights
        weights = adjusted_returns / adjusted_returns.sum()

        # Ausgabe der Gewichtungen als DataFrame
        weight_df = pd.DataFrame({'Ticker': tickers, 'Weight': weights})

        return "Black-Litterman Model Portfolio", weight_df

    # Hierarchical Risk Parity (HRP) Portfolio
    def hierarchical_risk_parity_portfolio(df):
        from scipy.cluster.hierarchy import linkage, fcluster
        returns = df.iloc[:, 1:].pct_change().dropna()
        corr_matrix = returns.corr()
        distances = np.sqrt((1 - corr_matrix) / 2)
        clusters = linkage(distances, method='ward')
        tickers = df.columns[1:]
        cluster_assignments = fcluster(clusters, t=1.5, criterion='distance')
        unique_clusters = np.unique(cluster_assignments)
        weights = np.zeros(len(tickers))
        for cluster in unique_clusters:
            cluster_indices = np.where(cluster_assignments == cluster)[0]
            equal_weight = 1 / len(cluster_indices)
            weights[cluster_indices] = equal_weight
        weights /= weights.sum()
        weight_df = pd.DataFrame({'Ticker': tickers, 'Weight': weights})

        return "Hierarchical Risk Parity Portfolio", weight_df

    # Logo sidebar
    st.sidebar.image("Images/FinGraph Logo.png",
                     use_column_width=True)

    # Draw Line for the sidebar (3 Pixel)
    draw_line_sidebar(3)

    portfolio_performacne_optimization_asset_type_options = ['Aktien', 'Kryptowährungen', 'Währungen', 'Rohstoffe',
                                                             'Fonds']
    portfolio_performacne_optimization_asset_type = st.sidebar.selectbox(label='Asset-Typ wählen:',
                                                                         options=portfolio_performacne_optimization_asset_type_options)

    # st.write(market_caps)
    performance_optimization_date_from_col, performance_optimization_date_to_col = st.sidebar.columns(2)
    from dateutil.relativedelta import relativedelta

    today = datetime.datetime.today().date()

    today_minus_one_year = today - relativedelta(years=1)
    with performance_optimization_date_from_col:
        performance_optimization_date_from = st.date_input(label='Von:',
                                                           value=today_minus_one_year,
                                                           key='performance_optimization_date_from')

    performance_optimization_date_from_plus_one_minute = performance_optimization_date_from + relativedelta(minutes=1)

    with performance_optimization_date_to_col:
        performance_optimization_date_to = st.date_input(label='Bis:',
                                                         value=today,
                                                         min_value=performance_optimization_date_from_plus_one_minute,
                                                         max_value=today,
                                                         key='performance_optimization_date_to')

    # Liste der Methodennamen
    optimization_method_names = [
        "Mean-Variance Optimization",
        "Minimum Variance Portfolio",
        "Maximum Sharpe Ratio Portfolio",
        "Equal Weight Portfolio",
        "Risk Parity Portfolio",
        "Inverse Variance Portfolio",
        "Maximum Diversification Portfolio",
        "Maximum Decorrelation Portfolio",
        "Black-Litterman Model Portfolio",
        "Hierarchical Risk Parity Portfolio"
    ]

    selected_optimization_method = st.sidebar.selectbox('Optimierungsmethode:',
                                                        options=optimization_method_names,
                                                        key='selected_optimization_method')

    # Tickers importieren
    import Tickers as tic
    tickers, big_four_tickers = tic.run_tickers(asset_type=portfolio_performacne_optimization_asset_type)

    # Einfachauswahl für Ticker
    tickers_portfolio_performance_optimization = st.sidebar.multiselect('Tickers (mind. 2 auswählen):',
                                                                        options=tickers,
                                                                        key='tickers_portfolio_performance_optimization',
                                                                        default=big_four_tickers)

    # Marktkapital Aktien
    if portfolio_performacne_optimization_asset_type == 'Aktien':
        market_caps = get_market_caps_stocks(tickers_portfolio_performance_optimization)


    # Marktkapital für Kryptowährungen
    elif portfolio_performacne_optimization_asset_type == 'Kryptowährungen':
        market_caps = get_market_caps_crypto(tickers_portfolio_performance_optimization)


    # Marktkapital für Kryptowährungen
    elif portfolio_performacne_optimization_asset_type == 'Währungen':
        market_caps = get_exchange_rates(tickers_portfolio_performance_optimization)



    # Marktkapital für Rohstoffe
    elif portfolio_performacne_optimization_asset_type == 'Rohstoffe':
        market_caps = get_commodity_prices(tickers_portfolio_performance_optimization)


    # Marktkapital für Fonds
    elif portfolio_performacne_optimization_asset_type == 'Fonds':
        market_caps = get_market_caps_funds(tickers_portfolio_performance_optimization)

    # Foto Sidebar Stocks API
    st.sidebar.write('')
    st.sidebar.write('')
    st.sidebar.write('')
    st.sidebar.write('')

    # Page Title
    Centred_Title.run_centred_title('Portfolio Performance Optimization')

    st.markdown(
        f"""
            <div style='text-align: center; font-weight: bold; font-size: 1.2vw;'>
                {selected_optimization_method}
            </div>
            """,
        unsafe_allow_html=True
    )

    st.write('')
    st.write('')

    data = portfolio_performacne_fetch_data(tickers_portfolio_performance_optimization,
                                            performance_optimization_date_from,
                                            performance_optimization_date_to,
                                            portfolio_performacne_optimization_asset_type)

    data = data.reset_index()

    # Marktkapital für Kryptowährungen
    if portfolio_performacne_optimization_asset_type == 'Kryptowährungen':
        data.columns = data.columns.str.replace(r'-USD', '', regex=True)


    # Marktkapital für Kryptowährungen
    elif portfolio_performacne_optimization_asset_type == 'Währungen':
        data.columns = data.columns.str.replace(r'USD=X', '', regex=True)



    # Marktkapital für Rohstoffe
    elif portfolio_performacne_optimization_asset_type == 'Rohstoffe':
        data.columns = data.columns.str.replace(r'=F', '', regex=True)

    # Daten visualisieren
    create_line_chart(data, portfolio_performacne_optimization_asset_type)

    # Calculate Perofrmance Optimization

    result_text, result_df = calculate_performance_optimization(data=data,
                                                                selected_optimization_method=selected_optimization_method,
                                                                market_caps=market_caps)

    # st.write(result_df)
    # Index-Spalte umbennen (index -> Ticker)
    result_df = result_df.rename(columns={'index': 'Ticker'})

    # Ergebnis nach Gewichten absteigend sortieren
    result_df = result_df.sort_values(by='Weight',
                                      ascending=False)

    # Eine horizontale zwei Pixel Linie hinzufügen
    draw_line(2)

    create_pie_chart(result_df)
    tickers_count = len(result_df['Ticker'].values)

    # Eine horizontale zwei Pixel Linie hinzufügen
    draw_line(2)

    ticker_weight_col_one, ticker_weight_col_two, ticker_weight_col_three, ticker_weight_col_four = st.columns(4)

    with ticker_weight_col_one:
        iteration = 1

        for ticker in result_df['Ticker']:

            weight = float(result_df[result_df['Ticker'] == ticker]['Weight'].values)

            if iteration % 4 == 1:
                make_metric(ticker, weight, tickers_count, market_caps)
            iteration += 1

    with ticker_weight_col_two:
        iteration = 1
        for ticker in result_df['Ticker']:

            weight = float(result_df[result_df['Ticker'] == ticker]['Weight'].values)

            if iteration % 4 == 2:
                make_metric(ticker, weight, tickers_count, market_caps)
            iteration += 1

    with ticker_weight_col_three:
        iteration = 1
        for ticker in result_df['Ticker']:
            weight = float(result_df[result_df['Ticker'] == ticker]['Weight'].values)
            if iteration % 4 == 3:
                make_metric(ticker, weight, tickers_count, market_caps)
            iteration += 1

    with ticker_weight_col_four:
        iteration = 1
        for ticker in result_df['Ticker']:
            weight = float(result_df[result_df['Ticker'] == ticker]['Weight'].values)
            if iteration % 4 != 1 and iteration % 4 != 2 and iteration % 4 != 3:
                make_metric(ticker, weight, tickers_count, market_caps)
            iteration += 1

    # Eine horizontale drei Pixel Linie hinzufügen
    draw_line(3)

    # Footer importieren
    import Footer as ft
    ft.run_footer(language_index=language_index,
                  doc_path='test_documentation.pdf')


