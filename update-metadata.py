import selenium
import os, warnings
from time import sleep
import pandas as pd, ssl
from selenium import webdriver

warnings.simplefilter("ignore", UserWarning)
warnings.simplefilter("ignore", FutureWarning)
pd.options.display.float_format = '{:.2f}'.format
ssl._create_default_https_context = ssl._create_unverified_context

def fetch_wikis_codes():
    try:
        url = r'https://en.wikipedia.org/wiki/List_of_Wikipedias'
        tables = pd.read_html(url)
        
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
    
    except KeyError:
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
        

def fetch_wiki_metadata(wiki, metric, submetric, timeout):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", f"{os.getcwd()}")
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
    driver = webdriver.Firefox(options=options, firefox_profile=profile, executable_path='geckodriver', service_log_path=os.devnull)

    if metric == 'pages':
        base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/content/pages-to-date/full|table|'

    elif metric == 'edits':
        base_url = f'https://stats.wikimedia.org/#/{wiki}.wikipedia.org/contributing/edits/full|table|'

    parameters = f'1-month|editor_type~anonymous*group-bot*name-bot*user+(page_type)~{submetric}|monthly'
    request_url = "".join([base_url, parameters])

    driver.implicitly_wait(3)
    driver.get(request_url)
    driver.page_source

    sleep(timeout)

    csvFilename = f"{wiki}--{metric}--{submetric}.csv"
    csvFilename = csvFilename.replace(' ','-')
    driver.find_element_by_class_name("ui.icon.button.tooltipped.tooltipped-n").click()
    sleep(3) ; os.rename("undefined.csv", csvFilename)

    driver.close()
    driver.quit()

    print(f'    [+] Metadata Exported to `{wiki}/{csvFilename}`.')
    
    return csvFilename


wiki_codes = fetch_wikis_codes()
labels = []
for key, value in wiki_codes.items():
    labels.append(f"{value} ({key})")
    
wikis = list(wiki_codes.keys())
metrics = ['pages', 'edits']
submetrics = ['content', 'non-content']

timeout = 3
counter = 1

for wiki in wikis:

    print(f'{counter}## {wiki_codes[wiki]} Wikipedia Files:')
    if not os.path.exists(f'{wiki}'): os.makedirs(f'{wiki}')
    if not os.path.exists('all-metadata'): os.makedirs('all-metadata')

    for metric in metrics:
        
        for submetric in submetrics:
            
            try: 
                csvFilename = fetch_wiki_metadata(wiki, metric, submetric, timeout)
                dataframe = pd.read_csv(csvFilename).iloc[-1]
                
            except selenium.common.exceptions.ElementClickInterceptedException:
                dataframe = pd.read_csv(fetch_wiki_metadata(wiki, metric, submetric, timeout*2)).iloc[-1]
                timeout *= 2

            retrieval_date = pd.to_datetime(dataframe['timeRange.end']).strftime('%Y-%m-%d')

            if metric == 'pages':
                if submetric == 'content':
                    pages_content_bots = dataframe['total.group-bot']+dataframe['total.name-bot']
                    pages_content_humans = dataframe['total.user']+dataframe['total.anonymous']
                elif submetric == 'non-content':
                    pages_non_content_bots = dataframe['total.group-bot']+dataframe['total.name-bot']
                    pages_non_content_humans = dataframe['total.user']+dataframe['total.anonymous']
                else: print(f'Error: this submetric: {submetric} is not supported!')
            
            elif metric == 'edits':
                if submetric == 'content':
                    edits_content_bots = dataframe['total.group-bot']+dataframe['total.name-bot']
                    edits_content_humans = dataframe['total.user']+dataframe['total.anonymous']
                elif submetric == 'non-content':
                    edits_non_content_bots = dataframe['total.group-bot']+dataframe['total.name-bot']
                    edits_non_content_humans = dataframe['total.user']+dataframe['total.anonymous']
                else: print(f'Error: this submetric: {submetric} is not supported!')
            
            else: print(f'Error: this metric: {metric} is not supported!')
            
            os.system(f'mv {wiki}--{metric}--{submetric}.csv {wiki}/{wiki}--{metric}--{submetric}.csv')
            
    selected_language = f'{wiki_codes[wiki]} ({wiki})'

    metadata = {'Wiki' : [selected_language, selected_language, selected_language, selected_language, 
                          selected_language, selected_language, selected_language,selected_language],
                
                'Metric' : ['Pages', 'Pages', 'Pages', 'Pages', 'Edits', 'Edits', 'Edits', 'Edits'],
                
                'Sub-Metric' : ['Articles', 'Articles',  'Non-Articles', 'Non-Articles', 
                                'Articles', 'Articles',  'Non-Articles', 'Non-Articles'],
                
                'Editors' : ['Bots', 'Humans', 'Bots', 'Humans', 'Bots', 'Humans', 'Bots', 'Humans'],
                
                'Values' : [pages_content_bots, pages_content_humans, pages_non_content_bots, pages_non_content_humans, 
                            edits_content_bots, edits_content_humans, edits_non_content_bots, edits_non_content_humans]}

    wiki_metadata = pd.DataFrame(metadata)
    wiki_metadata['Retrieval-Date'] = retrieval_date
    wiki_metadata.to_csv(f'{wiki_codes[wiki].replace(" ","-")}--Wikipedia--Metadata.csv', index=False)
    
    os.system(f'mv {wiki} all-metadata/')
    counter = counter + 1
    sleep(1)
    break
