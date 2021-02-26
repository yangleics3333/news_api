# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnalysisArticleClassDict(models.Model):
    policy = models.CharField(max_length=255, blank=True, null=True)
    preprimary_education = models.CharField(max_length=255, blank=True, null=True)
    middle_primary_school = models.CharField(max_length=255, blank=True, null=True)
    high_school = models.CharField(max_length=255, blank=True, null=True)
    university = models.CharField(max_length=255, blank=True, null=True)
    postgraduate = models.CharField(max_length=255, blank=True, null=True)
    study_abroad = models.CharField(max_length=255, blank=True, null=True)
    adult_education = models.CharField(max_length=255, blank=True, null=True)
    educational_training = models.CharField(max_length=255, blank=True, null=True)
    conference = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_article_class_dict'


class AnalysisCommonNews(models.Model):
    news_id = models.CharField(unique=True, max_length=32)
    similar_id = models.CharField(max_length=32)
    title = models.CharField(max_length=200)
    news_time = models.DateTimeField()
    content = models.TextField()
    news_img = models.TextField(blank=True, null=True)
    site_name = models.CharField(max_length=10)
    article_source = models.CharField(max_length=40)
    first_class = models.CharField(max_length=10, blank=True, null=True)
    second_class = models.CharField(max_length=50, blank=True, null=True)
    locations = models.CharField(max_length=500, blank=True, null=True)
    article_tags = models.CharField(max_length=500, blank=True, null=True)
    insert_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    is_show = models.IntegerField(blank=True, null=True)
    filter_words = models.TextField(blank=True, null=True)
    is_illegal = models.IntegerField(blank=True, null=True)
    illegal_content = models.TextField(blank=True, null=True)
    is_check = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_common_news'


class AnalysisCommonNewsComments(models.Model):
    news_id = models.CharField(max_length=32)
    comment_id = models.CharField(unique=True, max_length=255)
    content = models.CharField(max_length=500)
    author_id = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    reply_time = models.DateTimeField(blank=True, null=True)
    insert_time = models.DateTimeField()
    floor = models.IntegerField()
    floor_link = models.CharField(max_length=1000, blank=True, null=True)
    good_number = models.IntegerField(blank=True, null=True)
    reply_floor = models.CharField(max_length=32, blank=True, null=True)
    frequency = models.CharField(max_length=32, blank=True, null=True)
    author_name = models.CharField(max_length=255, blank=True, null=True)
    author_img = models.CharField(max_length=255, blank=True, null=True)
    is_show = models.IntegerField(blank=True, null=True)
    cmt_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_common_news_comments'


class AnalysisCommonNewsCopy1(models.Model):
    news_id = models.CharField(unique=True, max_length=32)
    similar_id = models.CharField(max_length=32)
    title = models.CharField(max_length=200)
    news_time = models.DateTimeField()
    content = models.TextField()
    news_img = models.TextField(blank=True, null=True)
    site_name = models.CharField(max_length=10)
    article_source = models.CharField(max_length=40)
    first_class = models.CharField(max_length=10, blank=True, null=True)
    second_class = models.CharField(max_length=50, blank=True, null=True)
    locations = models.CharField(max_length=500, blank=True, null=True)
    article_tags = models.CharField(max_length=500, blank=True, null=True)
    insert_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    is_show = models.IntegerField(blank=True, null=True)
    filter_words = models.TextField(blank=True, null=True)
    is_illegal = models.IntegerField(blank=True, null=True)
    illegal_content = models.TextField(blank=True, null=True)
    is_check = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_common_news_copy1'


class AnalysisCommonNewsTop(models.Model):
    news_id = models.CharField(max_length=32)
    title = models.CharField(max_length=200)
    second_class = models.CharField(max_length=50)
    update_time = models.DateTimeField(blank=True, null=True)
    is_show = models.IntegerField()
    is_check = models.IntegerField(blank=True, null=True)
    is_top = models.IntegerField(blank=True, null=True)
    top_time = models.DateTimeField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_common_news_top'
        unique_together = (('news_id', 'second_class'),)


class AnalysisFilterKeywords(models.Model):
    name = models.CharField(max_length=255)
    time = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_filter_keywords'


class ArticleReplyWsContent(models.Model):
    news_id = models.CharField(max_length=255, blank=True, null=True)
    news_title = models.CharField(max_length=1000, blank=True, null=True)
    comment_id = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    reply_time = models.DateTimeField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    comment_url = models.CharField(max_length=255, blank=True, null=True)
    comment_seg = models.TextField(blank=True, null=True)
    content_emotion = models.CharField(max_length=1000, blank=True, null=True)
    exisit_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_reply_ws_content'
        unique_together = (('id', 'comment_id'),)


class AuthUsername(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    encrypt_type = models.CharField(max_length=16, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_username'


class BasicCorpus(models.Model):
    from_content = models.TextField(blank=True, null=True)
    to_content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basic_corpus'


class CommonApp(models.Model):
    app_code = models.CharField(max_length=64)
    app_name = models.CharField(max_length=100)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'common_app'


class CommonAppVersion(models.Model):
    app_code = models.CharField(max_length=64)
    platform = models.CharField(max_length=255)
    device = models.CharField(max_length=255)
    version_number = models.IntegerField(blank=True, null=True)
    version_code = models.CharField(max_length=64)
    download_url = models.CharField(max_length=500)
    version_memo = models.CharField(max_length=2048)
    valid_flag = models.IntegerField()
    optional_version = models.CharField(max_length=1024, blank=True, null=True)
    force_version = models.CharField(max_length=1024, blank=True, null=True)
    not_version = models.CharField(max_length=1024, blank=True, null=True)
    release_time = models.DateTimeField()
    create_user_id = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    force_up = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_app_version'


class CommonColumn(models.Model):
    column = models.CharField(max_length=16, blank=True, null=True)
    disable = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    show_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_column'


class DjangoTest(models.Model):
    news_id = models.CharField(unique=True, max_length=32, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=700, blank=True, null=True)
    news_time = models.DateTimeField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    site_name = models.CharField(max_length=255, blank=True, null=True)
    article_source = models.CharField(max_length=255, blank=True, null=True)
    first_class = models.CharField(max_length=255, blank=True, null=True)
    second_class = models.CharField(max_length=255, blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    task_name = models.CharField(max_length=255, blank=True, null=True)
    task_page_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_test'


class EcCloneRoster(models.Model):
    rose_name = models.CharField(max_length=16, blank=True, null=True)
    roster_type = models.IntegerField(blank=True, null=True)
    roster_type_desc = models.CharField(max_length=16, blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    rose_url = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_clone_roster'


class EcCloneRoster1(models.Model):
    rose_name = models.CharField(max_length=16, blank=True, null=True)
    roster_type = models.IntegerField(blank=True, null=True)
    roster_type_desc = models.CharField(max_length=16, blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    rose_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_clone_roster_1'


class EcGoodUser(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    good_type = models.IntegerField(blank=True, null=True)
    biz_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    has_del = models.IntegerField(blank=True, null=True)
    to_uid = models.IntegerField(blank=True, null=True)
    has_read = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_good_user'


class EcGroupCategory(models.Model):
    category = models.CharField(max_length=32, blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_group_category'


class EcGroupDynamic(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    comment_cnt = models.IntegerField(blank=True, null=True)
    good_cnt = models.IntegerField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    choice_order = models.IntegerField(blank=True, null=True)
    top_order = models.IntegerField(blank=True, null=True)
    hot_order = models.IntegerField(blank=True, null=True)
    has_del = models.IntegerField(blank=True, null=True)
    dy_type = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    link_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_group_dynamic'


class EcGroupDynamicComment(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    dynamic_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    good_cnt = models.IntegerField(blank=True, null=True)
    reply_cnt = models.IntegerField(blank=True, null=True)
    has_del = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    has_read = models.IntegerField(blank=True, null=True)
    to_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_group_dynamic_comment'


class EcGroupReqRecord(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    verify_msg = models.CharField(max_length=128, blank=True, null=True)
    has_del = models.IntegerField(blank=True, null=True)
    req_status = models.IntegerField(blank=True, null=True)
    agree_time = models.DateTimeField(blank=True, null=True)
    has_read = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_group_req_record'


class EcPrivateChat(models.Model):
    be_uid = models.IntegerField(blank=True, null=True)
    zu_uid = models.IntegerField(blank=True, null=True)
    pc_id = models.CharField(max_length=11, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    has_start = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_private_chat'


class EcSysUser(models.Model):
    username = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    salt = models.CharField(max_length=32, blank=True, null=True)
    full_name = models.CharField(max_length=16, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    avatar_url = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_sys_user'


class EcUserBrowseRecord(models.Model):
    biz_id = models.IntegerField(blank=True, null=True)
    biz_type = models.IntegerField(blank=True, null=True)
    recent_time = models.DateTimeField(blank=True, null=True)
    last_time = models.DateTimeField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_user_browse_record'


class EcUserCnt(models.Model):
    uid = models.IntegerField(unique=True, blank=True, null=True)
    fork_cnt = models.PositiveIntegerField(blank=True, null=True)
    fans_cnt = models.PositiveIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    good_cnt = models.IntegerField(blank=True, null=True)
    cnt_good = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_user_cnt'


class EcUserComment(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    to_uid = models.IntegerField(blank=True, null=True)
    biz_id = models.IntegerField(blank=True, null=True)
    cm_type = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    good_cnt = models.IntegerField(blank=True, null=True)
    reply_cnt = models.IntegerField(blank=True, null=True)
    has_del = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    has_read = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_user_comment'


class EcUserDailyBrowseRecord(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    biz_id = models.IntegerField(blank=True, null=True)
    biz_type = models.IntegerField(blank=True, null=True)
    recent_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_user_daily_browse_record'


class EcUserDynamic(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    comment_cnt = models.IntegerField(blank=True, null=True)
    good_cnt = models.IntegerField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    has_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_user_dynamic'


class EcUserGood(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    good_type = models.IntegerField(blank=True, null=True)
    biz_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    has_del = models.IntegerField(blank=True, null=True)
    to_uid = models.IntegerField(blank=True, null=True)
    has_read = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_user_good'


class EcUserRose(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    rose_id = models.IntegerField(blank=True, null=True)
    rose_name = models.CharField(max_length=16, blank=True, null=True)
    rose_url = models.CharField(max_length=512, blank=True, null=True)
    has_del = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    rose_img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ec_user_rose'


class FriendReqRecord(models.Model):
    from_user_id = models.IntegerField(blank=True, null=True)
    to_user_id = models.IntegerField(blank=True, null=True)
    verify_msg = models.CharField(max_length=256, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    agree_time = models.DateTimeField(blank=True, null=True)
    req_status = models.IntegerField(blank=True, null=True)
    invalid = models.IntegerField(blank=True, null=True)
    has_read = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friend_req_record'


class FriendShip(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    remark_name = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    relation_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friend_ship'


class GroupChat(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    group_chat_name = models.CharField(max_length=128, blank=True, null=True)
    member_cnt = models.IntegerField(blank=True, null=True)
    group_chat_img = models.CharField(max_length=256, blank=True, null=True)
    announcement = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    disable = models.IntegerField(blank=True, null=True)
    has_start = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_chat'


class GroupCompletedList(models.Model):
    group_name = models.CharField(max_length=500, blank=True, null=True)
    group_avatar = models.CharField(max_length=255, blank=True, null=True)
    group_img = models.CharField(max_length=500, blank=True, null=True)
    dynamic_cnt = models.IntegerField(blank=True, null=True)
    group_people_total = models.IntegerField(blank=True, null=True)
    group_create_time = models.DateTimeField(blank=True, null=True)
    group_location = models.CharField(max_length=255, blank=True, null=True)
    group_tags = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    group_exist_id = models.CharField(max_length=32, blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    summary = models.CharField(max_length=128, blank=True, null=True)
    announcement = models.TextField(blank=True, null=True)
    member_review = models.IntegerField(blank=True, null=True)
    show_dynamic = models.IntegerField(blank=True, null=True)
    has_pay = models.IntegerField(blank=True, null=True)
    pay_amount = models.IntegerField(blank=True, null=True)
    has_start = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_completed_list'


class GroupCompletedList1(models.Model):
    group_name = models.CharField(max_length=500, blank=True, null=True)
    group_avatar = models.CharField(max_length=255, blank=True, null=True)
    group_img = models.CharField(max_length=500, blank=True, null=True)
    dynamic_cnt = models.IntegerField(blank=True, null=True)
    group_people_total = models.IntegerField(blank=True, null=True)
    group_create_time = models.DateTimeField(blank=True, null=True)
    group_location = models.CharField(max_length=255, blank=True, null=True)
    group_tags = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    group_exist_id = models.CharField(max_length=32, blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    summary = models.CharField(max_length=128, blank=True, null=True)
    announcement = models.TextField(blank=True, null=True)
    member_review = models.IntegerField(blank=True, null=True)
    show_dynamic = models.IntegerField(blank=True, null=True)
    has_pay = models.IntegerField(blank=True, null=True)
    pay_amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_completed_list_1'


class GroupDynamicContent(models.Model):
    group_id = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=500, blank=True, null=True)
    group_img = models.CharField(max_length=500, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_img = models.CharField(max_length=255, blank=True, null=True)
    dynamic_content = models.TextField(blank=True, null=True)
    dynamic_img = models.CharField(max_length=1000, blank=True, null=True)
    dynamic_good_number = models.IntegerField(blank=True, null=True)
    dynamic_comments_number = models.IntegerField(blank=True, null=True)
    dynamic_transpond_number = models.IntegerField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    dynamic_content_exist_id = models.CharField(max_length=32, blank=True, null=True)
    news_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_dynamic_content'


class GroupDynamicContentComments(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    dynamic_id = models.IntegerField(blank=True, null=True)
    user_target_id = models.IntegerField(blank=True, null=True)
    comment_content = models.TextField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    exisit_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_dynamic_content_comments'


class GroupDynamicContentGood(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    dynamic_id = models.IntegerField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_dynamic_content_good'


class GroupUserJoinList(models.Model):
    group_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    group_role = models.IntegerField(blank=True, null=True)
    join_type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_user_join_list'


class GroupUserJoinList1(models.Model):
    group_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    group_role = models.IntegerField(blank=True, null=True)
    join_type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_user_join_list_1'


class SpiderWsAudio(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    discipline = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_img = models.CharField(max_length=1000, blank=True, null=True)
    cover_img = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_audio'


class SpiderWsCourseRemark(models.Model):
    course_name = models.CharField(max_length=255, blank=True, null=True)
    course_id = models.CharField(max_length=255, blank=True, null=True)
    course_url = models.CharField(max_length=500, blank=True, null=True)
    course_agent = models.CharField(max_length=255, blank=True, null=True)
    course_agent_id = models.IntegerField(blank=True, null=True)
    course_agent_summary = models.CharField(max_length=700, blank=True, null=True)
    course_agent_img = models.CharField(max_length=255, blank=True, null=True)
    course_img = models.CharField(max_length=255, blank=True, null=True)
    course_fisrt_class = models.CharField(max_length=255, blank=True, null=True)
    course_second_class = models.CharField(max_length=255, blank=True, null=True)
    course_third_class = models.CharField(max_length=255, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_course_remark'


class SpiderWsCourseRemarkCatalogue(models.Model):
    course_class = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_course_remark_catalogue'


class SpiderWsCourseRemarkComments(models.Model):
    course_id = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    user_img = models.CharField(max_length=1000, blank=True, null=True)
    rating = models.CharField(max_length=255, blank=True, null=True)
    reply_time = models.DateTimeField(blank=True, null=True)
    course_buy_time = models.DateTimeField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    course_agent = models.CharField(max_length=255, blank=True, null=True)
    course_fisrt_class = models.CharField(max_length=255, blank=True, null=True)
    course_second_class = models.CharField(max_length=255, blank=True, null=True)
    course_third_class = models.CharField(max_length=255, blank=True, null=True)
    course_name = models.CharField(max_length=255, blank=True, null=True)
    course_agent_summary = models.CharField(max_length=700, blank=True, null=True)
    course_agent_img = models.CharField(max_length=255, blank=True, null=True)
    course_img = models.CharField(max_length=255, blank=True, null=True)
    course_agent_id = models.CharField(max_length=255, blank=True, null=True)
    exisit_id = models.CharField(unique=True, max_length=32, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_course_remark_comments'


class SpiderWsCourseRemarkCourses(models.Model):
    course_name = models.CharField(max_length=255, blank=True, null=True)
    exisit_id = models.CharField(max_length=32, blank=True, null=True)
    course_url = models.CharField(max_length=500, blank=True, null=True)
    course_agent_id = models.IntegerField(blank=True, null=True)
    course_img = models.CharField(max_length=255, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_course_remark_courses'


class SpiderWsCourseRemarkInstitutions(models.Model):
    institutions_name = models.CharField(max_length=255, blank=True, null=True)
    institutions_summary = models.CharField(max_length=700, blank=True, null=True)
    institutions_img = models.CharField(max_length=255, blank=True, null=True)
    course_fisrt_class = models.CharField(max_length=255, blank=True, null=True)
    course_second_class = models.CharField(max_length=255, blank=True, null=True)
    course_third_class = models.CharField(max_length=255, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    exisit_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_course_remark_institutions'


class SpiderWsCourseRemarkTask(models.Model):
    list_page = models.TextField(blank=True, null=True)
    content_page = models.TextField(blank=True, null=True)
    course_fisrt_class = models.CharField(max_length=255, blank=True, null=True)
    course_second_class = models.CharField(max_length=255, blank=True, null=True)
    course_third_class = models.CharField(max_length=255, blank=True, null=True)
    url_prefix = models.CharField(max_length=1000, blank=True, null=True)
    url_postfix = models.CharField(max_length=1000, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    min_page = models.IntegerField(blank=True, null=True)
    max_page = models.IntegerField(blank=True, null=True)
    page_gap = models.IntegerField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_course_remark_task'


class SpiderWsDianpingTask(models.Model):
    news_id = models.CharField(unique=True, max_length=32)
    url = models.CharField(max_length=500)
    title = models.CharField(max_length=400)
    news_time = models.DateTimeField()
    insert_time = models.DateTimeField()
    content = models.TextField()
    site_name = models.CharField(max_length=255)
    article_source = models.CharField(max_length=255, blank=True, null=True)
    article_type = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    first_class = models.CharField(max_length=255)
    second_class = models.CharField(max_length=255)
    title_keyword = models.CharField(max_length=500, blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    task_name = models.CharField(max_length=255)
    task_page_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'spider_ws_dianping_task'


class SpiderWsNews(models.Model):
    news_id = models.CharField(unique=True, max_length=32)
    url = models.CharField(max_length=500)
    title = models.CharField(max_length=700)
    news_time = models.DateTimeField()
    insert_time = models.DateTimeField()
    content = models.TextField()
    site_name = models.CharField(max_length=255)
    article_source = models.CharField(max_length=255, blank=True, null=True)
    first_class = models.CharField(max_length=255)
    second_class = models.CharField(max_length=255)
    images = models.TextField(blank=True, null=True)
    task_name = models.CharField(max_length=255)
    task_page_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'spider_ws_news'


class SpiderWsNewsComments(models.Model):
    news_id = models.CharField(max_length=32)
    title = models.CharField(max_length=255, blank=True, null=True)
    news_time = models.DateTimeField(blank=True, null=True)
    comment_id = models.CharField(unique=True, max_length=255)
    content = models.CharField(max_length=500)
    reply_time = models.DateTimeField(blank=True, null=True)
    insert_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spider_ws_news_comments'


class SpiderWsNewsCommentsPage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    list_rule = models.CharField(max_length=2000, blank=True, null=True)
    content_rule = models.CharField(max_length=2000, blank=True, null=True)
    invaild_keyword = models.TextField(blank=True, null=True)
    pricke_keyword = models.TextField(blank=True, null=True)
    remark_keyword = models.TextField(blank=True, null=True)
    negative = models.TextField(blank=True, null=True)
    postive = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_news_comments_page'


class SpiderWsNewsGood(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    news_id = models.CharField(max_length=32, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_news_good'


class SpiderWsNewsPage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    list_rule = models.CharField(max_length=2000, blank=True, null=True)
    content_rule = models.CharField(max_length=2000, blank=True, null=True)
    headers = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_news_page'


class SpiderWsNewsTasks(models.Model):
    task_name = models.CharField(max_length=255)
    task_page = models.CharField(max_length=255)
    first_class = models.CharField(max_length=255)
    second_class = models.CharField(max_length=255)
    site_class = models.CharField(max_length=255, blank=True, null=True)
    site_name = models.CharField(max_length=255)
    url_prefix = models.CharField(max_length=1000, blank=True, null=True)
    url_postfix = models.CharField(max_length=1000, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    min_page = models.IntegerField(blank=True, null=True)
    max_page = models.IntegerField(blank=True, null=True)
    page_gap = models.IntegerField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    is_important = models.IntegerField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    task_type = models.IntegerField(blank=True, null=True)
    is_run = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_news_tasks'


class SpiderWsNewsTasksBaidu(models.Model):
    task_name = models.CharField(max_length=255)
    task_page = models.CharField(max_length=255)
    first_class = models.CharField(max_length=255)
    second_class = models.CharField(max_length=255)
    site_class = models.CharField(max_length=255, blank=True, null=True)
    site_name = models.CharField(max_length=255)
    url_prefix = models.CharField(max_length=1000, blank=True, null=True)
    url_postfix = models.CharField(max_length=1000, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    min_page = models.IntegerField(blank=True, null=True)
    max_page = models.IntegerField(blank=True, null=True)
    page_gap = models.IntegerField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    is_important = models.IntegerField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_news_tasks_baidu'


class SpiderWsVideo(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    discipline = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=500, blank=True, null=True)
    user_img = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_video'


class SpiderWsWeibo(models.Model):
    news_id = models.CharField(unique=True, max_length=32)
    url_id = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    text_time = models.DateTimeField()
    insert_time = models.DateTimeField()
    content = models.TextField()
    site_name = models.CharField(max_length=255)
    first_class = models.CharField(max_length=255)
    second_class = models.CharField(max_length=255)
    images = models.TextField(blank=True, null=True)
    reposts_count = models.IntegerField(blank=True, null=True)
    comments_count = models.IntegerField(blank=True, null=True)
    attitudes_count = models.IntegerField(blank=True, null=True)
    user_followers_count = models.IntegerField(blank=True, null=True)
    user_follow_count = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    user_image = models.CharField(max_length=500, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    is_important = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_weibo'


class SpiderWsWeiboSearch(models.Model):
    f_class = models.CharField(max_length=255, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_weibo_search'


class SpiderWsWeiboSearchTasks(models.Model):
    first_class = models.CharField(max_length=255, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_weibo_search_tasks'


class SpiderWsWeiboTasks(models.Model):
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255)
    first_class = models.CharField(max_length=255, blank=True, null=True)
    second_class = models.CharField(max_length=255, blank=True, null=True)
    site_name = models.CharField(max_length=255, blank=True, null=True)
    url_prefix = models.CharField(max_length=1000, blank=True, null=True)
    url_postfix = models.CharField(max_length=1000, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    min_page = models.IntegerField(blank=True, null=True)
    max_page = models.IntegerField(blank=True, null=True)
    page_gap = models.IntegerField(blank=True, null=True)
    is_important = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_ws_weibo_tasks'
        unique_together = (('id', 'user_id'),)


class TestSpiderWsNews(models.Model):
    news_id = models.CharField(unique=True, max_length=32)
    url = models.CharField(max_length=500)
    title = models.CharField(max_length=700)
    news_time = models.DateTimeField()
    insert_time = models.DateTimeField()
    content = models.TextField()
    site_name = models.CharField(max_length=255)
    article_source = models.CharField(max_length=255, blank=True, null=True)
    first_class = models.CharField(max_length=255)
    second_class = models.CharField(max_length=255)
    images = models.TextField(blank=True, null=True)
    task_name = models.CharField(max_length=255)
    task_page_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'test_spider_ws_news'


class TestSpiderWsNewsPage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    list_rule = models.CharField(max_length=2000, blank=True, null=True)
    content_rule = models.CharField(max_length=2000, blank=True, null=True)
    headers = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_spider_ws_news_page'


class TestSpiderWsNewsTasks(models.Model):
    task_name = models.CharField(max_length=255)
    task_page = models.CharField(max_length=255)
    first_class = models.CharField(max_length=255)
    second_class = models.CharField(max_length=255)
    site_class = models.CharField(max_length=255, blank=True, null=True)
    site_name = models.CharField(max_length=255)
    url_prefix = models.CharField(max_length=1000, blank=True, null=True)
    url_postfix = models.CharField(max_length=1000, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    min_page = models.IntegerField(blank=True, null=True)
    max_page = models.IntegerField(blank=True, null=True)
    page_gap = models.IntegerField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    is_important = models.IntegerField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    task_type = models.IntegerField(blank=True, null=True)
    is_run = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_spider_ws_news_tasks'


class UserColumn(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    cid = models.IntegerField(blank=True, null=True)
    column = models.CharField(max_length=16, blank=True, null=True)
    c_type = models.IntegerField(blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    key_word = models.CharField(max_length=255, blank=True, null=True)
    has_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_column'


class UserFansAttention(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    attention_user_id = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    has_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_fans_attention'


class UserGoodList(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    target_id = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    content_id = models.CharField(max_length=32, blank=True, null=True)
    good_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_good_list'


class UserGroupChat(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    g_chat_id = models.IntegerField(blank=True, null=True)
    gc_nick_name = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    has_del = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group_chat'


class UserIndividualTags(models.Model):
    user_id = models.CharField(max_length=255, blank=True, null=True)
    user_tag = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_individual_tags'


class UserInformation(models.Model):
    user_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=500, blank=True, null=True)
    user_sign = models.CharField(max_length=500, blank=True, null=True)
    user_img = models.CharField(max_length=1000, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    sys_role = models.IntegerField(blank=True, null=True)
    user_no = models.CharField(max_length=16, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    salt = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_information'


class UserLoginPhoneNumberCode(models.Model):
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    phone_code = models.CharField(max_length=255, blank=True, null=True)
    code_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_login_phone_number_code'
