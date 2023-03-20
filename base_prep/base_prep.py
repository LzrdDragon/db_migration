from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base

from connection_prep.sqlalchemy_connection import engines


def get_tables(engine_alias: str, tables: list[str]):
    engine_wp = engines[engine_alias]

    metadata = MetaData()

    metadata.reflect(
        engine_wp,
        only=tables
    )

    Base = automap_base(metadata=metadata)

    Base.prepare()

    UserWP, PostWP, CommentWP, PaymentWP, TariffWP = Base.classes.wpnb_users, \
                                                     Base.classes.wpnb_posts, \
                                                     Base.classes.wpnb_comments, \
                                                     Base.classes.wpnb_6be3_wau_payments, \
                                                     Base.classes.wpnb_6be3_wau_tariffs


if __name__ == '__main__':
    print('wp_base has ran')
