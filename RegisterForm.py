from wtforms import Form, StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, Email, Regexp, EqualTo
from flask_wtf import FlaskForm
from mysql_util import MysqlUtil


# Register Form Class
class RegisterForm(FlaskForm):
    username = StringField(
        '用户名',
        validators=[
            DataRequired(message='请输入用户名'),
            Length(min=2, max=25, message='长度在4-25个字符之间')
        ]
    )
    email = StringField(
        '邮箱',
        validators=[
            DataRequired(message='邮箱不能为空'), Email(message="邮箱格式输入有误")
        ]
    )
    password = PasswordField(
        '密码',
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=6, max=20, message='长度在6-20个字符之间'),
            Regexp(regex="[0-9a-zA-Z]{5,}", message='密码不允许使用特殊字符'),
        ]
    )
    confirm_password = PasswordField(
        '确认密码',
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=6, max=20, message='长度在6-20个字符之间'),
            Regexp(regex="[0-9a-zA-Z]{5,}", message='密码不允许使用特殊字符'),
            EqualTo("password", message="两次密码输入必须一致"),
        ]

    )

    def validate_username(self, field):
        sql = "SELECT * FROM users  WHERE username = '%s'" % (field.data)  # 根据用户名查找user表中记录
        db = MysqlUtil()  # 实例化数据库操作类
        result = db.fetchone(sql)  # 获取一条记录
        if result:
            raise ValidationError("该用户名已被注册！")

    submit = SubmitField(
        label="用 户 注 册",
        render_kw={"class": "btn btn-success"}
    )
