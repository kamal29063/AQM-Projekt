import requests


def run_currency_converter(language_index):
    import json
    import Centred_Title
    import  streamlit as st
    import Background_Style
    from datetime import datetime
    import pandas as pd
    import numpy as np

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

    # Währungen konvertieren mit yfiance
    st.cache
    def convert_currency_yfinace(first_currency,second_currency,first_currency_amount,exchange_date):

        import yfinance as yf
        from datetime import  timedelta

        ticker = str(first_currency ).upper()+str(second_currency).upper()+'=X'


        date_minus_one = exchange_date - timedelta(days=1)
        date_minus_two = exchange_date - timedelta(days=2)
        date_minus_three = exchange_date - timedelta(days=3)
        date_minus_four = exchange_date - timedelta(days=4)
        date_minus_five = exchange_date - timedelta(days=5)
        date_minus_six = exchange_date - timedelta(days=6)

        date_plus_one = exchange_date + timedelta(days=1)


        def get_data(exchange_date_par):
            # Daten mit yfinance abrufen
            data = yf.download(ticker, start=exchange_date_par, end=date_plus_one)
            data = data.reset_index()
            # Lösche die Ticker-Level aus den Daten
            data.columns = data.columns.droplevel(1)
            return data

        # 1. Versuch
        data = get_data(exchange_date)
        if not data.empty:
            current_rate = data['Close'].iloc[-1] * first_currency_amount
            return current_rate, exchange_date
        else:
            # 2. Versuch
            data = get_data(date_minus_one)
            if not data.empty:
                current_rate = data['Close'].iloc[-1] * first_currency_amount
                return current_rate,date_minus_one
            else:
                # 3. Versuch
                data = get_data(date_minus_two)
                if not data.empty:
                    current_rate = data['Close'].iloc[-1] * first_currency_amount
                    return current_rate,date_minus_two
                else:
                    # 4. Versuch
                    data = get_data(date_minus_three)
                    if not data.empty:
                        current_rate = data['Close'].iloc[-1] * first_currency_amount
                        return current_rate, date_minus_three
                    else:
                        # 5. Versuch
                        data = get_data(date_minus_four)
                        if not data.empty:
                            current_rate = data['Close'].iloc[-1] * first_currency_amount
                            return current_rate, date_minus_four
                        else:
                            # 6. Versuch
                            data = get_data(date_minus_five)
                            if not data.empty:
                                current_rate = data['Close'].iloc[-1] * first_currency_amount
                                return current_rate, date_minus_five
                            else:
                                # 7. Versuch
                                data = get_data(date_minus_six)
                                if not data.empty:
                                    current_rate = data['Close'].iloc[-1] * first_currency_amount
                                    return current_rate, date_minus_six
                                else:
                                    return 0,None


    # Lat. und Long. zurückgeben (Karte) => First Currency
    st.cache
    def get_country_location_info(countries_names):

        GeoData_df = pd.read_excel(r'GeoData\geoData.xlsx',
                                 usecols=['country_name_1','country_name_2','abbr_1','lat','lon'])

        df = GeoData_df[GeoData_df['country_name_1'].isin(countries_names)| GeoData_df['country_name_2'].isin(countries_names)]

        return df.loc[:,['lat','lon']], df.loc[:,['abbr_1']]


    # Flagge für jedes Land (Image)
    def get_country_flag_image(country_name):

        _,abbr= get_country_location_info([country_name])
        abbr = str(abbr.values).replace('[','').replace(']','').replace("'","").lower()

        import base64
        try:


            svg_file_path = rf"Images\Countries Flags\{abbr}.svg"
            # SVG-Datei lesen und in Base64 kodieren
            with open(svg_file_path, "rb") as svg_file:
                svg_content = svg_file.read()
                encoded_image = base64.b64encode(svg_content).decode()

        # Wenn das Land nicht gefunden wurde, also das Land hat kein Bild auch  (Dummy URL)
        except:
            svg_file_path = rf"Images\Countries Flags\Empty.svg"
            # SVG-Datei lesen und in Base64 kodieren
            with open(svg_file_path, "rb") as svg_file:
                svg_content = svg_file.read()
                encoded_image = base64.b64encode(svg_content).decode()

        # Width and height set to a responsive unit
        image_size = "7vw"  # Adjust this value to suit your layout; vw means "viewport width"

        # Display HTML in Streamlit
        st.markdown(
            f"""
            <div style='display: flex; flex-direction: column; align-items: center; justify-content: center; width: {image_size}; max-width: 300px; margin: 0 auto;'>
                <div style='width: 100%; padding-top: 100%; position: relative;'>
                    <img src='data:image/svg+xml;base64,{encoded_image}' alt='{country_name}' 
                         style='width: 100%; height: 100%; object-fit: contain; border-radius: 7px; position: absolute; top: 0; left: 0;' />
                </div>
                <p style='font-size: 1.2em; font-weight: bold; text-align: center; margin-top: 8px;'>{country_name}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')


    # Währung Zeichen
    def get_currency_symbol(currency_abbreviation, amount, delta):
        from forex_python.converter import CurrencyCodes

        # Erstelle ein CurrencyCodes Objekt
        currency = CurrencyCodes()


        symbol = currency.get_symbol(currency_abbreviation)


        if delta>=1:
            st.markdown(
                f"""
                            <div style='border: 1px solid black; box-shadow: 0px 0px 25px 3px black; padding: 10px; background-color: #f8f8f8;'>
                                <h1 style='text-align: center; background-color:#d5d5d5;'>
                                    {amount:.5f} {currency_abbreviation}
                                    ‎ ‎ ‎ <span style='color:green; background-color:#bdbdbd;'>↑{delta:.3f} %</span>
                                </h1>
                                <h1 style='text-align: center; background-color:#eeeeee;'>
                                    <span style='color:#009999;'>{currencies_names.get(currency_abbreviation)} ({symbol})</span>
                                </h1>
                            </div>
                            """,
                unsafe_allow_html=True
            )



        else:

            st.markdown(
                f"""
                <div style='border: 1px solid black; box-shadow: 0px 0px 15px 3px black; padding: 10px; background-color: #f8f8f8;'>
                    <h1 style='text-align: center; background-color:#d5d5d5;'>
                        {amount:.5f} {currency_abbreviation}
                        ‎ ‎ ‎ <span style='color:red; background-color:#bdbdbd;'>↓{delta:.3f} %</span>
                    </h1>
                    <h1 style='text-align: center; background-color:#eeeeee;'>
                        <span style='color:#009999;'>{currencies_names.get(currency_abbreviation)} ({symbol})</span>
                    </h1>
                </div>
                """,
                unsafe_allow_html=True
            )

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

    currency_countries = {
        "USD": ["United States", "Ecuador", "El Salvador", "Panama", "Puerto Rico", "Guam", "Northern Mariana Islands",
                "American Samoa", "United States Virgin Islands"],
        "EUR": ["Germany", "Austria", "Belgium", "Cyprus", "Estonia", "Finland", "France", "Greece", "Ireland", "Italy",
                "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Portugal", "Slovakia", "Slovenia",
                "Spain"],
        "AED": ["United Arab Emirates"],
        "AFN": ["Afghanistan"],
        "ALL": ["Albania"],
        "AMD": ["Armenia"],
        "ANG": ["Curaçao", "Sint Maarten"],
        "AOA": ["Angola"],
        "ARS": ["Argentina"],
        "AUD": ["Australia", "Kiribati", "Nauru", "Tuvalu"],
        "AWG": ["Aruba"],
        "AZN": ["Azerbaijan"],
        "BAM": ["Bosnia and Herzegovina"],
        "BBD": ["Barbados"],
        "BDT": ["Bangladesh"],
        "BGN": ["Bulgaria"],
        "BHD": ["Bahrain"],
        "BIF": ["Burundi"],
        "BMD": ["Bermuda"],
        "BND": ["Brunei Darussalam"],
        "BOB": ["Bolivia (Plurinational State of)"],
        "BRL": ["Brazil"],
        "BSD": ["Bahamas"],
        "BTN": ["Bhutan"],
        "BWP": ["Botswana"],
        "BYN": ["Belarus"],
        "BZD": ["Belize"],
        "CAD": ["Canada"],
        "CDF": ["Democratic Republic of the Congo"],
        "CHF": ["Switzerland", "Liechtenstein"],
        "CLP": ["Chile"],
        "CNY": ["China"],
        "COP": ["Colombia"],
        "CRC": ["Costa Rica"],
        "CUP": ["Cuba"],
        "CVE": ["Cabo Verde"],
        "CZK": ["Czechia"],
        "DJF": ["Djibouti"],
        "DKK": ["Denmark", "Greenland", "Faroe Islands (Associate Member)"],
        "DOP": ["Dominican Republic"],
        "DZD": ["Algeria"],
        "EGP": ["Egypt"],
        "ERN": ["Eritrea"],
        "ETB": ["Ethiopia"],
        "FJD": ["Fiji"],
        "FKP": ["Falkland Islands (Malvinas)"],
        "FOK": ["Faroe Islands (Associate Member)"],
        "GBP": ["United Kingdom", "Isle of Man", "Jersey", "Guernsey", "South Georgia and the South Sandwich Islands",
                "British Antarctic Territory"],
        "GEL": ["Georgia"],
        "GGP": ["Guernsey"],
        "GHS": ["Ghana"],
        "GIP": ["Gibraltar"],
        "GMD": ["Gambia"],
        "GNF": ["Guinea"],
        "GTQ": ["Guatemala"],
        "GYD": ["Guyana"],
        "HKD": ["Hong Kong"],
        "HNL": ["Honduras"],
        "HRK": ["Croatia"],
        "HTG": ["Haiti"],
        "HUF": ["Hungary"],
        "IDR": ["Indonesia"],
        "ILS": ["Israel"],
        "IMP": ["Isle of Man"],
        "INR": ["India"],
        "IQD": ["Iraq"],
        "IRR": ["Iran (Islamic Republic of)"],
        "ISK": ["Iceland"],
        "JEP": ["Jersey"],
        "JMD": ["Jamaica"],
        "JOD": ["Jordan"],
        "JPY": ["Japan"],
        "KES": ["Kenya"],
        "KGS": ["Kyrgyzstan"],
        "KHR": ["Cambodia"],
        "KID": ["Kiribati"],
        "KMF": ["Comoros"],
        "KRW": ["Republic of Korea"],
        "KWD": ["Kuwait"],
        "KYD": ["Cayman Islands"],
        "KZT": ["Kazakhstan"],
        "LAK": ["Lao People's Democratic Republic"],
        "LBP": ["Lebanon"],
        "LKR": ["Sri Lanka"],
        "LRD": ["Liberia"],
        "LSL": ["Lesotho"],
        "LYD": ["Libya"],
        "MAD": ["Morocco", "Western Sahara"],
        "MDL": ["Republic of Moldova"],
        "MGA": ["Madagascar"],
        "MKD": ["North Macedonia"],
        "MMK": ["Myanmar"],
        "MNT": ["Mongolia"],
        "MOP": ["Macao"],
        "MRU": ["Mauritania"],
        "MUR": ["Mauritius"],
        "MVR": ["Maldives"],
        "MWK": ["Malawi"],
        "MXN": ["Mexico"],
        "MYR": ["Malaysia"],
        "MZN": ["Mozambique"],
        "NAD": ["Namibia"],
        "NGN": ["Nigeria"],
        "NIO": ["Nicaragua"],
        "NOK": ["Norway", "Svalbard and Jan Mayen"],
        "NPR": ["Nepal"],
        "NZD": ["New Zealand", "Cook Islands", "Niue", "Pitcairn Islands", "Tokelau (Associate Member)"],
        "OMR": ["Oman"],
        "PAB": ["Panama"],
        "PEN": ["Peru"],
        "PGK": ["Papua New Guinea"],
        "PHP": ["Philippines"],
        "PKR": ["Pakistan"],
        "PLN": ["Poland"],
        "PYG": ["Paraguay"],
        "QAR": ["Qatar"],
        "RON": ["Romania"],
        "RSD": ["Serbia"],
        "RUB": ["Russian Federation"],
        "RWF": ["Rwanda"],
        "SAR": ["Saudi Arabia"],
        "SBD": ["Solomon Islands"],
        "SCR": ["Seychelles"],
        "SDG": ["Sudan"],
        "SEK": ["Sweden"],
        "SGD": ["Singapore"],
        "SHP": ["Saint Helena", "Ascension Island", "Tristan da Cunha"],
        "SLE": ["Sierra Leone"],
        "SLL": ["Sierra Leone"],
        "SOS": ["Somalia"],
        "SRD": ["Suriname"],
        "SSP": ["South Sudan"],
        "STN": ["Sao Tome and Principe"],
        "SYP": ["Syrian Arab Republic"],
        "SZL": ["Eswatini"],
        "THB": ["Thailand"],
        "TJS": ["Tajikistan"],
        "TMT": ["Turkmenistan"],
        "TND": ["Tunisia"],
        "TOP": ["Tonga"],
        "TRY": ["Türkiye"],
        "TTD": ["Trinidad and Tobago"],
        "TVD": ["Tuvalu"],
        "TWD": ["Taiwan"],
        "TZS": ["United Republic of Tanzania"],
        "UAH": ["Ukraine"],
        "UGX": ["Uganda"],
        "UYU": ["Uruguay"],
        "UZS": ["Uzbekistan"],
        "VES": ["Venezuela (Bolivarian Republic of)"],
        "VND": ["Viet Nam"],
        "VUV": ["Vanuatu"],
        "WST": ["Samoa"],
        "XAF": ["Cameroon", "Central African Republic", "Chad", "Congo", "Equatorial Guinea", "Gabon"],
        "XCD": ["Anguilla", "Antigua and Barbuda", "Dominica", "Grenada", "Montserrat", "Saint Kitts and Nevis",
                "Saint Lucia", "Saint Vincent and the Grenadines"],
        "XOF": ["Benin", "Burkina Faso", "Côte d'Ivoire", "Guinea-Bissau", "Mali", "Niger", "Senegal", "Togo"],
        "XPF": ["French Polynesia", "New Caledonia", "Wallis and Futuna"],
        "YER": ["Yemen"],
        "ZAR": ["South Africa"],
        "ZMW": ["Zambia"],
        "ZWL": ["Zimbabwe"]
    }

    currencies_names = {
        "AED": "United Arab Emirates Dirham",
        "AFN": "Afghan Afghani",
        "ALL": "Albanian Lek",
        "AMD": "Armenian Dram",
        "ANG": "Netherlands Antillean Guilder",
        "AOA": "Angolan Kwanza",
        "ARS": "Argentine Peso",
        "AUD": "Australian Dollar",
        "AWG": "Aruban Florin",
        "AZN": "Azerbaijani Manat",
        "BAM": "Bosnia-Herzegovina Convertible Mark",
        "BBD": "Barbadian Dollar",
        "BDT": "Bangladeshi Taka",
        "BGN": "Bulgarian Lev",
        "BHD": "Bahraini Dinar",
        "BIF": "Burundian Franc",
        "BMD": "Bermudian Dollar",
        "BND": "Brunei Dollar",
        "BOB": "Bolivian Boliviano",
        "BRL": "Brazilian Real",
        "BSD": "Bahamian Dollar",
        "BTN": "Bhutanese Ngultrum",
        "BWP": "Botswana Pula",
        "BYN": "Belarusian Ruble",
        "BZD": "Belize Dollar",
        "CAD": "Canadian Dollar",
        "CDF": "Congolese Franc",
        "CHF": "Swiss Franc",
        "CLP": "Chilean Peso",
        "CNY": "Chinese Yuan",
        "COP": "Colombian Peso",
        "CRC": "Costa Rican Colón",
        "CUP": "Cuban Peso",
        "CVE": "Cape Verdean Escudo",
        "CZK": "Czech Koruna",
        "DJF": "Djiboutian Franc",
        "DKK": "Danish Krone",
        "DOP": "Dominican Peso",
        "DZD": "Algerian Dinar",
        "EGP": "Egyptian Pound",
        "ERN": "Eritrean Nakfa",
        "ETB": "Ethiopian Birr",
        "EUR": "Euro",
        "FJD": "Fijian Dollar",
        "FKP": "Falkland Islands Pound",
        "FOK": "Faroese Króna",
        "GBP": "British Pound Sterling",
        "GEL": "Georgian Lari",
        "GGP": "Guernsey Pound",
        "GHS": "Ghanaian Cedi",
        "GIP": "Gibraltar Pound",
        "GMD": "Gambian Dalasi",
        "GNF": "Guinean Franc",
        "GTQ": "Guatemalan Quetzal",
        "GYD": "Guyanese Dollar",
        "HKD": "Hong Kong Dollar",
        "HNL": "Honduran Lempira",
        "HRK": "Croatian Kuna",
        "HTG": "Haitian Gourde",
        "HUF": "Hungarian Forint",
        "IDR": "Indonesian Rupiah",
        "ILS": "Israeli New Shekel",
        "IMP": "Isle of Man Pound",
        "INR": "Indian Rupee",
        "IQD": "Iraqi Dinar",
        "IRR": "Iranian Rial",
        "ISK": "Icelandic Króna",
        "JEP": "Jersey Pound",
        "JMD": "Jamaican Dollar",
        "JOD": "Jordanian Dinar",
        "JPY": "Japanese Yen",
        "KES": "Kenyan Shilling",
        "KGS": "Kyrgyzstani Som",
        "KHR": "Cambodian Riel",
        "KID": "Kiribati Dollar",
        "KMF": "Comorian Franc",
        "KRW": "South Korean Won",
        "KWD": "Kuwaiti Dinar",
        "KYD": "Cayman Islands Dollar",
        "KZT": "Kazakhstani Tenge",
        "LAK": "Lao Kip",
        "LBP": "Lebanese Pound",
        "LKR": "Sri Lankan Rupee",
        "LRD": "Liberian Dollar",
        "LSL": "Lesotho Loti",
        "LYD": "Libyan Dinar",
        "MAD": "Moroccan Dirham",
        "MDL": "Moldovan Leu",
        "MGA": "Malagasy Ariary",
        "MKD": "Macedonian Denar",
        "MMK": "Myanmar Kyat",
        "MNT": "Mongolian Tögrög",
        "MOP": "Macanese Pataca",
        "MRU": "Mauritanian Ouguiya",
        "MUR": "Mauritian Rupee",
        "MVR": "Maldivian Rufiyaa",
        "MWK": "Malawian Kwacha",
        "MXN": "Mexican Peso",
        "MYR": "Malaysian Ringgit",
        "MZN": "Mozambican Metical",
        "NAD": "Namibian Dollar",
        "NGN": "Nigerian Naira",
        "NIO": "Nicaraguan Córdoba",
        "NOK": "Norwegian Krone",
        "NPR": "Nepalese Rupee",
        "NZD": "New Zealand Dollar",
        "OMR": "Omani Rial",
        "PAB": "Panamanian Balboa",
        "PEN": "Peruvian Sol",
        "PGK": "Papua New Guinean Kina",
        "PHP": "Philippine Peso",
        "PKR": "Pakistani Rupee",
        "PLN": "Polish Złoty",
        "PYG": "Paraguayan Guaraní",
        "QAR": "Qatari Riyal",
        "RON": "Romanian Leu",
        "RSD": "Serbian Dinar",
        "RUB": "Russian Ruble",
        "RWF": "Rwandan Franc",
        "SAR": "Saudi Riyal",
        "SBD": "Solomon Islands Dollar",
        "SCR": "Seychellois Rupee",
        "SDG": "Sudanese Pound",
        "SEK": "Swedish Krona",
        "SGD": "Singapore Dollar",
        "SHP": "Saint Helena Pound",
        "SLL": "Sierra Leonean Leone",
        "SOS": "Somali Shilling",
        "SRD": "Surinamese Dollar",
        "SSP": "South Sudanese Pound",
        "STN": "São Tomé and Príncipe Dobra",
        "SYP": "Syrian Pound",
        "SZL": "Eswatini Lilangeni",
        "THB": "Thai Baht",
        "TJS": "Tajikistani Somoni",
        "TMT": "Turkmenistani Manat",
        "TND": "Tunisian Dinar",
        "TOP": "Tongan Paʻanga",
        "TRY": "Turkish Lira",
        "TTD": "Trinidad and Tobago Dollar",
        "TVD": "Tuvaluan Dollar",
        "TWD": "New Taiwan Dollar",
        "TZS": "Tanzanian Shilling",
        "UAH": "Ukrainian Hryvnia",
        "UGX": "Ugandan Shilling",
        "USD": "United States Dollar",
        "UYU": "Uruguayan Peso",
        "UZS": "Uzbekistani Som",
        "VES": "Venezuelan Bolívar",
        "VND": "Vietnamese Đồng",
        "VUV": "Vanuatu Vatu",
        "WST": "Samoan Tālā",
        "XAF": "Central African CFA Franc",
        "XCD": "East Caribbean Dollar",
        "XDR": "Special Drawing Rights",
        "XOF": "West African CFA Franc",
        "XPF": "CFP Franc",
        "YER": "Yemeni Rial",
        "ZAR": "South African Rand",
        "ZMW": "Zambian Kwacha",
        "ZWL": "Zimbabwean Dollar"
    }

    first_currency_converter_col, second_currency_converter_col = st.sidebar.columns(2)

    with first_currency_converter_col:

        first_currency = st.selectbox(label ='Erste Währung',
                                              options= currency_codes,
                                              key='first_currency_converter',
                                              index=0)


    with second_currency_converter_col:
        second_currency = st.selectbox(label ='Zweite Währung',
                                              options= currency_codes,
                                              key='second_currency_converter',
                                              index=1)

    first_currency_amount_converter_col, exchange_date_converter_col = st.sidebar.columns(2)

    with first_currency_amount_converter_col:
        first_currency_amount = st.number_input(label='Menge',
                                                        key='first_currency_amount_currency_converter',
                                                        min_value=1,
                                                        max_value=100000000,
                                                        step=1)

    with exchange_date_converter_col:
        today = datetime.today().date()
        exchange_date_converter = st.date_input(label='Wechseldatum',
                                              value=today,
                                              max_value=today,
                                              key='exchange_date_currency_converter')



    # Länder-Flaggen anzeigen checkbox
    show_country_flags_map = st.sidebar.radio(label= 'Currency County',
                                              options=['Keins','Flaggen','Landkarte'],
                                              key='show_country_flags_map_currency_converter',
                                              horizontal=True)





    Centred_Title.run_centred_title('Währungswechsel')

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

    first_currency_dummy = first_currency
    second_currency_dummy = second_currency

    if currency_changed:
        first_currency = second_currency_dummy
        second_currency = first_currency_dummy



    try:



        second_currency_amount_selected_date, valid_converting_date = convert_currency_yfinace(first_currency=first_currency,
                                                                        second_currency=second_currency,
                                                                        first_currency_amount=first_currency_amount,
                                                                        exchange_date=exchange_date_converter)

        valid_converting_date = valid_converting_date.strftime("%d. %B %Y")
        st.markdown(
            f"""
                    <div style='text-align: center; font-weight: bold; font-size: 1.2vw;'>
                        Wechselkurs vom {valid_converting_date}
                    </div>
                    """,
            unsafe_allow_html=True
        )

        st.write('')
        st.write('')

        second_currency_amount_selected_date = float(f'{second_currency_amount_selected_date:.6f}')

        countries_first_currency_column, countries_second_currency_column = st.columns(2)
        with countries_first_currency_column:

            delta = (( second_currency_amount_selected_date / first_currency_amount))

            get_currency_symbol(first_currency,
                                amount=first_currency_amount,
                                delta=delta)

            # Liste von Ländern erster Währung
            countries_first_currency = currency_countries.get(first_currency)


            if show_country_flags_map in ['Landkarte','Flaggen']:
                st.write('')
                draw_line_curreny(3)
                st.write('')
            else:
                st.write('')
                st.write('')


            if show_country_flags_map =='Flaggen':
                first_currency_flaggs_col_one, first_currency_flaggs_col_two, first_currency_flaggs_col_three, first_currency_flaggs_col_four = st.columns(
                    4)

                with first_currency_flaggs_col_one:
                    iteration = 1
                    for country_first_currency in countries_first_currency:
                        if iteration % 4 == 1:
                            get_country_flag_image(country_first_currency)
                        iteration += 1

                with first_currency_flaggs_col_two:
                    iteration = 1
                    for country_first_currency in countries_first_currency:
                        if iteration % 4 == 2:
                            get_country_flag_image(country_first_currency)
                        iteration += 1
                with first_currency_flaggs_col_three:
                    iteration = 1
                    for country_first_currency in countries_first_currency:
                        if iteration % 4 == 3:
                            get_country_flag_image(country_first_currency)
                        iteration += 1

                with first_currency_flaggs_col_four:
                    iteration = 1
                    for country_first_currency in countries_first_currency:
                        if iteration % 4 != 1 and iteration % 4 != 2 and iteration % 4 != 3:
                            get_country_flag_image(country_first_currency)
                        iteration += 1


            if show_country_flags_map =='Landkarte':
                df,_ = get_country_location_info(countries_first_currency)
                st.map(df)





        with countries_second_currency_column:


            delta = ((first_currency_amount / second_currency_amount_selected_date))

            get_currency_symbol(second_currency,
                                amount=second_currency_amount_selected_date,
                                delta=delta)

            # Liste von Ländern zweiter Währung
            countries_second_currency = currency_countries.get(second_currency)

            if show_country_flags_map in ['Landkarte', 'Flaggen']:
                st.write('')
                draw_line_curreny(3)
                st.write('')
            else:
                st.write('')
                st.write('')

            if show_country_flags_map =='Flaggen':
                second_currency_flaggs_col_one,second_currency_flaggs_col_two,second_currency_flaggs_col_three,second_currency_flaggs_col_four = st.columns(4)

                with second_currency_flaggs_col_one:
                    iteration = 1
                    for country_second_currency in countries_second_currency:
                            if iteration %4==1:
                                get_country_flag_image(country_second_currency)
                            iteration +=1

                with second_currency_flaggs_col_two:
                    iteration = 1
                    for country_second_currency in countries_second_currency:
                            if iteration %4==2:
                                get_country_flag_image(country_second_currency)
                            iteration +=1
                with second_currency_flaggs_col_three:
                    iteration = 1
                    for country_second_currency in countries_second_currency:
                            if iteration %4==3:
                                get_country_flag_image(country_second_currency)
                            iteration += 1

                with second_currency_flaggs_col_four:
                    iteration = 1
                    for country_second_currency in countries_second_currency:
                            if iteration %4!=1  and iteration %4!=2 and iteration %4!=3:
                                get_country_flag_image(country_second_currency)
                            iteration += 1
            if show_country_flags_map == 'Landkarte':
                df,_ = get_country_location_info(countries_second_currency)
                st.map(df)
    except:
        st.warning('Bitte andere Daten wählen')


    # Eine horizontale drei Pixel Linie hinzufügen
    draw_line(3)

    # Footer importieren
    import Footer as ft
    ft.run_footer(language_index=language_index,
                  doc_path='test_documentation.pdf')
