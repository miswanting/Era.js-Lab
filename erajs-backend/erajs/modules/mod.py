
class ModManager:
    """
    # 模组管理器
    # Mod File Structure
    ```
    Mod
    ├─ config
    │  ├─ *.yml
    │  ├─ *.json
    │  └─ ...
    ├─ data
    │  ├─ *.yml
    │  ├─ *.json
    │  └─ ...
    ├─ res
    │  ├─ *.svg
    │  ├─ *.png
    │  └─ ...
    ├─ meta.yml
    ├─ *.py
    └─ ...
    ```
    # Mod Meta File Structure(meta.yml)
    ```yml
    id: test #(required)[Short,NoSpace]
    name: A Friendly Name #(optional)[AnyStr]
    version: v0.1.0-beta+201112.fix #(required)[QualifiedSemVer]
    main: test.py #(required)
    ```
    """

    def __init__(self):
        super().__init__()

    def scan_mods(self) -> Dict[str, str]:
        mods: Dict[str, str] = {}
        for entry_name in os.listdir('mods'):
            path = os.path.join('mods', entry_name)
            if os.path.isdir(path):
                meta_path = os.path.join(path, 'meta.yml')
                if os.path.isfile(meta_path):
                    meta = self.read(meta_path)
                    meta['path'] = path
                    if meta['id'] in mods:
                        new_dot_path = DotPath.path2dot(path)[0]
                        old_dot_path = DotPath.path2dot(
                            mods[meta['id']]['path']
                        )[0]
                        self.warn(
                            f'│  ├─ [!] Mod ID Conflict! [{new_dot_path}] will overwrite [{old_dot_path}]!'
                        )
                    mods[meta['id']] = meta
        return mods

    def load_mod_data(self, id: str):
        sys_config = self.cfg('sys')
        if sys_config is None:
            return
        configs = sys_config['mods']
        config = configs[self.findModInCfg(id)]
        data_file_paths = self.scan(config['path'])
        data_file_dot_paths = []
        for path in data_file_paths:
            path = path.replace('/', '\\')
            if path.split('\\')[2] == 'data':
                data_file_dot_paths.append(['{}.'.format(config['id'])+DotPath.path2dot('\\'.join(path.split('\\')[3:]))[0], path])
                self.register(path)
        for pair in data_file_dot_paths:
            self.dat()[pair[0]] = self.read(pair[1])

    def load_mod(self, id: str):
        sys_config = self.cfg('sys')
        if sys_config is None:
            return
        configs = sys_config['mods']
        config = configs[self.findModInCfg(id)]
        module = self.get_mod_module(config)
        if 'on_loaded' in dir(module):
            module.on_loaded()

    def enable_mod(self, id: str):
        sys_config = self.cfg('sys')
        if sys_config is None:
            return
        configs = sys_config['mods']
        config = configs[self.findModInCfg(id)]
        config['enabled'] = True
        module = self.get_mod_module(config)
        if 'on_enabled' in dir(module):
            module.on_enabled()

    def disable_mod(self, id: str):
        sys_config = self.cfg('sys')
        if sys_config is None:
            return
        configs = sys_config['mods']
        config = configs[self.findModInCfg(id)]
        config['enabled'] = False
        self.write(os.path.join('config', 'sys.yml'), self.cfg('sys'))
        module = self.get_mod_module(config)
        if 'on_disabled' in dir(module):
            module.on_disabled()

    def get_mod_module(self, config: Dict[str, str]):
        meta_path = os.path.join(config['path'], 'meta.yml')
        meta = self.read(meta_path)
        main_path = os.path.join(config['path'], meta['main'])
        modFolderName = os.path.split(config['path'])[1]
        spec = spec_from_file_location(
            f'mods.{modFolderName}.', main_path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def findModInCfg(self, id: str):
        sys_config = self.cfg('sys')
        if sys_config is None:
            return
        configs = sys_config['mods']
        for i, cfg in enumerate(configs):
            if id == cfg['id']:
                return i
        return -1
