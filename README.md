# Wikipedia Corpora Meta Report
We, in this repository, share with the community our Python scripts for the “**Wikipedia Corpora Meta Report**” as an online metadata report (dashboard), designed to shed light on how bots or humans generate or edit Wikipedia editions to provide the NLP community with detailed information (metadata) about each Wikipedia edition’s articles, enabling them to make informed decisions regarding using these Wikipedia articles for training their NLP tasks and systems. 

This dashboard interactively displays the metadata of each Wikipedia edition using sunburst visualization and provides users with the options to view the metadata in a tabular format and to download the displayed metadata as a CSV file. The dashboard is open-sourced on GitHub with an MIT license and publicly hosted on Streamlit Community Cloud at [https://wikipedia-corpora-report.app](https://wikipedia-corpora-report.streamlit.app/).

This dashboard was presented as a *transparency* tool in our **accepted** paper, [**Performance Implications of Using Unrepresentative Corpora in Arabic Natural Language Processing**](https://webspace.clarkson.edu/~alshahsf/unrepresentative_corpora.pdf), at [*The First Arabic Natural Language Processing Conference (ArabicNLP 2023)*](https://sites.google.com/view/wanlp2023), co-located with [EMNLP 2023](https://2023.emnlp.org/) in Singapore (hybrid conference), December 7, 2023.

#### Local Run of Dashboard
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


#### BibTeX Citation:
```bash
@inproceedings{alshahrani-etal-2023-implications,
    title = "{{Performance Implications of Using Unrepresentative Corpora in Arabic Natural Language Processing}}",
    author = "Alshahrani, Saied and Alshahrani, Norah and Dey, Soumyabrata and Matthews, Jeanna",
    booktitle = "Proceedings of the The First Arabic Natural Language Processing Conference (ArabicNLP 2023)",
    month = dec,
    year = "2023",
    address = "Singapore (Hybrid)",
    publisher = "Association for Computational Linguistics",
    url = "https://webspace.clarkson.edu/~alshahsf/unrepresentative_corpora.pdf",
    doi = "#################",
    pages = "###--###",
    abstract = "Wikipedia articles are a widely used source of training data for Natural Language Processing (NLP) research, particularly as corpora for low-resource languages like Arabic. However, it is essential to understand the extent to which these corpora reflect the representative contributions of native speakers, especially when many entries in a given language are directly translated from other languages or automatically generated through automated mechanisms. In this paper, we study the performance implications of using inorganic corpora that are not representative of native speakers and are generated through automated techniques such as bot generation or automated template-based translation. The case of the Arabic Wikipedia editions gives a unique case study of this since the Moroccan Arabic Wikipedia edition (ARY) is small but representative, the Egyptian Arabic Wikipedia edition (ARZ) is large but unrepresentative, and the Modern Standard Arabic Wikipedia edition (AR) is both large and more representative. We intrinsically evaluate the performance of two main NLP upstream tasks, namely word representation and language modeling, using word analogy evaluations and fill-mask evaluations using our two newly created datasets: Arab States Analogy Dataset (ASAD) and Masked Arab States Dataset (MASD). We demonstrate that for good NLP performance, we need both large and organic corpora; neither alone is sufficient. We show that producing large corpora through automated means can be a counter-productive, producing models that both perform worse and lack cultural richness and meaningful representation of the Arabic language and its native speakers.",
}
```
