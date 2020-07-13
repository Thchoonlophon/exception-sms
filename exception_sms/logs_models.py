# python3.7
# encoding: utf-8
"""
@author: Chenjin.Qian
@email:  chenjin.qian@xquant.com
@file:   logs_models.py
@time:   2020-07-09 13:15
"""
from traceback import format_exc

from exception_sms.to_get_logs import FinalLogger


class GetNotification(object):
    def __init__(self, access_key, secret_key, template_id, author, phone: str or list, log_path):
        from qiniu import QiniuMacAuth, Sms
        self.access_key = access_key
        self.secret_key = secret_key
        self.template_id = template_id
        self.author = author
        self.phone = self.get_phone_list(phone)
        self.auth = QiniuMacAuth(self.access_key, self.secret_key)
        self.smser = Sms(self.auth)
        self.log_path = log_path

    @staticmethod
    def get_phone_list(phone):
        if type(phone) == str:
            if "," in phone:
                phone_list = phone.split(",")
            else:
                phone_list = [phone]
        else:
            phone_list = phone
        return phone_list

    def exce_note(self, func):
        def get_info(*args, **kwargs):
            name, res = func.__name__, None
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                self.smser.sendMessage(self.template_id, self.phone, self.get_params(e, name))
                logger = FinalLogger(self.log_path)
                logger.get_logs(format_exc())
            finally:
                return res

        return get_info

    def get_params(self, exece, func_name):
        params = dict()
        params["api_name"] = f"{func_name} 函数"
        params["name"] = self.author
        message = f"{func_name} 函数报错 {exece}"
        params["code"] = message
        return params
