# -*- coding:UTF-8-*-
# 冒泡排序
def bubbleSort(numbers):
    for j in xrange(len(numbers) -1,-1,-1):
        for i in xrange(j):
            if numbers[i] > numbers[i+1]:   # 把数值小的放在顶端
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
            print numbers
def main():
    numbers = [23,12,9,15,6]
    bubbleSort(numbers)
if __name__ == '__name__':
    main()
