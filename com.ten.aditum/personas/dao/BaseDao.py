import pymysql
from personas.entity import Record


class BaseDao:
    """
    数据库操作类
    """

    def __init__(self,
                 host='127.0.0.1',
                 port=3306, user='root',
                 password='wangshihao',
                 database='aditum_mocker',
                 charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

        # 数据库连接对象
        self.db = self.connect()

        # 数据库游标对象
        self.cursor = self.db.cursor()

        # 测试数据库连接
        self.select_version()

    # 打开数据库连接
    def connect(self):
        return pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               password=self.password,
                               database=self.database,
                               charset=self.charset)

    # 数据库连接测试: 获取数据库版本
    def select_version(self):
        # 使用 execute()  方法执行 SQL 查询
        self.cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取单条数据.
        data = self.cursor.fetchone()
        print("Database version : %s " % data)

    # 查询所有record记录
    def select_all_record(self):
        select_sql = 'SELECT id, imei, personnel_id, visite_time, visite_status, is_deleted FROM record'

        try:
            self.cursor.execute(select_sql)

            record = self.cursor.fetchone()

            print(record)
        except:
            print("select_all_record is failed")


dao = BaseDao()
dao.select_all_record()
