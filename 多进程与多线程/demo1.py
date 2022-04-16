from threading import Thread

def func(name):
    for i in range(1000):
        print(name,i)



# class MYTheard(Thread):
#     def run(self):
#         for i in range(100):
#             print("多进程",i)

if __name__ == '__main__':
    t = Thread(target=func,args=("周杰伦",))#必须跟一个元组
    t.start()#多线程任务可以开始
    # for i in range(100):
    #     print('主线程',i)
    s = Thread(target=func, args=("任嘉伦", ))
    s.start()  # 多线程任务可以开始