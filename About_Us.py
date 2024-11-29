def run_about_us(language_index):
    import streamlit as st
    from PIL import Image

    import Background_Style

    language_index = st.session_state.language_index
    ########################################################################
    # Hintergrundfarbe von der APP
    Background_Style.run_background_styl()

    translations_about_us = {
        1: ["Project Presentation", "Projektvorstellung", "Presentazione del progetto", "Présentation du projet",
            "Presentación del proyecto", "Apresentação do projeto", "Projektpresentation", "Prosjektpresentasjon",
            "Projektpræsentation", "Prezentacja projektu", "Презентация проекта", "Презентація проєкту"],
        2: ["Created by Kamal Badawi, Hannah Andres, Yelda Öztürk and Aysenur Tekin", "Erstellt von Kamal Badawi, Hannah Andres, Yelda Öztürk und Aysenur Tekin", "Creato da Kamal Badawi", "Créé par Kamal Badawi",
            "Creado por Kamal Badawi", "Criado por Kamal Badawi", "Skapad av Kamal Badawi", "Opprettet av Kamal Badawi",
            "Oprettet af Kamal Badawi", "Utworzone przez Kamala Badawi", "Создано Камалем Бадави",
            "Створено Камалом Бадаві"],
        3: ["Software Engineer specializing in Process Automation & Business Intelligence",
            "Softwareingenieur mit Schwerpunkt Prozessautomatisierung und Business Intelligence",
            "Ingegnere del software specializzato in automazione dei processi e business intelligence",
            "Ingénieur logiciel spécialisé en automatisation des processus et intelligence économique",
            "Ingeniero de software especializado en automatización de procesos e inteligencia empresarial",
            "Engenheiro de software especializado em automação de processos e inteligência de negócios",
            "Mjukvaruingenjör med inriktning på processautomation och affärsintelligens",
            "Programvareingeniør med spesialisering i prosessautomatisering og forretningsintelligens",
            "Softwareingeniør med speciale i procesautomatisering og business intelligence",
            "Inżynier oprogramowania specjalizujący się w automatyzacji procesów i inteligencji biznesowej",
            "Инженер-программист, специализирующийся на автоматизации процессов и бизнес-аналитике",
            "Інженер-програміст, що спеціалізується на автоматизації процесів та бізнес-аналітиці"],
        4: ["Location:", "Ort:", "Luogo:", "Emplacement:", "Ubicación:", "Localização:", "Plats:", "Plassering:",
            "Placering:", "Lokalizacja:", "Местоположение:", "Місцезнаходження:"],
        5: ["Frankfurt am Main", "Frankfurt am Main", "Francoforte sul Meno", "Francfort-sur-le-Main",
            "Fráncfort del Meno", "Frankfurt am Main", "Frankfurt am Main", "Frankfurt am Main", "Frankfurt am Main",
            "Frankfurt nad Menem", "Франкфурт-на-Майне", "Франкфурт-на-Майні"],
        6: ["Mobile Number:", "Handynummer:", "Numero di cellulare:", "Numéro de portable:", "Número de móvil:",
            "Número de celular:", "Mobilnummer:", "Mobilnummer:", "Mobilnummer:", "Numer telefonu komórkowego:",
            "Мобильный номер:", "Мобільний номер:"],
        7: ["Email Address:", "E-Mail-Adresse:", "Indirizzo email:", "Adresse e-mail:",
            "Dirección de correo electrónico:", "Endereço de e-mail:", "E-postadress:", "E-postadresse:",
            "E-mailadresse:", "Adres e-mail:", "Адрес электронной почты:", "Адреса електронної пошти:"],
        8: ["About the Project:", "Über das Projekt:", "Informazioni sul progetto:", "À propos du projet:",
            "Sobre el proyecto:", "Sobre o projeto:", "Om projektet:", "Om prosjektet:", "Om projektet:",
            "O projekcie:", "О проекте:", "Про проєкт:"],
        9: [
            "This project is a private, multilingual automation initiative developed using the Python programming language and the Streamlit framework. The goal of the project is to relieve professionals of repetitive and time-consuming routine tasks. By automating these tasks, valuable resources are freed up, allowing professionals to focus on their essential core tasks. The project supports multiple languages to address a broad user base and facilitate integration into various work environments. By increasing efficiency and reducing workload, this automation project significantly contributes to improving productivity and job satisfaction among professionals.",
            "Dieses Projekt ist ein privates, mehrsprachiges Automatisierungsvorhaben, das mit der Programmiersprache Python und dem Framework Streamlit entwickelt wurde. Ziel des Projekts ist es, Fachkräfte von repetitiven und zeitaufwändigen Routineaufgaben zu entlasten. Durch die Automatisierung dieser Aufgaben werden wertvolle Ressourcen freigesetzt, sodass sich die Fachkräfte auf ihre wesentlichen Kernaufgaben konzentrieren können. Das Projekt unterstützt mehrere Sprachen, um eine breite Benutzerbasis anzusprechen und die Integration in verschiedene Arbeitsumgebungen zu erleichtern. Indem es die Effizienz steigert und die Arbeitsbelastung reduziert, trägt dieses Automatisierungsprojekt wesentlich zur Verbesserung der Produktivität und Zufriedenheit der Fachkräfte bei.",
            "Questo progetto è un'iniziativa privata di automazione multilingue sviluppata utilizzando il linguaggio di programmazione Python e il framework Streamlit. L'obiettivo del progetto è alleviare i professionisti da compiti di routine ripetitivi e dispendiosi in termini di tempo. Automatizzando questi compiti, vengono liberate risorse preziose, consentendo ai professionisti di concentrarsi sui loro compiti essenziali. Il progetto supporta più lingue per rivolgersi a una vasta base di utenti e facilitare l'integrazione in vari ambienti di lavoro. Aumentando l'efficienza e riducendo il carico di lavoro, questo progetto di automazione contribuisce in modo significativo a migliorare la produttività e la soddisfazione professionale.",
            "Ce projet est une initiative privée d'automatisation multilingue développée à l'aide du langage de programmation Python et du framework Streamlit. L'objectif du projet est de soulager les professionnels des tâches routinières répétitives et chronophages. En automatisant ces tâches, des ressources précieuses sont libérées, permettant aux professionnels de se concentrer sur leurs tâches essentielles. Le projet prend en charge plusieurs langues pour s'adresser à un large éventail d'utilisateurs et faciliter l'intégration dans différents environnements de travail. En augmentant l'efficacité et en réduisant la charge de travail, ce projet d'automatisation contribue de manière significative à améliorer la productivité et la satisfaction des professionnels.",
            "Este proyecto es una iniciativa privada de automatización multilingüe desarrollada utilizando el lenguaje de programación Python y el marco de trabajo Streamlit. El objetivo del proyecto es liberar a los profesionales de tareas rutinarias repetitivas y que consumen mucho tiempo. Al automatizar estas tareas, se liberan recursos valiosos, lo que permite a los profesionales centrarse en sus tareas esenciales. El proyecto admite varios idiomas para dirigirse a una amplia base de usuarios y facilitar la integración en diversos entornos de trabajo. Al aumentar la eficiencia y reducir la carga de trabajo, este proyecto de automatización contribuye significativamente a mejorar la productividad y la satisfacción laboral de los profesionales.",
            "Este projeto é uma iniciativa privada de automação multilíngue desenvolvida usando a linguagem de programação Python e o framework Streamlit. O objetivo do projeto é aliviar os profissionais de tarefas rotineiras repetitivas e demoradas. Ao automatizar essas tarefas, recursos valiosos são liberados, permitindo que os profissionais se concentrem em suas tarefas essenciais. O projeto suporta vários idiomas para atender a uma ampla base de usuários e facilitar a integração em diversos ambientes de trabalho. Ao aumentar a eficiência e reduzir a carga de trabalho, este projeto de automação contribui significativamente para melhorar a produtividade e a satisfação no trabalho dos profissionais.",
            "Detta projekt är ett privat, flerspråkigt automatiseringsinitiativ utvecklat med programmeringsspråket Python och ramverket Streamlit. Projektets mål är att avlasta yrkesverksamma från repetitiva och tidskrävande rutinuppgifter. Genom att automatisera dessa uppgifter frigörs värdefulla resurser, vilket gör att yrkesverksamma kan fokusera på sina väsentliga kärnuppgifter. Projektet stöder flera språk för att tilltala en bred användarbas och underlätta integrationen i olika arbetsmiljöer. Genom att öka effektiviteten och minska arbetsbelastningen bidrar detta automatiseringsprojekt avsevärt till att förbättra produktiviteten och arbetsnöjdheten bland yrkesverksamma.",
            "Dette prosjektet er et privat, flerspråklig automatiseringsinitiativ utviklet ved hjelp av programmeringsspråket Python og rammeverket Streamlit. Målet med prosjektet er å avlaste fagfolk fra repetitive og tidkrevende rutineoppgaver. Ved å automatisere disse oppgavene frigjøres verdifulle ressurser, slik at fagfolk kan fokusere på sine essensielle kjerneoppgaver. Prosjektet støtter flere språk for å henvende seg til en bred brukerbase og legge til rette for integrering i ulike arbeidsmiljøer. Ved å øke effektiviteten og redusere arbeidsmengden, bidrar dette automatiseringsprosjektet betydelig til å forbedre produktiviteten og arbeidstilfredsheten blant fagfolk.",
            "Dette projekt er et privat, flersproget automatiseringsinitiativ udviklet ved hjælp af programmeringssproget Python og rammeværket Streamlit. Projektets mål er at aflaste fagfolk fra gentagne og tidskrævende rutineopgaver. Ved at automatisere disse opgaver frigives værdifulde ressourcer, så fagfolk kan fokusere på deres væsentlige kerneopgaver. Projektet understøtter flere sprog for at henvende sig til en bred brugerbase og lette integrationen i forskellige arbejdsmiljøer. Ved at øge effektiviteten og reducere arbejdsbyrden bidrager dette automatiseringsprojekt væsentligt til at forbedre produktiviteten og jobtilfredsheden blandt fagfolk.",
            "Ten projekt to prywatna, wielojęzyczna inicjatywa automatyzacji opracowana przy użyciu języka programowania Python i frameworka Streamlit. Celem projektu jest odciążenie profesjonalistów od powtarzalnych i czasochłonnych zadań rutynowych. Poprzez automatyzację tych zadań uwalniane są cenne zasoby, co pozwala specjalistom skupić się na ich podstawowych zadaniach. Projekt obsługuje wiele języków, aby dotrzeć do szerokiej bazy użytkowników i ułatwić integrację w różnych środowiskach pracy. Zwiększając efektywność i zmniejszając obciążenie pracą, ten projekt automatyzacji znacznie przyczynia się do poprawy produktywności i zadowolenia z pracy wśród profesjonalistów.",
            "Этот проект является частной многоязычной инициативой по автоматизации, разработанной с использованием языка программирования Python и фреймворка Streamlit. Цель проекта - освободить специалистов от повторяющихся и трудоемких рутинных задач. Автоматизируя эти задачи, освобождаются ценные ресурсы, позволяя специалистам сосредоточиться на своих основных задачах. Проект поддерживает несколько языков, чтобы привлечь широкую аудиторию и облегчить интеграцию в различные рабочие среды. Повышая эффективность и снижая рабочую нагрузку, этот проект автоматизации значительно способствует повышению производительности и удовлетворенности специалистов.",
            "Цей проєкт є приватною багатомовною ініціативою з автоматизації, розробленою з використанням мови програмування Python та фреймворка Streamlit. Метою проєкту є полегшення рутинних повторюваних та трудомістких завдань для фахівців. Автоматизуючи ці завдання, вивільняються цінні ресурси, що дозволяє фахівцям зосередитись на їхніх основних завданнях. Проєкт підтримує кілька мов, щоб охопити широку базу користувачів і полегшити інтеграцію в різні робочі середовища. Підвищуючи ефективність і зменшуючи навантаження, цей проєкт автоматизації значно сприяє підвищенню продуктивності та задоволеності роботою серед фахівців."]

    }
    ########################################################################
    st.write('')
    st.write('')
    dummy_splate, image_spalte, text_spalte, sprache_spalte = st.columns([0.5, 4, 5, 1])
    with dummy_splate:
        pass
    with image_spalte:
        image = Image.open('Images/Foto_Kamal Badawi.png')
        st.image(image)

    with text_spalte:
        # Titel und Beschreibung
        st.title(f'{translations_about_us.get(1)[language_index]}')
        st.write('')
        st.write('')
        st.write('')
        st.write(f"""
        ### {translations_about_us.get(2)[language_index]}
        {translations_about_us.get(3)[language_index]}
        """)

        # Ort und E-Mail
        st.write(f"""
        **{translations_about_us.get(4)[language_index]}**  {translations_about_us.get(5)[language_index]}      
        **{translations_about_us.get(6)[language_index]}**  +49 1515 6646666      
        **{translations_about_us.get(7)[language_index]}**  [kamal.badawi@gmx.de](mailto:kamal.badawi@gmx.de)
        """)

        # Optional: Weitere Informationen oder Inhalte hinzufügen
        st.write(f"""
        ---
        #### {translations_about_us.get(8)[language_index]}
        {translations_about_us.get(9)[language_index]}


        """)

        with sprache_spalte:
            pass


