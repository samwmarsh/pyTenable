'''
template details - credentials key schema and nested details class
for TenableSC template_details endpoint
'''
from marshmallow import Schema, fields, EXCLUDE


class PolicyDetailsCredentialsAdsiSchema(Schema):
    '''schema structure for policy_template_details api credentials[adsi] dict response'''
    domain = fields.Str(allow_none=True)
    domain_admin = fields.Str(allow_none=True)
    domain_controller = fields.Str(allow_none=True)
    password = fields.Str(allow_none=True)


class PolicyDetailsCredentialsAltirisSchema(Schema):
    '''schema structure for policy_template_details api credentials[altiris] dict response'''
    db_name = fields.Str(allow_none=True)
    password = fields.Str(allow_none=True)
    port = fields.Int(allow_none=True)
    server = fields.Str(allow_none=True)
    use_windows_auth = fields.Bool(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsF5Schema(Schema):
    '''schema structure for policy_template_details api credentials[f5] dict response'''
    password = fields.Str(allow_none=True)
    port = fields.Int(allow_none=True)
    use_ssl = fields.Bool(allow_none=True)
    username = fields.Str(allow_none=True)
    verify_ssl = fields.Str(allow_none=True)


class PolicyDetailsCredentialsFtpSchema(Schema):
    '''schema structure for policy_template_details api credentials[ftp] dict response'''
    username = fields.Str(allow_none=True)
    password = fields.Str(allow_none=True)


class PolicyDetailsCredentialsHttpSchema(Schema):
    '''schema structure for policy_template_details api credentials[http] dict response'''
    auth_check_page = fields.Str(allow_none=True)
    auth_method = fields.Str(allow_none=True)
    auth_regex = fields.Str(allow_none=True)
    cookies_file = fields.Str(allow_none=True)
    login_page = fields.Str(allow_none=True)
    login_params = fields.Str(allow_none=True)
    login_submission_page = fields.Str(allow_none=True)
    password = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsIbmISeriesSchema(Schema):
    '''schema structure for policy_template_details api credentials[ibm_iseries] dict response'''
    password = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsIbmTemSchema(Schema):
    '''schema structure for policy_template_details api credentials[ibm_tem] dict response'''
    https = fields.Bool(allow_none=True)
    password = fields.Str(allow_none=True)
    port = fields.Int(allow_none=True)
    server = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)
    verify_ssl = fields.Bool(allow_none=True)


class PolicyDetailsCredentialsIMapSchema(Schema):
    '''schema structure for policy_template_details api credentials[imap] dict response'''
    password = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsIpmiSchema(Schema):
    '''schema structure for policy_template_details api credentials[ipmi] dict response'''
    password = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsK1000Schema(Schema):
    '''schema structure for policy_template_details api credentials[k1000] dict response'''
    org_db_name = fields.Str(allow_none=True)
    password = fields.Str(allow_none=True)
    port = fields.Int(allow_none=True)
    server = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsMongoDBSchema(Schema):
    '''schema structure for policy_template_details api credentials[mongodb] dict response'''
    database = fields.Str(allow_none=True)
    password = fields.Str(allow_none=True)
    port = fields.Int(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsNetappApiSchema(Schema):
    '''schema structure for policy_template_details api credentials[netapp_api] dict response'''
    password = fields.Str(allow_none=True)
    port = fields.Int(allow_none=True)
    username = fields.Str(allow_none=True)
    vFiler = fields.Str(allow_none=True)


class PolicyDetailsCredentialsNntpSchema(Schema):
    '''schema structure for policy_template_details api credentials[nntp] dict response'''
    password = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsPanOSSchema(Schema):
    '''schema structure for policy_template_details api credentials[panos] dict response'''
    password = fields.Str(allow_none=True)
    port = fields.Int(allow_none=True)
    username = fields.Str(allow_none=True)
    verify_ssl = fields.Bool(allow_none=True)


class PolicyDetailsCredentialsPOP2Schema(Schema):
    '''schema structure for policy_template_details api credentials[pop] dict response'''
    password = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsPOP3Schema(Schema):
    '''schema structure for policy_template_details api credentials[pop3] dict response'''
    password = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsRhevSchema(Schema):
    '''schema structure for policy_template_details api credentials[rhev] dict response'''
    password = fields.Str(allow_none=True)
    port = fields.Int(allow_none=True)
    username = fields.Str(allow_none=True)
    verify_ssl = fields.Bool(allow_none=True)


class PolicyDetailsCredentialsSatelliteSchema(Schema):
    '''schema structure for policy_template_details api credentials[satellite] dict response'''
    password = fields.Str(allow_none=True)
    port = fields.Int(allow_none=True)
    server = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)
    verify_ssl = fields.Bool(allow_none=True)


class PolicyDetailsCredentialsSatellite6Schema(Schema):
    '''schema structure for policy_template_details api credentials[satellite_6] dict response'''
    https = fields.Bool(allow_none=True)
    password = fields.Str(allow_none=True)
    port = fields.Int(allow_none=True)
    server = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)
    verify_ssl = fields.Bool(allow_none=True)


class PolicyDetailsCredentialsSCCMSchema(Schema):
    '''schema structure for policy_template_details api credentials[sccm] dict response'''
    domain = fields.Str(allow_none=True)
    password = fields.Str(allow_none=True)
    server = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsSnmpv3Schema(Schema):
    '''schema structure for policy_template_details api credentials[snmvp3] dict response'''
    auth_algorithm = fields.Str(allow_none=True)
    auth_password = fields.Str(allow_none=True)
    port = fields.Int(allow_none=True)
    privacy_algorithm = fields.Str(allow_none=True)
    privacy_password = fields.Str(allow_none=True)
    security_level = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsTelnetSchema(Schema):
    '''schema structure for policy_template_details api credentials[telnet] dict response'''
    password = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsVmwareEsxSchema(Schema):
    '''schema structure for policy_template_details api credentials[vmware_esx] dict response'''
    dont_verify_ssl = fields.Bool(allow_none=True)
    password = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)


class PolicyDetailsCredentialsVmwareVcenterSchema(Schema):
    '''schema structure for policy_template_details api credentials[vmware_vcentre] dict response'''
    host = fields.Str(allow_none=True)
    https = fields.Bool(allow_none=True)
    password = fields.Str(allow_none=True)
    port = fields.Int(allow_none=True)
    username = fields.Str(allow_none=True)
    verify_ssl = fields.Bool(allow_none=True)


class PolicyDetailsCredentialsWSUSSchema(Schema):
    '''schema structure for policy_template_details api credentials[wsus] dict response'''
    https = fields.Bool(allow_none=True)
    password = fields.Str(allow_none=True)
    port = fields.Int(allow_none=True)
    server = fields.Str(allow_none=True)
    username = fields.Str(allow_none=True)
    verify_ssl = fields.Bool(allow_none=True)


class PolicyDetailsCredentialsX509Schema(Schema):
    '''schema structure for policy_template_details api credentials[x509] dict response'''
    ca_cert = fields.Str(allow_none=True)
    client_cert = fields.Str(allow_none=True)
    client_key = fields.Str(allow_none=True)
    password = fields.Str(allow_none=True)


class PolicyTemplateDetailsCredentialsSchema(Schema):
    '''schema structure for policy_template_details api credentials dict response'''
    adsi = fields.Nested(PolicyDetailsCredentialsAdsiSchema(unknown=EXCLUDE))
    altiris = fields.Nested(PolicyDetailsCredentialsAltirisSchema(unknown=EXCLUDE))
    f5 = fields.Nested(PolicyDetailsCredentialsF5Schema(unknown=EXCLUDE))
    ftp = fields.Nested(PolicyDetailsCredentialsFtpSchema(unknown=EXCLUDE))
    http = fields.Nested(PolicyDetailsCredentialsHttpSchema(unknown=EXCLUDE))
    ibm_iseries = fields.Nested(PolicyDetailsCredentialsIbmISeriesSchema(unknown=EXCLUDE))
    ibm_tem = fields.Nested(PolicyDetailsCredentialsIbmTemSchema(unknown=EXCLUDE))
    imap = fields.Nested(PolicyDetailsCredentialsIMapSchema(unknown=EXCLUDE))
    ipmi = fields.Nested(PolicyDetailsCredentialsIpmiSchema(unknown=EXCLUDE))
    k1000 = fields.Nested(PolicyDetailsCredentialsK1000Schema(unknown=EXCLUDE))
    mongodb = fields.Nested(PolicyDetailsCredentialsMongoDBSchema(unknown=EXCLUDE))
    netapp_api = fields.Nested(PolicyDetailsCredentialsNetappApiSchema(unknown=EXCLUDE))
    nntp = fields.Nested(PolicyDetailsCredentialsNntpSchema(unknown=EXCLUDE))
    panos = fields.Nested(PolicyDetailsCredentialsPanOSSchema(unknown=EXCLUDE))
    pop2 = fields.Nested(PolicyDetailsCredentialsPOP2Schema(unknown=EXCLUDE))
    pop3 = fields.Nested(PolicyDetailsCredentialsPOP3Schema(unknown=EXCLUDE))
    rhev = fields.Nested(PolicyDetailsCredentialsRhevSchema(unknown=EXCLUDE))
    satellite = fields.Nested(PolicyDetailsCredentialsSatelliteSchema(unknown=EXCLUDE))
    satellite_6 = fields.Nested(PolicyDetailsCredentialsSatellite6Schema(unknown=EXCLUDE))
    sccm = fields.Nested(PolicyDetailsCredentialsSCCMSchema(unknown=EXCLUDE))
    snmpv3 = fields.Nested(PolicyDetailsCredentialsSnmpv3Schema(unknown=EXCLUDE))
    telnet = fields.Nested(PolicyDetailsCredentialsTelnetSchema(unknown=EXCLUDE))
    vmware_esx = fields.Nested(PolicyDetailsCredentialsVmwareEsxSchema(unknown=EXCLUDE))
    vmware_vcenter = fields.Nested(PolicyDetailsCredentialsVmwareVcenterSchema(unknown=EXCLUDE))
    wsus = fields.Nested(PolicyDetailsCredentialsWSUSSchema(unknown=EXCLUDE))
    x509 = fields.Nested(PolicyDetailsCredentialsX509Schema(unknown=EXCLUDE))
