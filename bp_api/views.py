import logging

from flask import Blueprint, jsonify, abort

from bp_posts.dao.comment import Comment
from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO
from bp_posts.dao.comment_dao import CommentDAO
from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS

bp_api = Blueprint("bp_api", __name__)
post_dao = PostDAO(DATA_PATH_POSTS)
comments_dao = CommentDAO(DATA_PATH_COMMENTS)

api_logger = logging.getLogger("api_logger")


@bp_api.route("/posts/")
def api_posts_all():
    all_posts: list[Post] = post_dao.get_all()
    all_posts_as_dict: list[dict] = ([post.as_dict() for post in all_posts])
    api_logger.debug("Запрошены все посты")

    return jsonify(all_posts_as_dict), 200

@bp_api.route("/posts/<int:pk>/")
def api_posts_single(pk: int):
    post: Post | None = post_dao.get_by_pk(pk)
    if post is None:
        api_logger.debug(f"Обращение к несуществующему посту {pk}")
        abort(404)
    api_logger.debug(f"Запрошен пост {pk}")
    return jsonify(post.as_dict()), 200

@bp_api.errorhandler(404)
def api_error_404(error):
    api_logger.error(f"Ошибка{error}")
    return jsonify({"error": str(error)}), 404


@bp_api.route('/')
def api_posts_hello():
    return "Смотри документацию"














