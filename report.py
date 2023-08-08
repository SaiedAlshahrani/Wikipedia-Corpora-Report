import pandas as pd
import ssl, warnings
import streamlit as st
import plotly.express as px

warnings.simplefilter("ignore", UserWarning)
warnings.simplefilter("ignore", FutureWarning)
pd.options.display.float_format = '{:.2f}'.format
ssl._create_default_https_context = ssl._create_unverified_context

st.set_page_config(page_title="Wikipedia Corpora Report", page_icon="https://webspace.clarkson.edu/~alshahsf/images/wikipedia1.png")

st.markdown("<h1 style='text-align: center';>Transparency in Wikipedia Corpora</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center';>A Metadata Report of How Wikipedia Corpora Are Generated and Edited</h5>", unsafe_allow_html=True)

st.markdown("##")

url = r'https://en.wikipedia.org/wiki/List_of_Wikipedias'
tables = pd.read_html(url)
dataframe = tables[4]

dataframe = dataframe[['Language', 'Wiki']]

labels = []
for i in range(dataframe.shape[0]):
    labels.append(f"{dataframe['Language'][i]} ({dataframe['Wiki'][i]})")

selected_language = st.selectbox("Select or Search for a Wikipedia language:", labels, placeholder="Select or Search for a Wikipedia language")
display_data_table = st.checkbox('Display data in a table.', value=False)

english__pages__content_pages__all_editors = pd.read_csv('en/en--pages--content-pages--all-editors--all.csv')
english__pages__content_pages__all_editors = english__pages__content_pages__all_editors.iloc[-1]
english__pages__content_pages__human = english__pages__content_pages__all_editors['total.user']+\
                                       english__pages__content_pages__all_editors['total.anonymous']
english__pages__content_pages__bots = english__pages__content_pages__all_editors['total.group-bot']+\
                                      english__pages__content_pages__all_editors['total.name-bot']

english__pages__non_content_pages__all_editors = pd.read_csv('en/en--pages--non-content-pages--all-editors--all.csv')
english__pages__non_content_pages__all_editors = english__pages__non_content_pages__all_editors.iloc[-1]
english__pages__non_content_pages__human = english__pages__non_content_pages__all_editors['total.user']+\
                                           english__pages__non_content_pages__all_editors['total.anonymous']
english__pages__non_content_pages__bots = english__pages__non_content_pages__all_editors['total.group-bot']+\
                                      english__pages__non_content_pages__all_editors['total.name-bot']

english__total_pages = english__pages__content_pages__human + english__pages__content_pages__bots +\
                       english__pages__non_content_pages__human + english__pages__non_content_pages__bots

english__pages__content_pages = english__pages__content_pages__human + english__pages__content_pages__bots 

english__pages__non_content_pages = english__pages__non_content_pages__human + english__pages__non_content_pages__bots

english__edits__content_pages__all_editors = pd.read_csv('en/en--edits--content-pages--all-editors--all.csv')
english__edits__content_pages__all_editors = english__edits__content_pages__all_editors.iloc[-1]
english__edits__content_pages__human = english__edits__content_pages__all_editors['total.user']+\
                                       english__edits__content_pages__all_editors['total.anonymous']
english__edits__content_pages__bots = english__edits__content_pages__all_editors['total.group-bot']+\
                                      english__edits__content_pages__all_editors['total.name-bot']

english__edits__non_content_pages__all_editors = pd.read_csv('en/en--edits--non-content-pages--all-editors--all.csv')
english__edits__non_content_pages__all_editors = english__edits__non_content_pages__all_editors.iloc[-1]
english__edits__non_content_pages__human = english__edits__non_content_pages__all_editors['total.user']+\
                                           english__edits__non_content_pages__all_editors['total.anonymous']
english__edits__non_content_pages__bots = english__edits__non_content_pages__all_editors['total.group-bot']+\
                                          english__edits__non_content_pages__all_editors['total.name-bot']

english__total_edits = english__edits__content_pages__human + english__edits__content_pages__bots +\
                       english__edits__non_content_pages__human + english__edits__non_content_pages__bots

english__edits__content_pages = english__edits__content_pages__human + english__edits__content_pages__bots 

english__edits__non_content_pages = english__edits__non_content_pages__human + english__edits__non_content_pages__bots

data = {'Wiki' : ['English (en)', 'English (en)', 'English (en)','English (en)', 'English (en)', 'English (en)', 'English (en)','English (en)'],
        'Metric' : ['Pages', 'Pages', 'Pages', 'Pages', 'Edits', 'Edits', 'Edits', 'Edits'],
        'Sub-Metric' : ['Articles', 'Articles',  'Non-Articles', 'Non-Articles', 'Articles', 'Articles',  'Non-Articles', 'Non-Articles'],
        'Editors' : ['Human', 'Bots', 'Human', 'Bots', 'Human', 'Bots', 'Human', 'Bots'],
        'Values' : [english__pages__content_pages__human, english__pages__content_pages__bots, 
                    english__pages__non_content_pages__human, english__pages__non_content_pages__bots,
                    english__edits__content_pages__human, english__edits__content_pages__bots, 
                    english__edits__non_content_pages__human, english__edits__non_content_pages__bots]}

english_data = pd.DataFrame(data)

fig = px.sunburst(data_frame=english_data, 
                  path=['Wiki','Metric', 'Sub-Metric', 'Editors'], 
                  values='Values', 
                  branchvalues="total",
                  color_discrete_sequence=['darkgray', 'black'],
                  template='xgridoff')

fig.update_traces(textinfo='label+percent parent')
fig.update_traces(hovertemplate="Label=%{label}<br>Value=%{value}<br>Parent=%{parent}</br>")
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
fig.update_layout(uniformtext = dict(minsize = 15))  
st.markdown("##") 
st.plotly_chart(fig, theme=None, use_container_width=True, config={'displayModeBar': False})

st.markdown("##")

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
                            <td style="text-align:center"; rowspan=8>English (en)</td>
                            <td style="text-align:center"; rowspan=4>Pages ({english__total_pages:,})</td>
                            <td style="text-align:center"; rowspan=2>Articles ({english__pages__content_pages:,})</td>
                            <td style="text-align:center">Human ({english__pages__content_pages__human:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center">Bots ({english__pages__content_pages__bots:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center"; rowspan=2>Non-Articles ({english__pages__non_content_pages:,})</td>
                            <td style="text-align:center">Human ({english__pages__non_content_pages__human:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center">Bots ({english__pages__non_content_pages__bots:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center"; rowspan=4>Edits ({english__total_edits:,})</td>
                            <td style="text-align:center"; rowspan=2>Articles ({english__edits__content_pages:,})</td>
                            <td style="text-align:center">Human ({english__edits__content_pages__human:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center"; >Bots ({english__edits__content_pages__bots:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center"; rowspan=2>Non-Articles ({english__edits__non_content_pages:,})</td>
                            <td style="text-align:center">Human ({english__edits__non_content_pages__human:,})</td>
                        </tr>
                        <tr>
                            <td style="text-align:center">Bots ({english__edits__non_content_pages__bots:,})</td>
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

        <div class="footer"> <p class="p1">© 2023 Saied Alshahrani</p>  </div>
"""
st.markdown(footer,unsafe_allow_html=True)  

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1.3rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)
