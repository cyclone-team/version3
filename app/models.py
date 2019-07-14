import json
from flask_login import UserMixin
from .exts import db

# 用户实体类 数据表user
class User(db.Model,UserMixin):
    # 表名
    __tablename__ = 'user'

    # 表的结构
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    account = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def to_json(self, message=None):
        dict = self.__dict__
        dict.pop("_sa_instance_state")
        if message is not None:
            print("additional")
            dict["msg"] = message.message
            dict["code"] = message.code
        print(dict)
        str_json = json.dumps(dict, ensure_ascii=False)
        return str_json


# 任务实体类 数据表mission
class Mission(db.Model):
    # 表的名字
    __tablename__ = 'mission'

    # 表的结构
    user_id = db.Column(db.Integer, primary_key=True,
                                nullable=False)
    start_time = db.Column(db.Time, primary_key=True, nullable=False)
    date = db.Column(db.Date, primary_key=True, nullable=False)
    stop_time = db.Column(db.Time, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    label = db.Column(db.String(20), nullable=True)
    finish = db.Column(db.Boolean, default=0, nullable=False)
    alarm_time = db.Column(db.Time, nullable=True)
    repeat = db.Column(db.Boolean, default=0, nullable=True)


    def to_json(self, message=None):
        dict = self.__dict__
        dict.pop("_sa_instance_state")
        if message is not None:
            print("additional")
            dict["msg"] = message.message
            dict["code"] = message.code
        print(dict)
        str_json = json.dumps(dict, ensure_ascii=False)
        return str_json


# 给未来的信 Mail
class Mail(db.Model):
    __tablename__ = 'mail'

    user_id = db.Column(db.Integer, primary_key=True,
                                nullable=False)
    mail_time = db.Column(db.DateTime, primary_key=True, nullable=False)
    content = db.Column(db.Text, nullable=True)

    def to_json(self, message=None):
        dict = self.__dict__
        dict.pop("_sa_instance_state")
        if message is not None:
            print("additional")
            dict["msg"] = message.message
            dict["code"] = message.code
        print(dict)
        str_json = json.dumps(dict, ensure_ascii=False)
        return str_json


# 在日历中的对某一天的评价 comment
class Comment(db.Model):
    __tablename__ = 'comment'

    user_id = db.Column(db.Integer,primary_key=True,
                                nullable=False)
    date = db.Column(db.Date, nullable=False)
    evaluate = db.Column(db.String(70), nullable=True)

    def to_json(self, message=None):
        dict = self.__dict__
        dict.pop("_sa_instance_state")
        if message is not None:
            print("additional")
            dict["msg"] = message.message
            dict["code"] = message.code
        print(dict)
        str_json = json.dumps(dict, ensure_ascii=False)
        return str_json


# 每月生成的总结
class Summary(db.Model):
    __tablename__ = 'summary'

    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    sum = db.Column(db.Text, nullable=False)


    def to_json(self, message=None):
        dict = self.__dict__
        dict.pop("_sa_instance_state")
        if message is not None:
            print("additional")
            dict["msg"] = message.message
            dict["code"] = message.code
        print(dict)
        str_json = json.dumps(dict, ensure_ascii=False)
        return str_json