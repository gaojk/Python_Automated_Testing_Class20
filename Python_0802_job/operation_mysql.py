# @Time :2019/8/3 17:41
# @Author :jinbiao

import pymysql
from Python_0802_job import operation_config


class OperationMysql:
    """
    操作mysql数据库
    """
    config = operation_config.do_conifg
    host = config.get_value(section="MYSQL", option="host")
    user = config.get_value(section="MYSQL", option="username")
    pwd = config.get_value(section="MYSQL", option="password")
    port = config.get_int_value(section="MYSQL", option="port")
    db = config.get_value(section="MYSQL", option="database")

    def __init__(self):
        """
        初始化实例中的数据库连接和游标对象
        """
        self.db_content = pymysql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db,
                                          port=self.port,
                                          charset="utf8", cursorclass=pymysql.cursors.DictCursor)   # 定义游标类输出结果为字典
        self.cursor = self.db_content.cursor()

    def get_value(self, sql, args=None, is_all=False):
        """
        获取SQL执行结果
        :param sql: sql语句
        :param args: sql中的参数
        :param is_all:是否返回全部数据
        :return:查询结果
        """
        self.cursor.execute(sql, args=args)
        self.db_content.commit()
        if is_all:
            value = self.cursor.fetchall()
        else:
            value = self.cursor.fetchone()
        return value

    def close_db(self):
        """
        关闭游标和数据库连接
        :return: None
        """
        self.cursor.close()
        self.db_content.close()


if __name__ == '__main__':
    mobile = 13611767797
    sql = "select * from member where MobilePhone = %s"
    mysql = OperationMysql()
    value = mysql.get_value(sql=sql, args=mobile)
    mysql.close_db()
    print(value)
