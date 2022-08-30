from flask import Blueprint, render_template, current_app, request
from werkzeug.exceptions import abort

from bp_posts.dao.comment import Comment
from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO
from bp_posts.dao.comment_dao import CommentDAO
from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS

bp_posts = Blueprint("bp_posts", __name__, template_folder="templates")
post_dao = PostDAO(DATA_PATH_POSTS)
comments_dao = CommentDAO(DATA_PATH_COMMENTS)

@bp_posts.route("/")
def page_posts_index():
    all_posts = post_dao.get_all()
    return render_template("index.html", posts=all_posts)

@bp_posts.route("/posts/<int:pk>/")
def page_posts_single(pk: int):
    post: Post | None = post_dao.get_by_pk(pk)
    comments: list[Comment] = comments_dao.get_comments_by_post_pk(pk)

    if post is None:
        abort(404)

    return render_template("posts_single.html",
                           post=post,
                           comments=comments,
                           comments_len=len(comments)
    )

@bp_posts.route("/users/<user_name>")
def page_posts_by_user(user_name: str):
    posts: list[Post] = post_dao.get_by_poster(user_name)

    if not posts:
        abort(404, "Такого пользователя не существует")

    return render_template("user-feed.html", posts=posts, user_name=user_name)

@bp_posts.route("/search/")
def page_posts_search():

    query: str = request.args.get("s", "")
    if query == "":
        posts: list = []
    else:    
        posts = post_dao.search_in_content(query)

    return render_template("search.html", posts=posts, query=query, posts_len=len(posts))






