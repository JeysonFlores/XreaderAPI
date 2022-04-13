from __main__ import ma


class NovelSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
            "description",
            "author",
            "image_path",
            "publishing_year",
            "status",
        )
