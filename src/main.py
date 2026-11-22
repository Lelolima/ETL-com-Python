import os

from .dashboard.ibovespa_dashboard import IbovespaDashboard
from .utils.logger import get_logger

logger = get_logger(__name__)

def main():
    try:
        dashboard = IbovespaDashboard()
        logger.info("Starting dashboard")
        # debug desligado por padrão (o modo debug do Dash expõe o depurador); ative com DASH_DEBUG=1
        dashboard.run(debug=os.getenv("DASH_DEBUG") == "1")
    except Exception as e:
        logger.error(f"Failed to start dashboard: {str(e)}")
        raise

if __name__ == "__main__":
    main()