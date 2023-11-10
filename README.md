# Suomi24 Corpus Analysis
 
In this project the Suomi24 corpus dataset from https://www.kielipankki.fi/corpora/suomi24/ was used. The parser of data was implemented and it generates a csv file for each year containing main threads, tiles, and datetimes. Then some corpus analysis tasks implemented to explore this dataset and to test the Heaps' law and Zipfs' law on this corpus. To use the code for the preprocessing part use the dataset_prepare.ipynb code. For processing each years data and see the implemented tasks use the tasks.ipynb code.


## Data description and data parsing

In this research the dataset which was used, was created by the data collection from Suomi24 platform. The dataset consists two parts, first part consists all the data from 2001 to 2017 \cite{suomi24-2001-2017-korp-v1-2_en} and the other one has the data from 2018 to 2020 \cite{suomi24-2018-2020-vrt_en}. In total there is 20 years of data available. The dataset consists of threads posts with their titles, comments, and so many features for each post like the authors name, datetime, topic name, and etc. The structure of the dataset is like YAML structure, but it is not a standard structure, So it needs a parser to parse and prepare the data.

The dataset is huge. In order to parse the data efficiently zip data parsed without extracting. Also, to process the data more resource efficiently threading used to distribute the tasks to many threads to do it in parallel. The dataset parsed line by line, the required features extracted from the dataset and saved for the furthur process. Only the main threads took into account for analysis as it is required in the project description.

## Data Preprocessing and Keyword Filtering
In the first step of preprocessing the numerical values, URL links, emojis, and all the punctuations were removed from the dataset. The methodology was the NLTK library for text processing, including tokenization and stemming, and employed a SnowballStemmer specific to the Finnish language to reduce words to their base forms. The objective of this method is to filter text data from a huge dataset, which represents threads in Soumi24, and extract threads that contain a predefined keyword, "ilmastonmuutos" (climate change). This method is particularly useful for isolating discussions and content related to environmental topics, specifically climate change. The output of this stage is a dataset which preprocessed and it contains the threads that contain the required keyword.

## Vocabulary Calculation
The method lies in the calculation of vocabulary size and total tokens for each year. This is achieved by employing the CountVectorizer from the scikit-learn library, which is used to transform the text data into a numerical format suitable for analysis. For each year, the total unique vocabulary size and the total number of tokens in the corresponding text data were calculated.

## Data Visualization
Matplotlib library is used to create the plots. For showing the evolution of vocabulary size on a yearly basis, the evolution of vocabulary size over the years using a bar plot was visualized. This allowed us to observe trends and patterns in vocabulary changes within the Suomi24 corpus from 2001 to 2020. 

## Assessing Vocabulary Growth and Heaps’ Law Fit Over Time
### Heaps' Law and Linear Regression:
Heaps' Law, as it was explained previously, was applied to model vocabulary growth. Linear regression was utilized to fit a model to the relationship between the logarithm of the vocabulary size and the logarithm of the number of tokens. 
 
It was investigated whether a parametric model, specifically Heaps law, could be fitted to describe this relationship. The process involved the utilization of confidence values to establish the upper and lower bounds of the curve fitting and to evaluate the goodness of fit. Our approach is inspired by established statistical methods such as spacy.stats.linregress.  

Confidence intervals are computed to estimate the range within which the vocabulary size is expected to fall outside the calculated upper and lower bounds for each case. Different confidence levels (e.g., 80\%, 85\%, 90\%, and 95\%) were considered, and prediction intervals were determined based on statistical analysis.  

## Analyzing Co-Occurring Words for Selected Keywords (2001-2020)
Identifying the ten most frequent co-occurring words for selected keywords across each year (2001-2020) was developed. The methodology involved tokenizing the discussion data, locating instances of the keywords, and extracting words within a three-word proximity. The context window is set to three units, and it captures the words surrounding the keyword in the text. A frequency distribution was used to tally these neighboring words, excluding the target keyword. It utilizes the NLTK library's FreqDist to compute word frequencies and ranks the top co-occurring words. These findings were visually represented through scatter plots, demonstrating co-occurring word patterns. 

## Visualization and Analysis of Temporal Evolution of Co-occurring Words 
The method focuses on examining and visually representing how the frequency of co-occurring words changes over time. A pivotal step in the method involves pivoting the DataFrame to reorganize the data for visualization purposes. A heatmap was generated to illustrate the temporal evolution of the ten most frequent co-occurring words. The heatmap provides a visual representation of word frequency changes over the years, with colors indicating the relative frequency levels. 

## Scoring and Ranking of Discussion Threads
A systematic approach was offered to evaluate and rank discussion threads over multiple years, focusing on the discussion content's token count. The discussion score was determined by counting the number of tokens in the discussion part of each thread. This step ensures that the process can evaluate and rank the threads based on their textual content. 

## Temporal Topic Modeling and Analysis of Textual Data
For the implementation of topic modeling, Latent Dirichlet Allocation (LDA) was applied to textual data over a range of years, with a primary focus on extracting and examining topics and their associated keywords. For each year, the method organizes documents, separates text data, and constructs a dictionary to represent the unique terms within the text data. A corpus is also formed by converting the documents into a bag-of-words representation.

## Sentiment-Enhanced Temporal Topic Modeling and Analysis of Textual Data
To sentiment Analysis, it was created a sentiment analyzer for the Finnish language using the AFINN lexicon. Each text, comprised of the thread title and content, was assigned a sentiment label (positive or negative) based on its sentiment score. Topic modeling was performed separately for positive and negative sentiments. For each year and sentiment category, an LDA topic model with two topics was created. The most representative keywords for each topic were extracted. One thing that needs mentioning is that the AFINN package which is installed by package installers like pip doesn`t support the finnish language so in order to use that we needed to utilize the latest update on its github page.
## The other state of the art methods
To use a state of the art method to achieve the specifications we could use Non-Negative Matrix Factorization(NMF) and also FinBERT which are the two state of the art methods and they can be used in the same way as the LDA method. The NMF method selected to be used in the corpus topic modeling and the topic of the threads for each year extracted like the other method. Two topics were extracted for each years corpus.






