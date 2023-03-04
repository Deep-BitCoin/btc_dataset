import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import mplfinance as mpf
import sys

file = sys.argv[1]
data = np.fromfile(file,'float32')
data = np.reshape(data,[-1,9])


def kline(ohlc,ma=(5, 25,50),figsize=(6,3),dpi=200):
    fig = plt.figure(figsize=figsize,dpi=dpi)
    fig.set_tight_layout(True)
    ohlc = np.array(ohlc)
    o, h, l, c = ohlc[:, 0], ohlc[:, 1], ohlc[:, 2], ohlc[:, 3]
    data = {'Open':o,'High':h,'Low':l,'Close':c}
    index = list(range(len(o)))
    df = pd.DataFrame(data,index=pd.DatetimeIndex(index))

    ax = fig.add_subplot(1, 1, 1)
    mpl.rcParams['lines.linewidth'] = 1
    # mpf.plot(df,ax=ax,type='candle',style='binance',mav=ma)
    mpf.plot(df, ax=ax, type='candle', style='binance')
    plt.axis('off')

    plt.show()
    plt.close()

kline(data[:,:4])
