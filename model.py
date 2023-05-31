from sqlalchemy import Column, Integer, String, UnicodeText, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database engine
engine = create_engine('sqlite:///mydata.db')

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session object
session = Session()

Base = declarative_base()

class Journal(Base):
    __tablename__ = 'journal'

    title = Column(UnicodeText, primary_key=True)
    articles = relationship('Article')

class Category(Base):
    __tablename__ = 'category'

    name = Column(UnicodeText, primary_key=True)
    articles = relationship('Article', secondary='article_category')

class Article(Base):
    __tablename__ = 'article'

    name = Column(UnicodeText)
    doi = Column(UnicodeText)
    title = Column(UnicodeText, primary_key=True)
    contrib_authors = Column(UnicodeText, primary_key=True)
    abstract = Column(UnicodeText)
    year = Column(Integer)
    month = Column(Integer, nullable=True)
    day = Column(Integer, nullable=True)
    url = Column(UnicodeText)
    license_url = Column(UnicodeText)
    license_text = Column(UnicodeText)
    copyright_statement = Column(UnicodeText)
    copyright_holder = Column(UnicodeText)
    journal_title = Column(UnicodeText, ForeignKey('journal.title'))
    journal = relationship('Journal')
    supplementary_materials = relationship('SupplementaryMaterial')
    categories = relationship('Category', secondary='article_category')

    def __repr__(self):
        return '<Article "%s">' % self.title.encode('utf-8')

class SupplementaryMaterial(Base):
    __tablename__ = 'supplementary_material'

    label = Column(UnicodeText)
    title = Column(UnicodeText)
    caption = Column(UnicodeText)
    mimetype = Column(UnicodeText)
    mime_subtype = Column(UnicodeText)
    mimetype_reported = Column(UnicodeText)
    mime_subtype_reported = Column(UnicodeText)
    url = Column(UnicodeText, primary_key=True)
    article_title = Column(UnicodeText, ForeignKey('article.title'))
    article = relationship('Article')
    downloaded = Column(Boolean, default=False)
    converting = Column(Boolean, default=False)
    converted = Column(Boolean, default=False)
    uploaded = Column(Boolean, default=False)

    def __repr__(self):
        return '<SupplementaryMaterial "%s" of Article "%s">' % \
            (self.label.encode('utf-8'), self.article.title.encode('utf-8'))

def set_source(source):
    # Add your implementation here
    pass
