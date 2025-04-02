from PyInstaller.utils.hooks import collect_submodules

# Collect all submodules in libs.JAF (your plugin modules)
hiddenimports = collect_submodules('libs.JAF')

