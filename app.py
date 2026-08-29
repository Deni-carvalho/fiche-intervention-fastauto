from datetime import datetime
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Fast Auto 91 - Fiche d'Intervention", page_icon="🔧", layout="wide"
)

catalogue_services = [
    "10 - Documents véhicule : Contrôle présence documents, Validité EAD/TACHY/LIM...",
    "20 - Général : Lavage du véhicule",
    "30 - Général : Lavage moteur et ventilateur / radiateurs complet",
    "40 - Ext Vhl / Électricité : Contrôle éclairage extérieure, catadioptres",
    (
        "50 - Ext Vhl / Électricité : Contrôle circuit de charge, niveau,"
        " fixation et cosse BAT"
    ),
    (
        "60 - Ext Vhl / Électricité : Contrôle de la présence de la protection des"
        " batteries"
    ),
    "70 - Ext Vhl / Électricité : Contrôle Fonctionnement coupe batteries",
    "80 - Ext Vhl / Électricité : Contrôle et graissage glissière porte batteries",
    "90 - Ext Vhl / Porte : Contrôle des Fonctionnement des portes",
    "100 - Ext Vhl / Porte : Contrôle du Dégivrage des glaces de portes AV",
    "110 - Ext Vhl / Porte : Contrôle des Issues de secours des portes AV / AR",
    (
        "120 - Ext Vhl / Porte : Contrôle présence picto issue de secours AV/ AR"
        " / Pavillon"
    ),
    (
        "130 - Ext Vhl / Porte : Contrôle anti-pincement / Bord sensible /"
        " réversion portes"
    ),
    "140 - Ext Vhl / Porte : Contrôle des Sécurités de présence sur les marches",
    "150 - Ext Vhl / Porte : Contrôle éclairage des marches AV / Milieu / AR",
    "160 - Ext Vhl / Porte : Contrôle des Mains courantes et poignées",
    (
        "170 - Ext Vhl / Porte : Contrôle des état revêtement sol des marches"
        " AV / Milieu / AR"
    ),
    "180 - Ext Vhl / Porte : Contrôle système de verrouillage AV / Milieu / AR",
    "190 - Ext Vhl / Rampe PMR : Contrôle de l'état des trappes de rampe",
    "210 - Ext Vhl / Rampe PMR : Contrôle du Fonctionnement de la rampe d'accès",
    (
        "220 - Ext Vhl / Rampe PMR : Contrôle du Fonctionnement du dispositif"
        " d'urgence"
    ),
    (
        "230 - Ext Vhl / Rampe PMR : Contrôle du Fonctionnement des bords"
        " sensibles"
    ),
    (
        "240 - Ext Vhl / Carrosserie : Contrôle général carrosserie. Bandes"
        " réfléchissantes"
    ),
    (
        "250 - Ext Vhl / Carrosserie : Contrôle de la Plaque d'immat et présence"
        " raison sociale"
    ),
    (
        "260 - Ext Vhl / Carrosserie : Contrôle présence disques LIM vitesse /"
        " picto Angle mort"
    ),
    (
        "270 - Ext Vhl / Carrosserie : Contrôle des vérins de soute / trappe de"
        " maintenance"
    ),
    (
        "290 - Ext Vhl / Pneumatiques : Contrôle état général pneus, Enjoliveur"
        " et pression"
    ),
    (
        "300 - Ext Vhl / Pneumatiques : Contrôle présence Témoins et Resserrer"
        " si besoin"
    ),
    "310 - Poste CONDUC : Passage à la valise, lecture et effacement des défauts",
    "320 - Poste CONDUC : Contrôle état et Fonctionnement du siège conducteur",
    "330 - Poste CONDUC : Contrôle état et Fonctionnement des Pare-soleils",
    "340 - Poste CONDUC : Contrôle état et Fonctionnement des rétroviseur INT/EXT",
    "350 - Poste CONDUC : Contrôle état et Fonctionnement du réglage du volant",
    "360 - Poste CONDUC : Contrôle des Patins des pédales",
    "370 - Poste CONDUC : Contrôle du Fonctionnement dégivrage fenêtre conducteur",
    "380 - Poste CONDUC : Commande ralentisseur, Avertisseur sonore",
    (
        "390 - Poste CONDUC : Contrôle Fonctionnement caméra et radar de recul,"
        " alarme sonore"
    ),
    (
        "400 - Poste CONDUC : Contrôle et Fonctionnement des commodos et état"
        " essuie-glaces"
    ),
    (
        "410 - Poste CONDUC : Contrôle Fonctionnement éclairage et voyants Tableau"
        " de bord"
    ),
    "420 - Poste CONDUC : Contrôle date de validité Extincteur",
    "430 - Poste CONDUC : Contrôle de la présence pictogramme extincteur",
    "440 - Poste CONDUC : Contrôle validité, contenance et picto boite pharmacie",
    "450 - Poste CONDUC : Contrôle marteau brise-glace et picto",
    "460 - Poste CONDUC : Contrôle du FAE",
    "470 - Poste CONDUC : Contrôle freins de Parc",
    "480 - Poste CONDUC : Nettoyage filtre anti-pollen conducteur et passagers",
    (
        "490 - Poste CONDUC : Chauffage : Contrôle du fonctionnement du CHAUFF"
        " CONDUC et passager"
    ),
    (
        "500 - Poste CONDUC : Climatisation : Contrôle Fonctionnement Clim CONDUC"
        " + ventil PB"
    ),
    "510 - Poste CONDUC : Climatisation : Contrôle du fonctionnement Clim passager",
    "520 - Int Vhl / Carrosserie : Contrôle présence de la plaque de tare",
    "530 - Int Vhl : Contrôle ouverture fenêtres basculantes (si équipé)",
    "540 - Int Vhl : Contrôle Fonctionnement arrêt demandé, signalisation",
    "550 - Int Vhl : Contrôle état du revêtement de sol",
    "560 - Int Vhl : Contrôle des garnitures / revêtement intérieur",
    "570 - Int Vhl / Électricité : Contrôle et état des éclairages intérieurs",
    "580 - Int Vhl / Bouteilles d'air : Contrôle validité / Purge / Signer le registre",
    "590 - Int Vhl : Contrôle et état Fixation des sièges et ceintures de sécurité",
    (
        "600 - Int Vhl / Articulation : Contrôle de la plateforme articulation"
        " (Joints, bâche)"
    ),
    (
        "610 - Moteur / Électricité : Contrôle état et fixation alternateur et"
        " câblage"
    ),
    (
        "620 - Moteur / Électricité : Contrôle état et fixation des passages des"
        " câblages élec"
    ),
    (
        "630 - Moteur / Électricité : Contrôle câblages, connectiques et"
        " protection démarreur"
    ),
    (
        "640 - Moteur : Contrôle Fonctionnement contacteur de sécurité"
        " démarrage (capot moteur)"
    ),
    "650 - Moteur : Contrôle des niveaux des fluides",
    "660 - Moteur : Contrôle état et Fixation silentbloc moteur",
    "670 - Moteur : Contrôle état et fixation faisceaux électriques moteur",
    "680 - Moteur : Contrôle des courroie, tendeurs et poulies",
    "690 - Moteur : Contrôle étanchéité moteur",
    (
        "700 - Moteur : Contrôle et/ou graissage turbo - Contrôle vis fixation"
        " protect chaleur"
    ),
    (
        "710 - Moteur : Contrôle détection incendie (Etat"
        " flexible/buses/pression bouteille)"
    ),
    (
        "720 - Moteur / Admission d'air : Contrôle état et fixations circuit"
        " d'admission d'air"
    ),
    "730 - Moteur / Admission d'air : Contrôle radiateur / intercooler",
    (
        "740 - Moteur / Échappement : Contrôle des fixations et étanchéité système"
        " de gaz échap"
    ),
    (
        "750 - Moteur / Circuit Refroid : Etanchéité, vase d'expansion, Niv LR,"
        " bouchon, clapet"
    ),
    "760 - Moteur / Circuit Refroid : Contrôle radiateur et ventilation moteur",
    "770 - Moteur / Circuit Refroid : Etanchéité, Niv réservoir hydro",
    (
        "780 - Moteur / Circuit Refroid : Réglage tension courroie pompe eau,"
        " ventilo hydrostat"
    ),
    "790 - Moteur / Compresseur dair : Etat général / Contrôle fixation",
    "800 - Moteur / Déshuileur : Etat général / Contrôle fixation",
    "810 - Moteur / Dessiccateur : Etat état et fixation faisceau",
    "820 - Boîte de vitesse : Contrôle fixation et des silentbloc",
    "830 - Boîte de vitesse : Contrôle état et fixation faisceau",
    "840 - Boîte de vitesse : Contrôle étanchéité et niveaux",
    "850 - Sous Vhl / Général : Graissages multiples sur châssis, selon conception Vhl",
    "860 - Sous Vhl / Châssis : Contrôle état général du treillis / traverses",
    "870 - Sous Vhl : Contrôle du moteur d'Essui-glace",
    "880 - Sous Vhl / Direction : Contrôle Cardans, boitier de direction (Jeu / étanchéité)",
    "890 - Sous Vhl / Direction : Contrôle Pompe de direction et canalisation hydraulique",
    "900 - Sous Vhl / Direction : Contrôle Renvoi d'angle, rotule, barre Accoupl, liaisons",
    "910 - Sous Vhl / Direction : Contrôle de l'étanchéité des conduites de la DA",
    "920 - Sous Vhl / Direction : Contrôle étachéité et fixation boîtier de DA et support",
    (
        "930 - Sous Vhl / Frein AV : Contrôle Disques de freins AV, mesure"
        " épaisseur D: ...; G: ..."
    ),
    "940 - Sous Vhl / Frein AV : Contrôle plaquettes AV",
    "950 - Sous Vhl / Freins AV : Contrôle étriers, flexibles et cylindres des freins AV",
    "960 - Sous Vhl / Freins AV : Contrôle câblages ABS AV + capteur usure plaquette",
    "970 - Sous Vhl / Freins AV:Ctrl, réglage et graissage des Cames freins AV",
    (
        "980 - Sous Vhl / Frein Milieu : Contrôle Disques, mesure épaisseur D:"
        " ......; G: ....."
    ),
    "990 - Sous Vhl / Frein Milieu : Contrôle plaquettes Milieu",
    "1000 - Sous Vhl / Freins Milieu : Contrôle étriers, flexibles et cylindres freins Milieu",
    "1010 - Sous Vhl / Freins Milieu : Contrôle câblages ABS et capteur usure plaquettes",
    "1020 - Sous Vhl / Freins Milieu : Ctrl, réglage et graissage des Cames freins Milieu",
    "1030 - Sous Vhl / Freins Milieu : Contrôle du modulateurs d'essieu de freinage Milieu",
    (
        "1040 - Sous Vhl / Freins ARR : Contrôle Disques, mesure épaisseur D:"
        " ......; G: ....."
    ),
    "1050 - Sous Vhl / Freins ARR : Contrôle plaquette freins ARR",
    "1060 - Sous Vhl / Freins ARR : Contrôle étriers, flexibles et cylindres freins ARR",
    "1070 - Sous Vhl / Freins Milieu: Contrôle câblages ABS et capteur usure plaquette",
    "1080 - Sous Vhl / Freins ARR : Ctrl, réglage et graissage des Cames freins AR",
    "1090 - Sous Vhl / Freins ARR : Contrôle du modulateurs d'essieu de freinage",
    "1100 - Sous Vhl / Train AV: Contrôle et graissage pivots (+ renvoi direction si équipé)",
    "1110 - Sous Vhl / Train AV: Contrôle rotules de suspension / fixation triangles/tirants",
    "1120 - Sous Vhl / Train AV: Contrôle des moyeux",
    "1130 - Sous Vhl / Train AV: Contrôle de la barre stable et biellettes",
    "1140 - Sous Vhl / Train AV: Contrôle des amortisseurs et coussins d'air",
    "1150 - Sous Vhl / Train AV: Contrôle des Valves de nivellement",
    "1160 - Sous Vhl / Train AV : Contrôle des tirants de pont INF / SUP",
    "1170 - Sous Vhl / Train Milieu: Contrôle des rotules de suspension",
    "1180 - Sous Vhl / Train Milieu: Contrôle des moyeux",
    "1190 - Sous Vhl / Train Milieu: Contrôle des fixations des triangles de suspension",
    "1200 - Sous Vhl / Train Milieu: Contrôle de la barre stable",
    "1210 - Sous Vhl / Train Milieu: Contrôle des amortisseurs et coussins d'air",
    "1220 - Sous Vhl / Train Arrière : Contrôle et graissage pivots et renvoi DA si équipé",
    "1230 - Sous Vhl / Train arrière : Contrôle des tirants de pont INF / SUP",
    "1240 - Sous Vhl / Train arrière : Contrôle des amortisseurs et coussins d'air",
    "1250 - Sous Vhl / Train arrière : Contrôle de la barre stable et biellettes",
    "1260 - Sous Vhl / Train arrière : Contrôle des Valves de nivellement",
    "1270 - Sous Vhl / Valve 4 Voies : Contrôle indépendance circuit pneumatique",
    "1280 - Sous Vhl / Articulation : Contrôle du soufflet d'articulation",
    "1290 - Sous Vhl / Châssis : Contrôle de l'état et de la protection anti-corrosion",
    "1300 - Pont / transmission : Contrôle étanchéité, niveau du pont / réducteurs de roues",
    "1310 - Pont / transmission : Contrôle et nettoyage mise à l'air libre",
    "1320 - Pont / transmission : Contrôle fixations et jeux arbre de transmission",
    "1330 - VHL HYBRIDE : Contrôle du niveau d'huile du moteur électrique de traction",
    (
        "1340 - VHL HYBRIDE : Contrôle Etat des tuyaux refroidissement de la chaîne"
        " de traction"
    ),
    (
        "1350 - VHL HYBRIDE : Contrôle Etat des connecteurs, des câbles du circuit"
        " électrique"
    ),
    (
        "1360 - VHL HYBRIDE : Contrôle / nettoyage radiateurs de refroidis (chaîne"
        " de traction)"
    ),
    "1370 - VHL HYBRIDE : Contrôle de l'efficacité du reniflard, Nettoyage",
    "1380 - VHL HYBRIDE : Faire l'appoint d'huile du réducteur cumulatif",
    "1390 - VHL HYBRIDE : Contrôle de l'étanchéité du réducteur d'adaptation",
    "1400 - VHL HYBRIDE : Contrôle du bouchon de vidange magnétique",
    "1410 - VHL ELEC: Contrôle purge automatique de la condensation sur le séparateur",
    "1420 - VHL ELEC: Nettoyage séparateur de condensation",
    "1430 - VHL ELEC: Contrôle batterie(s) (voltage, fixations, protection ...)",
    "1440 - VHL ELEC: Contrôle du niveau d'électrolytique et appoint éventuel",
    "1450 - VHL ELEC: Nettoyage et contrôle des filtres de la ventilation forcée",
    "1460 - VHL ELEC: Contrôle visuel support avec guides",
    "1470 - VHL GNV : Contrôle vis de fixation protection chaleur turbocompresseur",
    "1480 - VHL GNV : Contrôle de l'étanchéité du circuit du ventilateur hydrostatique",
    "1490 - VHL GNV : Etanchéité conduites liquide chauff (régulateur pression gaz)",
    (
        "1500 - VHL GNV : Contrôle visuel du bon état du câblage du circuit"
        " électrique moteur"
    ),
    "1510 - VHL GNV : Diagnostic du système CNG moteur par outil de diagnostic",
    "1520 - VHL GNV : Contrôle état tuyaux flexibles cylindres commande freins",
    "1530 - VHL GNV : Contrôle intégrité des bagues des barres stabilisatrices",
    "1540 - VHL GNV : Contrôle de l'état des soufflets des suspensions pneumatiques",
    "1550 - VHL GNV : Contrôle de l'étanchéité du circuit pneumatique",
    "1560 - VHL GNV : Contrôle étanchéité hydraulique amortisseurs",
    "1570 - VHL GNV : Contrôle l'amortisseur et les fixations du stabilisateur",
    (
        "1580 - VHL GNV : Contrôle fixation flasques/supports arbre de"
        " transmission contrôle jeu"
    ),
    "1590 - VHL GNV : Contrôle de l'étanchéité du Circuit Refroid du moteur",
    "1600 - VHL GNV : Contrôle de l'étanchéité des fluides des groupes mécaniques",
    "1610 - VHL GNV : Contrôle de l'efficacité du reniflard de la BV mécanique",
    "1620 - VHL GNV : Contrôle du système de surpression CNG",
    "1630 - VHL GNV : Vérification du fonctionnement des capteurs de détection CNG",
    "1640 - VHLGNV : Circuit refroidissement: Mesure du PH liquide refroidissement",
]

if "selecionados" not in st.session_state:
    st.session_state.selecionados = []

if "form_ot" not in st.session_state:
    st.session_state.form_ot = "18909723"
    st.session_state.form_client = "Transdev Sud Ouest Essonne DSP24"
    st.session_state.form_type = "PRÉPARATION AUX MINES"
    st.session_state.form_date = datetime.now().strftime("%d/%m/%Y")
    st.session_state.form_chassis = "227531"
    st.session_state.form_immat = "EQ-300-KX"
    st.session_state.form_km = "272 288"
    st.session_state.form_pere = "122170"

if "modo_impressao" not in st.session_state:
    st.session_state.modo_impressao = False

if st.session_state.modo_impressao:
    if st.button("⬅️ Voltar ao Painel Principal"):
        st.session_state.modo_impressao = False
        st.rerun()

    st.markdown(
        """
        <style>
            .stApp { background-color: white !important; }
            header { visibility: hidden; }
        </style>
    """,
        unsafe_allow_html=True,
    )

    html_ficha = f"""
    <div style="background: white; padding: 20px; font-family: sans-serif; color: black; max-width: 800px; margin: auto;">
        <div style="display: flex; align-items: center; border-bottom: 2px solid #d32f2f; padding-bottom: 10px; margin-bottom: 15px;">
            <div style="font-size: 20px; font-weight: bold; color: #d32f2f;">FAST AUTO 91 — RAPPORT D'INTERVENTION</div>
        </div>
        <div style="font-size: 11px; color: #444; margin-bottom: 15px;">
            MÉCANIQUE V.L - P.L | Intervention sur site<br/>6 rue Gustave Madiot, 91070 Bondoufle
        </div>
        
        <table style="width: 100%; font-size: 11pt; border-collapse: collapse; margin-bottom: 20px;">
            <tr>
                <td style="padding: 4px 0;"><b>Client / Réseau :</b> {st.session_state.form_client}</td>
                <td style="padding: 4px 0;"><b>N° d'OT :</b> <span style="color: #d32f2f;">{st.session_state.form_ot}</span></td>
            </tr>
            <tr>
                <td style="padding: 4px 0;"><b>Type d'intervention :</b> {st.session_state.form_type}</td>
                <td style="padding: 4px 0;"><b>Date :</b> {st.session_state.form_date}</td>
            </tr>
            <tr>
                <td style="padding: 4px 0;"><b>Châssis (N° de parc) :</b> <b>{st.session_state.form_chassis}</b></td>
                <td style="padding: 4px 0;"><b>Équipement père :</b> {st.session_state.form_pere}</td>
            </tr>
            <tr>
                <td style="padding: 4px 0;"><b>Immatriculation / VIN :</b> {st.session_state.form_immat}</td>
                <td style="padding: 4px 0;"><b>Kilométrage :</b> {st.session_state.form_km}</td>
            </tr>
        </table>

        <h4 style="border-bottom: 1px solid #ccc; padding-bottom: 5px; margin-top: 20px;">Contrôles et Observations (Sélectionnés)</h4>
        
        <table style="width: 100%; border-collapse: collapse; font-size: 10pt; margin-top: 10px;">
            <thead>
                <tr style="background-color: #f2f2f2; border-bottom: 1px solid #ddd;">
                    <th style="border: 1px solid #ddd; padding: 8px; text-align: left; width: 60%;">Activités (Ce qu'il y a à faire)</th>
                    <th style="border: 1px solid #ddd; padding: 8px; text-align: center; width: 15%;">Fait ? ([ X ])</th>
                    <th style="border: 1px solid #ddd; padding: 8px; text-align: left; width: 25%;">Remarques / Observations</th>
                </tr>
            </thead>
            <tbody>
    """

    if st.session_state.selecionados:
        for item_text in st.session_state.selecionados:
            html_ficha += f"""
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px;">{item_text}</td>
                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;"></td>
                    <td style="border: 1px solid #ddd; padding: 8px;"></td>
                </tr>
            """
    else:
        html_ficha += """
                <tr>
                    <td colspan="3" style="border: 1px solid #ddd; padding: 12px; text-align: center; color: #666;">Aucun contrôle sélectionné.</td>
                </tr>
        """

    html_ficha += """
            </tbody>
        </table>

        <table style="width: 100%; margin-top: 40px; border-collapse: collapse;">
            <tr>
                <td style="border: 1px solid #bbb; padding: 10px; width: 48%; height: 60px; vertical-align: top; font-size: 10pt;">
                    <b>Visa du Technicien / Fast Auto 91</b>
                </td>
                <td style="width: 4%;"></td>
                <td style="border: 1px solid #bbb; padding: 10px; width: 48%; height: 60px; vertical-align: top; font-size: 10pt;">
                    <b>Visa du Client / Exploitation</b>
                </td>
            </tr>
        </table>
    </div>
    """

    components.html(html_ficha, height=900, scrolling=True)

    st.markdown(
        """
        <script>
            window.print();
        </script>
    """,
        unsafe_allow_html=True,
    )

else:
    col_esq, col_dir = st.columns([1, 1.3], gap="large")

    with col_esq:
        st.markdown("### 🔧 Fast Auto 91 — Sélection des Contrôles")

        if st.button("🔄 Réinitialiser la Fiche (Tout Effacer)", type="primary"):
            st.session_state.selecionados = []
            st.session_state.form_ot = ""
            st.session_state.form_chassis = ""
            st.session_state.form_immat = ""
            st.session_state.form_km = ""
            st.session_state.form_pere = ""
            st.rerun()

        with st.expander("📝 Informations Générales du Véhicule", expanded=True):
            st.session_state.form_ot = st.text_input(
                "N° d'OT / Intervention", st.session_state.form_ot
            )
            st.session_state.form_client = st.text_input(
                "Client / Réseau", st.session_state.form_client
            )
            st.session_state.form_type = st.text_input(
                "Type d'Intervention", st.session_state.form_type
            )
            st.session_state.form_date = st.text_input(
                "Date d'intervention", st.session_state.form_date
            )

            c1, c2 = st.columns(2)
            with c1:
                st.session_state.form_chassis = st.text_input(
                    "Châssis (N° de parc)", st.session_state.form_chassis
                )
                st.session_state.form_immat = st.text_input(
                    "Immatriculation / VIN", st.session_state.form_immat
                )
            with c2:
                st.session_state.form_km = st.text_input(
                    "Kilométrage", st.session_state.form_km
                )
                st.session_state.form_pere = st.text_input(
                    "Équipement père", st.session_state.form_pere
                )

        st.markdown("---")
        st.markdown("### ➕ Ajouter un service à la fiche")

        filtro_busca = st.text_input(
            "🔍 Rechercher un contrôle dans le catalogue...", ""
        )

        itens_filtrados = [
            item
            for item in catalogue_services
            if filtro_busca.lower() in item.lower()
            and item not in st.session_state.selecionados
        ]

        container_scroll = st.container(height=300)
        with container_scroll:
            if not itens_filtrados:
                st.info("Tous les services filtrés ont déjà été ajoutés.")
            for item in itens_filtrados:
                col_btn, col_txt = st.columns([1, 8])
                if col_btn.button("➕", key=f"add_{item}"):
                    st.session_state.selecionados.append(item)
                    st.rerun()
                col_txt.markdown(f"<small>{item}</small>", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 🗑️ Retirer de la fiche")
        if not st.session_state.selecionados:
            st.write("Aucun contrôle sélectionné.")

        for idx, item_sel in enumerate(st.session_state.selecionados):
            col_item, col_rem = st.columns([4, 1])
            col_item.text(f"• {item_sel[:30]}...")
            if col_rem.button("Retirer", key=f"rm_{idx}"):
                st.session_state.selecionados.pop(idx)
                st.rerun()

    with col_dir:
        if st.button(
            "🖨️ Générer la Fiche Propre pour Impression / PDF",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.modo_impressao = True
            st.rerun()

        st.markdown(
            "<div style='border: 1px solid #ccc; padding: 20px; background:"
            " white; border-radius: 5px;'>",
            unsafe_allow_html=True,
        )

        col_logo, col_info = st.columns([1, 3.5])
        with col_logo:
            try:
                st.image("input_file_8.png", width=95)
            except:
                st.write("🔧 **FAST AUTO**")

        with col_info:
            st.markdown(
                (
                    "<p style='font-size: 18px; font-weight: bold; color:"
                    " #d32f2f; text-transform: uppercase; margin-bottom: 0px;'>FAST"
                    " AUTO 91 — RAPPORT D'INTERVENTION</p>"
                ),
                unsafe_allow_html=True,
            )
            st.markdown(
                (
                    "<p style='font-size: 12px; color: #444; margin-bottom:"
                    " 10px;'>MÉCANIQUE V.L - P.L | Intervention sur site<br/>6"
                    " rue Gustave Madiot, 91070 Bondoufle</p>"
                ),
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
        <hr style='margin: 5px 0 10px 0;'>
        <table style='width: 100%; font-size: 10pt;'>
            <tr>
                <td><b>Client / Réseau :</b> {st.session_state.form_client}</td>
                <td><b>N° d'OT :</b> <span style='color: #d32f2f;'>{st.session_state.form_ot}</span></td>
            </tr>
            <tr>
                <td><b>Type d'intervention :</b> {st.session_state.form_type}</td>
                <td><b>Date :</b> {st.session_state.form_date}</td>
            </tr>
            <tr>
                <td><b>Châssis (N° de parc) :</b> <b>{st.session_state.form_chassis}</b></td>
                <td><b>Équipement père :</b> {st.session_state.form_pere}</td>
            </tr>
            <tr>
                <td><b>Immatriculation / VIN :</b> {st.session_state.form_immat}</td>
                <td><b>Kilométrage :</b> {st.session_state.form_km}</td>
            </tr>
        </table>
        <hr style='margin: 10px 0;'>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("#### Contrôles et Observations (Sélectionnés)")

        dados_tabela = []
        for i, item_text in enumerate(st.session_state.selecionados):
            dados_tabela.append({
                "Activités (Ce qu'il y a à faire)": item_text,
                "Fait ? ([ X ])": "",
                "Remarques / Observations": "",
            })

        if dados_tabela:
            df_exibicao = pd.DataFrame(dados_tabela)
            st.table(df_exibicao)
        else:
            st.warning(
                "Aucun contrôle ajouté pour le moment. Veuillez en sélectionner dans"
                " la colonne de gauche."
            )

        st.markdown(
            """
        <table style='width: 100%; margin-top: 25px; border-collapse: collapse;'>
            <tr>
                <td style='border: 1px solid #bbb; padding: 10px; width: 48%; height: 50px; vertical-align: top;'>
                    <b>Visa du Technicien / Fast Auto 91</b>
                </td>
                <td style='width: 4%;'></td>
                <td style='border: 1px solid #bbb; padding: 10px; width: 48%; height: 50px; vertical-align: top;'>
                    <b>Visa du Client / Exploitation</b>
                </td>
            </tr>
        </table>
        </div>
        """,
            unsafe_allow_html=True,
        )
