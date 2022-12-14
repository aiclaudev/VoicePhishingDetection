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

### Cosine Similarity
* Cosine similarity is the most frequently used similarity to compare token similarities in the field of NLP.

## VoicePhishing Data and Normal Data Visualization
![그림2](https://user-images.githubusercontent.com/88221233/207528354-f986bec6-50ae-43bb-a6b2-78e00ec470b9.png)
* Blue line is Voicephishing data, and Red line is normal data 
* We can confirm that the voice phishing data has higher average values and higher variability than normal data.
* However, both data are too volatile, so EWMA is used to reduce for this.

## EWMA
![20221214141602](https://user-images.githubusercontent.com/88221233/207528743-5bf2c613-5e23-4a5a-b1d6-cc27e160325f.png)
* EWMA is an abbreviation for Exponentially Weighted Moving Average, which is a method of calculating the average of values ​​within a specific range by considering weights.
* Volatility can be reduced using EWMA, which is derived by the equation below.

![20221214141725](https://user-images.githubusercontent.com/88221233/207529024-c55fbd45-b0f1-4bf4-97ee-c3b70cb40c11.png)

![20221214141732](https://user-images.githubusercontent.com/88221233/207529181-3e880e45-4260-4d0c-b65a-d48a5619e11b.png)

* The larger the beta, the lower the volatility due to the influence of the previous values. The smaller the beta, the weaker the effect of the current value than the influence of the previous values, so the lower the volatility.

## Feasibility of using EWMA for current data
![20221214142619](https://user-images.githubusercontent.com/88221233/207529363-f5807794-6d28-4277-81b9-dfc2dd2ec936.png)
* EWMA is useful for detecting small shifts. 
* In general, it can be assumed that a value higher than 1.5 sigma is a large shift, and a value of 0.5 sigma is a small shift.
* As can be seen in the figure above, the average difference between the average of the voice phishing data and the average of the normal data is not more than 1.5 times greater than the sigma of the two data.
* So we can use EWMA

## Evaluation metrics
* We use Accuracy, Recall, Predicision and ARL1, ARL0
* ARL1 : Average number of information extractions it took to raise an alarm when the process actually got out of control
* ARL0 : Average number of information extractions until a false alarm is issued when the process is under normal control contitions
* Adjusting the threshold to lower ARL1 and increase ARL0 lowers accuracy, recall, and precision accordingly.
* Accuracy, recall, and precision can be increased as much as possible, but our main purpose is to reduce ARL1 and lower ARL0.

## Performance
![20221214161547](https://user-images.githubusercontent.com/88221233/207530263-bd3ccea0-3e38-4f99-9fa0-8dd3c2b6d74c.png)

## Reference
* Data source : https://www.fss.or.kr/fss/main/main.do
* Data augmentation method : 'Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks'


