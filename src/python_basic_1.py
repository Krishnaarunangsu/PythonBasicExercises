import sys
from datetime import date
import datetime

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a "
      "diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

print(f"python version:{sys.version_info}")

today = date.today()
print(f"Today's Date:{today}")

now = datetime.datetime.now()
print("Current Date Time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


