'''
template details schema class for TenableSC template_details endpoint
'''
from marshmallow import Schema, fields, pre_dump, EXCLUDE
from tenable.sc.schema.policies.template_details.credentials.policy_credentials import \
    PolicyTemplateDetailsCredentialsSchema
from tenable.sc.schema.policies.template_details.preferences.policy_preferences import PolicyTemplateDetailsPreferences
from tenable.sc.schema.utils import convert_blank_string_to_none


class PolicyTemplateDetailsSchema(Schema):
    '''schema structure for policy_template_details api response'''
    id = fields.Int(allow_none=True)
    name = fields.Str(allow_none=True)
    description = fields.Str(allow_none=True)
    credentials = fields.Nested(PolicyTemplateDetailsCredentialsSchema(unknown=EXCLUDE))
    preferences = fields.Nested(PolicyTemplateDetailsPreferences(unknown=EXCLUDE))
    createdTime = fields.Int(allow_none=True)
    modifiedTime = fields.Int(allow_none=True)
    templateDefModTime = fields.Int(allow_none=True)
    templateModTime = fields.Int(allow_none=True)
    templatePubTime = fields.Int(allow_none=True)

    @pre_dump()
    def filter_none(self, data, **kwargs):
        ''' convert all blank strings to None'''
        return convert_blank_string_to_none(data)