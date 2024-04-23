# -*- coding: utf-8 -*-
"""LVADSUSR161_krithiksri(ia2).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yEQE-Rcxb-iG3bj1mqHQddcH74L2E3kl
"""

import pandas as pd
import numpy as np

#1
arithmatic=np.array([1,2,3,4,5])
mean_value=np.mean(arithmatic)
std_value=np.std(arithmatic)
min_value=np.min(arithmatic)
max_value=np.max(arithmatic)
sum_value=np.sum(arithmatic)
print("mean value",mean_value)
print("Standard value",std_value)
print("minimum value",min_value)
print("maximum value",max_value)
print("sum value",sum_value)

#2
health_data = np.array([[160, 70, 30],
                        [165, 65, 35],
                        [170, 75, 40]])
print("mean of the health:",health_data[0].mean())
print("standard deviation:",health_data[1].std())

#3
score_student=np.array([['s1',30,40,50,40],['s2',90,80,79,56]
                        ])
s1_avg=score_student[0,-3:].astype(int).mean()
s2_avg=score_student[1,-3:].astype(int).mean()
print("student 1:",s1_avg)
print("student 2:",s2_avg)

#4
sensor=np.linspace(15,25,24)
print(sensor)

#5
import numpy as np
daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])
window_size = 5
print(np.mean(daily_closing_prices))

#6
ml=np.arange(100)

matrix=np.array([[1,0.5],[0.5,2]])
matrix.var()

#7
properties_matrix = np.array([[[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]]])
print("dimension of the array:",np.ndim(properties_matrix))

#8
three_array=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(three_array)
print("above 5:",three_array[three_array>5])
np.where(three_array>5)

#9
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 45, 50, 55],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Boston'],
        'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']}

df=pd.DataFrame(data)
under_age=df[df['Age']<45]
final_dataset=under_age[under_age['Department']!='HR']
result=pd.DataFrame(final_dataset['Name'])
result['City']=pd.DataFrame(final_dataset['City'])
print(result)

#10
data = {'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
        'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Sales': [70000, 50000, 30000, 40000, 60000]}
sale=pd.DataFrame(data)
print(sale)
sale.groupby(['Department','Salesperson']).aggregate({'Sales':'mean'}).sort_values(by='Sales',ascending=False)

#11
data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}
supermarket=pd.DataFrame(data)
#print(supermarket)


fruit=supermarket[supermarket['Category']=='Fruit']
avg=fruit['Price'].mean()

print("average for fruit category:",avg)
fruit_avg=fruit[fruit['Price']>=avg]
final=fruit_avg[fruit_avg['Promotion']==False]
print(final)

#12
employee_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Manager': ['John', 'Rachel', 'Emily', 'Rachel']
}

# Dataset of employee project assignments
project_data = {
    'Employee': ['Alice', 'Charlie', 'Eve'],
    'Project': ['P1', 'P3', 'P2']
}
emp=pd.DataFrame(employee_data)
pro=pd.DataFrame(project_data)
pd.merge(emp,pro,how='left')

#13
sport=pd.read_csv("Q13_sports_team_stats.csv")
print(sport)
sport.groupby('TeamID').aggregate({'Wins':['count','sum']})

#14

customer=pd.read_csv("Q14_customer_purchases.csv")
#print(customer)

print("Total purchase amount:",customer['PurchaseAmount'].sum())
print("is there any null values?",customer.isnull().sum())
customer.groupby('CustomerID').aggregate({'PurchaseAmount':'sum'})

#15
student=pd.read_csv("Q15_student_grades.csv")
print(student)
student.groupby('Subject').aggregate({'Grade':'mean'}).sort_values(by='Grade',ascending=False)