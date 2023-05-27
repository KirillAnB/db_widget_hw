import sys

from PySide6 import QtWidgets, QtSql, QtCore, QtGui

class My_Db_Widget(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.initDb()
        self.initTableModel()
        self.initUi()
        self.initSignals()

    def initDb(self) -> None:
        """
        Поключаемся к локальной базде данных sqlite
        :return: None
        """
        connection = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        connection.setDatabaseName('DZ_database.db')
        connection.open()


    def initUi(self):
        """
        Инициализация ui
        :return: None
        """

        self.setWindowTitle('DZ Putilovo')
        self.resize(850, 480)
        self.tableView = QtWidgets.QTableView()
        self.tableView.resizeColumnsToContents()
        self.tableView.setModel(self.dzTableModel)
        #
        # Скрываю колонку id
        # self.tableView.hideColumn(0)


        self.addButton = QtWidgets.QPushButton('Внести запись')
        self.deleteButton = QtWidgets.QPushButton('Удалить запись')
        self.applyButton = QtWidgets.QPushButton('Сохранить изменения')
        buttonsLayout = QtWidgets.QHBoxLayout()
        buttonsLayout.addWidget(self.addButton)
        buttonsLayout.addWidget(self.deleteButton)
        buttonsLayout.addWidget(self.applyButton)


        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.tableView)
        self.vbox.addLayout(buttonsLayout)
        self.setLayout(self.vbox)

    def initTableModel(self) -> None:
        """
        Создаем модель таблицы AAD
        :return: None
        """
        self.dzTableModel = QtSql.QSqlTableModel(self)
        self.dzTableModel.setTable('AAD')
        self.dzTableModel.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
        self.dzTableModel.select()

        # self.stm.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, "ID")
        self.dzTableModel.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, "AAD ID")
        self.dzTableModel.setHeaderData(3, QtCore.Qt.Orientation.Horizontal, "SERIAL NUMBER")
        self.dzTableModel.setHeaderData(4, QtCore.Qt.Orientation.Horizontal, "MANUFACTURER")
        self.dzTableModel.setHeaderData(5, QtCore.Qt.Orientation.Horizontal, "MODEL")
        self.dzTableModel.setHeaderData(6, QtCore.Qt.Orientation.Horizontal, "MFD")
        self.dzTableModel.setHeaderData(7, QtCore.Qt.Orientation.Horizontal, "SERVICE DATE")
        self.dzTableModel.setHeaderData(8, QtCore.Qt.Orientation.Horizontal, "VALID DATE")

    def initSignals(self) -> None:
        """
        Инициализируем сигналы
        :return: None
        """

        self.addButton.clicked.connect(self.addButtonPushed)
        self.deleteButton.clicked.connect(self.deleteButtonPushed)
        self.applyButton.clicked.connect(self.applyButtonPushed)

    def addButtonPushed(self) -> None:
        """
        Добавляем пустую строку для внесения данных
        :return: None
        """
        self.dzTableModel.insertRow(self.dzTableModel.rowCount())

    def deleteButtonPushed(self) -> None:
        """
        Удаляем строку из модели и обновляем модель
        :return: None
        """
        self.dzTableModel.removeRow(self.tableView.currentIndex().row())
        self.dzTableModel.select()

    def applyButtonPushed(self) -> None:
        """
        Сохраняет внесенные изменения в таблицу
        :return: None
        """
        self.dzTableModel.submitAll()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    db_widget = My_Db_Widget()

    db_widget.show()
    app.exec()

# TODO скрыть id, кнопка сохранить, делегаты на дату