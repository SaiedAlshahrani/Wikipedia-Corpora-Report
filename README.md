# Wikipedia Corpora Meta Report
We, in this repository, share with the community our Python scripts for the “**Wikipedia Corpora Meta Report**” as an online metadata report (dashboard), designed to shed light on how bots or humans generate or edit Wikipedia editions to provide the NLP community with detailed information (metadata) about each Wikipedia edition’s articles, enabling them to make informed decisions regarding using these Wikipedia articles for training their NLP tasks and systems. 

This dashboard interactively displays the metadata of each Wikipedia edition using sunburst visualization and provides users with the options to view the metadata in a tabular format and to download the displayed metadata as a CSV file. The dashboard is open-sourced on GitHub with an MIT license and publicly hosted on Streamlit Community Cloud at [https://wikipedia-corpora-report.app](https://wikipedia-corpora-report.streamlit.app/).

This dashboard was presented as a *transparency* tool in our **accepted** paper, [**Performance Implications of Using Unrepresentative Corpora in Arabic Natural Language Processing**](https://webspace.clarkson.edu/~alshahsf/unrepresentative_corpora.pdf), at [*The First Arabic Natural Language Processing Conference (ArabicNLP 2023)*](https://sites.google.com/view/wanlp2023), co-located with [EMNLP 2023](https://2023.emnlp.org/) in Singapore (hybrid conference), December 7, 2023.

### Local Run of Dashboard
The dashboard is publicly hosted online on Streamlit Community Cloud, yet if you desire to run the dashboard locally on your machine, follow these steps.

1- Clone the dashboard's GitHub repository to your machine. Use this command in your terminal:

```bash
git clone https://github.com/SaiedAlshahrani/Wikipedia-Corpora-Report.git
cd Wikipedia-Corpora-Report 
```

2- Download the required Python packages. Use this command in your terminal:

```bash
pip install -r requirements.txt
```

3- Run Streamlit local server. Use this command in your terminal:

```bash
streamlit run report.py
```


