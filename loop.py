from scraper import scrape_wuxia
import settings
import time
import sys
import traceback

def main():
    while True:
        print("{}: Starting scrape session!".format(time.ctime()))
        try:
            scrape_wuxia()
        except KeyboardInterrupt:
            print("You don't want to see updates anymore?....")
            sys.exit(1)
        except Exception as exc:
            print("Uh oh! There's an error:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Finished a scraping session!".format(time.ctime()))
        time.sleep(settings.SLEEP_INTERVAL)

if __name__ == "__main__":
    main()
