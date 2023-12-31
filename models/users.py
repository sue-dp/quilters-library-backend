import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db
from models.users_roles_xref import users_roles_xref


class Users(db.Model):
    __tablename__ = 'Users'

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    roles = db.relationship('Roles', secondary=users_roles_xref, back_populates='users')
    organizations = db.relationship('Organizations', secondary=users_orgs_xref, back_populates='users')
    auth = db.relationship('AuthTokens', back_populates='user')

    def __init__(self, first_name, last_name, email, password, active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.active = active

    def get_new_user():
        return Users('', '', '', '', True)


class UsersSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'first_name', 'last_name', 'email', 'active', 'roles', 'organizations']

    roles = ma.fields.Nested('RolesSchema', many=True, exclude=['users'])
    organizations = ma.fields.Nested('OrganizationsSchema', many=True, exclude=['users'])


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
