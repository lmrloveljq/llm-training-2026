from loguru import logger
import os

# 自动获取项目根目录，永远不会错
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
log_file = os.path.join(BASE_DIR, "logs", "app.log")

# 配置日志
logger.add(
    sink=log_file,
    rotation="00:00",
    retention="7 days",
    compression="zip",
    encoding="utf-8",

    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}\n{exception}"
)

__all__ = ["my_logger"]