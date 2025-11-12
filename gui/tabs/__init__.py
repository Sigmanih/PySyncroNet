"""
Tabs package per l'interfaccia grafica di PySyncroNet
"""

from gui.tabs.pdf_creator_tab import PDFCreatorTab
from gui.tabs.project_recreator_tab import ProjectRecreatorTab
from gui.tabs.exclusions_tab import ExclusionsTab
from gui.tabs.settings_tab import SettingsTab

__all__ = [
    'PDFCreatorTab',
    'ProjectRecreatorTab',
    'ExclusionsTab',
    'SettingsTab'
]