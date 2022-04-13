from __main__ import ma


class NovelSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "author", "publishing_year", "status")
