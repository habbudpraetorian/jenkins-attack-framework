from PyInstaller.utils.hooks import collect_submodules

# This grabs all submodules inside jaf.commands (or wherever your commands live)
hiddenimports = collect_submodules('jaf.commands')

