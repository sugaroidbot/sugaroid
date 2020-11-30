# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['launcher.py'],
             pathex=['C:\\Windows\\System32\\vcomp140.dll', 'O:\\'],
             binaries=[('C:\\Windows\\System32\\vcomp140.dll', '.')],
             datas=[],
             hiddenimports=['sugaroid', 'sugaroid_chatterbot', 'sugaroid_chatterbot_corpus', 'pkg_resources.py2_warn', 'en_core_web_sm'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='sugaroid',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='sugaroid.ico')
