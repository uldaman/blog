# -*- coding: utf-8 -*-

import mock


'''
初始化
name mock 对象名字
spec mock 对象属性
return_value mock 对象返回值
side_effect 对象返回指定的值

调用统计
mock_calls mock 对象所有调用顺序
call_args mock 对象初始化参数
call_args_list 调用中使用参数
call_count mock 被调用次数


断语语句
assert_called_with(arg) 检查函数调用参数是否正确
assert_called_once_with(arg) 同上, 但只调用一次
assert_has_calls() 期望调用方法列表
'''

'''
attrs = ['connect', 'disconnect']
testmock = mock.Mock(name='TestMock', spec=attrs)
# testmock.connect.return_value = 200
# testmock.disconnect.return_value = 200

testmock.connect.side_effect = [200, 404, 501]

rcode = {'ok': 200, 'error': 404}

testmock.disconnect.side_effect = lambda x : rcode[x]

print testmock

# print testmock.connect()

for i in range(3):
    print testmock.connect()

# print testmock.disconnect()

print testmock.disconnect('ok')
'''

import mock

class CouldClient(object):

    def connect(self):
        pass

    def disconnect(self):
        pass


tmock = mock.Mock(CouldClient)

tmock.connect.return_value = 200

print tmock.connect()

'''
import unittest


class Count(object):

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y


class TestCount(unittest.TestCase):

    def setUp(self):
        # 构造
        self.obj = Count()

    def test_add(self):
        self.assertEqual(self.obj.add(10, 20), 30)

    @unittest.expectedFailure
    def test_sub(self):
        self.assertEqual(self.obj.sub(10, 5), 10)

    def tearDown(self):
        # 析构
        self.obj = None


if __name__ == '__main__':
    unittest.main(exit=False)
'''
