# VoicePhishing Detection 
## Data
![20221214151149](https://user-images.githubusercontent.com/88221233/207520008-87038a07-61f8-4c66-b9f7-892a0d0ccb7a.png)

* The Financial Supervisory Service is disclosing about 300 voice data of voice phishing.
* We will use this data for voice phishing detection. 
* However, the number of data is too small, so a data augmentation method is needed.

## Data Augmentation Method
![그림1](https://user-images.githubusercontent.com/88221233/207520526-846342c7-f25a-4b4f-9aff-556c5849f041.png)

* We refer to the paper 'Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks'
* Above paper propose a method to augment text data through four methodologies, and it is said that these augmentation methods are effective through the above figure.
* Finally, 280 pieces of data are augmented to generate 800 pieces of training data and 180 pieces of test data.

## TextData to Time Series Data
* We can convert text data into time series data through keyword extraction, word embedding, and cosine similarity measurement.

### Keyword Extraction
* From the voice phishing data, keyBERT extracts some key keywords, and also considers keywords disclosed by the Financial Supervisory Service.

### FastText
* FastText is used as the word embedding methodology.
* Although the number of voice phishing data is small, the range of data of everyday conversation is very wide and the distribution is diverse, so FastText, which is robust to OOV problems, is used.
