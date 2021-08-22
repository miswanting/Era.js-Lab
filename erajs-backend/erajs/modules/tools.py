from datetime import datetime
from secrets import randbelow, token_hex


class Tools:
    @staticmethod
    def random_hash(level: int = 4):
        """
        # 随机哈希值生成器
        返回随机生成的哈希字符串
        - level == n，返回长度为2n的字符串，在16^n个项目中随机，任意两个值相同的概率为1/16^n/2。
        - 示例：U2S3T7F5
        """
        return token_hex(level).upper()

    @staticmethod
    def timestamp():
        """
        # 时间戳生成器
        - 示例：201231-030619-123456
        """
        return datetime.today().strftime("%y%m%d-%H%M%S-%f")

    @staticmethod
    def uuid():
        """
        # UUID生成器
        - 示例：201231-030619-123456-394527
        """
        timestamp = Tools.timestamp()
        hash = '{:0>6d}'.format(randbelow(1000000))
        uuid = '{}-{}'.format(timestamp, hash)
        return uuid
