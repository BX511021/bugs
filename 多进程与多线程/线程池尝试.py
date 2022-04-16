from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fn(url):
    for i in range(1000):
        print(url,i)

if __name__ == '__main__':
    with ThreadPoolExecutor(50) as T:
        for i in range(100):
            T.submit(fn, url=f"线程{i}")
    #线程池任务结束后执行
    print("over!!")
