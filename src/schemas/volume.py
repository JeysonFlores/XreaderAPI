from __main__ import ma


class VolumeSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "link", "image_path", "status", "id_novel")
