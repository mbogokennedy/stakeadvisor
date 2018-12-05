from django.contrib.syndication.views import Feed
from django.shortcuts import redirect
from django.views.generic import DetailView
from el_pagination.views import AjaxListView
from django.contrib.auth.decorators import login_required
from .forms import UserCommentForm
from .models import Comment, Post
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogListView(AjaxListView):
    context_object_name = "posts"
    queryset = Post.objects.all().select_related()


class BlogDetailView(DetailView):
    model = Post
    date_field = 'post_date'
    month_format = '%m'
    page_template = "blog/post_detail_page.html"

    def get_queryset(self):
        queryset = super(BlogDetailView, self).get_queryset()
        return queryset.select_related()

    def post(self, request, *args, **kwargs):
        self.object = post = self.get_object()
        form = UserCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = self.request.user
            comment.user_name = self.request.user
            comment.user_email = self.request.user.email
            comment.ip = '0.0.0.0'
            comment.save()
        return redirect(post.get_absolute_url())
        context = self.get_context_data(object=post)
        context['comment_form'] = form
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        form = UserCommentForm()
        context = {
            'page_template': self.page_template,
            'comment_form': form,
            'comments': Comment.objects.filter(post=self.object.id).select_related()
        }
        return super(BlogDetailView, self).get_context_data(**context)

    def render_to_response(self, context, **response_kwargs):

        if self.request.is_ajax():
            template = self.page_template
        else:
            template = self.get_template_names()
        return self.response_class(
            request=self.request,
            template=template,
            context=context,
            **response_kwargs
        )
