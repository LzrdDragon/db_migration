from sqlalchemy.orm import sessionmaker

from connection_prep.sqlalchemy_connection import engines


def make_session(engine_alias: str):
    session = sessionmaker(engines[engine_alias])
    return session()


# WpSession = sessionmaker(engines['wp'])
# NewSession = sessionmaker(engines['new'])
#
# wp_session = WpSession()
# new_session = NewSession()
#
# wp_session.query()
# new_session.query()
#
# wp_session.commit()
# new_session.commit()
#
# wp_session.close()
# new_session.close()
