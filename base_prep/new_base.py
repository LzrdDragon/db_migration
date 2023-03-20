from sqlalchemy import Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

from connection_prep.sqlalchemy_connection import engines


def get_new_tables():
    engine_new = engines['new']

    metadata = MetaData()

    metadata.reflect(
        engine_new,
        only=[
            'users',
            'posts',
            'comments',
            'user_to_tariffs',
            'tariff_modifications',
            'reactions',
            'sub_categories',
            'post_to_sub_categories',
            'categories'
        ]
    )

    Base = automap_base(metadata=metadata)

    Base.prepare()

    UserNew, PostNew, CommentNew, UserToTariffNew, TariffModificationsNew, \
    ReactionsNew, SubCategoriesNew, PostToSubCategoriesNew, CategoriesNew = \
        Base.classes.users, \
        Base.classes.posts, \
        Base.classes.comments, \
        Base.classes.user_to_tariffs, \
        Base.classes.tariff_modifications, \
        Base.classes.reactions, \
        Base.classes.sub_categories, \
        Base.classes.post_to_sub_categories, \
        Base.classes.categories

    return UserNew, PostNew, CommentNew, UserToTariffNew, TariffModificationsNew, \
           ReactionsNew, SubCategoriesNew, PostToSubCategoriesNew, CategoriesNew


# Base = declarative_base()
#
#
# class UsersWp(Base):
#     __table__ = Table('users', Base.metadata, autoload=True, autoload_with=engines['wp'])


if __name__ == '__main__':
    print('new_base has ran')
