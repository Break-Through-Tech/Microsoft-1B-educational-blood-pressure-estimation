# CufflessAI: An Educational Blood Pressure Estimation

**Company / Org:** Microsoft  
**Challenge Advisor:** Wee Hyong Tok, weehyong@gmail.com   
**AI Studio Coach:** Anshul Rehpade, anshul.rehpade@breakthroughtech.org   
**Program:** Break Through Tech AI Studio - Fall 2026

---

## 🏢 About Microsoft
Microsoft creates platforms and tools powered by AI to deliver innovative solutions that meet the evolving needs of our customers. The technology company is committed to making AI available broadly and doing so responsibly, with a mission to empower every person and every organization on the planet to achieve more.

---

## 🎯 The Challenge

### Project Summary
This project enables a responsible AI and hands-on AI education by giving students experience with real-world sensor data, signal preprocessing, model evaluation, and the limitations of health-related machine learning prototypes.

A photoplethysmogram (PPG) enables one to track changes in blood volume under your skin. When the heart beats, there are changes to the amount of blood at your fingertip. This change in the amount of blood can affect the amount of light that passes through your finger. It’s similar to the pulse oximeters that you often experience in clinic, where the doctor/nurse clips a device on your finger.

In this project, you will use public physiological signal data, including photoplethysmography (PPG), electrocardiogram (ECG), and arterial blood pressure waveforms. There are different machine learning approaches that can be used to predict blood pressure from this signal. For example, you can use traditional feature engineering with classification/regression techniques, use a neural network to learn directly from the raw signal, or leverage Large Language models (LLMs) for the prediction.

The goal is to build an educational AI model that estimates systolic and diastolic blood pressure from pulse-signal features. 

### Success Criteria

Success should be measured by whether the team produces a complete, responsible, end-to-end ML prototype rather than by whether the model achieves clinical accuracy.

A successful outcome by December would include:   
- A reproducible Python notebook that loads the dataset, preprocesses signals, extracts features, trains models, and evaluates predictions.   
- At least two regression models compared against a naïve baseline.   
- Evaluation metrics reported for both SBP and DBP:   
- Evaluation using Mean Absolute Error, or MAE Root Mean Squared Error, or RMSE   
- A clear model comparison table.   
- Basic feature importance or interpretability analysis.   

### Stretch Goals
A demo app will be an excellent approach to demonstrate the AI model that you have built for blood pressure prediction.
Students can expand the scope of the project by building a [Replit app](https://replit.com/) with waveform plots, model confidence/error bands, feature explanations, and side-by-side model comparisons. 

You can also consider deploying the Replit app using [Rayfin](https://www.microsoft.com/en-us/microsoft-fabric/features/rayfin) on [Microsoft Fabric](https://www.microsoft.com/en-us/microsoft-fabric/features/rayfin)

The app can consider using signals from a phone-camera or webcam-based to extract the pulse of a user, and then feed this as inputs to the demo app for blood pressure prediction.

Examples 
* [smartphone based heart rate monitoring](https://medium.com/@bgallois/smartphone-based-heart-rate-monitoring-preprocessing-and-analysis-of-ppg-signals-de443473f529)


_Blood pressure category classification_
In addition to predicting SBP and DBP, students can classify readings into broad categories such as low, normal, elevated, or high blood pressure. This would add a classification component.

_Advanced modeling_
Students who progress quickly can try a simple 1D convolutional neural network that learns directly from raw PPG waveforms, instead of relying only on hand-crafted features.


### Project Milestones

Use these milestones to guide your work. Your team will create a **GitHub Projects board** to track tasks within each milestone.

| Month | Milestone | Key Activities |
|---|---|---|
| September | Data Understanding | Explore dataset, handle missing values, document findings |
| October | Model Development | Model training and evaluation |
| November | Evaluation & Presentation | Finalize model, prepare presentation, document results|

> **Note for the team:** Please create a GitHub Projects board in this repository to break these milestones into weekly tasks. Go to the **Projects** tab → **New project** → Choose **Board** → Add columns for each month.

---

## 📊 Dataset

**Name and Source:** Cuff-Less Blood Pressure Estimation   
**Format:** CSV, TSV, Matlab v7.3 mat file  
**Size:** 1gb to 5gb  
**Location:** https://archive.ics.uci.edu/dataset/340/cuff%2Bless%2Bblood%2Bpressure%2Bestimation


### Key Details
The UCI Cuff-less Blood Pressure dataset contains the data that we will use to train the AI model.
Each patient has a PPG signal and an ABP signal. We do not need to use the ECG signal for now.

When you download the files from the location above, the dataset is in Matlab's v7.3 mat file.
The dataset has a cell array of matrices, each cell is one record part.
In each matrix each row corresponds to one signal channel: 
- PPG signal, FS=125Hz;  photoplethysmograph from fingertip
- ABP signal, FS=125Hz; invasive arterial blood pressure (mmHg)
- ECG signal, FS=125Hz; electrocardiogram from channel II

To load the Matlab file, you can consider using scipy.io

Example on how to Load the. mat data file (update path to your local file location)

`mat_data = scipy.io.loadmat('part_1.mat')`

Few things to consider as you preprocess the data
- When you load the MATLAB files, you might want to consider processing them into 5-second windows. 
When you process the data into 5-second window, each window should contain 625 PPG samples as input and a pair of blood pressure values as labels.

- For each window, you can extract systolic and diastolic pressure from the ABP signal by finding the peaks (systolic) and valleys (diastolic). If a window contains noisy signals or physiologically impossible values, you can consider discarding the noisy data.

- After pre-processing all the data files, you will have a dataset with 10,000+ paired dataset. Each example is a 625-sample PPG window, and the systolic and diastolic labels.

## 📊 Feature Engineering
Feature engineering is an important step, as you work towards training an AI model. Feature engineering is the process of transforming raw data into relevant information (or features) that can be used as inputs towards training an AI model.

As you prepare for training, you might have to further pre-process the data to extract the relevant features needed to train the model.
NeuroKit2 is a good library that you can use to further clean the signal, find heartbeat peaks, and calculate meaningful measurements.
You can use NeuroKit to extract relevant morphological features from PPG signals that correlate with blood pressure. Some of these features include heart rate variability, pulse morphology, and more.

As you work through feature engineering to identify the relevant features, you should have about 10+ features and the label that corresponds to whether it is high blood or low blood pressure. 

---

## 🛠️ Suggested Approach

**ML Problem Type:** Classification,Regression,Time Series Analysis,Large Language Models (LLMs)/ Generative AI

**Recommended Libraries:**
- pandas, scikit-learn, scipy, Hugging Face
- NeuroKit [https://neuropsychology.github.io/NeuroKit/]

**Evaluation Metrics:**
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² score

As you explore different evaluation metrics that you can use to evaluate the AI model, think about whether there are other evaluation metrics that you can use.

---

## 📚 Resources to Get Started

The following resources will help your team understand the problem space and potential technical approaches for this project:

**Background Reading:**
- [Nature - A benchmark for machine-learning based non-invasive blood pressure estimation using photoplethysmogram](https://www.nature.com/articles/s41597-023-02020-6)
- [Estimating Blood Pressure from the Photoplethysmogram Signal and Demographic Features Using Machine Learning Techniques](https://pmc.ncbi.nlm.nih.gov/articles/PMC7309072/)
- [Exploring supervised machine learning models to estimate blood pressure using non-fiducial features of the photoplethysmogram (PPG) and its derivatives](https://pmc.ncbi.nlm.nih.gov/articles/PMC12511243/)
- [A continuous cuffless blood pressure measurement from optimal PPG characteristic features using machine learning algorithms](https://pmc.ncbi.nlm.nih.gov/articles/PMC10963242/)

**Technical Tutorials:**
- [Using SciPy to load MatLab files](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.loadmat.html)
- [Neurokit Examples](https://neuropsychology.github.io/NeuroKit/examples/)
- [pyPPG](https://pypi.org/project/pyPPG/)

**Code Examples:**
- [Kaggle - Blood Pressure Analysis](https://www.kaggle.com/code/stephenmugisha/bloodpressure-analysis)

**Other:**
- [Blood Pressure Estimation from PPG Signals - ICASSP 2020](https://www.youtube.com/watch?v=tZLotOFiyZ4)


*Feel free to explore beyond these, and share anything interesting you find with me!*

---

## 🤝 How We'll Work Together

**Official check-ins:** During our biweekly 45-minute AI Studio Lab Section meeting block (2nd and 4th week of every month)

 **Other ways to reach out to me with questions:** 
* Bi-weekly Lab Section check-ins
* Email if you have any questions - please copy your teammates and AI Studio Coach
* Request a team check-in on Zoom
* I will aim to respond within 48 hours. Please reach out to your AI Studio Coach with urgent questions.

**Recommended free coding / collaboration tools**
* [Visual Studio Code](https://code.visualstudio.com/)
* [Jupyter](https://jupyter.org/try)
  
  

---

## 🚀 Getting Started

1. **Review this overview document** and note any questions for our first meeting
2. **Begin reviewing the dataset** using the link above
3. **Read the GitHub Projects documentation** [here](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)

I’m excited to work with you!

---

## ❓ Questions?

Please bring any questions to our first meeting during the week of August 24th (Break Through Tech’s Bridge to Studio - Session C). 
