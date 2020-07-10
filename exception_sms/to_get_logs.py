# C:\Python3.6
# -*- coding:utf-8 -*-
# Project: send_log
# File   : get_log
# @Author: Chenjin QIAN
# @Time  : 2018-09-05 08:27

import time
import os
import logging.handlers


date = time.strftime("%Y%m%d")
date_month = time.strftime("%Y%m")
lpath = os.path.dirname(os.path.abspath(__file__))
pre_log_path = os.path.join(lpath, "logs")
the_log_path = os.path.join(pre_log_path, date_month)
if not os.path.exists(the_log_path):
    os.makedirs(the_log_path)
log_file = "{}logs.log".format(date)
log_path = os.path.join(the_log_path, log_file)


class FinalLogger:
    logger = None

    levels = {"n": logging.NOTSET,
              "d": logging.DEBUG,
              "i": logging.INFO,
              "w": logging.WARN,
              "e": logging.ERROR,
              "c": logging.CRITICAL}

    log_level = "e"
    log_file = log_path
    log_max_byte = 10 * 1024 * 1024
    log_backup_count = 5

    @staticmethod
    def get_logger():
        if FinalLogger.logger is not None:
            return FinalLogger.logger

        FinalLogger.logger = logging.Logger("oggingmodule.FinalLogger")
        log_handler = logging.handlers.RotatingFileHandler(filename=FinalLogger.log_file,
                                                           maxBytes=FinalLogger.log_max_byte,
                                                           backupCount=FinalLogger.log_backup_count)
        log_fmt = logging.Formatter("[%(levelname)s][%(asctime)s]%(message)s")
        log_handler.setFormatter(log_fmt)
        FinalLogger.logger.addHandler(log_handler)
        FinalLogger.logger.setLevel(FinalLogger.levels.get(FinalLogger.log_level))
        return FinalLogger.logger


def get_logs(message, recv=""):
    the_logger = FinalLogger.get_logger()
    the_logger.error(str(message)+"\n\n")
    #message_mail = message.replace("\n", "<br/>")
    #sender = SendMail(recv["addr"], recv["name"], "BACKEND API ERROR", message_mail)
    #sender.send_mail()


def get_logs_only(message):
    the_logger = FinalLogger.get_logger()
    the_logger.error(str(message)+"\n\n")
