import numpy as np
import matplotlib.pyplot as plt
import pickle, gzip

def view_data1(x, y):
    k = 0
    for i in range(4):
        for j in range(4):
            plt.subplot(4, 4, k+1)
            plt.imshow( x[k].reshape(32, 32), interpolation='none', cmap='gray')
            plt.title(r'$y_{%d}$ = %d' % (k, y[k]))
            plt.gca().axis('off')
            k += 1
    plt.show()

def view_data2(x, y):
    k = 0
    for i in range(2):
        for j in range(2):
            plt.subplot(2, 4, 2*k+1)
            plt.imshow( x[k].reshape(32, 32), interpolation='none', cmap='gray')
            plt.title(r'$x_{%d}$' % k)
            plt.gca().axis('off')
            
            plt.subplot(2, 4, 2*k+2)
            plt.imshow( y[k].reshape(32, 32), interpolation='none',cmap='gray')
            plt.title(r'$y_{%d}$' % k)
            plt.gca().axis('off')
            k += 1
    plt.show()

def view_data3(x, y, o):
    k = 0
    for i in range(2):
        for j in range(2):
            
            plt.subplot(2, 6, 3*k+1)
            plt.imshow( x[k].reshape(32, 32), interpolation='none', cmap='gray')
            plt.title(r'$x_{%d}$' % k)
            plt.gca().axis('off')
        
            plt.subplot(2, 6, 3*k+2)
            plt.imshow( y[k].reshape(32, 32), interpolation='none',cmap='gray')
            plt.title(r'$y_{%d}$' % k)
            plt.gca().axis('off')

            plt.subplot(2, 6, 3*k+3)
            plt.imshow( o[k].reshape(32, 32), interpolation='none',cmap='gray')
            plt.title(r'$o_{%d}$' % k)
            plt.gca().axis('off')
            k += 1
    plt.show()


