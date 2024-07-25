import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv('C:/AIML 4 SEM/DATA SCIENCE/MICRO PROJECT/healthcare-dataset-stroke-data.csv')
df.head()
df.tail()
df.sample()
df.shape
df.describe()
df.describe().T
df.info()
df.isna().sum()
df.isna()
df["id"].isna()
df['id'].isna().sum()
df.columns
df['id']
df.nunique()
df['id'].nunique()df['id'].nunique()
df['id'].describe()
df['id'].value_counts()
df[df['gender']=='Other']
plt.figure(figsize=(15,7))
sns.distplot(df['age'])
plt.title('Age Histogram')
plt.show()
plt.figure(figsize=(12,7))
sns.boxplot(df['avg_glucose_level'])
plt.title('Boxplot of age')
plt.show()
plt.figure(figsize=(12,7))
sns.boxplot(df['bmi'])
plt.title('BMI boxplot')
plt.show()
high_bmi=df[df['bmi']>=65]
high_bmi
plt.figure(figsize=(12,7))
plt.hist(x=df['avg_glucose_level'])
plt.title('AVG GLUCOSE LEVEL ')
plt.xlabel('avg_glucose_level')
plt.ylabel('stroke')
plt.show()
plt.figure(figsize=(5,5))
plt.hist(x=df["avg_glucose_level"])
plt.title("Average glucose level by stroke histogram")
plt.xlabel("avg_glucose_level")
plt.ylabel("stroke")
plt.show()
plt.figure(figsize=(12,7))
plt.hist(x=df['bmi'])
plt.title('bmi using stroke')
plt.xlabel('bmi')
plt.ylabel('stroke')
plt.show()
plt.pie(df['ever_married'].value_counts(),labels=df['ever_married'].unique(),autopct='%1.1f%%')
plt.title('pie')
plt.pie(df['work_type'].value_counts(),labels=df['work_type'].unique(),autopct='%1.1f%%')
plt.title('work type')
plt.pie(df['Residence_type'].value_counts(),labels=df['Residence_type'].unique(),autopct='%1.1f%%')
plt.title('..');
plt.pie(df['smoking_status'].value_counts(),labels=df['smoking_status'].unique(),autopct='%1.1f%%')
plt.title('..');
plt.figure(figsize=(12,7))
plt.hist(x=df['avg_glucose_level'])
plt.title('...');
plt.xlabel('avg_glucose_level')
plt.ylabel('gender')
plt.show()
ax=plt.scatter(data=df,x='avg_glucose_level',y='bmi',marker='+')
plt.title('..');
df.groupby(['hypertension','heart_disease'])[['stroke']].sum()
stroke=df[df['stroke']==1]
stroke.head()
stroke['stroke'].count()
df.corr()
plt.figure(figsize=(12,7))
heatmap=sns.heatmap(df.corr(),vmin=-1,vmax=1,annot=True,cmap=sns.color_palette("vlag"))
heatmap.set_title('correlation matrix');
plt.figure(figsize=(16, 9))
heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True, cmap=sns.color_palette("vlag"))
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':14});
