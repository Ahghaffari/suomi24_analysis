# Suomi24 Corpus Analysis
 
In this project the Suomi24 corpus datset from https://www.kielipankki.fi/corpora/suomi24/ was used. The parser of data was implemented and it generates a csv file for each year containing main threads, tiles, and datetimes. Then some corpus analysis tasks implemented to explore this dataset and to test the Heaps' law and Zipfs' law on this corpus. To use the code for the preprocessing part use the dataset_prepare.ipynb code. For processing each years data and see the implemented tasks use the tasks.ipynb code.


### section 3:
we created a line plot with the years on the x-axis and the vocabulary size for each year on the y-axis. this plot shows us how the vocabulary size has changed over time.

#question 4:
analyze the evolution of vocab size with respect to the number of tokens over years .  considering Heaps' law and confidence intervals for this.
 The script did this by separating the data into different years and calculating vocabulary size and token counts for each year. It then fits a linear regression model to the log-transformed data to estimate the relationship between tokens and vocab size. Confidence intervals are calculated to understand the bounds of this connection. The script visualizes this data with graphs for each year and various confidence levels, allowing us to determine how well Heaps' law fits  vocab data and identify points outside the confidence bounds.


#section 5:
we created a scatter plot that visualizes the co-occurring words for specific keywords across different years. It does this by iterating through a dictionary called results, where each keyword is associated with a list of co-occurring words for each year. For each keyword and year combination, the code checks if there are co-occurring words available . If co-occurring words exist, it extracts the year and frequency of occurrence of these words and plots them as dots on the graph. The x-axis represents the years, and the y-axis represents the frequency of the co-occurring words. The size of the dots is proportional to the frequency of the words. By creating this scatter plot,we observe the evolving patterns of word co-occurrence over different years and keywords, providing insights into language trends and usage.


Section 6:
 we created a stacked bar chart to display the annual evolution of the ten most frequent co-occurring words in the dataset. The chart provides a visual representation of how the prevalence of these words changed over the years, allowing for a quick understanding of evolving themes and trends within the Suomi24 community.

section 7:
This script is designed to investigate threads that generate substantial discussion within each year of a given dataset. It accomplishes this by first tokenizing and counting the number of tokens in the discussion part of each thread's title. The result is a table showing the yearly evolution of discussion tokens. It then identifies the top 5 ranked threads with the most discussion tokens in each year and records this information. However, the distinguishing feature of this script is that it enables manual exploration of the top threads. After identifying these threads, the script facilitates the process of reading and manually recording perceptions and understandings of the content within each of these threads. This human-augmented analysis is essential for gaining insights into the most engaging and important discussions across different years, making it a valuable tool for content understanding and trend monitoring.


#section 8
 This script covers several key tasks, including data preprocessing, topic modeling using Latent Dirichlet Allocation (LDA), data storage in an SQLite database, and export of results to an Excel file. The code ensures the proper creation of the database table and handles year-wise topic modeling, with each year's results stored in the database. Finally, the script extracts the data from the database and exports it into an Excel file. To address potential module-related errors, necessary packages like "openpyxl" and others should be installed in your Python environment, ensuring a successful execution of the code. The tokenize_and_preprocess function was introduced for text preprocessing, incorporating tokenization, lowercase conversion, punctuation removal, and stopword elimination. 






