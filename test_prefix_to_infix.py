from sys import prefix
from prefix import Prefix
from prefix_to_infix import PrefixToInfix as pi

# okay ra
# prefix = Prefix("+ 3 5")
# pi = pi(prefix)
# pi.convertPrefixToInfix()

# okay ra
# prefix = Prefix("^ E F $ 6")
# pi = pi(prefix)
# pi.convertPrefixToInfix()

# okay ra
# prefix = Prefix("+ - + 7 2 / * 3 2")
# pi = pi(prefix)
# pi.convertPrefixToInfix()

# okay ra
# prefix = Prefix("+ 4 6 7 ^")
# pi = pi(prefix)
# pi.convertPrefixToInfix()

# okay ra
# prefix = Prefix("+ 3")
# pi = pi(prefix)
# pi.convertPrefixToInfix()

# okay ra
prefix = Prefix("+ + a / * b c d 123”")
pi = pi(prefix)
pi.convertPrefixToInfix()

# DI INSAKTO ANG OUTPUT HAHAAH
# HELP UNSAON NI
# prefix = Prefix("+ One Two")
# pi = pi(prefix)
# pi.convertPrefixToInfix()
