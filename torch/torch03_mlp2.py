import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F 

#1. 데이터
x = np.array([[1,2,3,4,5,6,7,8,9,10],
             [1,1.1,1.2,1.3,1.4,1.5,
              1.6,1.5,1.4,1.3],
             [10,9,8,7,6,5,4,3,2,1]])

y = np.array([11,12,13,14,15,16,17,18,19,20])

##### GPU #####
USE_CUDA = torch.cuda.is_available()
DEVICE = torch.device('cuda' if USE_CUDA else 'cpu')
print('torch: ', torch.__version__, '사용DEVICE: ', DEVICE)

x = np.transpose(x) 

x = torch.FloatTensor(x).to(DEVICE)
y = torch.FloatTensor(y).unsqueeze(1).to(DEVICE) #(10,) -> (10,1)

print(x, y)
print(x.shape, y.shape) # torch.Size([10, 3]) torch.Size([10, 1])

#2. 모델구성
#model = nn.Linear(1, 1).to(DEVICE) 
model = nn.Sequential(
    nn.Linear(3, 5),
    nn.Linear(5, 3),
    nn.Linear(3, 4),
    nn.Linear(4, 2),
    nn.Linear(2, 1),
).to(DEVICE)           

#3. 컴파일, 훈련
criterion = nn.MSELoss() # 평가지표의 표준
optimizer = optim.AdamW(model.parameters(), lr = 0.01) 

def train(model, criterion, optimizer, x, y):
    #model.train()  # 훈련모드
    optimizer.zero_grad() # 기울기 초기화
    
    hypothesis = model(x) 
    
    loss = criterion(hypothesis, y) # 예측값과 실제값 비교 # MSE
    #loss = nn.MSELoss()(hypothesis, y) # 정상작동 (방법1)
    #loss = F.mse_loss(hypothesis, y) # 정상작동 (방법2)
    
    # 여기까지가 순전파
    
    loss.backward() # 기울기값 계산까지
    optimizer.step() # 가중치 수정(역전파)
    return loss.item() # loss반환

epochs = 100
for epoch in range(1, epochs+1):
    loss = train(model, criterion, optimizer, x, y)
    print('epoch : {}, loss: {}'.format(epoch, loss))

print("==========================================")

#4. 평가, 예측
def evaluate(model, criterion, x, y):
    model.eval() # 평가모드
    
    with torch.no_grad(): 
        predict = model(x) 
        loss2 = criterion(predict, y)
    return loss2.item()

loss2 = evaluate(model, criterion, x, y)
print('최종 loss: ', loss2)

result = model(torch.Tensor([[10, 1.3, 1]]).to(DEVICE))
print('10, 1.3, 1의 예측값 : ', result.item())

'''
최종 loss:  0.00589944189414382
10, 1.3, 1의 예측값 :  20.042001724243164
'''