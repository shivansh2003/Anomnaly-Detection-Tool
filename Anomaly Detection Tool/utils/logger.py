from rich.console import Console
from rich.logging import RichHandler
import logging
from datetime import datetime

console = Console()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console)]
)

log = logging.getLogger("rich")

# Custom log functions
def log_info(message):
    log.info(message)

def log_debug(message):
    log.debug(message)

def log_error(message):
    log.error(message)

def log_success(msg):
    console.log(f"[bold bright_green][{timestamp()}] SUCCESS [/bold bright_green] {msg}")

def timestamp():
    return datetime.now().strftime("%H:%M:%S")

def log_warning(msg):
    console.log(f"[bold yellow][{timestamp()}] WARNING [/bold yellow] {msg}")

