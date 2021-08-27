import sys
from logging import DEBUG, INFO
from os import chdir, mkdir
from os.path import dirname, isdir, isfile, join
from typing import Any, Dict, List, Optional

from semver import compare

from .modules.data import DataManager
from .modules.debug import DebugManager
from .modules.dot_path import path2dot
from .modules.event import EventManager
from .modules.mod import ModManager
from .modules.net import NetManager
from .modules.ui import UiManager
# from .modules.server import start
from .prototypes.singleton import Singleton


class Engine(Singleton):
    def __init__(self, configs: Optional[Dict[str, Any]] = {'debug': True}):
        super().__init__()
        self.dem = DebugManager()
        self.dem.init(DEBUG if configs['debug'] else INFO)
        self.em = EventManager()
        self.dam = DataManager()
        self.nm = NetManager()
        self.mm = ModManager()
        self.um = UiManager()
        # start()

    def init(self):
        """
        # 初始化 Era.js 游戏引擎
        绝大部分游戏引擎的功能只能在初始化后使用
        """
        def fix_path():
            """
            # 修正根路径
            """
            self.dem.info('├─ Fixing Path...')
            if getattr(sys, 'frozen', False):
                # 生产环境（已打包）
                path = dirname(sys.executable)
            else:
                # 开发环境（未打包）
                path = join(dirname(__file__), '..')
            chdir(path)
            self.dem.info('│  └─ Path Fixed!')

        def fix_fs_hierarchy():
            """
            # 维护文件系统架构
            """
            fs_hierarchy = {
                'cache': {},
                'config': {
                    'sys.yml': None
                },
                'data': {},
                'mods': {},
                'res': {},
                'save': {},
            }

            def fix_one_layer(path: str, template: Dict[str, Any]):
                for key in template:
                    if type(template[key]) is dict:
                        dir_path = join(path, key)
                        if not isdir(dir_path):
                            self.dem.warning(
                                f'│  ├─ Folder [{key}] Missing. Creating...')
                            mkdir(dir_path)
                        fix_one_layer(dir_path, template[key])
                    else:
                        file_path = join(path, key)
                        if not isfile(file_path):
                            self.dem.warning(
                                f'│  ├─ File [{key}] Missing. Creating...')
                            data = None
                            if file_path == '.\\config\\sys.yml':
                                data = {
                                    'resolution': [800, 600],
                                    'mods': []
                                }
                            self.dam.write(file_path, data)
            self.dem.info('├─ Checking Data Integrity...')
            fix_one_layer('.', fs_hierarchy)
            self.dem.info('│  └─ Data Integrity Checked!')

        def load_configs():
            self.dem.info('├─ Scanning Configs...')
            paths = self.dam.scan('config')
            for path in paths:
                dp = self.dam.GDP2DP(self.dam.register(path)[0])[0]
                self.dem.info(f'│  ├─ Config [{dp}] Found.')
            self.dem.info(f'│  └─ {len(paths)} Configs Found!')
            self.dem.info('├─ Loading Configs...')
            n = 0
            for gdp in self.dam.get_registries('cfg'):
                dp = self.dam.GDP2DP(gdp)[0]
                if self.dam.cfg() is not None:
                    self.dam.cfg()[dp] = self.dam.read(self.dam.registry[gdp])
                    self.dem.info(f'│  ├─ Config [{dp}] Loaded.')
                    n += 1
            self.dem.info(f'│  └─ {len(paths)} Configs Loaded!')

        def send_config():
            self.dem.info('├─ Sending Engine Config...')
            self.nm.send({'type': 'cfg', 'data': self.dam.cfg('sys')})
            self.dem.info('│  └─ Configs Sent!')

        def load_data_files():
            self.dem.info('├─ Scanning Data Files...')
            self.um.push('set_loading_title', {
                         'value': 'Scanning Data Files...'})
            self.um.push('set_loading_text', {'value': ''})
            paths = self.dam.scan('data')
            for path in paths:
                dp = self.dam.GDP2DP(self.dam.register(path)[0])[0]
                self.dem.info(f'│  ├─ Data File [{dp}] Found.')
                self.um.push('set_loading_text', {
                    'value': f'Data File [{dp}] Found.'})
            # for path in paths:
            #     dot_path = '.'.join(DotPath.path2dot(path)[0].split('.')[1:])
            #     e.register(path)
            #     e.info(f'│  ├─ Data File [{dot_path}] Found.')
            #     e.push('set_loading_text', {
            #            'value': f'Data File [{dot_path}] Found.'})
            self.dem.info(f'│  └─ {len(paths)} Data Files Found!')
            self.dem.info('├─ Loading Data Files...')
            self.um.push('set_loading_title', {
                         'value': 'Loading Data Files...'})
            self.um.push('set_loading_text', {'value': ''})
            for gdp in self.dam.get_registries('dat'):
                dp = self.dam.GDP2DP(gdp)[0]
                if self.dam.dat() is not None:
                    self.dam.dat()[dp] = self.dam.read(self.dam.registry[gdp])
                    self.dem.info(f'│  ├─ Data File [{dp}] Loaded.')
                    self.um.push('set_loading_text', {
                        'value': f'Data File [{dp}] Loaded.'})
            # for path in paths:
            #     dot_path = '.'.join(DotPath.path2dot(path)[0].split('.')[1:])
            #     data = e.dat()
            #     if data is not None:
            #         data[dot_path] = e.read(path)
            #         e.info(f'│  ├─ Data File [{dot_path}] Loaded.')
            #         e.push('set_loading_text', {
            #             'value': f'Data File [{dot_path}] Loaded.'})
            self.dem.info(f'│  └─ {len(paths)} Data Files Loaded!')

        def register_resource_files():
            """
            """
            self.dem.info('├─ Scanning Resource Files...')
            self.um.push('set_loading_title', {
                'value': 'Scanning Resource Files...'})
            self.um.push('set_loading_text', {'value': ''})
            paths = self.dam.scan('res')
            for path in paths:

                self.dam.registry[path2dot(path)] = path
                dot_path = '.'.join(path2dot(path)[0].split('.')[1:])
                self.dem.info(f'│  ├─ Resource File [{dot_path}] Found.')
                self.um.push('set_loading_text', {
                    'value': f'Resource File [{dot_path}] Found.'})
            self.dem.info(f'│  └─ {len(paths)} Resource Files Found!')
            self.dem.info('├─ Register Resource Files...')
            self.um.push('set_loading_title', {
                'value': 'Register Resource Files...'})
            self.um.push('set_loading_text', {'value': ''})
            for path in paths:
                dp_pair = path2dot(path)
                dot_path = '.'.join(dp_pair[0].split('.')[1:])
                self.dam.data['res'][dot_path] = {
                    'path': path, 'ext': dp_pair[1]}
                self.dem.info(f'│  ├─ Resource File [{dot_path}] Registered.')
                self.um.push('set_loading_text', {
                    'value': f'Resource File [{dot_path}] Registered.'})
            self.dem.info(f'│  └─ {len(paths)} Resource Files Registered!')

        def load_mods():
            self.dem.info('├─ Scanning Mods...')
            self.um.push('set_loading_title', {'value': 'Scanning Mods...'})
            self.um.push('set_loading_text', {'value': ''})
            # Config -> File System : Check Config Deletes
            metas = self.mm.scan_mods()
            sys_config = self.dam.cfg('sys')
            if sys_config is None:
                return
            configs = sys_config['mods']
            new_configs: List[Dict[str, Any]] = []
            for config in configs:
                # Find If Config Item Exist.
                found = False
                for id in metas:
                    if id == config['id']:
                        if compare(metas[id]['version'], config['version']) == 1:
                            # New Version
                            config['version'] = metas[id]['version']
                            self.dem.info(
                                f'│  ├─ Update Mod [{config["name"]}] Found.')
                        found = True
                if found:
                    new_configs.append(config)
                else:
                    self.dem.info(
                        f'│  ├─ Mod [{config["name"] if "name" in config else config["id"]}] Deleted.')
            # File System -> Config : Check New Mods
            for id in metas:
                self.dem.info(
                    f'│  ├─ Mod [{metas[id]["name"] if "name" in metas[id] else id}] Found.')
                self.um.push('set_loading_text', {
                    'value': f'Mod [{metas[id]["name"] if "name" in metas[id] else id}] Found.'})
                index = self.mm.findModInCfg(id)
                if index == -1:
                    new_config = {
                        'id': id,
                        'version': metas[id]['version'],
                        'enabled': False,
                        'path': metas[id]['path']
                    }
                    if 'name' in metas[id]:
                        new_config['name'] = metas[id]['name']
                    if 'alias' in metas[id]:
                        new_config['alias'] = metas[id]['alias']
                    if 'description' in metas[id]:
                        new_config['description'] = metas[id]['description']
                    if 'dependencies' in metas[id]:
                        new_config['dependencies'] = metas[id]['dependencies']
                    sys_config['mods'].append(new_config)
                self.dam.write(join('config', 'sys.yml'), self.dam.cfg('sys'))
            self.dem.info(f'│  └─ {len(metas)} Mods Found!')
            # Load Mods
            self.dem.info('├─ Loading Mods...')
            self.um.push('set_loading_title', {'value': 'Loading Mods...'})
            self.um.push('set_loading_text', {'value': ''})
            n = 0
            for config in configs:
                if config['enabled']:
                    self.dem.info(
                        f'│  ├─ Mod [{config["name"] if "name" in config else config["id"]}] Loading...')
                    self.um.push('set_loading_text', {
                        'value': f'Mod [{config["name"] if "name" in config else config["id"]}] Loading...'})
                    self.mm.load_mod_data(config['id'])
                    self.mm.load_mod(config['id'])
                    n += 1
            self.dem.info(f'│  └─ {n} Mods Loaded!')
        # Init Start
        self.dem.info('Era.js Engine Initializing...')
        fix_path()
        fix_fs_hierarchy()
        load_configs()
        self.nm.start('localhost', 8080)
        self.dem.info('├─ Server Start!')
        # if not self.nm.connect('localhost', 11994):
        #     self.dem.info('Initialization Failed!')
        #     sys.exit(1)
        # send_config()
        # load_data_files()
        # register_resource_files()
        # load_mods()
        # self.dam.umount_all()
        # self.um.push('loaded')
        # self.dem.info('Initialization Done!')

    def entry(self):
        pass
