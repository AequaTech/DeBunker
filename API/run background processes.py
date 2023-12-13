from Background.ThreadNetworkCrawler import ThreadNetworkCrawler
from Background.ThreadNetworkMetrics import ThreadNetworkMetrics
from Background.ThreadWhoIs import ThreadWhoIs


ThreadNetworkCrawler().retrieveDomains()

ThreadWhoIs().retrieveDomains()

ThreadNetworkMetrics().retrieveDomains()