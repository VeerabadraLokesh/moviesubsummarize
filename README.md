# Movie Summarization based on Subtitles
### CS2731 Intro to NLP
### Prof: Michael Miller Yoder
#### Team: Lokesh Paturu, Shuhao Yu, Vincent Yang

### Dataset:
Download [Subtitles and Summary Dataset](https://drive.google.com/file/d/1P12oN9SrbSxJavZvXS3FVHQYDLm6dMHa/view?usp=sharing) using this link. Extract the dataset in the directory where code is present.
<br/>
Run jupyter notebook and `load_data.ipynb` to load the dataset and get the statistics for the data.


### Train the Model

Run `data_preporcess.ipynb` to process csv data from the `load_data.ipynb` to modulates the training data for bert summerization model. The output is a CSV file.

Run `data_summarization.ipynb` to load the outputs csv file from the `data_preprocess.ipynb`, it will output the results of subtitles ranking.


### Evaluation


### Data sources
Subtitles are downloaded from [opensubtitles.org](https://www.opensubtitles.org/)
<br />
Movie summaries source: [CMU Movie Summary Corpus](https://www.cs.cmu.edu/~ark/personas/)
