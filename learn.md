#### Print 
    print('My number is: {one}, and my name is: {two}'.format(one=num,two=name))
> output: My number is: 12, and my name is: Sam 

#### Dictionaries, dic.index can get dic's index   
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
> 像上上個結果, 只是變成0~4 

#### list comprehension 
    x = [1,2,3,4] 
    out = [] 
    for item in x: 
        out.append(item**2)
    print(out) 
> [1, 4, 9, 16] 

#### Special list 
    x = [1, 2, 3, 4]
    out=[num**2 for num in x]
> [1, 4, 9, 16] 

#### functions 
    def my_func(param1='default'):
        """
        DOCSTRING GOES HERE.
        """ 
        print(param1)
        # return param1... 
    my_func() 
> default 

    my_func('new param')
> new param 

#### map() function 
    def times2(var): 
        return var*2
    seq = [1, 2, 3, 4, 5] 
    list(map(times2,seq)) 
> [2, 4, 6, 8, 10] 

#### lambda expressions 
    def times2(var): 
        return var*2 
        || equal
    t = lambda var: var*2
    t(6) 
> 12 

    seq = [1, 2, 3, 4, 5] 
    list(map(lambda var: var*3, seq)) 
> [3, 6, 9, 12, 15] 

#### filter() function 
    seq = [1, 2, 3, 4, 5]
    list(filter (lambda var: var%2 == 0, seq))
> [2, 4] 




    

