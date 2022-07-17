##Load Require Library
library(tm)
library(SnowballC)
library(RColorBrewer)
library(wordcloud)
library(wordcloud2)
library (rtweet)

##Read the Data

comm<-read.csv("Bytime.csv", header = TRUE)
corpus <- VCorpus(VectorSource(comm))

#corpus [[1]][1]
inspect(corpus)

##Data Cleaning and wrangling

corpus <- tm_map(corpus,removeNumbers)
corpus<-tm_map(corpus,removeWords,stopwords("english"))
corpus<-tm_map(corpus,removePunctuation)
corpus<-tm_map(corpus,stripWhitespace)
 
#Word Frequency

cdm <- TermDocumentMatrix(corpus)
m <- as.matrix(cdm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v), freq=v)
head(d, 100)

wordcloud(words = corpus, min.freq = 1,
          max.words=500, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))


write.csv(d,"d.csv", row.names = TRUE)

csv_data<-read.csv("d.csv")
print(csv_data)



plot(x = csv_data$freq,
     y = csv_data$word,
     xlab = "freq",
     ylab = "words",
     col = "red",
     pch = 1,
     main = "freq vs words")

#csv_data<-read.csv("d.csv")
#library(ggplot2)

#ggplot(csv_data$freq,csv_data$word, 
 #       xlab  = "freq",
 #       ylab = "words")

