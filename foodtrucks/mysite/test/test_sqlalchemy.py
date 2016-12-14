from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, types
from sqlalchemy.dialects.mssql import *
import os
import unittest


def get_type_name(col_type):
    if col_type == types.NULLTYPE:
        ret_type = "Geometry"
    else:
        ret_type = col_type.__class__.__name__
        if ret_type == INTEGER.__name__:
            ret_type = "db.Integer"
        elif ret_type == VARCHAR.__name__ or ret_type == NVARCHAR.__name__ or ret_type == NTEXT.__name__ or ret_type == TEXT.__name__:
            ret_type = "db.String(500)"
        elif ret_type == DECIMAL.__name__ or ret_type == FLOAT.__name__:
            ret_type = "db.DECIMAL(18,2)"
        elif ret_type == DATETIME.__name__:
            ret_type = "db.DateTime"
        elif ret_type == "TINYINT":
            ret_type = "db.Boolean(1)"
        elif ret_type == UNIQUEIDENTIFIER.__name__:
            ret_type = "GUID"
        else:
            ret_type = "db." + ret_type
    return ret_type


class TestCase(unittest.TestCase):

    def test_generate_model(self):
        app = Flask(__name__)

        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost:3306/mydb?charset=utf8"
        app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

        db = SQLAlchemy(app)

        inspector = inspect(db.engine)

        output = []

        try:
            for table_name in inspector.get_table_names("mydb", None):
                if table_name:
                    class_name = str(table_name.strip(os.linesep)).title().replace("_", "")
                    table_name = table_name.strip(os.linesep)
                    print "####", table_name
                    output.append(os.linesep)
                    output.append(os.linesep)
                    output.append(os.linesep)
                    output.append("class {0}(CommonRootModel, db.Model):".format(class_name))
                    output.append(os.linesep)
                    output.append("    __tablename__ = '{0}'".format(table_name.lower()))
                    output.append(os.linesep)
                    for column in inspector.get_columns(table_name):
                        output.append(os.linesep)

                        col_type = get_type_name(column['type'])

                        if "autoincrement" in column:
                            if column['autoincrement'] is True:
                                output.append("    {0} = db.Column({1}, nullable={2}, autoincrement=True, primary_key=True)".format(str(column['name']).lower(), col_type,
                                                                                                                  str(column['nullable'])))
                            else:
                                output.append("    {0} = db.Column({1}, nullable={2})".format(str(column['name']).lower(), col_type, str(column['nullable'])))
                        else:
                            output.append("    {0} = db.Column({1}, nullable={2})".format(str(column['name']).lower(), col_type, str(column['nullable'])))
                else:
                    continue

        finally:
            f_out = open("outmodel.txt", "w")

            f_out.write(''.join(output))
            f_out.flush()
            f_out.close()
            print 'ok'
