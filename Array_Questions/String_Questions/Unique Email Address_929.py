emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
valid_emails = set()
for i in emails:
    main_split = i.split("@")
    local = main_split[0]
    domain = main_split[1]
    local = local.replace('.','')
    local = local.split('+')[0]
    valid_emails.add(local+'@'+domain)

print(valid_emails)