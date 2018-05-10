# -*-coding:utf-8-*-
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

######################################################################
###################            基本用法            ###################
######################################################################
# x = np.linspace(-1,1,50)
# y = x**2
# plt.plot(x,y)
# plt.show()
### plt是作图工具
### plt.plot的括号里面需按照先横轴再纵轴的顺序排列变量
### plt.show()是为了显示所画图形

######################################################################
##################           Figure设置            ###################
######################################################################
# x = np.linspace(-3, 3, 50)
# y1 = 2*x+1
# y2 = x**2
#
# plt.figure()
# plt.plot(x,y1)
# ### 每出现一个plt.figure()，系统就出现一张图
#
# plt.figure(num=3,figsize=(8, 5))
# plt.plot(x, y2)
# plt.plot(x, y1, color = 'red', linewidth=1.0, linestyle='--')
# ### 若需要同一个figure绘制多个曲线，则在同一个plt.figure()下面添加多个plt.plot()
# ### plt.figure()可设置参数规定figure框的大小与编号
# ### plt.plot()的参数可以设置线条的特征
#
# plt.show()

######################################################################
###################          坐标轴设置            ###################
######################################################################
# x = np.linspace(-3, 3, 50)
# y1 = 2*x+1
# y2 = x**2
#
# plt.figure(num=3,figsize=(8, 5))
# plt.plot(x, y2)
# plt.plot(x, y1, color = 'red', linewidth=1.0, linestyle='--')
#
# plt.xlim((-1,2))  #坐标轴范围，注意用区间表示
# plt.ylim((-2,3))
# plt.xlabel('I am X')   #坐标轴名称，单引号
# plt.ylabel('I am Y')
#
# new_ticks = np.linspace(-1,2,5)
# print new_ticks
# plt.xticks(new_ticks) #坐标轴的刻度范围
# #plt.yticks([-2, -1.8, -1, 1.22, 3], ['really bad', 'bad', 'normal', 'good', 'really good'])
# ### 文字型坐标轴刻度范围，注意需要有数字一一对应
# #plt.yticks([-2, -1.8, -1, 1.22, 3], ['r$really\ bad$', 'bad', r'$normal$', r'$good$', r'$really\ good$'])
# ### 改变文字字体
# plt.yticks([-2, -1.8, -1, 1.22, 3], ['r$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])
# ### 打印特殊符号
#
# ax = plt.gca() # gca = 'get current axis'；即，将现有的figure中的坐标轴提取出来
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# #spines指的是figure的矩形边框，有“上、下、左、右”之分
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# # 指定哪些边框作x轴和y轴
# ax.spines['bottom'].set_position(('data', -1))
# #对X轴定义其在Y轴的位值，data表示坐标轴的值进行参数传递
# #data还可以替换为outward,axes等
# ax.spines['left'].set_position(('data', 0))
#
# plt.show()

######################################################################
#####################          Legend            #####################
######################################################################
# x = np.linspace(-3, 3, 50)
# y1 = 2*x+1
# y2 = x**2
#
# plt.figure(num=3,figsize=(8, 5))
# plt.xlim((-1,2))
# plt.ylim((-2,3))
# plt.xlabel('I am X')
# plt.ylabel('I am Y')
# new_ticks = np.linspace(-1,2,5)
# print new_ticks
# plt.xticks(new_ticks)
# plt.yticks([-2, -1.8, -1, 1.22, 3], ['r$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data', -1))
# ax.spines['left'].set_position(('data', 0))
#
# l1,=plt.plot(x, y2, label='up')
# l2,=plt.plot(x, y1, color = 'red', linewidth=1.0, linestyle='--', label='down')
# ## plt.legend() #各个函数获得label后可以生成默认的legend
# plt.legend(handles = [l1,l2,], labels = ['aaa','bbb'], loc='best')
# ## handles用于传递图像对应的函数，注意变量名后面需要加'，';
# ## handles可以只传递一个参数，则另一条曲线不会显示label
# ## labels可以为相应的图像命名
# #loc可以有best, upper right等
# plt.show()

######################################################################
#######################       Annotation           ###################
######################################################################
# x = np.linspace(-3, 3, 50)
# y = 2*x+1
#
# plt.figure(num=3,figsize=(8, 5))
# ## plt.scatter(x,y) 绘制散点图
# plt.plot(x,y)
#
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data', -1))
# ax.spines['left'].set_position(('data', 0))
#
# x0 = 1
# y0 = 2*x0 + 1
# plt.scatter(x0,y0,s=50,color='b')
# #图像中标注某个点，先画背景曲线，然后绘制点或线
# #s是半径
# plt.plot([x0,x0],[y0,-1],'k--',lw=2.5)
# # 两点之间连成一条直线
#
# ###################  Annotation Method 1  ###################
# plt.annotate(r'$2x+1==%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(30, -30), textcoords='offset points',
#             fontsize = 16, arrowprops={'arrowstyle': '->', 'connectionstyle': 'arc3,rad=.2'})
# ## 第一个参数表示注释的文字内容，第二个参数表示注释指向的数据点，第三个参数表示xy参数作为之后所有操作的对象
# ## 第五个参数表示偏离对象点，第四个参数表示偏离的距离；如果不加textcoords，则默认以原点为中心来安排位置
# ## fontsize是字体大小，arrowprops是画箭头
#
# ###################  Annotation Method 2  ###################
# plt.text(-3.7,3,r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i \ \alpha_t$',
#          fontdict={'size':16,'color':'r'})
# ## 开始的两个参数是text在坐标轴的位置，第二个参数是文本内容，注意空格需要转换
# ## fontdict集合相关的所有参数
# plt.show()

######################################################################
#######################           能见度           ###################
######################################################################
# x = np.linspace(-3, 3, 50)
# y = 0.1*x
#
# plt.figure()
# plt.plot(x,y, linewidth = 10)
# plt.ylim(-2,2)
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['left'].set_position(('data', 0))
#
# for label in ax.get_xticklabels() + ax.get_yticklabels():
#     label.set_fontsize(12)
#     label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))
#
# plt.show()

######################################################################
#######################         散 点 图           ###################
######################################################################
# n = 1024
# x = np.random.normal(0,1,n) #随机数，均数-sd-数量
# y = np.random.normal(0,1,n)
# t = np.arctan2(y,x) #随机颜色
#
# #plt.scatter(x,y,s=75,c=t,alpha=0.5)
# plt.scatter(np.arange(5),np.arange(5)) #绘制直线的散点，无非是把plot改为scatter
#
# plt.xlim((-1.5,1.5))
# plt.ylim((-1.5,1.5))
# plt.xticks(()) #隐藏坐标轴刻度
# plt.yticks(())
#
# plt.show()

######################################################################
#######################         柱 状 图           ###################
######################################################################
# n = 12
# x = np.arange(n)
# y1 = (1-x/float(n))*np.random.uniform(0.5,1.0,n)
# y2 = (1-x/float(n))*np.random.uniform(0.5,1.0,n)
#
# plt.bar(x,+y1, facecolor = '#9999ff', edgecolor = 'white')
# plt.bar(x,-y2, facecolor = '#ff9999', edgecolor = 'white')
#
# for i,j in zip(x,y1):
#     plt.text(i, j + 0.05, '%.2f' %j, ha = 'center', va = 'bottom')
# for i,j in zip(x,y2):
#     plt.text(i, -j-0.05,'%.2f' %j, ha = 'center', va = 'top')
#
# # zip的作用是将x和y1同时传递给i，j
# # %.2f表示保留两位小数，ha是水平对齐，va是垂直对齐
#
# plt.xlim(-0.5, n)
# plt.xticks(())
# plt.ylim(-1.25, 1.25)
# plt.yticks(())
#
# plt.show()

######################################################################
#######################         柱 状 图           ###################
######################################################################
# def f(x,y):
#     return (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
#
# n = 256
# x = np.linspace(-3,3,n)
# y = np.linspace(-3,3,n)
# x,y = np.meshgrid(x,y)
#
# plt.contourf(x,y,f(x,y),8, alpha=0.75, cmap = plt.cm.hot) #8表示分层，即等高线有几条
# c = plt.contour(x,y,f(x,y),8,colors = 'black', linewidth = 0.5)
# plt.clabel(c,inline = True, fontsize = 10) #inline表示是否将标注数字放进线条里
#
# plt.xticks(())
# plt.yticks(())
#
# plt.show()

######################################################################
#######################         图    片           ###################
######################################################################
# a = np.array([0.31366,0.36534,0.42373,
#               0.36562,0.43959,0.52508,
#               0.42373,0.52508,0.65153]).reshape(3,3)
#
# plt.imshow(a,interpolation='nearest', cmap='bone',origin='upper')
# #lower表示黑色在下边，upper表示黑色在上边
# #interpolation表示数字排列方法
# plt.colorbar()
#
# plt.xticks(())
# plt.yticks(())
# plt.show()

######################################################################
#######################          3D制图            ###################
######################################################################
# fig = plt.figure()
# #定义图片窗口
# ax = Axes3D(fig)
# #在窗口中添加三维坐标轴
#
# x = np.arange(-4,4,0.25)
# y = np.arange(-4,4,0.25)
# x,y = np.meshgrid(x,y)
# # 将x和y映射至底面的平面中
# r = np.sqrt(x**2+y**2)
# z = np.sin(r)
#
# ax.plot_surface(x,y,z,rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# # rstride和cstride是曲线跨度，值越大则图越粗糙
# ax.contourf(x, y, z, zdir='z', offset=-2, cmap = 'rainbow')
# # zdir表示从哪一个方向将3D图像压扁；offset表示从原点偏移多少位置
# ax.set_zlim(-2,2)
# # 固定z坐标轴的刻度范围
#
# plt.show()

######################################################################
#######################        多合一显示          ###################
######################################################################
# plt.figure()
#
# ###  Method 1  ###
# # plt.subplot(2,2,1)
# # # 2行2列的第一个位置填图
# # plt.plot([0,1],[0,1])
# # plt.subplot(222)
# # plt.plot([0,1],[0,2])
# # #注意是从左往右，从上往下数
# # plt.subplot(223)
# # plt.plot([0,2],[0,1])
# # plt.subplot(224)
# # plt.plot([2,0],[0,1])
#
# ###  Method 2  ###
# plt.subplot(2,1,1)
# plt.plot([0,1],[0,1])
#
# plt.subplot(234)
# plt.plot([0,1],[0,2])
# #注意是从左往右，从上往下数
# plt.subplot(235)
# plt.plot([0,2],[0,1])
# plt.subplot(236)
# plt.plot([2,0],[0,1])
#
# plt.show()

######################################################################
#######################         分格显示           ###################
######################################################################

#################    Method 1 subplot2grid     #################
# plt.figure()
# ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
# ax1.plot([1,2],[1,2])
# ax1.set_title('ax1_title')
# # colspan表示跨越三列，rowspan表示跨越1行，这两个参数默认为1
# # 注意是从0开始计数，即0行0列的格子
# ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)
# ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)
# ax2 = plt.subplot2grid((3,3),(2,0))
# ax2 = plt.subplot2grid((3,3),(2,1))
#
# plt.show()

#################    Method 2 gridspec     #################
# import matplotlib.gridspec as gridspec
#
# plt.figure()
# gs = gridspec.GridSpec(3, 3)
# # 定义格子
# ax1 = plt.subplot(gs[0, :])
# ax2 = plt.subplot(gs[1, :2])
# ax3 = plt.subplot(gs[1:, 2])
# ax4 = plt.subplot(gs[2, 0])
# ax5 = plt.subplot(gs[2, 1])
#
# plt.tight_layout()
# # 合理布局
# plt.show()

#################    Method 3 easy define structure     #################
# f, ((ax11,ax12),(ax21,ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
# # f是plt.subplots传递的关于图像的信息,类似于plt.figure()
# # 逗号后面的内容传递的是格子的排列信息
# # sharex表示是否共享x轴
# ax11.scatter([1,2],[1,2])
#
# plt.tight_layout()
# plt.show()

######################################################################
#######################          图中图            ###################
######################################################################
# fig = plt.figure()
# x = [1,2,3,4,5,6,7]
# y = [1,3,4,2,5,8,6]
#
# left,bottom,width,height = 0.1,0.1,0.8,0.8
# ax1 = fig.add_axes([left,bottom,width,height])
# # 添加坐标轴，数字表示的是比例，也就是相对左侧10%，相对底边10%
# ax1.plot(x,y,'r')
# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax1.set_title('title')
#
# left,bottom,width,height = 0.2,0.6,0.25,0.25
# ax2 = fig.add_axes([left,bottom,width,height])
# # 添加坐标轴，数字表示的是比例，也就是相对左侧10%，相对底边10%
# ax2.plot(y,x,'b')
# ax2.set_xlabel('x')
# ax2.set_ylabel('y')
# ax2.set_title('title inside 1')
#
# plt.axes([0.6,0.2,0.25,0.25])
# plt.plot(y[::-1],x,'g')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('title inside 2')
#
# plt.show()

######################################################################
#######################         次坐标轴           ###################
######################################################################
# x = np.arange(0,10,0.1)
# y1 = 0.05*x**2
# y2 = -1*y1
#
# fig,ax1 = plt.subplots()
# # 结合上一个实例，fig相当于figure信息，ax1是坐标轴信息
# ax2 = ax1.twinx()
# # 坐标轴镜像翻转
# ax1.plot(x,y1,'g-')
# ax2.plot(x,y2,'b--')
#
# ax1.set_xlabel('X data')
# ax1.set_ylabel('Y1', color = 'g')
# ax2.set_ylabel('Y2',color = 'b')
#
# plt.show()

######################################################################
#######################          动  画            ###################
######################################################################
# from matplotlib import animation
#
# fig,ax = plt.subplots()
#
# x = np.arange(0,2*np.pi,0.01)
# line, = ax.plot(x, np.sin(x))
#
# def animate(i):
#     #i传递的是frame的值
#     line.set_ydata(np.sin(x+i/5))
#     return line,
#
# def init():
#     line.set_ydata(np.sin(x))
#     return line,
#
# ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=50, blit=True)
# # 还有其它animaition形式
# # blit， true表示更新图像变化的点，false表示更新全部图像
# # frames是动画的帧数
# # interval是更新频率
#
# plt.show()