import ssl
import warnings
import datasets
import subprocess
import pandas as pd
import urllib.request
from time import sleep
import streamlit as st
from datetime import date
import plotly.express as px
from urllib.error import HTTPError


warnings.simplefilter("ignore", UserWarning)
warnings.simplefilter("ignore", FutureWarning)
pd.options.display.float_format = '{:.2f}'.format
ssl._create_default_https_context = ssl._create_unverified_context

st.set_page_config(page_title="Wikipedia Corpora Report", page_icon="https://webspace.clarkson.edu/~alshahsf/images/wikipedia1.png")

st.markdown("""
        <h1 style='text-align: center';>Wikipedia Corpora Meta Report</h1>
        <h5 style='text-align: center';>A Metadata Report of How Wikipedia Editions Are Generated and Edited</h5>
""", unsafe_allow_html=True)


def fetch_wikis_codes():
    try:
        urls = [r'https://en.wikipedia.org/wiki/Statistics_of_Wikipedias',
                r'https://meta.wikimedia.org/wiki/List_of_Wikipedias']

        for url in urls:
            try: tables = pd.read_html(url)
            except urllib.error.HTTPError: continue

            for i in range(len(tables)):
                dataframe = tables[i]
                columns = list(dataframe.columns.values)

                if(set(['Language', 'Wiki']).issubset(set(columns))):
                    wikis_codes = tables[i]
                    break

        wikis_codes = wikis_codes[['Wiki', 'Language']]
        wikis_codes = wikis_codes[wikis_codes["Language"].str.contains("(closed)") == False]
        wikis_codes = wikis_codes.set_index('Wiki').to_dict()['Language']
        return wikis_codes

    except:
        wikis_codes = {'en': 'English', 'ceb': 'Cebuano', 'de': 'German', 'sv': 'Swedish', 'fr': 'French', 'nl': 'Dutch', 'ru': 'Russian',
                       'es': 'Spanish', 'it': 'Italian', 'arz': 'Egyptian Arabic', 'pl': 'Polish', 'ja': 'Japanese', 'zh': 'Chinese', 'vi':
                       'Vietnamese', 'uk': 'Ukrainian', 'war': 'Waray', 'ar': 'Arabic', 'pt': 'Portuguese', 'fa': 'Persian', 'ca': 'Catalan',
                       'sr': 'Serbian', 'id': 'Indonesian', 'ko': 'Korean', 'no': 'Norwegian (Bokmål)', 'ce': 'Chechen', 'fi': 'Finnish', 'cs':
                       'Czech', 'tr': 'Turkish', 'hu': 'Hungarian', 'tt': 'Tatar', 'sh': 'Serbo-Croatian', 'ro': 'Romanian', 'zh-min-nan':
                       'Southern Min', 'eu': 'Basque', 'ms': 'Malay', 'eo': 'Esperanto', 'he': 'Hebrew', 'hy': 'Armenian', 'da': 'Danish', 'bg':
                       'Bulgarian', 'cy': 'Welsh', 'sk': 'Slovak', 'azb': 'South Azerbaijani', 'uz': 'Uzbek', 'et': 'Estonian', 'simple':
                       'Simple English', 'be': 'Belarusian', 'kk': 'Kazakh', 'min': 'Minangkabau', 'el': 'Greek', 'hr': 'Croatian', 'lt': 'Lithuanian',
                       'gl': 'Galician', 'az': 'Azerbaijani', 'ur': 'Urdu', 'sl': 'Slovene', 'lld': 'Ladin', 'ka': 'Georgian', 'nn': 'Norwegian (Nynorsk)',
                       'hi': 'Hindi', 'th': 'Thai', 'ta': 'Tamil', 'bn': 'Bengali', 'la': 'Latin', 'mk': 'Macedonian', 'zh-yue': 'Cantonese', 'ast':
                       'Asturian', 'lv': 'Latvian', 'af': 'Afrikaans', 'tg': 'Tajik', 'my': 'Burmese', 'mg': 'Malagasy', 'mr': 'Marathi', 'sq': 'Albanian',
                       'bs': 'Bosnian', 'oc': 'Occitan', 'te': 'Telugu', 'ml': 'Malayalam', 'nds': 'Low German', 'be-tarask': 'Belarusian (Taraškievica)',
                       'br': 'Breton', 'ky': 'Kyrgyz', 'sw': 'Swahili', 'jv': 'Javanese', 'lmo': 'Lombard', 'new': 'Newar', 'pnb': 'Western Punjabi', 'vec':
                       'Venetian', 'ht': 'Haitian Creole', 'pms': 'Piedmontese', 'ba': 'Bashkir', 'lb': 'Luxembourgish', 'su': 'Sundanese', 'ku': 'Kurdish (Kurmanji)',
                       'ga': 'Irish', 'szl': 'Silesian', 'is': 'Icelandic', 'fy': 'West Frisian', 'cv': 'Chuvash', 'ckb': 'Kurdish (Sorani)', 'pa': 'Punjabi', 'tl':
                       'Tagalog', 'an': 'Aragonese', 'wuu': 'Wu Chinese', 'diq': 'Zaza', 'io': 'Ido', 'sco': 'Scots', 'vo': 'Volapük', 'yo': 'Yoruba', 'ne': 'Nepali',
                       'ia': 'Interlingua', 'kn': 'Kannada', 'gu': 'Gujarati', 'als': 'Alemannic German', 'ha': 'Hausa', 'avk': 'Kotava', 'bar': 'Bavarian', 'crh':
                       'Crimean Tatar', 'scn': 'Sicilian', 'bpy': 'Bishnupriya Manipuri', 'qu': 'Quechua (Southern Quechua)', 'nv': 'Navajo', 'mn': 'Mongolian', 'xmf':
                       'Mingrelian', 'ban': 'Balinese', 'si': 'Sinhala', 'tum': 'Tumbuka', 'ps': 'Pashto', 'frr': 'North Frisian', 'os': 'Ossetian', 'mzn': 'Mazanderani',
                       'bat-smg': 'Samogitian', 'or': 'Odia', 'ig': 'Igbo', 'sah': 'Yakut', 'cdo': 'Eastern Min', 'gd': 'Scottish Gaelic', 'bug': 'Buginese', 'yi': 'Yiddish',
                       'sd': 'Sindhi', 'ilo': 'Ilocano', 'am': 'Amharic', 'nap': 'Neapolitan', 'li': 'Limburgish', 'bcl': 'Central Bikol', 'fo': 'Faroese', 'gor': 'Gorontalo',
                       'hsb': 'Upper Sorbian', 'map-bms': 'Banyumasan', 'mai': 'Maithili', 'shn': 'Shan', 'eml': 'Emilian-Romagnol', 'ace': 'Acehnese', 'zh-classical':
                       'Classical Chinese', 'sa': 'Sanskrit', 'as': 'Assamese', 'wa': 'Walloon', 'ie': 'Interlingue', 'hyw': 'Western Armenian', 'lij': 'Ligurian', 'mhr':
                       'Meadow Mari', 'zu': 'Zulu', 'sn': 'Shona', 'hif': 'Fiji Hindi', 'mrj': 'Hill Mari', 'bjn': 'Banjarese', 'mni': 'Meitei', 'km': 'Khmer', 'hak':
                       'Hakka Chinese', 'roa-tara': 'Tarantino', 'pam': 'Kapampangan', 'sat': 'Santali', 'rue': 'Rusyn', 'nso': 'Northern Sotho', 'bh': 'Bihari (Bhojpuri)',
                       'so': 'Somali', 'mi': 'Māori', 'se': 'Northern Sámi', 'myv': 'Erzya', 'vls': 'West Flemish', 'nds-nl': 'Dutch Low Saxon', 'dag': 'Dagbani', 'sc':
                       'Sardinian', 'ary': 'Moroccan Arabic', 'co': 'Corsican', 'kw': 'Cornish', 'bo': 'Lhasa Tibetan', 'vep': 'Veps', 'glk': 'Gilaki', 'tk': 'Turkmen', 'kab':
                       'Kabyle', 'gan': 'Gan Chinese', 'rw': 'Kinyarwanda', 'fiu-vro': 'Võro', 'ab': 'Abkhaz', 'gv': 'Manx', 'ug': 'Uyghur', 'nah': 'Nahuatl', 'zea': 'Zeelandic',
                       'skr': 'Saraiki', 'frp': 'Franco-Provençal', 'udm': 'Udmurt', 'pcd': 'Picard', 'mt': 'Maltese', 'kv': 'Komi', 'csb': 'Kashubian', 'gn': 'Guarani', 'smn':
                       'Inari Sámi', 'ay': 'Aymara', 'nrm': 'Norman', 'ks': 'Kashmiri', 'lez': 'Lezgian', 'lfn': 'Lingua Franca Nova', 'olo': 'Livvi-Karelian', 'mwl': 'Mirandese',
                       'stq': 'Saterland Frisian', 'lo': 'Lao', 'ang': 'Old English', 'mdf': 'Moksha', 'fur': 'Friulian', 'rm': 'Romansh', 'lad': 'Judaeo-Spanish', 'kaa': 'Karakalpak',
                       'gom': 'Konkani (Goan Konkani)', 'ext': 'Extremaduran', 'koi': 'Permyak', 'tyv': 'Tuvan', 'pap': 'Papiamento', 'av': 'Avar', 'dsb': 'Lower Sorbian', 'ln':
                       'Lingala', 'dty': 'Doteli', 'tw': 'Twi', 'cbk-zam': 'Chavacano (Zamboanga)', 'dv': 'Maldivian', 'ksh': 'Ripuarian', 'za': 'Zhuang (Standard Zhuang)', 'gag':
                       'Gagauz', 'bxr': 'Buryat (Russia Buriat)', 'pfl': 'Palatine German', 'lg': 'Luganda', 'szy': 'Sakizaya', 'pag': 'Pangasinan', 'blk': "Pa'O", 'pi': 'Pali',
                       'tay': 'Atayal', 'haw': 'Hawaiian', 'awa': 'Awadhi', 'inh': 'Ingush', 'krc': 'Karachay-Balkar', 'xal': 'Kalmyk Oirat', 'pdc': 'Pennsylvania Dutch', 'to':
                       'Tongan', 'atj': 'Atikamekw', 'tcy': 'Tulu', 'arc': 'Aramaic (Syriac)', 'mnw': 'Mon', 'jam': 'Jamaican Patois', 'shi': 'Shilha', 'kbp': 'Kabiye', 'wo':
                       'Wolof', 'anp': 'Angika', 'kbd': 'Kabardian', 'nia': 'Nias', 'nov': 'Novial', 'om': 'Oromo', 'ki': 'Kikuyu', 'nqo': "N'Ko", 'bi': 'Bislama', 'xh': 'Xhosa',
                       'tpi': 'Tok Pisin', 'tet': 'Tetum', 'ff': 'Fula', 'roa-rup': 'Aromanian', 'jbo': 'Lojban', 'fj': 'Fijian', 'kg': 'Kongo (Kituba)', 'lbe': 'Lak', 'ty': 'Tahitian',
                       'guw': 'Gun', 'cu': 'Old Church Slavonic', 'trv': 'Seediq', 'ami': 'Amis', 'srn': 'Sranan Tongo', 'sm': 'Samoan', 'mad': 'Madurese', 'alt': 'Southern Altai',
                       'ltg': 'Latgalian', 'gcr': 'French Guianese Creole', 'chr': 'Cherokee', 'tn': 'Tswana', 'ny': 'Chewa', 'st': 'Sotho', 'pih': 'Norfuk', 'rmy': 'Romani (Vlax Romani)',
                       'got': 'Gothic', 'ee': 'Ewe', 'pcm': 'Nigerian Pidgin', 'bm': 'Bambara', 'ss': 'Swazi', 'ts': 'Tsonga', 've': 'Venda', 'kcg': 'Tyap', 'chy': 'Cheyenne', 'rn':
                       'Kirundi', 'ch': 'Chamorro', 'gur': 'Frafra', 'ik': 'Iñupiaq', 'ady': 'Adyghe', 'pnt': 'Pontic Greek', 'guc': 'Wayuu', 'iu': 'Inuktitut', 'pwn': 'Paiwan', 'sg':
                       'Sango', 'din': 'Dinka', 'ti': 'Tigrinya', 'kl': 'Greenlandic', 'dz': 'Dzongkha', 'cr': 'Cree', 'ak': 'Akan'}
        return wikis_codes


def run_daemon(args):
    result = subprocess.run(args, capture_output=True, text=True)
    try: result.check_returncode()
    except subprocess.CalledProcessError as exception: raise exception


labels = []
wiki_codes = fetch_wikis_codes()
for key, value in wiki_codes.items():
    labels.append(f"{value} ({key})")

st.markdown("<br>",unsafe_allow_html=True)

selected_language = st.selectbox("Select or Search for a Wikipedia language:", labels, placeholder="Select or Search for a Wikipedia language")


@st.cache_data
def fetch_metadata_dataset():
        # HF_TOKEN = st.secrets["HF_TOKEN"]
        dataset = datasets.load_dataset("SaiedAlshahrani/Wikipedia-Corpora-Report", split="train")#, use_auth_token=HF_TOKEN)
        dataset = dataset.to_pandas()
        return dataset

dataset = fetch_metadata_dataset()

metadata = dataset[dataset['Wiki'] == selected_language]

retrieval_date = metadata['Retrieval-Date'].iloc[0]

now_date = date.today()
data_date = date(int(retrieval_date.split('-')[0]), int(retrieval_date.split('-')[1]), int(retrieval_date.split('-')[2]))
delta = now_date - data_date

# if delta.days > 45: run_daemon(["bash", "update-daemon.sh"])

pages_content_bots = metadata['Values'].iloc[0]
pages_content_humans = metadata['Values'].iloc[1]
pages_non_content_bots = metadata['Values'].iloc[2]
pages_non_content_humans = metadata['Values'].iloc[3]

edits_content_bots = metadata['Values'].iloc[4]
edits_content_humans = metadata['Values'].iloc[5]
edits_non_content_bots = metadata['Values'].iloc[6]
edits_non_content_humans = metadata['Values'].iloc[7]

pages_content_pages = pages_content_bots+pages_content_humans
pages_non_content_pages = pages_non_content_bots+pages_non_content_humans
total_pages = pages_content_pages+pages_non_content_pages

edits_content_pages = edits_content_bots+edits_content_humans
edits_non_content_pages = edits_non_content_bots+edits_non_content_humans
total_edits = edits_content_pages + edits_non_content_pages

wiki_metadata = pd.DataFrame(metadata).reset_index(drop=True)

col1 , cc, col2 = st.columns([1.5, 1.75, 1], gap="small")

with col1:
    display_data_table = st.checkbox(f'Display metadata in a table.', value=False)

with cc:
    st.markdown(f"<p style='color:lightgray;font-family:'IBM Plex Sans',sans-serif;font-size:18px;'> &#9432; Latest Metadata Update: {retrieval_date}</p>", unsafe_allow_html=True)

with col2:
    download_button = st.download_button(label="Download Metadata", data=wiki_metadata.to_csv().encode('utf-8'),
                                        file_name=f'{selected_language.split("(")[0].strip(" ")}-Metadata-{retrieval_date}.csv', mime='text/csv',)

fig = px.sunburst(data_frame=wiki_metadata,
                  path=['Wiki','Metric', 'Sub-Metric', 'Editors'],
                  values='Values',
                  branchvalues="total",
                  color_discrete_sequence=['darkgray', 'black'],
                  template='xgridoff')

fig.update_traces(textinfo='label+percent parent')
fig.update_traces(hovertemplate="Label=%{label}<br>Value=%{value}<br>Parent=%{parent}</br>")
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
# fig.update_layout(uniformtext=dict(minsize=12, mode='hide'))
fig.add_layout_image(dict(x=.430, y=.615, sizex=0.23, sizey=0.23, opacity=0.22, layer="below",
                    source="https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png"))

st.markdown("<br>",unsafe_allow_html=True)

st.plotly_chart(fig, theme=None, use_container_width=True, config={'displayModeBar': False})

# st.markdown("##")
# st.markdown("<br>",unsafe_allow_html=True)


if display_data_table:
    table_st_style = """
            <style>
                table {
                    border-collapse: collapse;
                    border: 1px solid black;
                    border-spacing: 0;
                    margin-left: 0;
                    margin-right: 0;
                    width: 100%;}

                page {
                    border-collapse: collapse;}

                td, th, tr {
                    border: 1px solid black;
                    padding: 0;}

                .contentTableHeader {
                    background-color: lightgray;
                    color: black;}
            </style>
            """
    st.markdown(table_st_style, unsafe_allow_html=True)

    st.markdown(f"""
                <table border="1" width="100%" cellpadding="0" cellspacing="0">
                    <thead class="contentTableHeader">
                        <tr>
                            <td style="text-align:center"><b>Wikipedia</b></td>
                            <td style="text-align:center"><b>Totals</b></td>
                            <td style="text-align:center"><b>Pages</b></td>
                            <td style="text-align:center"><b>Editors</b></td>
                        </tr>
                    </thead>
                    <tbody style="margin: 0;padding: 0">
                        <tr>
                            <td style="text-align:center"; rowspan=8>{selected_language}</td>
                            <td style="text-align:center"; rowspan=4>Pages ({total_pages:,})</td>
                            <td style="text-align:center"; rowspan=2>Articles ({pages_content_pages:,})</td>
                            <td style="text-align:center">Bots ({pages_content_bots:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center">Humans ({pages_content_humans:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center"; rowspan=2>Non-Articles ({pages_non_content_pages:,})</td>
                            <td style="text-align:center">Bots ({pages_non_content_bots:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center">Humans ({pages_non_content_humans:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center"; rowspan=4>Edits ({total_edits:,})</td>
                            <td style="text-align:center"; rowspan=2>Articles ({edits_content_pages:,})</td>
                            <td style="text-align:center">Bots ({edits_content_bots:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center"; >Humans ({edits_content_humans:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center"; rowspan=2>Non-Articles ({edits_non_content_pages:,})</td>
                            <td style="text-align:center">Bots ({edits_non_content_bots:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center">Humans ({edits_non_content_humans:,})</td>
                        </tr>
                    </tbody>
                </table>
                """, unsafe_allow_html=True)

fonts_style = """
            <style>
                    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@200&display=swap');
            </style>
            """
st.markdown(fonts_style, unsafe_allow_html=True)

hide_st_style = """
            <style>
                    MainMenu {visibility: hidden;}
                    header {visibility: hidden;}
                    footer {visibility: hidden;}
                    button[title="View fullscreen"]{visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

footer="""
        <style>
            .footer {
                    position: fixed;
                    left: 0;
                    bottom: 0;
                    width: 100%;
                    background-color: white;
                    color: #737373;
                    text-align: center;}

            .p1 {
                    font-family: 'IBM Plex Sans', sans-serif;
                    font-size: 12px}

        </style>

        <div class="footer"> <p class="p1">Copyright © 2023 by Saied Alshahrani<br>Hosted with Streamlit Community Cloud</p> </div>

"""
st.markdown(footer, unsafe_allow_html=True)

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.markdown("""
        <style>
        .br {
            display: block;
            margin: 0px 0;
            }
        </style>
        """, unsafe_allow_html=True)
