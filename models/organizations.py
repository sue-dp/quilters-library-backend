import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Organizations(db.Model):
    __tablename__ = 'Organizations'

    org_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_name = db.Column(db.String(), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    users = db.relationship('Users', secondary=users_orgs_xref, back_populates='organizations')
    roles = db.relationship('Roles', secondary=roles_orgs_xref, back_populates='organizations')

    def __init__(self, org_name, active)
        self.org_name = org_name
        self.active = active

    def get_new_organization():
        return Organizations('', True)
    

class OrganizationsSchema(ma.Schema):
    class Meta:
        fields = ['org_id', 'org_name', 'active', 'users', 'roles']

    users = ma.fields.Nested('UsersSchema', many=True, exclude=['organizations'])
    roles = ma.fields.Nested('RolesSchema', many=True, exclude=['organizations'])


organization_schema = OrganizationsSchema()
organizations_schema = OrganizationsSchema(many=True)