#!/usr/bin/env Python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')




def openfile1(filename):
    f = open(filename, 'r')
    line = f.read()
    # print line
    xx = line.split('\n')
    # print xx
    print '物理服务器CPU核数:', xx[0].split(' ')[0]
    print '内存大小（GB）:', xx[0].split(' ')[1]
    print '硬盘大小（GB）:', xx[0].split(' ')[2]
    print '虚拟机规格数量:', xx[2]
    mm = int(xx[2])
    for i in range(mm):
        print '虚拟机规格名称:' + str(i + 1), xx[3 + i].split(' ')[0]
        print 'CPU核数:', xx[3 + i].split(' ')[1]
        print '内存大小（MB）:', xx[3 + i].split(' ')[2]

    print '预测开始时间:', xx[3 + mm + 1 + 2]
    print '预测结束时间:', xx[3 + mm + 1 + 3]

    f.close()

def openfile2(filename):
    f = open(filename, 'r')
    line = f.read()
    # print line
    xx = line.split('\n')
    # print (xx[1].split(' '))
    for i in range(len(xx)):
        print '虚拟机ID',xx[i].split('\t')[0]
        print '虚拟机规格名称', xx[i].split('\t')[1]
        print '创建时间', xx[i].split('\t')[2]


if __name__ == '__main__':
    filename1 = 'input_5flavors_cpu_7days.txt'
    openfile1(filename1)
    filename2 = 'TrainData_2015.1.1_2015.2.19.txt'
    openfile2(filename2)





