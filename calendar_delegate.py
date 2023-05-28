

from PySide6 import QtWidgets, QtCore
from typing import Union

class CalendarToDelegate(QtWidgets.QStyledItemDelegate):
    """Класс для создания календаря-делегата"""

    def createEditor(self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem,
                     index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> QtWidgets.QWidget:

        editor = QtWidgets.QCalendarWidget()
        return editor
    def updateEditorGeometry(self, editor: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem, index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> None:

        self.updateEditorGeometry(option.rect)

    def setModelData(self, editor: QtWidgets.QWidget, model: QtCore.QAbstractItemModel, index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> None:

        date = editor.selectedDate()
        model.setData(value=date)