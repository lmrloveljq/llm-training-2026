from  src.utils.logger import logger
def divide_numbers(a,b):
    try:
        result=a/b
        logger.info(f"计算成功：{a}/{b}={result}")
        return result
    except ZeroDivisionError as e:
        logger.error(f"计算错误：除以0！错误信息{e}")
        return None
    except TypeError as e:
        logger.error(f"类型错误：参数不是数字！错误信息{e}",exc_info=False)
    except Exception as e:
        logger.exception(f"未知错误：{e}",exc_info=True)
        return None



if __name__=="__main__":
    divide_numbers(10,2)
    divide_numbers(10,0)
    divide_numbers(10,'2')
# print(1+2)    # divide_numbers("你好呀")
