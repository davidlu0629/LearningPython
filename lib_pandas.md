pandas  
==============  
# import library  
    import numpy as np  
    import pandas as pd  
    labels = ['a', 'b', 'c']  
    my_list = [10, 20, 30]  
    arr = np.array([10, 20, 30])  
    d = {'a': 10, 'b': 20}  
  
# pandas Series function  
    pd.Series(data= my_list)  
> 0    10  
> 1    20  
> 2    30  
> dtype: int64  
    
    pd.Series(data= my_list, index= labels), pd.Series(d) 得到的結果相同  
> a 10  
> b 20  
> c 30  
> dtype: int64  

# DataFrames,有點像是一堆Series組成  
    from numpy.random import randn  
    np.random.seed(101)  
# 建DataFrame  
    df= pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split()) or 
    df= pd.DataFrame(randn(5, 4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])    
    


# dataframe can easily let user to see their column data  
    ex. df['W'] or want to see more than one column df[['W','X']]  
# add new column  
    ex. df['new']=df['W']+df['X']   
# 看所有columns或index的名字   
    ex. data= pd.DataFrame()  
    data.columns.values or data.index.values  
# remove columns, drop function, axis=0(row), axis=1(column) , inplace(default is false)(是否取代)   
    df.drop('new' , axis=1, implace=True)  
# 選擇row, loc or iloc  
    ex. df.loc['A']  
    df.iloc[0]  
# 聯合選取,一定要用&跟|  
    df[(df['W']>0) & (df['Y']>1)]  
    #符合上面兩個條件的row就會被顯示出來  
# plus original index (reset_index())  
    sta="Taiwan USA Japan China Korea".split()
    df['States']=sta  
    can change index, use: set_index('States'), 有點像變成Series之後才能加入表格       
# Multi-Index and Index Hierarchy  
    outside=['G1', 'G1', 'G1', 'G2', 'G2', 'G2']  
    inside= [1, 2, 3, 1, 2, 3]  
    hier_index= list(zip(outside, inside))  
    hier_index= pd.MultiIndex.from_tuples(hier_index)  
    df= pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])  
# dropna, fillna (對NAN值做處理)  
# groupby (將值統整)    
# concatenation, pd.concat([df, df, df], axis=)  
    ex. df1, df2, df3  
    pd.concat([df1, df2, df3])  
# 將DataFrame組合起來 pd.merge , pd.join  
# 將function 讓DataFrame代入    
    ex. def times2(x):
            return x*2
        df['col1'].apply(times2)    
# column 中資料元素統計 use .value_counts()    
    ex. ecom['AM or PM'].value_counts()  
    output:    
    PM    5068    
    AM    4932     
    


    
    
    
