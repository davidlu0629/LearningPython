#### Print 
    print('My number is: {one}, and my name is: {two}'.format(one=num,two=name))
> output: My number is: 12, and my name is: Sam 

#### Dictionaries 
    d = {'key1':'item1','key2':'item2'}
    d['key1']
> 'item1'    

#### Tuples 
    t = (1,2,3)
    t[0]
> 1  
  
    t[0] = 'NEW'
> error, tuples 無法改變  
#### Sets 
    {1,2,3} 
> {1,2,3} 

    {1,1,1,2,2,2,3,3,3} 
> {1,2,3} 

    s.add(5) 
> {1,2,3,5} 

#### for Loops 
    seq = [1,2,3,4,5] 
    for item in seq: 
        print(item) 
> 1 

> 2 

> 3 

> 4 

> 5 

#### range() 
    list(range(10)) 
> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

    for x in range(0,5):
        print(x) 
> 向上上個結果, 只是變成0~4 




