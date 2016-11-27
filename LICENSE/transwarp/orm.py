#encoding:utf-8
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
print "success"
session = DBSession()
new_user = User(id='7', name='Mike')
session.add(new_user)
session.commit()
session.close()

session = DBSession()
user = session.query(User).filter(User.id=='5').one()
print 'type:', type(user)
print 'name:', user.name
session.close()
