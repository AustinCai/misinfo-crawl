# Fake Hydroxychloroquine News Scraper
Author: Austin Cai<br/>
August 2, 2020<br/>
Completed as a recruiting programming assignment for TrustLab<br/>

### Strategy:
I compiled a list of news articles with hydroxychloroquine their titles from known right-wing news websites, and generated bagged word embeddings for those titles. Then, I created two artifical "titles" that I called the target and the anti_target. For the target, I concatenated a selection of actual titles that I would like my scraper to classify as fake news, and for the anti_target I concatenated a selection of actual titles I would like my scraper to ignore. Then, I found the bagged embeddings closest to the embedding of my target, while excluding too close to my anti_target. 

### How I evaluated whether an article "promoted hydroxychloroquine as a cure":
I considered articles that cite doctors, studies, or non-political testimonials to proclaim the effectiveness of hydroxychloroquine as "promoted hydroxychloroquine as a cure" and designed my scraper to find them. I consiered articles that report on the political debate around hydroxychloroquine, however misleading or right-wing, as not "promoted hydroxychloroquine as a cure" and designed my scraper to ignore them. For example, "Dr. Praises Hydroxychloroquine For Coronavirus: ‘Very Ill’ To ‘Basically Symptom Free’ In Hours" would be caught by my scraper, "Alyssa Milano Floats Impeachment over Trump Pushing Hydroxychloroquine" would not be caught. Note that this is a necessarly fuzzy definition, as some articles like "Robert Wilkie Blasts Phony Media on Hydroxychloroquine Study" fall in between. 

### Process:
I spent about 90 minutes before writing real code experimenting with cdx_toolkit. I also experimented with a GUI tool called Common Crawler, but that turned out to be a dead end. My first idea was to use sentiment analysis on article titles, and then use that sentiment, along the title, author, date of publication, etc. as features for a rule-based classifier. However, I realized it would be difficult to extract this structured data from so many different websites. Moreover, I realized that any rule-based classifiers I could come up with within 6 hours would be essentially arbitrary. This inspired me to use word vector distances as the "rule" by which I would make classifcation decsions off of. 

### Extensions - improvements I would make if given more time:
* I limited the scraped articles from each website to relatively small number to speed up runtime (even so, it took me several hours just to load the urls wit cdx_toolkit). I would increase this number to perform a more exhaustive scrape. 
* My target and anti_target were created somewhat arbitrarily, due to the time constraints of this problem. In the future I would try different ways to formulate my target/anti_target and compare their performance. 
* I would run unsupervised clustering algorithms on my article title embeddings to explore the natural structure of these article titles, and use my findings to inform the design of my scraper. 
* Exploring whether concatonation (and thus bagging of all lot of words) is an effective strategy for generating my target and anti_target. It cold be the case that, because my concatonated target/anti_targets are much longer than normal article titles, the embeddings average each other out.  
* More extensive testing of my target/anti_target strategy, which could potentially be memorizing the articles titles I concatonated to create them. Given more time, explore how my method generalizes to articles from diverse sources. 
* I observed that an article's distance from the target and anti_target are often quite similar. This is likely because word2vec embeddings (which are broadly trained) cannot effectively distinguish between my article set, which are all right-wing commentary involving hydroxychloroquine. Given more time and resources, I would retrain the word2vec embeddings on right wing articles commentating on hydroxychloroquine.
* Integrate other features besides the title, such as sentiment, publication date, author, and text, into my decision to label articles as fake news. 
