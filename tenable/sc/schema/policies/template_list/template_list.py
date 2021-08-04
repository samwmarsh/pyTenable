'''
template list schema class for TenableSC template_list endpoint
'''
from marshmallow import Schema, fields, pre_dump
from tenable.sc.schema.utils import convert_blank_string_to_none


class PolicyTemplateListSchema(Schema):
    '''schema structure for list_policy_template api response'''
    id: int = fields.Int(allow_none=True)
    name: str = fields.Str(allow_none=True)
    description: str = fields.Str(allow_none=True)

    @pre_dump()
    def filter_none(self, data, **kwargs):
        ''' convert all blank strings to None'''
        return convert_blank_string_to_none(data)