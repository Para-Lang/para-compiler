# -*- mode: python ; coding: utf-8 -*

block_cipher = None
GLOBAL_EXCLUDE = [
    "jedi",
    "IPython",
    "numpy",
    "matplotlib"
]
HIDDEN_IMPORTS = [
    "paralang_cli",
    "paralang_base"
]

# 'para' CLI command
para_a = Analysis(['para.py'],
                  pathex=[],
                  binaries=[],
                  datas=[],
                  hiddenimports=HIDDEN_IMPORTS,
                  hookspath=[],
                  hooksconfig={},
                  runtime_hooks=[],
                  excludes=GLOBAL_EXCLUDE,
                  win_no_prefer_redirects=False,
                  win_private_assemblies=False,
                  cipher=block_cipher,
                  noarchive=False)

# 'paraproj' CLI command
paraproj_a = Analysis(['paraproj.py'],
                      pathex=[],
                      binaries=[],
                      datas=[],
                      hiddenimports=HIDDEN_IMPORTS,
                      hookspath=[],
                      hooksconfig={},
                      runtime_hooks=[],
                      excludes=GLOBAL_EXCLUDE,
                      win_no_prefer_redirects=False,
                      win_private_assemblies=False,
                      cipher=block_cipher,
                      noarchive=False)

# Merging them into a single distribution
MERGE((para_a, 'para', 'para'), (paraproj_a, 'paraproj', 'paraproj'))

# Generating the executable for 'para'
pyz = PYZ(para_a.pure, para_a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          para_a.scripts,
          [],
          exclude_binaries=True,
          name='para',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='../img/para.ico')
coll = COLLECT(exe,
               para_a.binaries,
               para_a.zipfiles,
               para_a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='para')

# Generating the executable for 'paraproj'
pyz = PYZ(paraproj_a.pure, paraproj_a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          paraproj_a.scripts,
          [],
          exclude_binaries=True,
          name='paraproj',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='../img/para.ico'
          )
coll = COLLECT(exe,
               paraproj_a.binaries,
               paraproj_a.zipfiles,
               paraproj_a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='paraproj')
