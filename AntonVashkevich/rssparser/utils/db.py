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

Base.metadata.create_all(engine, checkfirst=True)

session = Session(bind=engine)


@logger
def insert_data(data):
    data = json.loads(data)
    for i in data["content"]:
        item = Archive(feed=data.get("info").get("link"),
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
def get_articles_by_date(date, link=None, limit=None):
    date = datetime.datetime.strptime(date, "%Y%m%d").date()
    if link:
        q = session.query(Archive).filter_by(date=date, feed=link).all()
    else:
        q = session.query(Archive).filter_by(date=date).all()
    print(q)
    header = f"News archive\nDate:{date}\nFeed:{link if link else 'all feeds'}\n"
    content = "".join([f"\nTitle: {article.title}\n"
                       f"Pubdate: {article.date}\n"
                       f"Description: {article.description}\n"
                       f"Link: {article.link}\n"f""
                       f"Media: {article.media}\n"
                       for article in q[:limit]]
                      )
    if not content:
        raise FileNotFoundError(f"File not Found 'date:{date}, link:{link}'")
    return header+content


def get_json(date, link=None, limit=None):
    date = datetime.datetime.strptime(date, "%Y%m%d").date()
    if link:
        q = session.query(Archive).filter_by(date=date, feed=link).all()
    else:
        q = session.query(Archive).filter_by(date=date).all()
    r = {"info": link if link else "all feeds",
                    "content": [{"title": i.title,
                                 "pubDate": str(i.date),
                                 "description": i.description,
                                 "link": i.link,
                                 "media": i.media}
                                for i in q[:limit]]}
    return json.dumps(r)
