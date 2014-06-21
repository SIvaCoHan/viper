#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

import unittest

from basesite import create_app
from basesite import configs
from basesite.configs import db, cache
from basesite.models import *


class TestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.app = create_app(configs.TestConfig)
        self.app.config['TESTING'] = True
        super(TestCase, self).__init__(*args, **kwargs)

    def setUp(self):
        self.client = self.app.test_client()
        with self.app.app_context():
            db.drop_all()
            db.create_all()
        return

    def tearDown(self):
        return
