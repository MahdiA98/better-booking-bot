from Scraper import Scraper
from Notification import Notification

days = ["Wed", "Tue", "Mon"]
times = ["08:00 - 09:00", "09:00 - 10:00"]
s1 = Scraper(days, times)
s1.run()


