# Predicting Mental Health-Related Dispositions and Sentences From Cook County Court Data

### Classifier developed by Kelsey Markey, Alene Rhea, Angela Teng, and Karmen Hutchinson<br/>New York University Center for Data Science, 2019

Abstract: People living with mental illness are especially likely to have encounters with the law; they need dedicated resources and thoughtful treatment as they make their way through the criminal justice system. This project aims to predict mental health-related dispositions and sentences from a set of judicial and case-based features available only at initiation. Early detection of people who are likely to be suffering from mental illnesses will enable governments and other institutions to provide appropriate support to these people as early as possible. The project underscores the need for disparate impact tracking in such systems.

<b> Relevant file descriptions</b>:
- MHI_building.ipynb- notebook that reads in the "Dispositions" and "Sentencing" files and indicates rows which should have a mental health indicator (MHI)
- Data_Prep.ipynb- notebook for data cleaning and prep, as well as feature engineering
- Data Analysis.ipynb- Notebook for data analysis (including distributions, base rates, etc.)
- Final_Data_Prep.py- functions for train/test/val splits and downsampling
- MHI_true.csv- File built from 'MHI_building.ipynb' containing case participant ids in the positive 'MHI' class
- Sentencing.csv- original Sentencing dataset downloaded from Cook County
- Dispositions.csv- original Disposition dataset downloaded from Cook County
- Initiation.csv- original Initation dataset downloaded from Cook County
- FINAL PAPER.pdf- Final project writeup, submitted 12/2019
- total_df.pckl.gz- Intermediate dataset read into modeling notebooks, categorical features one-hot encoded
- init_clean.pckl.gz- Intermediate dataset read into modeling notebooks, categorical features not one-hot encoded

Original Initiation, Sentencing, and Disposition datasets can also be downloaded from [this Google Drive folder](https://drive.google.com/drive/folders/1gL_7NqyI4gx68XVRWVSeLc-LVTdICb0-?usp=sharing)

<b>If you want to recreate this project you should run the notebooks in this order:</b>
1) MHI_building.ipynb
2) Data_Prep.ipynb
3) Data Analysis.ipynb
4) Modeling Notebook.ipynb
5) Final_Gradient_Boosting_Model.ipynb
