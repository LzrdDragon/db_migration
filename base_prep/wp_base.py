from sqlalchemy import Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

from connection_prep.sqlalchemy_connection import engines


def get_wp_tables():
    engine_wp = engines['wp']

    metadata = MetaData()

    metadata.reflect(
        engine_wp,
        only=[
            'wpnb_users',
            'wpnb_posts',
            'wpnb_comments',
            'wpnb_6be3_wau_payments',
            'wpnb_6be3_wau_tariffs',
            'wpnb_ulike',
            'wpnb_terms',
            'wpnb_term_relationships',
        ]
    )

    Base = automap_base(metadata=metadata)

    Base.prepare()

    UserWP, PostWP, CommentWP, PaymentWP, TariffWP, ReactionsWP, TermsWP, TermsRelationshipsWP = \
        Base.classes.wpnb_users, \
        Base.classes.wpnb_posts, \
        Base.classes.wpnb_comments, \
        Base.classes.wpnb_6be3_wau_payments, \
        Base.classes.wpnb_6be3_wau_tariffs, \
        Base.classes.wpnb_ulike, \
        Base.classes.wpnb_terms, \
        Base.classes.wpnb_term_relationships

    return UserWP, PostWP, CommentWP, PaymentWP, TariffWP, ReactionsWP, TermsWP, TermsRelationshipsWP


# Base = declarative_base()
#
#
# class UsersWp(Base):
#     __table__ = Table('users', Base.metadata, autoload=True, autoload_with=engines['wp'])


if __name__ == '__main__':
    print('wp_base has ran')
