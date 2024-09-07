import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post

class LatestPostFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog.'
    
    def items(self):
        return Post.published.all()[:5]
    
    def item_title(self, item):
        return item.title # type: ignore
    
    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30) # type: ignore

    def item_pubdate(self, item):
        return item.publish    