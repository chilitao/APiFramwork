# -*- coding:utf-8 -*-
from Common.Run import *
import requests
from Common.Token import *
import unittest
class GZWechat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def test_1(self):
        Result=runner(1,Region='CN')
        self.assertIn('errno',Result,"导航列表查询失败")
    def test_2(self):
        Result=runner(2,Region='CN')
        print(Result)
        self.assertIn('errno',Result,"视频列表查询失败")
    def test_3(self):
        Result=runner(3,Region='CN')
        print(Result)
        self.assertIn('errno',Result,"云控列表查询失败")

    def test_4(self):
        Result = runner(4, Region='CN')
        print(Result)
        self.assertIn('errno', Result, "奇料段子列表查询失败")
    def test_5(self):
        Result = runner(5, Region='CN')
        print(Result)
        self.assertIn('errno', Result, "热词列表查询失败")
    def test_6(self):
        Result = runner(6, Region='CN')
        print(Result)
        self.assertIn('result', Result, "热词列表查询失败")