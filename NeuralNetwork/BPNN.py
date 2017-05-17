# coding=utf-8

#该网络中隐含层所有的偏置项使用在输入层增加一个节点（节点输入输出值恒为1.0来代替），而输出层没有偏置项

import numpy as np
'''
激活函数类
'''
class Sigmoid:
    #sigmoid函数
    def f(self,x):
        return 1/(1+np.exp(-x))

    #sigmoid函数的导数
    def df(self,x):
        y = self.f(x)
        return y-np.multiply(y,y)

class Tanh:
    #双正切函数
    def f(self,x):
        return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

    #双正切函数的导数
    def df(self,x):
        y = self.f(x)
        return 1-np.multiply(y,y)
'''
工具类
'''
class Utils:
    def uniform_distribution(self,x1,x2):
        return np.random.uniform(x1,x2)
    def create_random_matrix(self,row,col,periphery):
        m = np.zeros((row,col))
        for i in range(row):
            for j in range(col):
                m[i][j] = self.uniform_distribution(-1*periphery, periphery)
        return m
    def create_matrix(self,row,col,init_value=None):
        m = np.zeros((row,col))
        if init_value is not None:
            for i in range(row):
                for j in range(col):
                    m[i][j] = init_value
        return m
    def matrix_fill_zeros(self,m):
        return np.zeros(np.shape(m))
'''
BP神经网络类
输入层、隐含层、输出层三层网络结构
'''
class BPNN:
    #网络初始化
    def __init__(self,input_node_num,hidden_node_num,output_node_num):
        #输入层节点个数,增加一个偏置项
        self.i_n = input_node_num+1
        #隐含层层节点个数
        self.h_n = hidden_node_num
        #输出层节点个数
        self.o_n = output_node_num

        self.utils = Utils()

        #输入层的输入(第i个样本),增加的偏置项节点的输入输出恒为1
        self.i_i = self.utils.create_matrix(self.i_n,1,1.0)
        #隐含层对第i个样本的输入
        self.h_i = self.utils.create_matrix(self.h_n,1,0.0)
        #输出层对第i个样本的输入
        self.o_i = self.utils.create_matrix(self.o_n,1,0.0)

        #输入层的第i个样本输出,增加的偏置项节点的输入输出恒为1
        self.i_o = self.utils.create_matrix(self.i_n,1,1.0)
        #隐含层对于第i个样本的输出
        self.h_o = self.utils.create_matrix(self.h_n,1,0.0)
        #o_o是预测值，第i个样本的预测值
        self.o_o = self.utils.create_matrix(self.o_n,1,0.0)

        #初始化连接权值矩阵
        self.w_i_h = self.utils.create_random_matrix(self.i_n,self.h_n,0.2)
        self.w_h_o = self.utils.create_random_matrix(self.h_n,self.o_n,2)


        #delta
        self.o_delta = self.utils.create_matrix(self.o_n, 1,0.0)
        self.h_delta = self.utils.create_matrix(self.h_n, 1,0.0)

        #delta w和，batch_size个样本的训练的和，也就是批量更新
        self.w_h_o_delta = self.utils.create_matrix(self.h_n,self.o_n,0.0)
        self.w_i_h_delta = self.utils.create_matrix(self.i_n,self.h_n,0.0)

    #训练
    def train(self,hidden_activation,output_activation,train_inputs,train_outputs,alpha,error_threshold,iteration_num,batch_percent):
        #隐含层的激活函数
        self.h_activation = hidden_activation
        #输出层的激活函数
        self.o_activation = output_activation
        #学习步长
        self.alpha = alpha
        #训练样本的个数
        self.train_sample_n = np.shape(train_inputs)[0]
        #这次迭代的总误差
        self.train_error = 0.0
        #误差阈值
        self.error_threshold = error_threshold
        #最大迭代次数
        self.iteration_num = iteration_num
        #每一次批量更新需要使用的样本个数
        if batch_percent>100:
            batch_percent = 100
        self.batch_size = (int)(self.train_sample_n*batch_percent/100)

        #训练样本输入,矩阵,每一行为一个样本特征
        self.train_inputs = train_inputs
        #训练样本真实值,矩阵,每一行为一个样本的值
        self.train_outputs = train_outputs

        #开始训练
        self.batch()

    #测试
    def test(self,test_inputs,test_outputs=None):
        #测试样本个数
        self.test_sample_n = np.shape(test_inputs)[0]
        #预测集合
        predict_outputs = self.utils.create_matrix(self.test_sample_n, self.o_n,0.0)
        for i in range(self.test_sample_n):
            #预测第i个测试样本
            self.predict(test_inputs[i:i+1:,::])
            #预测结果在self.o_o中
            predict_outputs[i:i+1:,::] = np.transpose(self.o_o)
            print "actural: ",test_outputs[i]
        '''
        print "predict values:"
        print predict_outputs
        #如果测试样本有结果，则输出真实结果以及预测总误差
        if test_outputs is not None:
            diff = test_outputs-predict_outputs
            self.test_error = 0.5*np.sum(np.sum(np.multiply(diff,diff),axis=1),axis=0)[0,0]
            print "actural values:"
            print test_outputs
            print "test error:"
            print self.test_error
        '''


    #预测一个样本
    def predict(self,test_input):
        #输入层的输出，即为其输入,i_nx1矩阵,因为有个偏置项，所有两个矩阵行数不一样，需要进行这样的赋值操作
        self.i_o[0:self.i_n-1:,0:1:] = np.transpose(test_input[0:1:,::])
        #计算隐含层每个节点的输出h_o
        self.h_o = self.h_activation.f(np.transpose(self.w_i_h)*self.i_o)

        #计算输出层每个节点的输出o_o
        self.o_o = self.o_activation.f(np.transpose(self.w_h_o)*self.h_o)

        print "predict: ",self.o_o

    #批量更新
    def batch(self):
        #一次batch使用的样本的编号集
        inputs_indexs = [i for i in range(self.batch_size)]
        #下次batch的需要使用的第一个样本的编号
        last_index = (inputs_indexs[-1]+1)%self.train_sample_n
        #批量更新，直到误差小于阈值或者达到最大迭代次数
        while True:
            #print "inputs_indexs:",inputs_indexs
            self.one_batch(inputs_indexs)
            #print "error: ",self.train_error
            #剩余的迭代次数减1
            self.iteration_num -= 1
            #判断误差是否不再改变或者达到最大迭代次数
            if self.terminate():
                break
            else:#否则继续迭代
                #得到下次batch所需要使用的样本集所对应的编号集
                '''
                举例：训练样本集所对应的编号集是[0,1,2,3,4,5],样本个数为6，即train_sample_n＝6
                如果batch_size=4，即每一次batch使用四个样本，
                那么第一次使用的batch样本集所对应的编号集inputs_indexs=[0,1,2,3]
                last_index = 4
                第二次使用的batch样本集所对应的编号集inputs_indexs=[4,5,0,1]
                即以后每次batch的inputs_indexs为：
                for i in range(self.batch_size):
                    inputs_indexs.append((i+last_index)%self.train_sample_n)
                '''
                inputs_indexs = []
                for i in range(self.batch_size):
                    inputs_indexs.append((i+last_index)%self.train_sample_n)
                last_index = (inputs_indexs[-1]+1)%self.train_sample_n

    #一次batch
    def one_batch(self,inputs_indexs):
        #对每一个样本，首先使用前向传递，然后使用误差反向传播
        for i in inputs_indexs:
            #前向传递
            self.fp(i)
            #break
            #反向传播
            self.bp(i)
        #更新权值
        self.update()



    #第i个样本前向传递
    def fp(self,i):
        #输入层的输出，即为其输入,第i个样本, i_nx1矩阵
        self.i_o[0:self.i_n-1:,0:1:] = np.transpose(self.train_inputs[i:i+1:,::])

        #计算隐含层每个节点的输入h_i,以及隐含层的输出h_o
        self.h_i = np.transpose(self.w_i_h)*np.matrix(self.i_o)
        self.h_o = self.h_activation.f(self.h_i)

        #计算输出层每个节点的输入o_i,以及隐含层的输出o_o
        self.o_i = np.transpose(self.w_h_o)*self.h_o
        self.o_o = self.o_activation.f(self.o_i)


        #计算平方误差和
        actural = np.transpose(self.train_outputs[i:i+1:,::])
        tmp = self.o_o-actural
        self.train_error = self.train_error + (np.transpose(tmp)*tmp)[0,0]

    #第i个样本误差反向传播
    def bp(self,i):

        #对输出层每一个节点，计算\Delta_{ij}^{T-1}=(y_{ij}-\hat{y}_{ij}) \cdot f'^{T}(v)|_{v=I_{ij}^{T}}
        self.o_delta = np.multiply((self.o_o-np.transpose(self.train_outputs[i:i+1:,::])),
                                   self.o_activation.df(self.o_i))
        #print "self.o_delta:",self.o_delta
        #使用公式\frac{1}{p}\sum_{i=1}^{p}\Delta_{ij}^{T-1} \cdot o^{T-1}_{ik}计算\Delta {w_{kj}^{T-1}}
        #前面的系数frac{1}{p}还没乘
        self.w_h_o_delta = self.w_h_o_delta + self.h_o*np.transpose(self.o_delta)
        #print "self.w_h_o_delta:",self.w_h_o_delta


        #对隐含层每一个节点，计算\Delta_{ij}^{T-2}=\sum_{s=1}^{s_{T}}(y_{is}-\hat{y}_{is}) \cdot f'^{T}(v)|_{v=I_{is}^{T}}\cdot w_{js}^{T-1} \cdot f'^{T-1}(v)|_{v=I_{ij}^{T-1}}
        self.h_delta = np.multiply(self.w_h_o*np.multiply((self.o_o-np.transpose(self.train_outputs[i:i+1:,::])),self.o_activation.df(self.o_i)),self.h_activation.df(self.h_i))
        #print "self.h_delta:",self.h_delta
        #使用公式\frac{1}{p}\sum_{i=1}^{p}\Delta_{ij}^{T-2}\cdot o^{T-2}_{ik}计算\Delta {w_{kj}^{T-2}}
        #前面的系数frac{1}{p}还没乘
        self.w_i_h_delta = self.w_i_h_delta + self.i_o*np.transpose(self.h_delta)
        #print "self.w_i_h_delta:",self.w_i_h_delta

    #更新权值W
    def update(self):
        #按照公式更新输入层与隐含层之间的w: w^{T-2}_{kj}:=w^{T-2}_{kj}-\alpha\frac{1}{p}\sum_{i=1}^{p}\Delta_{ij}^{T-2}\cdot o^{T-2}_{ik}
        self.w_i_h = self.w_i_h - self.alpha/self.batch_size*self.w_i_h_delta
        #按照公式更新隐含层与输出层之间的w: w^{T-1}_{kj}:=w^{T-1}_{kj}-\alpha\frac{1}{p}\sum_{i=1}^{p}\Delta_{ij}^{T-1} \cdot o^{T-1}_{ik}
        self.w_h_o = self.w_h_o - self.alpha/self.batch_size*self.w_h_o_delta
        #delta清零
        self.w_i_h_delta = Utils().matrix_fill_zeros(self.w_i_h_delta)
        self.w_h_o_delta = Utils().matrix_fill_zeros(self.w_h_o_delta)


    #判断迭代是否终止
    def terminate(self):
        if(0.5*self.train_error/self.batch_size<self.error_threshold
            or self.iteration_num<=0):
            return True
        else:
            print "error: ",self.train_error
            self.train_error = 0.0
            return False


if __name__=="__main__":
    '''
    inputs = np.matrix([[0,0],[0,1],[1,0],[1,1]])
    outputs = np.matrix([[0],[1],[1],[0]])
    bpnn = BPNN(2, 5, 1)

    bpnn.train(Tanh(), Tanh(), inputs,
              outputs, 0.1, 0.001,
              10000, 100)
    bpnn.test(inputs)
    '''
    #读取数据
    r_fp = open("data","r")
    #输入层节点数
    input_level_node_num = 0
    #隐藏层层节点数
    hidden_level_node_num = 0
    #输出层节点数
    output_level_node_num = 0
    #输入数据
    inputs = []
    #数据的真实值
    outputs = []
    i = 0
    for line in r_fp:
        strs = line.strip().split(",")
        #第一行是每层的节点数
        if i==0:
            input_level_node_num = int(strs[0])
            hidden_level_node_num = int(strs[1])
            output_level_node_num = int(strs[2])
        else:
            #数据，最后一列是真实值
            #特征值向量
            i_v = []
            #真实值向量
            o_v = []
            for i in range(len(strs)-1):
                i_v.append(float(strs[i]))
            o_v.append(float(strs[-1]))
            inputs.append(i_v)
            outputs.append(o_v)
        i+=1
    inputs = np.matrix(inputs)
    outputs = np.matrix(outputs)
    #每个特征以及结果的的最大值最小值归一化
    max_inputs = np.max(inputs,axis=0)
    min_inputs = np.min(inputs,axis=0)
    normalize_inputs = (inputs-min_inputs)/(max_inputs-min_inputs)
    max_outputs = np.max(outputs,axis=0)
    min_outputs = np.min(outputs,axis=0)
    normalize_outputs = (outputs-min_outputs)/(max_outputs-min_outputs)
    #获取总共样本的个数
    smaple_n = np.shape(normalize_inputs)[0]
    #将数据按照2:1拆分成训练集与测试集
    train_sample_n = smaple_n*2.0/3
    train_inputs = normalize_inputs[0:train_sample_n:1,::]
    train_outputs = normalize_outputs[0:train_sample_n:1,::]
    test_inputs = normalize_inputs[train_sample_n:smaple_n:1,::]
    test_outputs = normalize_outputs[train_sample_n:smaple_n:1,::]

    #构建网络
    bpnn = BPNN(input_level_node_num, hidden_level_node_num, output_level_node_num)
    #训练
    bpnn.train(Sigmoid(), Sigmoid(), train_inputs,
                  train_outputs, 0.2, 0.01,
                  1000, 100)
    #测试,其实最后预测值需要进行反归一化，这里没有做此步骤
    bpnn.test(test_inputs,test_outputs)