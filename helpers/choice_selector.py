from helpers.logger import get_logger

logger = get_logger()

class SelectChoice:
    def __init__(self):
        logger.info('- Initializing SelectChoice')
    def select_choice(self, options):
        logger.info("- selecting choice")
        length = len(list(options))
        for i, option in enumerate(options):
            print(f"{i+1}: {option}")
        try:
            choice = int(input(f"Enter your choice(1-{length}): "))
            if isinstance(choice, int):
                if choice < 1 or choice > length: 
                    logger.exception(f"\nInvalid Choice - {choice}\n")
                logger.debug(f"\n choice - {choice}")
                return options[int(choice-1)]
        except ValueError as error:
            logger.exception(f"\nInvalid Choice - {choice}\nError: -{error}")


def get_selector(options):
    logger.info("- running get selector")
    selector = SelectChoice()
    selection = selector.select_choice(options)
    logger.debug(f"\n selector - {selector}\n options - {options}\n selection - {selection}")
    return selection

if __name__ == "__main__":
    selected = get_selector(options=["D&D", "Cyberpunk", "Scifi"])
    print(selected) 
    
