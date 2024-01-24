import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

    
def main():
    st.title('Perform EDA with ease...')

    def file_select(folder='./datasets'):
        filelist=os.listdir(folder)
        selectedfile=st.selectbox('select a default file',filelist)
        return os.path.join(folder,selectedfile)


    if st.checkbox('Select dataset from local machine'):
        data=st.file_uploader('Upload Dataset in .CSV',type=['CSV'])
        if data is not None:
            df=pd.read_csv(data)
    else:
        filename=file_select()
        st.info('You selected {}'.format(filename))
        if filename is not None:
            df=pd.read_csv(filename)
    #show data
    if st.checkbox('Show Dataset'):
        num=st.number_input('No. of Rows',5,10)
        head=st.radio('Select Head/Tail',('Head','Tail'))
        if head=='Head':
            st.dataframe(df.head(num))
        else:
            st.dataframe(df.tail(num))
        
    #show columns
    if st.checkbox('Columns'):
        st.write(df.columns)
    #show shape
    if st.checkbox('Shape'):
        st.text('(Rows,Columns)')
        st.write(df.shape)
    
    #select columns
    if st.checkbox('Select Columns to show'):
        collist=df.columns.tolist()
        selcols=st.multiselect("Select",collist)
        newdf=df[selcols]
        st.dataframe(newdf)
    #unique values
    if st.checkbox('Unique Values'):
        st.dataframe(df.nunique())
        selectedcol=st.selectbox('Select column to see unique values',df.columns.tolist())
        st.write(df[selectedcol].unique())
    #data type
    if st.checkbox('Data Types'):
        st.dataframe(df.dtypes)
    #chech for nul values
    if st.checkbox('Null values'):
        st.dataframe(df.isnull().sum()) 
        st.write(sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis'))
        st.pyplot()
    #show summary
    if st.checkbox('Summary/Describe'):
        st.write(df.describe())

    #plot and viz.
    st.header('Data Visualization with Seaborn')
    #seaborn correlation plot
    if st.checkbox('Correlation plot'):
        st.write(sns.heatmap(df.corr(),annot=True))
        st.pyplot()
    #univariate distribution
    if st.checkbox('Univariate Distribution'):
        cols=df.columns.tolist()
        plottype=st.selectbox('Select plot type',['dist','hist'])
        selectedcol=st.selectbox('Select columns to plot',cols)
        binnum=st.number_input('No. of bins',10,50)
        st.write(sns.distplot(df[selectedcol],bins=binnum))
        st.pyplot()
    #bivariate distribution
    if st.checkbox('Bivariate Distribution'):
        cols=df.columns.tolist()
        plottype=st.selectbox('Select plot type',['scatterplot','jointplot'])
        st.text('Select two columns')
        x=st.selectbox('Select X-axis column to plot',cols)
        y=st.selectbox('Select Y-axis column to plot',cols)
        kindtype=st.selectbox('Select plot kind',['none','reg','resid','hex','kde'])
        if kindtype!='none':
            st.write(sns.jointplot(df[x],df[y],kind=kindtype))
            st.pyplot()
        else:
            st.write(sns.jointplot(df[x],df[y]))
            st.pyplot()
    #pair wise plot
    if st.checkbox('Pair Plot'):
        cols=df.columns.tolist()
        cols.insert(0,'none')
        selectedcollist=st.multiselect('Select columns to plot',cols)
        hueval=st.selectbox('Select a hue column',cols)
        if hueval!='none':
            st.write(sns.pairplot(df[selectedcollist],hue=df[hueval]))
            st.pyplot()
        else:
            st.write(sns.pairplot(df[selectedcollist]))
            st.pyplot()
    
    #categorical plots
    if st.checkbox('Categorical Scatterplots'):
        cols=df.columns.tolist()
        cols.insert(0,'none')
        plottype=st.selectbox('Select plot type',['stripplot','swarmplot'])
        x=st.selectbox('Select X-axis(categorical) column to plot',cols)
        y=st.selectbox('Select Y-axis(numericall) column to plot',cols)
        hueval=st.selectbox('Select a hue column(categorical)',cols)
        if plottype=='stripplot':
            if x!='none' and hueval!='none':
                st.write(sns.stripplot(df[x],df[y],hue=df[hueval]))
                st.pyplot()
            elif x!='none' and hueval=='none':
                st.write(sns.stripplot(df[x],df[y]))
                st.pyplot()
        else:
            if x!='none' and hueval!='none':
                st.write(sns.swarmplot(df[x],df[y],hue=df[hueval]))
                st.pyplot()
            elif x!='none' and hueval=='none':
                st.write(sns.swarmplot(df[x],df[y]))
                st.pyplot()
    #categorical distributions
    if st.checkbox('Categorical Distributions'):
        cols=df.columns.tolist()
        cols.insert(0,'none')
        plottype=st.selectbox('Select plot type',['box','bar','violin','count','point','factor'])
        x=st.selectbox('Select X-axis(catrogrical) column to plot',cols)
        y=st.selectbox('Select Y-axis(numerical) column to plot',cols)
        hueval=st.selectbox('Select a hue column',cols)
        #box plot
        if plottype=='box':
            if hueval!='none':
                st.write(sns.boxplot(df[x],df[y],hue=df[hueval]))
                st.pyplot()
            else:
                st.write(sns.boxplot(df[x],df[y]))
                st.pyplot()
        #bar plot
        if plottype=='bar':
            if hueval!='none':
                st.write(sns.barplot(df[x],df[y],hue=df[hueval]))
                st.pyplot()
            else:
                st.write(sns.barplot(df[x],df[y]))
                st.pyplot()
        
        #violin plot
        if plottype=='violin':
            if hueval!='none':
                st.write(sns.violinplot(df[x],df[y],hue=df[hueval]))
                st.pyplot()
            else:
                st.write(sns.violinplot(df[x],df[y]))
                st.pyplot()
        #count plot
        if plottype=='count':
            st.text('Plotting countplot for selected X column')
            if hueval!='none':
                st.write(sns.countplot(df[x],hue=df[hueval]))
                st.pyplot()
            else:
                st.write(sns.countplot(df[x]))
                st.pyplot()
        
        #point plot
        if plottype=='point':
            if hueval!='none':
                st.write(sns.pointplot(df[x],df[y],hue=df[hueval]))
                st.pyplot()
            else:
                st.write(sns.pointplot(df[x],df[y]))
                st.pyplot()

        #factor plot
        if plottype=='factor':
            typekind=st.selectbox('Select plottype for factor for plot',['point','bar','box','violin','strip','swarm'])
            colm=st.selectbox('Select column(col) parameter',cols)
            rows=st.selectbox('Select(only if col is selected) column(row) parameter',cols)
            if hueval!='none':
                if colm!='none' and rows!='none':
                    st.write(sns.factorplot(x=x,y=y,hue=hueval,col=colm,row=rows,data=df,kind=typekind))
                    st.pyplot()
                elif colm!='none' and rows=='none':
                    st.write(sns.factorplot(x=x,y=y,hue=hueval,col=colm,data=df,kind=typekind))
                    st.pyplot()
            else:
                if colm!='none' and rows!='none':
                    st.write(sns.factorplot(x=x,y=y,col=colm,row=rows,data=df,kind=typekind))
                    st.pyplot()
                elif colm!='none' and rows=='none':
                    st.write(sns.factorplot(x=x,y=y,col=colm,data=df,kind=typekind))
                    st.pyplot()


    #linear relationship
    if st.checkbox('Linear Relationship'):
        cols=df.columns.tolist()
        cols.insert(0,'none')
        xval=st.selectbox('Select X-axis',cols)
        yval=st.selectbox('Select Y-axis',cols)
        hueval=st.selectbox('Select hue column',cols)
        if hueval!='none':
            st.write(sns.lmplot(x=xval,y=yval,hue=hueval,data=df))
            st.pyplot()
        else:
            st.write(sns.lmplot(x=xval,y=yval,data=df))
            st.pyplot()

###########

    st.subheader('Customizable plots')
    cols=df.columns.tolist()
    plottype=st.selectbox('Select plot type',['bar','hist','box','area','line','kde'])
    selectedcollist=st.multiselect('Select columns to plot',cols)

    if st.button('Generate plot'):
        st.success('Generating customizable {} plot for {}'.format(plottype,selectedcollist))
        #plot using streamlit
        if plottype=='area' :
            cusdata=df[selectedcollist]
            st.area_chart(cusdata)
        elif plottype=='bar' :
            cusdata=df[selectedcollist]
            st.bar_chart(cusdata)
        elif plottype=='line' :
            cusdata=df[selectedcollist]
            st.line_chart(cusdata)
        elif plottype :
            cusplot=df[selectedcollist].plot(kind=plottype)
            st.write(cusplot)
            st.pyplot()

    st.subheader('Project developed by:')
    st.info('Name: K Vikas Reddy')
    st.info('College: SASTRA Deemed to be University')
    st.info('Mail:  vikasreddy6446@gmail.com')

    
    st.text('')
    st.text('')
    st.warning('Please report bugs if any and suggest any new features')
    if st.checkbox('About this project'):
        st.write('Exploratory Data Analysis is the first step every Data Scientist does in every project.') 
        st.write('I saw many people groan to perform EDA. It is because of the same scripts written over and over for every project.')
        st.write('If you also felt the same, then this project is for you. This project helps you perform EDA with ease.')
        st.write('You dont need to write any scripts. EDA can be performed with just few clicks. It is also very time efficient.')
        st.write('As Data Science is becoming very popular, Data Science aspirants should also become smart and productive.')
        st.write('Hope this project helps you to some extent.')

if __name__=='__main__':
    main()

  
