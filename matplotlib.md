# spend some time on matplotlib.org to find out some idea  
    import matplotlib.pyplot as plt  
# 顯示圖片 plt.show()  
    plt.plot(x, y)  
    plt.show()  
# attributes that are common to use:  
    plt.xlabel('name')  
    plt.ylabel('name')  
    plt.title('name')  
# plt.subplot for more than one pic in the block  
    ex. plt.subplot(1, 2, 1)
    plt.plot(x, y, 'r')  
    plt.subplot(1, 2, 2)  
    plt.plot(y, x, 'b')  
# plt OO  
    fig= plt.figure()  
    axes1= fig.add_axes([0.1, 0.1, 0.8, 0.8])  
    axes2= fig.add_axes([0.2, 0.5, 0.4, 0.3])  
    axes1.set_xlabel('x')  
    axes1.set_ylabel('y')  
    axes1.set_title('title')  
    
    
    
    
