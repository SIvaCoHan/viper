#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Author: SivaCoHan <sivacohan@gmail.com>
# Date: 2014-06-21
# File: test_user.py

import json
from tests import TestCase


class TestSite(TestCase):

    def test_site(self):

        resp = self.client.get('/user/register')
        self.assertEqual(resp.data, """Register here""")
