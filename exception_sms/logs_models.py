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
    def __init__(self, access_key, secret_key, template_id, author, phone: str or list, log_path, local=None,
                 mail=None):
        """
        To init the class
        :param access_key: The access_key of qiniuyun
        :param secret_key: The secret_key of qiniuyun
        :param template_id: The template_id of qiniuyun
        :param author: The author of the function which catched exceptions
        :param phone: The phone number of author
        :param log_path: The absolute path of the log files
        :param local: The localtion function which catched exceptions
        :param mail: The mail object
        """
        from qiniu import QiniuMacAuth, Sms
        self.access_key = access_key
        self.secret_key = secret_key
        self.template_id = template_id
        self.author = author
        self.phone = self.get_phone_list(phone)
        if self.access_key and self.secret_key:
            self.auth = QiniuMacAuth(self.access_key, self.secret_key)
            self.smser = Sms(self.auth)
        self.log_path = log_path
        self.local = local
        self.mail = mail

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
                if self.access_key and self.secret_key:
                    self.smser.sendMessage(self.template_id, self.phone, self.get_params(e, name))
                logger = FinalLogger(self.log_path)
                string = format_exc()
                message = f"{str(self.local)}\n\n{str(string)}\n\n" if self.local else str(string)
                logger.get_logs(message)
                if self.mail:
                    with open(self.mail.file, "w+", encoding="utf-8") as f:
                        f.write(message)
                    self.mail.send_mail()
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
