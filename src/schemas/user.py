from __main__ import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "name", "password", "permissions", "token")
