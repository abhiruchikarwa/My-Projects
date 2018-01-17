#importing packages
library(RTextTools)
library(e1071)
library(SnowballC)
library(devtools)
library(curl)
library(twitteR)
library(ROAuth)
library(plyr)
library(dplyr)
library(stringr)
library(ggplot2)
library(wordcloud)
library(RCurl)
library(tm)
library(shiny)


#twitter credentials
api_key <- "jyNqDRY97sHuQ0bvcwl0a1CRn"

api_secret <- "74vzIBbJF62WBh99b33tbMFyVZq4u0YHSdTMh6oOnZeJaMTaaW"

access_token <- "163369996-kvEXKpI3n9q7XxOcxD2DOe1UGNZUZXADqLEei2aW"

access_token_secret <- "NQ2UwPeVTk2ZwNidPNIJgKrUkbi83wkfzVoUEPTd4g8TT"

setup_twitter_oauth(api_key,api_secret,access_token,access_token_secret)


#Getting command line arguments to get keyword
args=commandArgs(trailingOnly = TRUE)
kword <-args[1]


#Fetching tweets based on keyword
fetched_tweets<-searchTwitter(kword,n=400,lang = "en")

#Cleaning fetched tweets
fetched_txt = sapply(fetched_tweets, function(x) x$getText())

fetched_txt = gsub("(RT|via)((?:\\b\\W*@\\w+)+)", "", fetched_txt)

fetched_txt = gsub("@\\w+", "", fetched_txt)

fetched_txt = gsub("[[:punct:]]", "", fetched_txt)

fetched_txt = gsub("[[:digit:]]", "", fetched_txt)

fetched_txt = gsub("http\\w+", "", fetched_txt)

fetched_txt = gsub("[ \t]{2,}", "", fetched_txt)

fetched_txt = gsub("^\\s+|\\s+$", "", fetched_txt)

fetched_txt = gsub("^\\s*<U\\+\\w+>\\s*","",fetched_txt)

fetched_txt = gsub("[^\x20-\x7E]","",fetched_txt)

fetched_txt =gsub(kword,"",fetched_txt)

#Saving fetched tweets to a file
write.table(fetched_txt,"/Users/ameyakulkarni/Documents/fetched.txt",append = FALSE,quote = FALSE,sep = " ",row.names = FALSE)


#classifying code
# 
# positive = readLines("/Users/ameyakulkarni/Downloads/Twitter-Sentimental-Analysis-master/happy.txt")
# negative = readLines("/Users/ameyakulkarni/Downloads/Twitter-Sentimental-Analysis-master/sad.txt")
# 
# #trainset=c(positive,negative)
# 
# # test_mat=create_matrix(scan("/Users/ameyakulkarni/Documents/fetched.txt",sep = " ",what = 'character'),language="english",
# #                         removeStopwords=FALSE, removeNumbers=TRUE,
# #                         stemWords=FALSE, tm::weightTfIdf)
# 
# #test_mat = as.matrix(test_mat)
# 
# #dataset
# 
# traindata <-c(positive,negative)
# testdata <-readLines("/Users/ameyakulkarni/Documents/fetched.txt")
# 
# dataset <-c(traindata,testdata)
# 
# senti = c(rep("positive", length(positive) ),
#               rep("negative", length(negative)))
# sall=as.factor(senti)
# 
# train_matty=create_matrix(dataset, language="english",
#                         removeStopwords=FALSE, removeNumbers=TRUE,
#                         stemWords=FALSE, tm::weightTfIdf)
# 
# train_matty = as.matrix(train_matty)
# 
# classifier = naiveBayes(train_matty[1:160,], as.factor(sall[1:160]))
# 
# 
# predictedsentiment = predict(classifier, train_matty[161:560,]);
# 
# sentiment1 <- as.data.frame(predictedsentiment)
# 
# finalplott<-qplot(sentiment1$predictedsentiment)+xlab("polarity")
# finalplott

