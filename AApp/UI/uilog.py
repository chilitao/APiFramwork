#coding=gbk
import logging
import os.path
import time
from colorama import Fore, Style
import sys


class Logger(object):
    def __init__(self, logger):
        """
        ָ��������־���ļ�·������־�����Լ������ļ�
        ����־���뵽ָ�����ļ���
        :param logger:  �����Ӧ�ĳ���ģ����name��Ĭ��Ϊroot
        """

        # ����һ��logger
        self.logger = logging.getLogger(name=logger)
        self.logger.setLevel(logging.DEBUG)  # ָ����͵���־���� critical > error > warning > info > debug

        # ����һ��handler������д����־�ļ�
        rq = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
        log_path = os.getcwd() + "\\logs\\"
        log_name = log_path + rq + ".log"
        #  ��������жϣ����logger.handlers�б�Ϊ�գ�����ӣ�����ֱ��ȥд��־������ظ���ӡ������
        if not self.logger.handlers:
            # ����һ��handler���������������̨
            ch = logging.StreamHandler(sys.stdout)
            ch.setLevel(logging.DEBUG)

            # ����handler�������ʽ
            formatter = logging.Formatter(
                "%(asctime)s - %(filename)s[line:%(lineno)d] - %(name)s - %(message)s")
            ch.setFormatter(formatter)

            # ��logger���handler
            # self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    def debug(self, msg):
        """
        �����������ɫdebug--white��info--green��warning/error/critical--red
        :param msg: �����log����
        :return:
        """
        self.logger.debug(Fore.WHITE + "DEBUG - " + str(msg) + Style.RESET_ALL)

    def info(self, msg):
        self.logger.info(Fore.GREEN + "INFO - " + str(msg) + Style.RESET_ALL)

    def warning(self, msg):
        self.logger.warning(Fore.RED + "WARNING - " + str(msg) + Style.RESET_ALL)

    def error(self, msg):
        self.logger.error(Fore.RED + "ERROR - " + str(msg) + Style.RESET_ALL)

    def critical(self, msg):
        self.logger.critical(Fore.RED + "CRITICAL - " + str(msg) + Style.RESET_ALL)


if __name__ == '__main__':
    log = Logger(logger="test")
    log.debug("debug")
    log.info("info")
    log.error("error")
    log.warning("warning")
    log.critical("critical")