#Here want to take advantage of the "set()" DS.  It will add unique values.
#We traverse each email and split it into a local "name" and domain "@domain"
#We then want to split again on the "+" sign, and keep the first element.
#Lastly, we want to replace the "." with nothing. A local name would be the same without it.
#We add back on the "@domain" and add it to the set, then return the length of the set.

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            unique_emails.add(local.split('+')[0].replace('.', '') + '@' + domain)
        return len(unique_emails)