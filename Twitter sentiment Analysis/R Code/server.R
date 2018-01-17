#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#


library(RTextTools)
library(e1071)

library(SnowballC)

library(devtools)

library(curl)

library(shiny)
library(plyr)

library(dplyr)

library(stringr)

library(ggplot2)

library(wordcloud)

library(RCurl)

library(tm)

library(httk)
library(httpuv)
library(httr)
library(devtools)
library(ROAuth)
library(twitteR)
library(base64enc)


shinyServer(function(input, output) {
   
  
  observeEvent(input$submit, {
 
    #reading train files
    positive = readLines("/Users/ameyakulkarni/Downloads/Twitter-Sentimental-Analysis-master/happy.txt")
    negative = readLines("/Users/ameyakulkarni/Downloads/Twitter-Sentimental-Analysis-master/sad.txt")

   

    traindata <-c(positive,negative) #train file
    testdata <-readLines("/Users/ameyakulkarni/Documents/fetched.txt") #test file i.e fetched tweets

    dataset <-c(traindata,testdata)

    senti = c(rep("positive", length(positive) ),
                  rep("negative", length(negative)))
    sall=as.factor(senti)

    train_matty=create_matrix(dataset, language="english",
                            removeStopwords=FALSE, removeNumbers=TRUE,
                            stemWords=FALSE, tm::weightTfIdf)

    train_matty = as.matrix(train_matty)

    classifier = naiveBayes(train_matty[1:160,], as.factor(sall[1:160]))


    predictedsentiment = predict(classifier, train_matty[161:560,]);

    sentiment1 <- as.data.frame(predictedsentiment)
    
    #plotting final graph output
    finalplott<-qplot(sentiment1$predictedsentiment)+xlab("polarity")
    output$finalplott <-renderPlot(finalplott)
    
    
    #wordcloud code
    
    tw <-iconv(testdata, to = "utf-8", sub="")
    
    tcorpus = Corpus(VectorSource(tw))
    
    tdm1 = TermDocumentMatrix(tcorpus, control = list(removePunctuation = TRUE,stopwords = c("trump","president","Trump",stopwords("english")), removeNumbers = TRUE, tolower = TRUE))
    
    require(plyr)
    
    tdm_mat = as.matrix(tdm1)
    
    word_freqs = sort(rowSums(tdm_mat), decreasing=TRUE)
    
    dm1 = data.frame(word=names(word_freqs), freq=word_freqs) #we create our data set
    
    wc <-
    #output$wc <-renderPlot(wc)
    
    output$wc <-renderPlot({
      
      wordcloud(dm1$word, dm1$freq, random.order=FALSE, colors=brewer.pal(8, "Dark2"),max.words = 50) 
      
    })
    
  

    
    
  
    
    
    
  
    
    
    
    
  })
  
})
