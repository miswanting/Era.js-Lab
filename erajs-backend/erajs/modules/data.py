from typing import Any, Dict, List, Optional

from ..formats import csv


class IOProxy:
    def get_io_by_ext(self):
        pass

class DataManager:
    """
    # 数据管理器
    ## 数据范围Scope
    约定：单个账号同时只能存在一个数据实体
    为单人分配的数据为：
    ```
    ┌──────────────┬─────────────────────┐
    │Logic:        │Data:                │
    │Engine        │Global               │
    │├─────────┬┄  │├───────────────┬┄   │
    │Room      Room│World           World│
    │├────┬┄       │├───────┬┄           │
    │User User     │Profile Profile      │
    └──────────────┴─────────────────────┘
    ```
    ## 点路径
    Global Dot Path(GDP) <==> Path(P)
    代表物理文件的数字孪生（强制一对一，双向修改）
    (Local )Dot Path
    代表各种类数据
    Path → GDP → DP
    File → FileData → Data
    ```
    ┌───────────────────┐
    │Logic      Physics │
    │File  <==> FileData│Mount,Unmount
    │World <==> Cache   │
    │User  <==> Save    │save,load
    └───────────────────┘
    ```
    ## 数据类型
    ## 数据操作
    ### GDP
    raw('etc')      = \\data\\etc.yml
    mod('era.item') = \\mods\\EraLifeEraizationMod\\data\\items.yml
    res('cover')    = \\res\\cover.jpg
    cfg('sys')      = \\configs\\sys.ymvl
    dat('etc')      = \\data\\etc.yml--
    sav()           = \\save\\quick.save
    """
    SCOPE_MAP = {
        'config': 'cfg',
        'data': 'dat',
        'save': 'sav',
        'res': 'res',
        'mods': 'mod'
    }

    def __init__(self):
        super().__init__()
        self.__raw: Dict[str, Any] = {}
        self.__cfg: Dict[str, Any] = {}
        self.__dat: Dict[str, Any] = {}
        self.__sav: Dict[str, Dict[str, Any]] = {
            'meta': {},
            'data': {}
        }
        self.__res: Dict[str, Any] = {}
        self.__tmp: Dict[str, Any] = {}
        self.registry: Dict[str, str] = {}

    def register(self, path: str, mod_id: Optional[str] = None):
        """
        ['mod.era.items'] = \\mods\\EraLifeEraizationMod\\data\\items.yml
        """
        GDP = self.P2GDP(path, mod_id)
        self.registry[GDP[0]] = path
        return GDP

    def get_registries(self, scope: str):
        candidates: List[str] = []
        for gdp in self.registry:
            if gdp.split('.')[0] == scope:
                candidates.append(gdp)
        return candidates

    def get_io_by_ext(self, ext: str):
        if ext in ['.inf', '.ini', '.cfg', '.conf', '.config']:
            return cfg_file
        elif ext == '.csv':
            return csv_file
        elif ext == '.json':
            return json_file
        elif ext in ['.yml', '.yaml']:
            return yaml_file
        elif ext == '.zip':
            return zip_file
        elif ext == '.txt':
            return text_file
        elif ext in ['.save', '.sav']:
            return save_file
        else:
            return raw_file

    def read(self, path: str):
        """
        # 读取文件到数据
        """
        ext = os.path.splitext(path)[1].lower()
        reader = self.get_io_by_ext(ext)
        return reader.read(path)

    def write(self, path: str, data: Any = None):
        """
        # 写入数据到文件
        """
        ext = os.path.splitext(path)[1].lower()
        writer = self.get_io_by_ext(ext)
        writer.write(path, data)

    def P2GDP(self, path: str, mod_id: Optional[str] = None):
        pieces = path.replace('/', '\\').replace('\\', '.').split('.')
        pieces[0] = self.SCOPE_MAP[pieces[0]]
        if pieces[0] == 'mod' and mod_id is not None:
            pieces[1] = mod_id
        dot = '.'.join(pieces[0:-1])
        ext = pieces[-1].lower()
        return dot, ext

    def GDP2DP(self, gdp: str):
        pieces = gdp.split(".")
        scope = pieces[0]
        dp = '.'.join(pieces[1:])
        return dp, scope

    def DP2GDP(self, dp: str, scope: str, mod_id: Optional[str] = None):
        if scope == 'mod' and mod_id is not None:
            dp = '{}.{}'.format(mod_id, dp)
        gdp = '{}.{}'.format(scope, dp)
        return gdp

    def scan(self, path: str):
        """
        # 递归文件夹路径下文件的路径
        """
        files: List[str] = []
        for dirpath, _, filenames in os.walk(path, True):
            for filename in filenames:
                files.append('{}\\{}'.format(dirpath, filename))
        return files

    def mount(self, gdp: str):
        if gdp in self.registry:
            if gdp not in self.__raw:
                self.__raw[gdp] = self.read(self.registry[gdp])

    def umount(self, gdp: str):
        if gdp in self.__raw:
            del self.__raw[gdp]

    def umount_all(self):
        self.__raw.clear()

    def mounted(self, gdp: str):
        return gdp in self.__raw

    def save(self, gdp: str):
        if self.mounted(gdp):
            self.write(self.registry[gdp], self.__raw[gdp])

    def raw(self, gdp: str):
        """
        ('era.items', 'dat') = \\mods\\EraLifeEraizationMod\\data\\items.yml
        """
        if gdp in self.__raw:
            return self.__raw[gdp]
        elif gdp in self.registry:
            self.mount(gdp)
            return self.__raw[gdp]
        return None

    def cfg(self, dp: Optional[str] = None) -> Optional[Dict[str, str]]:
        """
        # CFG
        """
        if dp is None:
            return self.__cfg
        elif dp in self.__cfg:
            return self.__cfg[dp]
        else:
            gdp = self.DP2GDP(dp, 'cfg')
            if gdp in self.__raw:
                self.__cfg[dp] = self.__raw[gdp]
                return self.__cfg[dp]
            elif gdp in self.registry:
                if self.mount(gdp):
                    self.__cfg[dp] = self.__raw[gdp]
                    return self.__cfg[dp]
        return None

    def dat(self, dp: Optional[str] = None) -> Optional[Dict[str, str]]:
        """
        # DAT
        """
        if dp is None:
            return self.__dat
        elif dp in self.__dat:
            return self.__dat[dp]
        else:
            gdp = self.DP2GDP(dp, 'dat')
            if gdp in self.__raw:
                self.__dat[dp] = self.__raw[gdp]
                return self.__dat[dp]
            elif gdp in self.registry:
                if self.mount(gdp):
                    self.__dat[dp] = self.__raw[gdp]
                    return self.__dat[dp]
        return None

    def sav(self, dp: Optional[str] = None) -> Optional[Dict[str, str]]:
        """
        # SAV
        除非你需要操作存档信息，否则请不要占用“meta”点路径，因为sav('meta')是内置的存档信息保存点。
        """
        if dp is None:
            return self.__sav['data']
        elif dp == 'meta':
            return self.__sav['meta']
        elif dp in self.__sav['data']:
            return self.__sav['data'][dp]
        else:
            return None

    def tmp(self, key: Optional[str] = None) -> Dict[str, str]:
        """
        # TMP
        tmp
        """
        if key is None:
            return self.__tmp
        elif key in self.__tmp:
            return self.__tmp[key]
        else:
            self.__tmp[key] = {}
            return self.__tmp[key]

    @property
    def data(self):
        """
        Deprecated
        """
        data: Dict[str, Any] = {
            'cfg': self.__cfg,
            'dat': self.__dat,
            'sav': self.__sav,
            'tmp': self.__tmp,
            'res': self.__res,
        }
        return data
