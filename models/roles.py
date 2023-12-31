import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Roles(db.Model):
    __tablename__ = 'Roles'

    role_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_name = db.Column(db.String(), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    users = db.relationship('Users', secondary=users_roles_xref, back_populates='roles')
    organizations = db.relationship('Organizations', secondary=roles_orgs_xref, back_populates='roles')

    def __init__(self, role_name, active=True):
        self.role_name = role_name
        self.active = active

    def get_new_role():
        return Roles('', True)


class RolesSchema(ma.Schema):
    class Meta:
        fields = ['role_id', 'role_name', 'active', 'users', 'organizations']

    users = ma.fields.Nested('UsersSchema', many=True, exclude=['roles'])
    organizations = ma.fields.Nested('OrganizationsSchema', many=True, exclude=['roles'])


role_schema = RolesSchema()
roles_schema = RolesSchema(many=True)
