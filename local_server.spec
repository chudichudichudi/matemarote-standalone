# -*- mode: python -*-
a = Analysis(['local_server.py'],
             pathex=['/home/chudi/trabajo/metacog-mm'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='local_server',
          debug=False,
          strip=None,
          upx=True,
          console=True )
