class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mails = set()
        for i in range(len(emails)):
            mail = ''
            for j in emails[i]:
                if j == '.':
                    continue
                elif j == '+' or j == '@':
                    break
                else:
                    mail += j
            index = emails[i].index('@')
            mail += emails[i][index:]
            mails.add(mail)
        return len(mails)
