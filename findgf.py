#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""问世间情为何物

问题：一个人可以遇到N 个异性，遇到s个后，选择第一个超过这s个人（因此也超过他/她之前的所有人），结束。
如果没有找到，则选择最后一个。

术语：这s个人被称为样本，永远不可能被选择

假设：每个人的价值从0到N-1随机排序, 即排列S_N上的均匀分布, X ~ U(S_N)。
最终选择Y=X_d, X_d > max{X_1 ... X_s} > {X_{s+1} ... X_{d-1}}
估计：最优概率P(Y=N-1)，期望EY
"""

import numpy as np

N = 100

def find(s=15, N=100):
    """寻找函数
    
    一个人可以遇到N 个异性，遇到s个后，选择第一个超过这s个人（因此也超过他/她之前的所有人），结束。
如果没有找到，则选择最后一个。
    
    Keyword Arguments:
        s {number} -- 策略（样本量） (default: {15})
        N {number} -- 可能遇到的总人数 (default: {100})
    
    Returns:
        number -- 遇到的人（价值）
    """
    gfs = np.arange(N)
    np.random.shuffle(gfs)
    for gf in gfs[s:]:
        if np.all(gf > gfs[:s]):
            return gf
    else:
        return gfs[-1]

import matplotlib.pyplot as plt

def demo():
    # 演示程序
    stategies = (5, 10, 15, 20, 25, 30, 35, 40)
    ms = []
    ns = []
    for s in stategies:
        gf = np.array([find(s) for _ in range(100)])
        n = np.sum(gf==99)
        m = np.mean(gf)
        plt.plot(gf)
        ms.append(m)
        ns.append(n)
    plt.legend(['%d / %.2f / %d' % (s, m, n) for s, m, n in zip(stategies, ms, ns)])
    plt.show()

# 估计程序
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
myfont = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

plt.title('可能遇到 %d 个异性' %N, fontproperties=myfont)
stategies = np.arange(2, 60, 2)
ms = []
ps = []
SN = 1000
for s in stategies:
    gf = np.array([find(s, N) for _ in range(SN)])
    n = np.sum(gf==N-1) / SN
    m = np.mean(gf)
    ms.append(m)
    ps.append(n)
exp=plt.subplot(111)
prob = exp.twinx()
exp.plot(stategies, ms, color='r')
prob.plot(stategies, ps)
prob.plot(stategies, [x/N*np.log(N/x) for x in stategies])
exp.set_ylabel('期望值估计', color='r', fontproperties=myfont)
prob.set_ylabel('最优概率估计', fontproperties=myfont)
exp.set_xlabel('策略', fontproperties=myfont)
plt.show()