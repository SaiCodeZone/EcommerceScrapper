import matplotlib.pyplot as plt
import pandas as pd

def plotResults(filename):
    #plot section
    #filePath='C:/Users/Saikiran/'+filename
    data=pd.read_csv(filename,index_col='Source',encoding='utf-8').fillna(0)
    #snapdeal data
    Snapdeal_sno=data['S.no']['snapdeal']
    Snapdeal_prices=data['Price']['snapdeal']
    plt.bar(Snapdeal_sno,Snapdeal_prices,label="Snapdeal",color='r',width=.5)

    #flipkart data
    Flipkart_sno=data['S.no']['Flipkart']
    Flipkart_prices=data['Price']['Flipkart']
    plt.bar(Flipkart_sno,Flipkart_prices,label="Flipkart",color='b',width=.5)

    #display plot
    plt.title("Price graph")
    plt.legend(loc="upper left")
    plt.xlabel("Serial numbers")    
    plt.ylabel("Prices")
    plt.show()
