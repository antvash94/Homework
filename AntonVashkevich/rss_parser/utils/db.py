import datetime
from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import declarative_base, Session
import json
from logger import logger
from common import get_datetime

Base = declarative_base()


class Archive(Base):

      __tablename__ = "archive"
      id = Column(Integer, primary_key=True)
      feed = Column(String)
      title = Column(String)
      description = Column(String, nullable=True)
      link = Column(String)
      media = Column(String)
      date = Column(Date, default=datetime.date.today)


engine = create_engine('sqlite:///archive.db')
session = Session(bind=engine)




@logger
def insert_data(data):
    """
    Insert data to database, if data not in database
    :param data: json
    :return: None
    """
    Base.metadata.create_all(engine, checkfirst=True)
    data = json.loads(data)
    for i in data["content"]:
        item = Archive(feed=data.get("info"),
                       title=i.get("title"),
                       description=i.get("description"),
                       link=i.get("link"),
                       media=i.get("media"),
                       date=get_datetime(i.get("pubDate"))
                       )
        if bool(session.query(Archive).filter_by(link=item.link).first()) is False:
            session.add(item)
            session.commit()


@logger
def get_json_from_db(date, link=None, limit=None):
    """

    :param date:
    :param link:
    :param limit:
    :return:
    """
    date = datetime.datetime.strptime(date, "%Y%m%d").date()
    if link:
        q = session.query(Archive).filter_by(date=date, feed=link).all()
    else:
        q = session.query(Archive).filter_by(date=date).all()
    if not q:
        raise FileNotFoundError("No file in database")

    r = {"info": f"News archive\nDate:{date}\nFeed:{link if link else 'all feeds'}\n",
         "content": [{"title": i.title,
                      "pubDate": str(i.date),
                      "description": i.description,
                      "link": i.link,
                      "media": i.media} for i in q[:limit]]}
    return json.dumps(r, ensure_ascii=False)




