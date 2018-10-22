## flask 目录架构

### git地址

```
https://github.com/Hughendman/flask-program

```

### 目录结构

```
| - projectName
	| - app  //程序包
		| - templates //jinjia2模板
		|- static //css,js 图片等静态文件
		| - main  //py程序包 ，可以有多个这种包，每个对应不同的功能
			| - __init__.py
			|- errors.py
		|- __init__.py
		| - models  //数据库模型
			| - __init__.py
			|- models.py
	| - tests  //单元测试
		|- __init__.py
		|- test*.py //单元测试程序，可以包含多个对应不同的功能点测试
	|- venv  //虚拟环境
	|- requirements.txt //列出了所有依赖包以及版本号，方便在其他位置生成相同的虚拟环境以及依赖
	|- config.py //全局配置文件，配置全局变量
	|- manage.py //启动程序

```

### 启动命令

```
python manage.py runserver -p 9033

```

### 自动生成Sqlalchemy的models文件

#### 安装sqlacodegen

```
pip install sqlacodegen

```

#### 使用

```
sqlacodegen mysql://root:abcd234@localhost:3306/superset_board?charset=utf8mb4 > models.py

```

### 开发文档

#### 开发接口

```
| - projectName
	| - app
		| - templates
		|- static
		| - main
			| - __init__.py
			|- errors.py
        | - auth //接口文件
			| - __init__.py
			|- users.py
		|- __init__.py
		| - models
			| - __init__.py
			|- models.py
	| - tests
		|- __init__.py
		|- test*.py
	|- requirements.txt
	|- config.py
	|- manage.py

```
auth/__init__.py
```
from flask import Blueprint

auth = Blueprint('auth', __name__)

from .users import *
```
auth/users.py

```
from flask import jsonify
from app.models import *
from app.auth import auth

@auth.route('/user', methods=['GET', 'POST'])
def user():
    jsonResponse = dict(name="yinxs", auth="admin")
    response = jsonify(jsonResponse)
    return response

@auth.route('/module', methods=['GET', 'POST'])
def module():
    authPermission = AuthPermission.query.all()
    auth = json.dumps(authPermission, cls=AlchemyEncoder)
    return auth

```
app/__init__.py

```
# 增加auth蓝本
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

```

#### 数据库配置

config.py
```
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:abcd234@localhost:3306/superset_board?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

```

采用的SQLAlchemy，
处理json
models/models.py
```
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    else:
                        fields[field] = None
                if "query" in fields:
                    del fields["query"]
                if "query_class" in fields:
                    del fields["query_class"]
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)

```

### 自动生成依赖包

```
pip freeze > requirements.txt

```

### 安装依赖包

```
pip install -r Requirements.txt

```

### 版本
10-18 first commit
10-22 mysqldb commit
