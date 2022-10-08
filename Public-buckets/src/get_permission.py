



from typing import List


GROUPS_TO_CHECK = {
    "http://acs.amazonaws.com/groups/global/AllUsers": "Everyone",
    "http://acs.amazonaws.com/groups/global/AuthenticatedUsers": "Authenticated AWS users"
}

def get_public_permission_informations(bucket_acl) -> List:
    """
    Checks if the Access Control List is public.
    :param permission: Acl instance that describes bucket's.
    :return: Bucket's public indicator and dangerous grants parsed from acl instance.
    """
    informations = []
    for grant in bucket_acl.grants:
        grantee = grant["Grantee"]
        if grantee["Type"] == "Group" and grantee["URI"] in GROUPS_TO_CHECK:
            permission = grant["Permission"]
            access = GROUPS_TO_CHECK[grantee["URI"]]
            public_indicator = True
            informations.append({"public": public_indicator, "access": access, "permission": permission})
    return informations