# suomi24_analysis
 



#section 3:
we created a line plot with the years on the x-axis and the vocabulary size for each year on the y-axis. this plot shows us how the vocabulary size has changed over time.

#question 4:
analyze the evolution of vocab size with respect to the number of tokens over years .  considering Heaps' law and confidence intervals for this.
 The script did this by separating the data into different years and calculating vocabulary size and token counts for each year. It then fits a linear regression model to the log-transformed data to estimate the relationship between tokens and vocab size. Confidence intervals are calculated to understand the bounds of this connection. The script visualizes this data with graphs for each year and various confidence levels, allowing us to determine how well Heaps' law fits  vocab data and identify points outside the confidence bounds.


#section 5:
we created a scatter plot that visualizes the co-occurring words for specific keywords across different years. It does this by iterating through a dictionary called results, where each keyword is associated with a list of co-occurring words for each year. For each keyword and year combination, the code checks if there are co-occurring words available . If co-occurring words exist, it extracts the year and frequency of occurrence of these words and plots them as dots on the graph. The x-axis represents the years, and the y-axis represents the frequency of the co-occurring words. The size of the dots is proportional to the frequency of the words. By creating this scatter plot,we observe the evolving patterns of word co-occurrence over different years and keywords, providing insights into language trends and usage.