import sys
from cx_Freeze import setup, Executable



base = None
# 判断Windows系统
# if sys.platform == 'win32':
#     base = 'Win32GUI'

packages = ['os', 'tensorflow', 'shutil', 'cv2', 'numpy', 'time', 'sys', 'scipy']

for dbmodule in ['win32gui', 'win32api', 'win32con', 'cx_Freeze']:
    try:
        __import__(dbmodule)
    except ImportError:
        pass
    else:
        packages.append(dbmodule)
options = {
    'build_exe':
        {
            'includes': 'atexit'
            # 依赖的包
            , "packages": packages
            # 额外添加的文件
            , 'include_files': ['nets', 'utils']  #'modules.py', 'config.py', 'data_generator.py'
        }

}

executables = [
    Executable(
        # 工程的 入口
        'EL.py'
        , base=base
        # 生成 的文件 名字
        , targetName='EL_CPU.exe'
        # 生成的EXE的图标
        , icon = "EL.ico" #图标, 32*32px
    )
]

setup(
    # 产品名称
    name='cx-CPTN',
    # 版本号
    version='1.0',
    # 产品说明
    description='cx-CPTN',
    options=options,
    executables=executables
)
