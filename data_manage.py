#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os


def openfile2(filename):
    f = open(filename, 'r')

    line = f.read()
    f2.write(line)

    # print line
    xx = line.split('\n')
    # print (xx[1].split(' '))
    for i in range(len(xx)):
        print '虚拟机ID',xx[i].split('\t')[0]
        print '虚拟机规格名称', xx[i].split('\t')[1]
        print '创建时间', xx[i].split('\t')[2]
    f.close()

def managedata(filename):
    f = open(filename, 'r')
    fname = {'flavor1':'flavor1.txt','flavor2':'flavor2.txt','flavor3':'flavor3.txt','flavor4':'flavor4.txt','flavor5':'flavor5.txt','flavor6':'flavor6.txt','flavor7':'flavor7.txt','flavor8':'flavor8.txt','flavor9':'flavor9.txt','flavor10':'flavor10.txt','flavor11':'flavor11.txt','flavor12':'flavor12.txt','flavor13':'flavor13.txt','flavor14':'flavor14.txt','flavor15':'flavor15.txt'}
    # for i in range(15):
    #     fnn = open('flavor'+str(i+1), 'w')
    # print fnn

    line = f.read()
    xx = line.split('\n')
    print len(xx)
    print xx
    # # print (xx[1].split(' '))
    for i in range(len(xx)):
        # print '虚拟机ID', xx[i].split('\t')[0]
        # print '虚拟机规格名称', xx[i].split('\t')[1]
        # print '创建时间', xx[i].split('\t')[2]
        keys = xx[i].split('\t')[1]
        # print keys
        if keys in fname:
            fnn = open(fname[keys], 'a')
            fnn.write(xx[i].split('\t')[0]+' '+xx[i].split('\t')[1]+' '+xx[i].split('\t')[2]+'\n')
            # .write(line)
        else:
            pass

    f.close()


f2 = open('data_managed.txt', 'w')
files = ['data_2015_1.txt', 'data_2015_2.txt', 'data_2015_3.txt','data_2015_4.txt','data_2015_5.txt','data_2015_12.txt', 'data_2016_1.txt']
if __name__ == '__main__':
    for i in range(7):
        filename2 = files[i]
        print filename2
        openfile2(filename2)
    f2.close()
    managedata('data_managed.txt')






