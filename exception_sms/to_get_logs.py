# C:\Python3.6
# -*- coding:utf-8 -*-
# Project: send_log
# File   : get_log
# @Author: Chenjin QIAN
# @Time  : 2018-09-05 08:27

import time
import os
import logging.handlers


class FinalLogger(object):
    def __init__(self, path):
        self.path = os.path.join(path, time.strftime("%Y%m%d"))
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.log_file = f"{time.strftime('%Y%m%d')}logs.log"
        self.log_path = os.path.join(self.path, self.log_file)

    logger = None

    levels = {"n": logging.NOTSET,
              "d": logging.DEBUG,
              "i": logging.INFO,
              "w": logging.WARN,
              "e": logging.ERROR,
              "c": logging.CRITICAL}

    log_level = "e"
    log_max_byte = 10 * 1024 * 1024
    log_backup_count = 5

    def get_logger(self):
        if FinalLogger.logger is not None:
            return FinalLogger.logger

        FinalLogger.logger = logging.Logger("oggingmodule.FinalLogger")
        log_handler = logging.handlers.RotatingFileHandler(
            filename=self.log_path,
            maxBytes=FinalLogger.log_max_byte,
            backupCount=FinalLogger.log_backup_count
        )
        log_fmt = logging.Formatter("[%(levelname)s][%(asctime)s]%(message)s")
        log_handler.setFormatter(log_fmt)
        FinalLogger.logger.addHandler(log_handler)
        FinalLogger.logger.setLevel(FinalLogger.levels.get(FinalLogger.log_level))
        return FinalLogger.logger

    def get_logs(self, message):
        the_logger = self.get_logger()
        the_logger.error(f"{str(message)}\n\n")
