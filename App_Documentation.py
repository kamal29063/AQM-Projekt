import  Process_Button_Styling

# Erstelle eine dicke Linie Funktion
def draw_line(groesse):
    import streamlit as st
    st.markdown(f"<hr style='border: {groesse}px solid black;'>", unsafe_allow_html=True)

def convert_page_size(page, target_width, target_height):
    import  fitz
    # Create a new page with the target size
    new_doc = fitz.open()  # Create a new empty PDF
    new_page = new_doc.new_page(width=target_width, height=target_height)
    # Draw the contents of the original page on the new page
    new_page.show_pdf_page(new_page.rect, page.parent, page.number)
    return new_page



def get_translations():
    import streamlit as st

    language_index = st.session_state.language_index

    translations_app_documentation = {
        1: [
            "Documentation Preview? (English Version)",  # English
            "Dokumentation Vorschau? (englische Version)",  # Deutsch
            "Anteprima della documentazione? (versione inglese)",  # Italiano
            "Aperçu de la documentation? (version anglaise)",  # Français
            "Vista previa de la documentación? (versión en inglés)",  # Español
            "Pré-visualização da documentação? (versão em inglês)",  # Português
            "Dokumentationsförhandsgranskning? (engelsk version)",  # Svenska
            "Dokumentasjon Forhåndsvisning? (engelsk versjon)",  # Norsk
            "Dokumentation Forhåndsvisning? (engelsk version)",  # Dansk
            "Podgląd dokumentacji? (wersja angielska)",  # Polski
            "Предварительный просмотр документации? (английская версия)",  # Русский
            "Попередній перегляд документації? (англійська версія)"  # українська
        ],
        2: [
            "Page",  # English
            "Seite",  # Deutsch
            "Pagina",  # Italiano
            "Page",  # Français
            "Página",  # Español
            "Página",  # Português
            "Sida",  # Svenska
            "Side",  # Norsk
            "Side",  # Dansk
            "Strona",  # Polski
            "Страница",  # Русский
            "Сторінка"  # українська
        ],
        3: [
            "Select a page area",  # English
            "Wählen Sie einen Seitenbereich aus",  # Deutsch
            "Seleziona un'area della pagina",  # Italiano
            "Sélectionnez une zone de page",  # Français
            "Seleccione un área de página",  # Español
            "Selecione uma área da página",  # Português
            "Välj ett sidområde",  # Svenska
            "Velg et sideområde",  # Norsk
            "Vælg et sideområde",  # Dansk
            "Wybierz obszar strony",  # Polski
            "Выберите область страницы",  # Русский
            "Виберіть область сторінки"  # українська
        ],
        4: [
            "Documentation",  # English
            "Dokumentation",  # Deutsch
            "Documentazione",  # Italiano
            "Documentation",  # Français
            "Documentación",  # Español
            "Documentação",  # Português
            "Dokumentation",  # Svenska
            "Dokumentasjon",  # Norsk
            "Dokumentation",  # Dansk
            "Dokumentacja",  # Polski
            "Документация",  # Русский
            "Документація"  # українська
        ],
        5: [
            "Page(s) loaded successfully",  # English
            "Seite(n) wurde(n) erfolgreich geladen",  # Deutsch
            "Pagina(e) caricata(e) con successo",  # Italiano
            "Page(s) chargée(s) avec succès",  # Français
            "Página(s) cargada(s) exitosamente",  # Español
            "Página(s) carregada(s) com sucesso",  # Português
            "Sida(or) laddad(e) framgångsrikt",  # Svenska
            "Side(r) lastet inn vellykket",  # Norsk
            "Side(r) indlæst med succes",  # Dansk
            "Strona(y) załadowana(e) pomyślnie",  # Polski
            "Страница(ы) успешно загружена(ы)",  # Русский
            "Сторінка(и) успішно завантажена(і)"  # українська
        ],
        6: [
            "Error loading documentation",  # English
            "Fehler beim Laden der Dokumentation",  # Deutsch
            "Errore durante il caricamento della documentazione",  # Italiano
            "Erreur lors du chargement de la documentation",  # Français
            "Error al cargar la documentación",  # Español
            "Erro ao carregar a documentação",  # Português
            "Fel vid inläsning av dokumentation",  # Svenska
            "Feil ved lasting av dokumentasjon",  # Norsk
            "Fejl ved indlæsning af dokumentation",  # Dansk
            "Błąd podczas ładowania dokumentacji",  # Polski
            "Ошибка загрузки документации",  # Русский
            "Помилка завантаження документації"  # українська
        ],
        7: [
            "Page(s)",  # English
            "Seite(n)",  # Deutsch
            "Pagina(e)",  # Italiano
            "Page(s)",  # Français
            "Página(s)",  # Español
            "Página(s)",  # Português
            "Sida(or)",  # Svenska
            "Side(r)",  # Norsk
            "Side(r)",  # Dansk
            "Strona(y)",  # Polski
            "Страница(ы)",  # Русский
            "Сторінка(и)"  # українська
        ],
        8: [
            "Do you want to adjust the PDF width to the page size?",  # English
            "Möchten Sie die PDF-Breite an die Seitengröße anpassen?",  # Deutsch
            "Vuole adattare la larghezza del PDF alla dimensione della pagina?",  # Italiano
            "Voulez-vous ajuster la largeur du PDF à la taille de la page ?",  # Français
            "¿Desea ajustar el ancho del PDF al tamaño de la página?",  # Español
            "Quer ajustar a largura do PDF ao tamanho da página?",  # Português
            "Vill du justera PDF-bredden till sidstorleken?",  # Svenska
            "Vil du justere PDF-bredden til sidestørrelsen?",  # Norsk
            "Vil du justere PDF-bredden til sidestørrelsen?",  # Dansk
            "Czy chcesz dostosować szerokość PDF do rozmiaru strony?",  # Polski
            "Вы хотите настроить ширину PDF на размер страницы?",  # Русский
            "Бажаєте налаштувати ширину PDF на розмір сторінки?"  # українська
        ],
        9: [
            "PDF Width:",  # English
            "PDF-Breite:",  # Deutsch
            "Larghezza PDF:",  # Italiano
            "Largeur du PDF :",  # Français
            "Ancho del PDF:",  # Español
            "Largura do PDF:",  # Português
            "PDF-bredd:",  # Svenska
            "PDF-bredde:",  # Norsk
            "PDF-bredde:",  # Dansk
            "Szerokość PDF:",  # Polski
            "Ширина PDF:",  # Русский
            "Ширина PDF:"  # українська
        ],
        10: [
            "PDF Height:",  # English
            "PDF-Höhe:",  # Deutsch
            "Altezza PDF:",  # Italiano
            "Hauteur du PDF :",  # Français
            "Altura del PDF:",  # Español
            "Altura do PDF:",  # Português
            "PDF-höjd:",  # Svenska
            "PDF-høyde:",  # Norsk
            "PDF-højde:",  # Dansk
            "Wysokość PDF:",  # Polski
            "Высота PDF:",  # Русский
            "Висота PDF:"  # українська
        ],
        11: [
            "Download documentation",  # English
            "Dokumentation herunterladen",  # Deutsch
            "Scarica documentazione",  # Italiano
            "Télécharger la documentation",  # Français
            "Descargar documentación",  # Español
            "Baixar documentação",  # Português
            "Ladda ner dokumentation",  # Svenska
            "Last ned dokumentasjon",  # Norsk
            "Download dokumentation",  # Dansk
            "Pobierz dokumentację",  # Polski
            "Скачать документацию",  # Русский
            "Завантажити документацію"  # українська
        ]
    }

    return  translations_app_documentation, language_index, st
def show_documentation_checkbox():

    translations, language_index, st = get_translations()
    # "Documentation Preview?"
    return st.checkbox(f'{translations.get(1)[language_index]}',
                       key='show_documentation_checkbox')

def run_app_documentation(file_path,show):
    try:
        translations, language_index, st = get_translations()
        import fitz  # PyMuPDF
        # Dictionary of possible PDF page sizes in points (1 point = 1/72 inch)
        file_path = rf'Documentations/{file_path}'
        pdf_document_tmp = fitz.open(file_path)
        num_pages_tmp = pdf_document_tmp.page_count
        pdf_document_tmp = None



        def show_documentation_pages(file_path,range_values,target_size,use_column_width):

            import streamlit as st

            import fitz  # PyMuPDF
            from PIL import Image
            import io

            min_page_num =  min(range_values)
            max_page_num = max(range_values)

            # Open the PDF file
            pdf_document = fitz.open(file_path)
            num_pages = pdf_document.page_count

            target_width, target_height = target_size
            for i in range(num_pages):
                page = pdf_document.load_page(i)
                if target_size != 'original':
                    page = convert_page_size(page, target_width, target_height)


                # Hole die Pixels von der PDF-Seite
                pix = page.get_pixmap()
                # Convert the Pixmap to a PIL Image
                image = Image.open(io.BytesIO(pix.tobytes()))


                # Display the image in Streamlit
                page_num = i + 1
                if page_num >= min_page_num and page_num <= max_page_num:
                    # "Page"
                    st.image(image, caption=f'{translations.get(2)[language_index]} {page_num}', use_column_width=use_column_width)
            return  min_page_num, max_page_num


        documentation_checkbox = False
        if show:
            documentation_checkbox_column, documentation_download_button_column = st.columns([10,2])
            with documentation_checkbox_column:
                documentation_checkbox = show_documentation_checkbox()

            with documentation_download_button_column:
                if documentation_checkbox:
                    # Download-Button Style
                    Process_Button_Styling.run_process_button_style()

                    with fitz.open(file_path) as doc:
                        pdf_bytes = doc.write()

                    # "Download documentation"
                    st.download_button(label=f'{translations.get(11)[language_index]}',
                                       data=pdf_bytes,
                                       file_name="downloaded_doumentation.no_open.pdf",
                                       mime="application/pdf")


            if documentation_checkbox:
                # 1 pixel Linie hinzufügen
                draw_line(1)
                range_values = st.slider(
                    # "Select a page area"                                          # "Page(s)"
                    f'{translations.get(3)[language_index]} ({num_pages_tmp} {translations.get(7)[language_index]})',
                    1, num_pages_tmp, (1, num_pages_tmp),
                    step=1
                )


                # Eine horizontale ein Pixel Linie hinzufügen
                draw_line(1)


                fit_pdf_width_column,target_width_column, dummy_spalte, target_height_column  = st.columns([9,4,2,4])
                # Create a range slider between 1 and 100 with a step of 1
                pdf_document = fitz.open(file_path)
                page = pdf_document.load_page(0)
                page_width = page.rect.width
                page_height = page.rect.height

                use_column_width = False
                with fit_pdf_width_column:
                    col1, col2 = st.columns([4,5])
                    with col1:
                        # "Do you want to adjust the PDF width to the page size?"
                        st.write(f'{translations.get(8)[language_index]}')

                    with col2:
                        fit_pdf_width = st.checkbox('',
                                                    key='fit_pdf_width_cb_documentation')

                    if fit_pdf_width:
                        use_column_width = True

                with target_width_column:
                    # "PDF-Width:"
                    target_size_width = st.number_input(f'{translations.get(9)[language_index]}',
                                                        value=int(page_width),
                                                        step=10,
                                                        min_value=100,
                                                        max_value=int(page_width) * 3,
                                                        key='show_documentation_target_size_width_number_input')
                with dummy_spalte:
                    pass
                with target_height_column:
                    # "PDF-Height:"
                    target_size_height = st.number_input(f'{translations.get(10)[language_index]}',
                                                         value=int(page_height),
                                                         min_value=100,
                                                         max_value=int(page_height) * 3,
                                                         step=10,
                                                         key = 'show_documentation_target_size_height_number_input')

                target_size = (target_size_width,target_size_height)

                # Eine horizontale ein Pixel Linie hinzufügen
                draw_line(1)

        if documentation_checkbox:
                min_page_num, max_page_num = show_documentation_pages(file_path,range_values,target_size,use_column_width)
                # "Documentation"                                # "Page(s) loaded successfully"
                st.success(rf'{translations.get(4)[language_index]} {max_page_num-min_page_num+1}  {translations.get(5)[language_index]}')

    except Exception as e:
        #"Error loading documentation"
        st.warning(f'Fehler: {e}')


