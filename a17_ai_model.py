#%%

def basic_collection(df):
    df['Close1']=df["Close"].shift(periods=1)
        
    df['SMA10'] = df["Close"].rolling(min_periods=1, window=10).mean()
    df['SMA20'] = df["Close"].rolling(min_periods=1, window=20).mean()
    df['SMA50'] = df["Close"].rolling(min_periods=1, window=50).mean()
    df['SMA200'] = df["Close"].rolling(min_periods=1, window=200).mean()
    df['SMA100'] = df["Close"].rolling(min_periods=1, window=100).mean()

    df["MAX50"] = df["High"].rolling(min_periods=1, window=50).max()
    df["MAX100"] = df["High"].rolling(min_periods=1, window=100).max()
    df["MAX200"] = df["High"].rolling(min_periods=1, window=200).max()

    df["MIN50"] = df["Low"].rolling(min_periods=1, window=50).min()
    df["MIN100"] = df["Low"].rolling(min_periods=1, window=100).min()
    df["MIN200"] = df["Low"].rolling(min_periods=1, window=200).min()
    return df

from import_models import *
# %%
do=pd.DataFrame()
#%%
# tickers='KGC,SKWD,PANW,MELI,RACE,CAH,GRMN,BRO,ROKU,AFRM,WING,NEU,AVAV,CDRE,CWCO,AVAH,DERM,CXDO,COR,IR,WRB,LII,LDOS,CE,GLOB,APG,ENSG,OBDC,AIR,PGTI,HCI,CVRX,ML,LWAY,HRTG,GHM,AJG,IR,WRB,LDOS,CE,GLOB,APG,AMR,WFDC,PGTI,AFYA,ROVR,HCI,TIPT,CVRX,ML,LWAY,HRTG,QUIK,KNSL,TSLA,SPY,AAPL,MSFT,WMT,AMZN,A,NOW,NU,CRWD,ZS,NET,KTOS,DDOG,DCBO,FTNT,ML'
tickers='KGC,SKWD,PANW,MELI,RACE,CAH,GRMN,BRO,ROKU,AFRM,WING,NEU,AVAV,CDRE,CWCO,AVAH,DERM,CXDO,COR,IR,WRB,LII,LDOS,CE,GLOB,APG,ENSG,OBDC,AIR,PGTI,HCI,CVRX,ML,LWAY,HRTG,GHM,AJG,IR,WRB,LDOS,CE,GLOB,APG,AMR,WFDC,PGTI,AFYA,ROVR,HCI,TIPT,CVRX,ML,LWAY,HRTG,QUIK,KNSL,TSLA,SPY,AAPL,MSFT,WMT,AMZN,A,NOW,NU,CRWD,ZS,NET,KTOS,DDOG,DCBO,FTNT,ML'
tickers='KGC,SKWD,PANW,MELI,RACE,CAH,GRMN,BRO,ROKU,AFRM,WING,NEU,AVAV,CDRE,CWCO,AVAH,DERM,CXDO,COR,IR,WRB,LII,LDOS,CE,GLOB,APG,ENSG,OBDC,AIR,PGTI,HCI,CVRX,ML,LWAY,HRTG,GHM,AJG,IR,WRB,LDOS,CE,GLOB,APG,AMR,WFDC,PGTI,AFYA,ROVR,HCI,TIPT,CVRX,ML,LWAY,HRTG,QUIK,KNSL,TSLA,SPY,AAPL,MSFT,WMT,AMZN,A,NOW,NU,CRWD,ZS,NET,KTOS,DDOG,DCBO,FTNT,ML,LULU,INTR,IT,CBOE'
# tickers='TSLA,SPY,AAPL,MSFT,WMT,AMZN,A,NOW,NU,CRWD,ZS,NET,KTOS,DDOG,DCBO,FTNT,ML'
tickers=list(set(tickers.split(',')))
tickers

#%%
# tickers=['KNSL','TSLA','SPY','AAPL','MSFT','WMT','AMZN','A','NOW','NU','CRWD','ZS','NET','KTOS','DDOG','DCBO','FTNT','ML']
#%%
ticker='A'
for ticker in tickers:
    try:
        df=weekly_ohlcv(ticker)[0]
    except:
        continue

    df=df.set_index('d')
    df

    df=basic_collection(df)
    # df=df[['Open','High','Low','Close','Volume','SMA10','MAX50']]
    column_selected=['Open','High','Low','Close','SMA10','SMA20']
    column_selected=['Open','High','Low','Close']
    
    df=df[column_selected]
    max1=df.max().max()
    min1=df.min().min()
    df=(df-min1)/(max1-min1)

    column1=[item+'_'+ticker for item in list(df.columns)]
    column1
    df.columns=column1

    df

    do=pd.concat([do,df],axis=1)

    do.fillna(method='ffill', inplace=True)

do
#%%
do.fillna(0, inplace=True)

#%%
do=reset_index(do)
do
#%%
do
do = do.drop('d', axis=1)
do
#%%
LENGTH=20



x_total=[]
y_total=[]

i=0
for i in range(len(df)-LENGTH):
    for ticker in tickers:
        
        column_list=[item for item in list(do.columns) if ticker == item.split('_')[1]]
        x=do[column_list][i:i+LENGTH].values
        # x=df[i:i+LENGTH].values
        x=torch.tensor(x)
        # print("\n>> x.shape= ", x.shape)
        try:
            y=do[f'Close_{ticker}'][i+LENGTH]
        except:
            continue
        y=torch.tensor(y)

        # print("\n>> y.shape= ", y.shape)

        x_total.append(x)
        y_total.append(y)
x_total

# x_total=torch.tensor(df.values)
# y_total=

#%%



#%%
x_total=torch.stack(x_total)
print("\n>> x_total.shape= ", x_total.shape)
y_total=torch.stack(y_total).unsqueeze(-1)
print("\n>> y_total.shape= ", y_total.shape)

#%%
x_total = torch.tensor(x_total, dtype=torch.float32)  
y_total = torch.tensor(y_total, dtype=torch.float32)
#%%

x_total



# x_total=x_total.to(device)
# y_total=y_total.to(device)
#%%
y_total[-1]
#%%
i
#%%
batch_size = int(len(tickers))  # You can adjust this


N = x_total.shape[0]
train_ratio = 0.8
num_train = int(train_ratio * N)#%%
indices=np.arange(N)
random.shuffle(indices)
train_index=indices[:num_train].tolist()
test_index=indices[num_train:].tolist()

Y=y_total[train_index]
YY=y_total[test_index]
X=x_total[train_index]
XX=x_total[test_index]

print("\n>> X.shape= ", X.shape)
print("\n>> XX.shape= ", XX.shape)
print("\n>> Y.shape= ", Y.shape)
print("\n>> YY.shape= ", YY.shape)


train_dataset = TensorDataset(X, Y)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=False)

test_dataset = TensorDataset(XX, YY)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# %%
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.nn.functional as F

class Conv1DModel_v2(nn.Module):
    def __init__(self,channel):
        super(Conv1DModel_v2, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=channel, out_channels=channel*2, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm1d(channel*2)
        self.conv2 = nn.Conv1d(in_channels=channel*2, out_channels=channel*4, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm1d(channel*4)
        self.conv3 = nn.Conv1d(in_channels=channel*4, out_channels=channel*8, kernel_size=3, padding=1)
        self.bn3 = nn.BatchNorm1d(channel*8)
        self.fc1 = nn.Linear(channel*8 * 20, 100)  # Adjust the size accordingly
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(100, 50)
        self.fc3 = nn.Linear(50, 1)

    def forward(self, x):
        x = x.permute(0, 2, 1)  # Rearrange to [batch_size, channels, seq_len]

        # Convolutional layers with ReLU and Batch Normalization
        x = F.relu(self.bn1(self.conv1(x)))
        x = F.relu(self.bn2(self.conv2(x)))
        x = F.relu(self.bn3(self.conv3(x)))

        # Flatten and Fully Connected Layers
        x = torch.flatten(x, start_dim=1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)  # Dropout for regularization
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return x

class Conv1DModel(nn.Module):
    def __init__(self,channel):
        super(Conv1DModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=channel, out_channels=10, kernel_size=3)
        self.conv2 = nn.Conv1d(in_channels=10, out_channels=20, kernel_size=3)
        self.fc1 = nn.Linear(20 * 16, 50)  # Adjust the size here depending on your sequence length after convolutions
        self.fc2 = nn.Linear(50, 1)

    def forward(self, x):
        # Assuming x is of shape [batch_size, seq_len, channels]
        x = x.permute(0, 2, 1)  # Rearrange to [batch_size, channels, seq_len]
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = torch.flatten(x, start_dim=1)  # Flatten except for the batch dimension
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
    

channel=x.shape[-1]
channel
#%%
model=Conv1DModel(channel)
criterion = nn.MSELoss()  # Use an appropriate loss function for your task
optimizer = torch.optim.Adam(model.parameters(), lr=0.01,weight_decay=0.001)
scheduler = StepLR(optimizer, step_size=100, gamma=0.1)  # Decay LR by a factor of 0.1 every 10 epochs




#%%
import matplotlib.pyplot as plt


epochs = 1000  # Example number of epochs
loss_=[]

for epoch in range(epochs):
    for ii,(x,y) in enumerate(train_loader):
        optimizer.zero_grad()
        y_hat = model(x)
        loss = criterion(y_hat, y)
        loss.backward()
        optimizer.step()
    # print("ii: ",ii)
    # print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item()}')

    total_loss=0
    with torch.no_grad():
        for ii,(x,y) in enumerate(test_loader):
            # optimizer.zero_grad()
            y_hat = model(x)
            loss = criterion(y_hat, y)
            # loss.backward()
            total_loss+=loss
            # optimizer.step()
    scheduler.step()
    total_loss=total_loss/(ii+1)
    print("total_loss: ",total_loss,epoch)
    loss_.append(total_loss)



plt.plot(loss_)
plt.show()
#%%
#%%

ticker=''

df=weekly_ohlcv(ticker)[0]
df

df=df.set_index('d')
df

df=df[column_selected]
df

df=reset_index(df)

df
df = df.drop('d', axis=1)
df#%%


x_total=[]
y_total=[]
max2=df.max().max()
min2=df.min().min()
df=(df-min2)/(max2-min2)
for i in range(len(df)-LENGTH):
    
    x=df[i:i+LENGTH].values
    # x=df[i:i+LENGTH].values
    x=torch.tensor(x)
    # print("\n>> x.shape= ", x.shape)

    y=df[f'Close'][i+LENGTH]
    y=torch.tensor(y)

    # print("\n>> y.shape= ", y.shape)

    x_total.append(x)
    y_total.append(y)

x_total=torch.stack(x_total)
print("\n>> x_total.shape= ", x_total.shape)
y_total=torch.stack(y_total).unsqueeze(-1)
print("\n>> y_total.shape= ", y_total.shape)


x_total = torch.tensor(x_total, dtype=torch.float32)  
y_total = torch.tensor(y_total, dtype=torch.float32)


i_selected=-13

tp,fp,tn,fn=0,0,0,0

for i_selected in range(len(x_total)):
    x_data=x_total[i_selected].unsqueeze(0)
    # print("\n>> x_data.shape= ", x_data.shape)

    y_hat=model(x_data).item()
    y_hat=(max2-min2)*y_hat+min2
    y_true=y_total[i_selected].item()
    y_true=(max2-min2)*y_true+min2

    y_true_prev=y_total[i_selected-1].item()
    y_true_prev=(max2-min2)*y_true_prev+min2

    # print("y_hat : ",y_hat)
    # print("y_true: ",y_true)
    # print("y_true_prev: ",y_true_prev)
    x_data[0]

    if y_true>y_true_prev:
        direction=1
        if y_hat>y_true_prev:
            tp+=1
        else:
            fn+=1    
    else:
        direction=0
        if y_hat>y_true_prev:
            fp+=1
        else:
            tn+=1
    tp,fp,tn,fn
print("tp,fp,tn,fn: ",tp,fp,tn,fn)
# %%
