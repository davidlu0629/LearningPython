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
# remove columns, drop function, axis=0(row), axis=1(column)  
    df.drop('new' , axis=1)  
# 選擇row, loc or iloc  
    ex. df.loc['A']  
        df.iloc[0]  
        
