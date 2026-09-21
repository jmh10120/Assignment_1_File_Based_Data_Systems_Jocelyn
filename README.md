# Three Data Questions
# Question 1: Which genre has the highest average popularity?
track_genre  
pop-film    59.283  
Name: popularity, dtype: float64

Pop-film has the highest average popularity score at 59.283.

The dataset contains a categorical "track_genre" column and a numerical "popularity" column. This allows the tracks to be grouped by genre and the average popularity score to be calculated for each group.


# Question 2: Are explicit songs more popular on average than non-explicit songs?
explicit  
False    32.908179  
True     36.454191  
Name: popularity, dtype: float64

Explicit songs have a higher average popularity score of 36.45 compared to 32.91 for non-explicit songs in this dataset.

The dataset contains an "explicit" column that categorizes each track as explicit (True) or non-explicit (False), as well as a numerical "popularity" column. This allows the tracks to be grouped based on whether they are explicit and their average popularity scores to be compared.


# Question 3: Among explicit songs with a popularity score of 80 or higher, which genre is most common?
track_genre  
hip-hop    48  
Name: count, dtype: int64

Hip-hop is the most common genre among explicit songs with a popularity score of 80 or higher, with 48 tracks.

The dataset contains "explicit", "popularity", and "track_genre" columns for each track. This allows the data to be filtered using two conditions tracks that are explicit and tracks with a popularity score of at least 80, and then the remaining tracks can be counted by genre.


# What the Data Cannot Answer
One question I would like to answer is whether certain musical characteristics, such as high danceability or energy, cause a song to become more popular. Although the dataset contains measures of these characteristics as well as a popularity score, it cannot determine whether one variable causes another. Other factors that could influence a song's popularity, such as marketing, playlist placement, social media exposure, the existing popularity of the artist, and changes in listening behaviour over time, are not included in the dataset. Therefore, it would be misleading to assume that a song is popular because of a particular musical characteristic simply because the two appear to be related in the data.


# Why I Chose This Dataset
I chose the Spotify dataset because its structure fits the requirements of this assignment and provides many different variables that can be compared and analysed. I also enjoy listening to a wide variety of music genres, so I thought it would be interesting to explore the different characteristics of songs and genres in the dataset.
