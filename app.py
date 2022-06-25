#Here we use the pywhatkit pip and then import datetime
import pywhatkit

from datetime import datetime
import time

#You may change the time it takes but it may be more prone to failing
seconds = time.time() + 60

date = datetime.fromtimestamp(seconds)

pywhatkit.sendwhatmsg("phone number with area code no spaces",
                      "text here",
                      date.hour,
                      date.minute)

time.sleep(1)
