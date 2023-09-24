def fun(s):
    parts = s.split("@")
    if len(parts) != 2:
        return False  #exactly one "@" symbol

    username, domain = parts
    
    domain_parts = domain.split('.')
    if len(domain_parts) != 2:
        return False  #exactly one "." symbol
    
    websiteName, extension = domain_parts
    
    allowed_username_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
    if not all(char in allowed_username_characters for char in username):
        return False
    
    allowed_website_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    if not all(char in allowed_website_characters for char in websiteName):
        return False
    
    allowed_extension_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if not all(char in allowed_extension_characters for char in extension):
        return False
    
    if len(extension) > 3:
        return False  # ensuring extension does not exceed 3 characters
    
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)