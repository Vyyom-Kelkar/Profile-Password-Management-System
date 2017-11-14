import collections
import sys

#def main():
def newPasswordToOldPasswordComparison(newPassword, oldPassword):
#    oldPassword = sys.argv[1]
#    newPassword = sys.argv[2]
    newPassword = newPassword.lower()
    oldPassword = oldPassword.lower()
    newPasswordLetters = collections.Counter(newPassword)
    oldPasswordLetters = collections.Counter(oldPassword)
    intersection = newPasswordLetters & oldPasswordLetters
    print intersection
    count = 0 
    for item in intersection:
        count = count + intersection[item]
    percent = float(count)/len(newPassword)
    print percent
    if (percent > .7):
#        print False
        return False
    else:
#        print True
        return True

#if __name__ == "__main__":
#    main()