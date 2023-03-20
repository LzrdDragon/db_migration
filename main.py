from uuid import uuid4
from math import floor
import datetime

from sqlalchemy.orm import Session

from base_prep.wp_base import get_wp_tables
from base_prep.new_base import get_new_tables
from session_prep.session_preps import make_session
from connection_prep.sqlalchemy_connection import engines


UserWP, PostWP, CommentWP, PaymentWP, TariffWP, ReactionsWP, TermsWP, TermsRelationshipsWP = get_wp_tables()
UserNew, PostNew, CommentNew, UserToTariffNew, TariffModificationsNew, \
    ReactionsNew, SubCategoriesNew, PostToSubCategoriesNew, CategoriesNew = get_new_tables()

wp_session = make_session('wp')
new_session = make_session('new')

wp_users = wp_session.query(UserWP).all()
print(f'wp users {len(wp_users)}')

new_users = new_session.query(UserNew).all()
print(f'new users before {len(new_users)}')

for user in new_users:
    new_session.delete(user)
new_session.commit()
new_session.flush()
new_users = new_session.query(UserNew).all()
print(f'new users after cleaning {len(new_users)}')

for user_wp in wp_users:
    user_new = UserNew(
        id=user_wp.ID,
        role_id=2,
        name=user_wp.user_login,
        email=user_wp.user_email,
        password=user_wp.user_pass,
        created_at=user_wp.user_registered,
        name_site=user_wp.display_name,
        ban_comment=0
    )
    if user_new not in new_users:
        new_session.add(user_new)

new_session.commit()


new_session.close()
wp_session.close()

engines['new'].dispose()
engines['wp'].dispose()





wp_session.close()
new_session.close()

wp_session = make_session('wp')
new_session = make_session('new')

wp_comments = wp_session.query(CommentWP).all()
new_comments = new_session.query(CommentNew).all()

print(f'wp comments {len(wp_comments)}')
print(f'new comments before {len(new_comments)}')

for comment in new_comments:
    new_session.delete(comment)
new_session.commit()
new_session.flush()
new_comments = new_session.query(CommentNew).all()
print(f'new comments after cleaning {len(new_comments)}')


for comment_wp in wp_comments:
    comment_new = CommentNew(
        id=comment_wp.comment_ID,
        value=comment_wp.comment_content,
        user_id=comment_wp.user_id,
        post_id=comment_wp.comment_post_ID,
        comment_id=comment_wp.comment_parent,
        created_at=comment_wp.comment_date,
        updated_at=comment_wp.comment_date,
        moderated=1
    )
    if comment_new not in new_comments:
        new_session.add(comment_new)

new_session.commit()


new_session.close()
wp_session.close()

engines['new'].dispose()
engines['wp'].dispose()





wp_session.close()
new_session.close()

wp_session = make_session('wp')
new_session = make_session('new')

wp_payments = wp_session.query(PaymentWP).all()
new_user_to_tariff = new_session.query(UserToTariffNew).all()

print(f'wp payment {len(wp_payments)}')
print(f'new user_to_tariff before {len(new_user_to_tariff)}')

for user_to_tariff in new_user_to_tariff:
    new_session.delete(user_to_tariff)
new_session.commit()
new_session.flush()
new_user_to_tariff = new_session.query(UserToTariffNew).all()
print(f'new user_to_tariff after cleaning {len(new_user_to_tariff)}')


for payment_wp in wp_payments:
    user_to_tariff_new = UserToTariffNew(
        id=payment_wp.payment_id,
        user_id=payment_wp.user_id,
        tariff_id=1,
        created_at=payment_wp.payment_date
    )
    tariff_ending = payment_wp.payment_date + datetime.timedelta(payment_wp.access_time/86400)
    dif = tariff_ending - datetime.datetime.now()
    if dif.days > 0:
        user_to_tariff_new.remainder = dif.days
        user_to_tariff_new.status = 1
    else:
        user_to_tariff_new.remainder = 0
        user_to_tariff_new.status = 0

    if user_to_tariff_new not in new_user_to_tariff:
        new_session.add(user_to_tariff_new)

new_session.commit()


new_session.close()
wp_session.close()

engines['new'].dispose()
engines['wp'].dispose()





wp_session.close()
new_session.close()

wp_session = make_session('wp')
new_session = make_session('new')

wp_tariffs = wp_session.query(TariffWP).all()
new_tariff_modifications = new_session.query(TariffModificationsNew).all()

print(f'wp tariff {len(wp_tariffs)}')
print(f'new tariff modifications before {len(new_tariff_modifications)}')

for tar_modific in new_tariff_modifications:
    new_session.delete(tar_modific)
new_session.commit()
new_session.flush()
new_user_to_tariff = new_session.query(TariffModificationsNew).all()
print(f'new tariff modifications after cleaning {len(new_user_to_tariff)}')


for tariff_wp in wp_tariffs:
    tariff_modification_new = TariffModificationsNew(
        id=tariff_wp.tariff_id,
        tariff_id=1,
        name=tariff_wp.tariff_name,
        price=tariff_wp.tariff_price,
        duration=int(float(tariff_wp.access_time) / 86400),
        description=tariff_wp.tariff_desc
    )
    if tariff_modification_new not in new_tariff_modifications:
        new_session.add(tariff_modification_new)

new_session.commit()


new_session.close()
wp_session.close()

engines['new'].dispose()
engines['wp'].dispose()





wp_session.close()
new_session.close()

wp_session = make_session('wp')
new_session = make_session('new')

wp_reactions = wp_session.query(ReactionsWP).all()
new_reactions = new_session.query(ReactionsNew).all()

print(f'wp reactions {len(wp_reactions)}')
print(f'new reactions before {len(new_reactions)}')

for reaction in new_reactions:
    new_session.delete(reaction)
new_session.commit()
new_session.flush()
new_reactions = new_session.query(ReactionsNew).all()
print(f'new reactions after cleaning {len(new_reactions)}')

# posts_id_new = new_session.query(PostNew).with_entities(PostNew.id).order_by(PostNew.id).all()
# p_ids = []
# for pair in posts_id_new:
#     p_ids.append(pair[0])
# # print(p_ids)
#
# users_id_new = new_session.query(UserNew).with_entities(UserNew.id).order_by(UserNew.id).all()
# u_ids = []
# for pair in users_id_new:
#     u_ids.append(pair[0])
# # print(u_ids)

posts_id_new = wp_session.query(PostWP).with_entities(PostWP.ID).order_by(PostWP.ID).all()
p_ids = []
for pair in posts_id_new:
    p_ids.append(pair[0])
# print(p_ids)

users_id_new = wp_session.query(UserWP).with_entities(UserWP.ID).order_by(UserWP.ID).all()
u_ids = []
for pair in users_id_new:
    u_ids.append(pair[0])
# print(u_ids)

for reaction_wp in wp_reactions:
    if reaction_wp.post_id in p_ids and reaction_wp.user_id in u_ids:
        reaction_new = ReactionsNew(
            id=reaction_wp.id,
            user_id=reaction_wp.user_id,
            post_id=reaction_wp.post_id,
            type=reaction_wp.status,
            is_active=1,
            created_at=reaction_wp.date_time,
            updated_at=reaction_wp.date_time
        )
        if reaction_new not in new_reactions:
            new_session.add(reaction_new)

new_session.commit()
new_session.flush()

reactions_new_now = new_session.query(ReactionsNew).all()
print(f'reactions new now {len(reactions_new_now)}')

new_session.close()
wp_session.close()

engines['new'].dispose()
engines['wp'].dispose()




wp_session.close()
new_session.close()

wp_session = make_session('wp')
new_session = make_session('new')

wp_terms = wp_session.query(TermsWP).all()
new_sub_categories = new_session.query(SubCategoriesNew).all()

print(f'wp terms {len(wp_terms)}')
print(f'new sub_categories before {len(new_sub_categories)}')

for sub_category in new_sub_categories:
    new_session.delete(sub_category)
new_session.commit()
new_session.flush()
new_sub_categories = new_session.query(SubCategoriesNew).all()
print(f'new sub_categories after cleaning {len(new_sub_categories)}')

categories_new = new_session.query(CategoriesNew).all()


for term_wp in wp_terms:
    sub_category_new = SubCategoriesNew(
        id=term_wp.term_id,
        category_id=None,
        description=None,
        image=None,
        order=1,
        name=term_wp.name,
        slug=term_wp.slug,
        created_at=None,
        updated_at=None
    )

    found = False
    for category in categories_new:
        if term_wp.slug == category.slug:
            sub_category_new.category_id = category.id
            found = True
    if not found:
        sub_category_new.category_id = 1

    if sub_category_new not in new_sub_categories:
        new_session.add(sub_category_new)

new_session.commit()


new_session.close()
wp_session.close()

engines['new'].dispose()
engines['wp'].dispose()


def clean_table(session_new: Session, session_wp: Session, table_new, table_wp, name_wp: str, name_new: str):
    all_rows_new = session_new.query(table_new).all()
    all_rows_wp = session_wp.query(table_wp).all()
    print(f'wp {name_wp} {len(all_rows_wp)}')
    print(f'new {name_new} before {len(all_rows_new)}')

    for row in all_rows_new:
        session_new.delete(row)
    session_new.commit()
    session_new.flush()
    all_rows_new = session_new.query(table_new).all()
    print(f'new {name_new} after cleaning {len(all_rows_new)}')
    return all_rows_wp, all_rows_new


def create_rows(session_new, wp_rows, table, all_rows_new, **kwargs):
    for row_wp in wp_rows:
        row_new = table(**kwargs)
        if row_new not in all_rows_new:
            new_session.add(row_new)
    session_new.commit()
    return




wp_session.close()
new_session.close()

wp_session = make_session('wp')
new_session = make_session('new')


wp_terms_rels = wp_session.query(TermsRelationshipsWP).all()

wp, new = clean_table(
    new_session,
    wp_session,
    PostToSubCategoriesNew,
    TermsRelationshipsWP,
    'wp_term_relationships',
    'post_to_sub_categories'
)
# create_rows(new_session, wp, PostToSubCategoriesNew, new, post_id=row_wp.object_id)
for term_rel_wp in wp_terms_rels:
    p_to_subc_new = PostToSubCategoriesNew(
        post_id=term_rel_wp.object_id,
        sub_category_id=term_rel_wp.term_taxonomy_id,
        created_at=None,
        updated_at=None
    )
    if p_to_subc_new not in new:
        new_session.add(p_to_subc_new)

new_session.commit()


new_session.close()
wp_session.close()

engines['new'].dispose()
engines['wp'].dispose()




# Posts
wp_session_posts = make_session('wp')
new_session_posts = make_session('new')

wp_posts = wp_session_posts.query(PostWP).all()
print(f'wp posts {len(wp_posts)}')

new_posts = new_session_posts.query(PostNew).all()
print(f'new posts before {len(new_posts)}')

for post in new_posts:
    new_session_posts.delete(post)
new_session_posts.commit()
new_session_posts.flush()
new_posts = new_session_posts.query(PostNew).all()
print(f'new posts after cleaning {len(new_posts)}')

new_sub_categories = new_session.query(SubCategoriesNew).all()
categories_new = new_session.query(CategoriesNew).all()


for post_wp in wp_posts:
    post_new = PostNew(
        id=post_wp.ID,
        author_id=post_wp.post_author,
        title=post_wp.post_title,
        excerpt=post_wp.post_excerpt,
        body=post_wp.post_content,
        slug=uuid4(),
        created_at=post_wp.post_date,
        updated_at=post_wp.post_modified,
        comments=post_wp.comment_count,
        image=post_wp.guid
    )

    # if post_wp.post_name != '':
    #     post_new.slug = post_wp.post_name
    # else:
    #     post_new.slug = uuid4()

    for category in categories_new:
        if post_wp.post_name == category.slug:
            post_new.category_id = category.id

    if post_wp.post_status == 'published':
        post_new.status = 'PUBLISHED'
    elif post_wp.post_status == 'draft':
        post_new.status = 'DRAFT'
    elif post_wp.post_status == 'pending':
        post_new.status = 'PENDING'

    if post_wp.comment_status == 'closed':
        post_new.comments_heed_tariff = 0
    else:
        post_new.comments_heed_tariff = 1

    if post_wp.ping_status == 'open':
        post_new.is_tariff = 1
    else:
        post_new.is_tariff = 0

    if post_new not in new_posts:
        new_session_posts.add(post_new)

new_session_posts.commit()

new_posts = new_session_posts.query(PostNew).all()
print(f'new posts after all {len(new_posts)}')

new_session_posts.close()
wp_session_posts.close()

engines['new'].dispose()
engines['wp'].dispose()
