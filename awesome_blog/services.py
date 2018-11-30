from awesome_blog import models


class BaseService:
    pass


class UserService(BaseService):
    def add(self, dto):
        return models.User.objects.update_or_create(username=dto.username, password=dto.password, email=dto.email)

    def delete(self, id):
        return models.User.objects.filter(id=id).delete()

    def update(self, dto):
        return models.User.objects.select_for_update(id=dto.id)

    def get(self, id):
        return models.User.objects.get(id=id)


class BlogService(BaseService):
    def add(self, dto):
        return models.Blog.objects.update_or_create(user_id=dto.user_id, username=dto.username, title=dto.title,
                                             summary=dto.summary, content=dto.content)

    def delete(self, id):
        return models.Blog.objects.filter(id=id).delete()

    def update(self, dto):
        return models.Blog.objects.select_for_update(id=dto.id)

    def get(self, id):
        return models.Blog.objects.get(id=id)

    def get_list(self):
        return models.Blog.objects.all()


class CommentService(BaseService):
    pass
