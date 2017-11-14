import collections
import sys








#def newPasswordToOldPasswordComparison(newPassword, oldPassword):
    newPassword = sys.argv[1]
    oldPassword = sys.argv[2]
    newPasswordLetters = collections.Counter(newPassword)
    oldPasswordLetters = collections.Counter(oldPassword)
    print newPasswordLetters
    print oldPasswordLetters
