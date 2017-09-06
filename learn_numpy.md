numpy
=========
#### 引入numpy library 
    import numpy as np 
#### np.array()
    製造array 
#### np.arange(0,11,2) 
    製造array  
    array([0, 2, 4, 6, 8, 10])
#### np.zeros(3), np.zeros((5, 5)) 
   array([0., 0., 0.])   
    5*5的零矩陣 
#### np.ones(4) 
    array([1., 1., 1., 1.]) 
#### np.linspace(0, 5, 100) 
    0到5 100個數字分布 
#### np.eye(4) 
    4*4的單位矩陣 
#### reshape()   
    將矩陣切割     
    ex. arr 是一個0~24組成的矩陣    
    arr.reshape(5, 5) 可以得到一個5*5的矩陣   
#### shape   
    arr.reshape(5, 5).shape    
> (5, 5)  

#### dtype  
    arr.dtype  
> dtype('int64')   



#### 注意,numpy中的array是用位置傳值   
    所以要使用arr_copy = arr.copy()來解決  
#### arr=[1, 2, 3, 4, 5], arr[arr>3]  
> array([4, 5])  


    
     
