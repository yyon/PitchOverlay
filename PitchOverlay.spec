# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'Images', 'Images' ),
         ( 'app.vrmanifest', '.'),
         ( 'config.json', '.'),
         ]

import openvr
import crepe
openvr_dll_path = os.path.join(os.path.dirname(openvr.__file__), 'libopenvr_api_64.dll')
crepe_model_path = os.path.join(os.path.dirname(crepe.__file__), 'model-tiny.h5')
         
a = Analysis(['PitchOverlay.py'],
             binaries=[ (openvr_dll_path, '.' ), (crepe_model_path, 'crepe/')],
             datas = added_files,
             hiddenimports=['ctypes'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='PitchOverlay',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='PitchOverlay')
