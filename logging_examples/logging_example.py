import logging
import time
import os 

def main():
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
    logger = logging.getLogger('logging')
    tot_time = 120 # seconds
    
    for i in range(tot_time):
        logger.info('t = %d s'%i)
        time.sleep(1)
    logger.info("Program completed.")

if __name__ == "__main__":
    main()