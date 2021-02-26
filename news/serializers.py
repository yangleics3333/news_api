from rest_framework import serializers
from news.models import AnalysisCommonNews


'''
class NewsSerializers(serializers.Serializer):
    news_id = serializers.CharField(max_length=32, help_text='新闻ID')
    similar_id = serializers.CharField(max_length=32, help_text='相似性ID')
    title = serializers.CharField(max_length=200, help_text='新闻标题')
    news_time = serializers.DateTimeField(help_text='新闻时间')
    content = serializers.CharField(help_text='新闻正文')
    news_img = serializers.CharField(help_text='新闻图片')
    site_name = serializers.CharField(max_length=10, help_text='抓取网站')
    article_source = serializers.CharField(max_length=40, help_text='发稿媒体')
    first_class = serializers.CharField(max_length=10, help_text='一级分类')
    second_class = serializers.CharField(max_length=50, help_text='二级分类')
    locations = serializers.CharField(max_length=500, help_text='所属地区')
    article_tags = serializers.CharField(max_length=500, help_text='新闻标签')
    insert_time = serializers.DateTimeField(help_text='插入时间')
    update_time = serializers.DateTimeField(help_text='更新时间')
    is_show = serializers.IntegerField(help_text='是否展示')
    filter_words = serializers.CharField(help_text='过滤词')
    is_illegal = serializers.IntegerField(help_text='是否存在非法标签')
    illegal_content = serializers.CharField(help_text='非法标签内容')
    is_check = serializers.IntegerField(help_text='人工检验')
'''


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnalysisCommonNews
        #fields = '__all__'
        fields = ['news_id', 'title', 'news_time', 'content', 'article_source']
