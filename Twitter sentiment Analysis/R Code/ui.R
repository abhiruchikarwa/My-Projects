library(shiny)
library(RTextTools)
library(e1071)

library(SnowballC)

library(devtools)

library(curl)

library(sentiment)

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
# Define UI for application that draws a histogram


shinyUI(fluidPage(
  theme = "ext.css" ,
  
  
  # Application title
  
 
  
  titlePanel("Twitter Sentiment Analysis"),
  
  # Sidebar with a slider input for number of bins 
  sidebarLayout(
    sidebarPanel(
      
      #textInput("keyword", "Enter keyword to be searched", value = "enter keyword here", width = NULL, placeholder = NULL),
      actionButton("submit", "Analyze")
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      
      plotOutput("finalplott"),
      plotOutput("wc")
      
       
       
    )
  )
))
