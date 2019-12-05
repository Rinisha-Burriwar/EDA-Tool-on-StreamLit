import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image,ImageFilter,ImageEnhance,ImageTk



# image = Image.open("D://Engagement2/backgrounds/500x400.png")
# backgroundImage=ImageTk.PhotoImage(image)

# st.title("Exploratory Data Analysis App")
# st.subheader("EDA Web App with Streamlit")

html_temp = """
	<div style="background-color:tomato;border-radius: 25px;"><p style="color:white;font-size:70px;padding:10px"><center>Exploratory Data Analysis</center></p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)


html_temp = """
	<div style="background-color:purple;"><p style="color:white;font-size:40px;padding:10px"><center>Add File Path</center></p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)

filename = st.text_input('Enter a file path:')
def read_data(filename):
    with open(filename) as input:
        df = pd.read_csv(os.path.join(filename))
    return df
        

# Show Dataset

html_temp = """
	<div style="background-color:purple;"><p style="color:white;font-size:40px;padding:10px"><center>Statistical Analysis of Data</center></p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)

if st.checkbox("Preview DataFrame"):
	data = read_data(filename)
	if st.button("Head"):
		st.write(data.head())
	if st.button("Tail"):
		st.write(data.tail())
	else:
		st.write(data.head(2))

# Show Entire Dataframe
if st.checkbox("Show All DataFrame"):
	data = read_data(filename)
	st.dataframe(data)

# Show Description
if st.checkbox("Show All Column Name"):
	data = read_data(filename)
	st.text("Columns:")
	st.write(data.columns)


# # Dimensions
if st.checkbox("Dimension"):
	data = read_data(filename)
	if st.button("Number of Rows"):
		st.write(data.shape[0])
	if st.button("Number of Columns"):
		st.write(data.shape[1])


# data_dim = st.radio('Dimension ',('Rows','Columns))
# if data_dim == 'Rows':
# 	data = read_data(filename)
# 	st.text("Showing Length of Rows")
# 	st.write(len(data))
# if data_dim == 'Columns':
# 	data = read_data(filename)
# 	st.text("Showing Length of Columns")
# 	st.write(data.shape[1])

#Null Values in the dataset
if st.checkbox("Number of Null Values"):
	data = read_data(filename)
	summ_null = data.isnull().sum()
	st.write(summ_null)

# if st.checkbox("Number of Null Values1"):
# 	summ_null = data.isnull().any().any()
# 	st.write(summ_null)

# Select Columns
if st.checkbox("Select Columns To Show"):
	data = read_data(filename)
	all_columns = data.columns.tolist()
	selected_columns = st.multiselect("Select",all_columns)
	new_df = data[selected_columns]
	st.dataframe(new_df)

if st.checkbox("Show Summary of Dataset"):
	data = read_data(filename)
	data = read_data(filename)
	st.write(data.describe())

# Show Values
if st.checkbox("Check if Data is Balanced or Imbalanced"):
	data = read_data(filename)
	st.write(data.iloc[:,-1].value_counts())


	# Show Datatypes
if st.checkbox("Data Type of each Column"):
	data = read_data(filename)
	st.write(data.dtypes)

## Plot and Visualization

html_temp = """
	<div style="background-color:purple;"><p style="color:white;font-size:40px;padding:10px"><center>Data Visualization</center></p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)


html_temp = """
	<div style="background-color:green;"><p style="color:white;font-size:20px;padding:10px">Bar Plot</p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)
# Show Plots
if st.checkbox("Bar Plots"):
	data = read_data(filename)
	all_columns_names = data.columns.tolist()
	primary_col = st.selectbox("Select the Target variable",all_columns_names)
	selected_columns_names = st.selectbox("Select a column",all_columns_names)
	st.write(sns.barplot(x = selected_columns_names,y = primary_col,data = data))
	st.pyplot()

html_temp = """
	<div style="background-color:green;"><p style="color:white;font-size:20px;padding:10px">Heatmaps</p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)
if st.checkbox("Simple Correlation Plot with Seaborn "):
	data = read_data(filename)
	st.write(sns.heatmap(data.corr(),annot=True))
	# Use Matplotlib to render seaborn
	st.pyplot()

html_temp = """
	<div style="background-color:green;"><p style="color:white;font-size:20px;padding:10px">Box Plot</p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)
# Box Plots
if st.checkbox("Box Plot "):
	data = read_data(filename)
	all_columns_names = data.columns.tolist()
	primary_col = st.selectbox("Select the Target variable",all_columns_names)
	selected_columns_names = st.selectbox("Select a column",all_columns_names)
	st.write(sns.catplot(kind = "box",x = selected_columns_names,y = primary_col,data = data))
	# Use Matplotlib to render seaborn
	st.pyplot()

html_temp = """
	<div style="background-color:green;"><p style="color:white;font-size:20px;padding:10px">Violin Plot</p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)
#Violin Plots
if st.checkbox("Violin Plot"):
	data = read_data(filename)
	all_columns_names = data.columns.tolist()
	primary_col = st.selectbox("Select the Target variable",all_columns_names)
	selected_columns_names = st.selectbox("Select a column",all_columns_names)
	st.write(sns.catplot(kind = "violin",x = selected_columns_names,y = primary_col,data = data))
	# Use Matplotlib to render seaborn
	st.pyplot()

html_temp = """
	<div style="background-color:green;"><p style="color:white;font-size:20px;padding:10px">Point Plot</p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)
#Scatter Plots
if st.checkbox("Point Plot"):
	data = read_data(filename)
	all_columns_names = data.columns.tolist()
	primary_col = st.selectbox("Select the Target variable",all_columns_names)
	selected_columns_names = st.selectbox("Select a column",all_columns_names)
	st.write(sns.catplot(kind = "point",x = selected_columns_names,y = primary_col,data = data))
	# Use Matplotlib to render seaborn
	st.pyplot()

html_temp = """
	<div style="background-color:green;"><p style="color:white;font-size:20px;padding:10px">Pie Plot</p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)
# Pie Chart
if st.checkbox("Pie Plot"):
	data = read_data(filename)
	all_columns_names = data.columns.tolist()
# if st.button("Generate Pie Plot"):
	st.success("Generating A Pie Plot")
	st.write(data.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
	st.pyplot()

html_temp = """
	<div style="background-color:green;"><p style="color:white;font-size:20px;padding:10px">Group By Plot</p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)
# Count Plot
if st.checkbox("Plot of Value Counts"):
	st.text("Value Counts By Target")
	data = read_data(filename)
	all_columns_names = data.columns.tolist()
	primary_col = st.selectbox("Primary Columm to GroupBy",all_columns_names)
	selected_columns_names = st.selectbox("Select Columns",all_columns_names)
	if st.button("Plot"):
		st.text("Generate Plot")
	if selected_columns_names:
		vc_plot = data.groupby(primary_col)[selected_columns_names].count()
		st.write(vc_plot.plot(kind="bar"))
		st.pyplot()
	else:
		vc_plot = data.iloc[:,-1].value_counts()
		st.write(vc_plot.plot(kind="bar"))
		st.pyplot()


st.sidebar.header("About Application")
st.sidebar.markdown("Exploratory Data Analysis tool")
st.sidebar.markdown("Made on StreamLit Platform")

st.sidebar.header("Author")
st.sidebar.markdown("Rinisha Burriwar")
st.sidebar.markdown("Git-Hub : https://github.com/Rinisha-Burriwar")






# # Customizable Plot

# st.subheader("Customizable Plot")
# all_columns_names = data.columns.tolist()
# type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
# selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

# if st.button("Generate Plot"):
# 	st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

# # Plot By Streamlit
# if type_of_plot == 'area':
# 	cust_data = data[selected_columns_names]
# 	st.area_chart(cust_data)

# elif type_of_plot == 'bar':
# 	cust_data = data[selected_columns_names]
# 	st.bar_chart(cust_data)

# elif type_of_plot == 'line':
# 	cust_data = data[selected_columns_names]
# 	st.line_chart(cust_data)

# # Custom Plot 
# elif type_of_plot:
# 	cust_plot= data[selected_columns_names].plot(kind=type_of_plot)
# 	st.write(cust_plot)
# 	st.pyplot()

# if st.button("Thanks"):
# 	st.balloons()

# if __name__ == '__main__':
# 	main()