# -*- coding: utf-8 -*-

from odoo import models, fields, api

import urllib
import json

global null
null = ''

class kuaidi100(models.Model):
    _name = 'kuaidi100.kuaidi100'

    express_company = fields.Char(u"快递公司",required=True)
    express_order = fields.Char(u"快递单号",required=True)
    express_message = fields.Text(u"快递信息")

    @api.multi
    def getHtml(self):
        page = urllib.urlopen("http://www.kuaidi100.com/query?type=%s&postid=%s" % (self.express_company,self.express_order))
        html = page.read()

        data = eval(html) #方法一，将str转换成dict

        data1 = json.loads(html) #方法二，将str转换成dict
        data2 = tuple(data1)


        print data
        print type(data1)
        print type(html)
        print type(data1)
        print type(data2)

        self.express_message=data

    #html = getHtml("http://www.kuaidi100.com/query?type=yuantong&postid=888688423729498670")

