from src.utils.logger import logger
def run_app():
    logger.info("项目启动成功：")
    try:
        logger.info("正常运行中 ")
    except Exception as e:
        logger.error(f'运行出错{e}')
if __name__=="__main__":
    run_app()