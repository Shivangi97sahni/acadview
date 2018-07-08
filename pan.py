#1
import pandas as pd
data = [['shivangi', 20, 'shivangisahni621@gmail.com', 8629805257],
        ['ishita', 21, 'ishitanarta@gmail.com', 9419276503]]

dataframe = pd.DataFrame(data=data, columns=['Name', 'Age', 'Email_id', 'Ph_no'])
print(dataframe)


#2
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv ")
a = df.head(5)
print(a)

b = df.head(10)
print(b)

c = df.describe()
print(c)

d = df.tail(5)
print(d)

second_col = df.iloc[:,2]
e = second_col.describe()
print(e)
