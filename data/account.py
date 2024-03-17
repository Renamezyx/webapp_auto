accounts = [
    {"phone": "12342058061", 'code': '001862', "country": "CN-86", "rg": "", "tags": [1,2]}
]


def get_account(phone="", code="", rg="", tags=None):
    filter_acc = accounts
    if phone:
        for account in filter_acc:
            if account["phone"] != phone:
                filter_acc.remove(account)
    if code:
        for account in filter_acc:
            if account["code"] != code:
                filter_acc.remove(account)
    if rg:
        for account in filter_acc:
            if account["rg"] != rg:
                filter_acc.remove(account)
    if tags:
        for account in filter_acc:
            for tag in tags:
                if tag not in account["tags"]:
                    filter_acc.remove(account)
                    break
    if filter_acc:
        return filter_acc[0]
    return None


if __name__ == '__main__':
    print(get_account(tags=[3]))
