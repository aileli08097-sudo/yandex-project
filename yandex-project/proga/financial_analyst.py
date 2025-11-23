import io
import sys
from random import choice
import matplotlib.pyplot as plt
import sqlite3
import os

from PyQt6 import uic
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStatusBar
from matplotlib.pyplot import title

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>785</width>
    <height>617</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Финансовый аналитик</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QHBoxLayout" name="horizontalLayout">
    <item>
     <widget class="QTabWidget" name="tabWidget">
      <property name="currentIndex">
       <number>0</number>
      </property>
      <widget class="QWidget" name="mainTab">
       <attribute name="title">
        <string>Главная</string>
       </attribute>
       <widget class="QPushButton" name="incomeButton">
        <property name="geometry">
         <rect>
          <x>20</x>
          <y>40</y>
          <width>351</width>
          <height>31</height>
         </rect>
        </property>
        <property name="text">
         <string>Посмотреть раздел &quot;Доходы&quot;</string>
        </property>
       </widget>
       <widget class="QPushButton" name="expensesButton">
        <property name="geometry">
         <rect>
          <x>20</x>
          <y>90</y>
          <width>351</width>
          <height>31</height>
         </rect>
        </property>
        <property name="text">
         <string>Посмотреть раздел &quot;Расходы&quot;</string>
        </property>
       </widget>
       <widget class="QPushButton" name="balanceButton">
        <property name="geometry">
         <rect>
          <x>20</x>
          <y>140</y>
          <width>351</width>
          <height>31</height>
         </rect>
        </property>
        <property name="text">
         <string>Посмотреть свой баланс</string>
        </property>
       </widget>
       <widget class="QPushButton" name="spendingButton">
        <property name="geometry">
         <rect>
          <x>20</x>
          <y>190</y>
          <width>351</width>
          <height>31</height>
         </rect>
        </property>
        <property name="text">
         <string>Посмотреть категории трат</string>
        </property>
       </widget>
       <widget class="QLabel" name="label_22">
        <property name="geometry">
         <rect>
          <x>20</x>
          <y>10</y>
          <width>251</width>
          <height>21</height>
         </rect>
        </property>
        <property name="text">
         <string>Узнайте про свои финансы:</string>
        </property>
       </widget>
       <widget class="QLabel" name="label_25">
        <property name="geometry">
         <rect>
          <x>410</x>
          <y>20</y>
          <width>321</width>
          <height>201</height>
         </rect>
        </property>
        <property name="text">
         <string>TextLabel</string>
        </property>
       </widget>
       <widget class="QTextBrowser" name="rec_1">
        <property name="geometry">
         <rect>
          <x>20</x>
          <y>250</y>
          <width>351</width>
          <height>91</height>
         </rect>
        </property>
       </widget>
       <widget class="QTextBrowser" name="rec_3">
        <property name="geometry">
         <rect>
          <x>390</x>
          <y>250</y>
          <width>351</width>
          <height>91</height>
         </rect>
        </property>
       </widget>
       <widget class="QTextBrowser" name="rec_2">
        <property name="geometry">
         <rect>
          <x>20</x>
          <y>360</y>
          <width>351</width>
          <height>91</height>
         </rect>
        </property>
       </widget>
       <widget class="QTextBrowser" name="rec_4">
        <property name="geometry">
         <rect>
          <x>390</x>
          <y>360</y>
          <width>351</width>
          <height>91</height>
         </rect>
        </property>
       </widget>
      </widget>
      <widget class="QWidget" name="balanceTab">
       <attribute name="title">
        <string>Бюджет</string>
       </attribute>
       <layout class="QHBoxLayout" name="horizontalLayout_2">
        <item>
         <widget class="QToolBox" name="toolBox">
          <property name="currentIndex">
           <number>0</number>
          </property>
          <widget class="QWidget" name="page_incomes">
           <property name="geometry">
            <rect>
             <x>0</x>
             <y>0</y>
             <width>743</width>
             <height>408</height>
            </rect>
           </property>
           <attribute name="label">
            <string>Доходы</string>
           </attribute>
           <widget class="QPushButton" name="RegIncButton">
            <property name="geometry">
             <rect>
              <x>10</x>
              <y>10</y>
              <width>201</width>
              <height>31</height>
             </rect>
            </property>
            <property name="text">
             <string>Добавить регулярный доход</string>
            </property>
           </widget>
           <widget class="QPushButton" name="OneIncButton">
            <property name="geometry">
             <rect>
              <x>10</x>
              <y>50</y>
              <width>201</width>
              <height>31</height>
             </rect>
            </property>
            <property name="text">
             <string>Добавить единоразовый доход</string>
            </property>
           </widget>
           <widget class="QPushButton" name="lookStatIncButton">
            <property name="geometry">
             <rect>
              <x>10</x>
              <y>90</y>
              <width>201</width>
              <height>31</height>
             </rect>
            </property>
            <property name="text">
             <string>Посмотреть статистику доходов</string>
            </property>
           </widget>
           <widget class="QStackedWidget" name="stackedIncomes">
            <property name="geometry">
             <rect>
              <x>240</x>
              <y>10</y>
              <width>491</width>
              <height>411</height>
             </rect>
            </property>
            <property name="currentIndex">
             <number>0</number>
            </property>
            <widget class="QWidget" name="mainIncomes">
             <widget class="QLabel" name="label_15">
              <property name="geometry">
               <rect>
                <x>150</x>
                <y>40</y>
                <width>200</width>
                <height>31</height>
               </rect>
              </property>
              <property name="text">
               <string/>
              </property>
             </widget>
            </widget>
            <widget class="QWidget" name="regularIncomes">
             <widget class="QLineEdit" name="regIncEdit">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>40</y>
                <width>221</width>
                <height>31</height>
               </rect>
              </property>
             </widget>
             <widget class="QLabel" name="label">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>10</y>
                <width>131</width>
                <height>16</height>
               </rect>
              </property>
              <property name="text">
               <string>Введите сумму:</string>
              </property>
             </widget>
             <widget class="QLabel" name="label_2">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>90</y>
                <width>151</width>
                <height>16</height>
               </rect>
              </property>
              <property name="text">
               <string>Выберите регулярность:</string>
              </property>
             </widget>
             <widget class="QComboBox" name="regularInc">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>120</y>
                <width>221</width>
                <height>31</height>
               </rect>
              </property>
             </widget>
             <widget class="QComboBox" name="typeRegInc">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>200</y>
                <width>221</width>
                <height>31</height>
               </rect>
              </property>
             </widget>
             <widget class="QLabel" name="label_3">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>170</y>
                <width>151</width>
                <height>16</height>
               </rect>
              </property>
              <property name="text">
               <string>Выберите тип дохода:</string>
              </property>
             </widget>
             <widget class="QPushButton" name="addRegIncButton">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>250</y>
                <width>111</width>
                <height>31</height>
               </rect>
              </property>
              <property name="text">
               <string>Добавить</string>
              </property>
             </widget>
             <widget class="QLabel" name="label_17">
              <property name="geometry">
               <rect>
                <x>240</x>
                <y>10</y>
                <width>181</width>
                <height>16</height>
               </rect>
              </property>
              <property name="text">
               <string>Список регулярных доходов:</string>
              </property>
             </widget>
             <widget class="QListWidget" name="listRegInc">
              <property name="geometry">
               <rect>
                <x>240</x>
                <y>30</y>
                <width>241</width>
                <height>341</height>
               </rect>
              </property>
             </widget>
             <widget class="QPushButton" name="deleteIncButton">
              <property name="geometry">
               <rect>
                <x>318</x>
                <y>370</y>
                <width>91</width>
                <height>31</height>
               </rect>
              </property>
              <property name="text">
               <string>Удалить</string>
              </property>
             </widget>
            </widget>
            <widget class="QWidget" name="oneInccomes">
             <widget class="QLineEdit" name="incEdit">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>40</y>
                <width>221</width>
                <height>31</height>
               </rect>
              </property>
             </widget>
             <widget class="QComboBox" name="typeInc">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>120</y>
                <width>221</width>
                <height>31</height>
               </rect>
              </property>
             </widget>
             <widget class="QLabel" name="label_4">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>10</y>
                <width>111</width>
                <height>16</height>
               </rect>
              </property>
              <property name="text">
               <string>Введите сумму:</string>
              </property>
             </widget>
             <widget class="QLabel" name="label_5">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>90</y>
                <width>151</width>
                <height>16</height>
               </rect>
              </property>
              <property name="text">
               <string>Выберите тип дохода:</string>
              </property>
             </widget>
             <widget class="QPushButton" name="AddOneIncButton">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>170</y>
                <width>111</width>
                <height>31</height>
               </rect>
              </property>
              <property name="text">
               <string>Добавить</string>
              </property>
             </widget>
            </widget>
            <widget class="QWidget" name="statIncomes">
             <widget class="QLabel" name="statIncImg">
              <property name="geometry">
               <rect>
                <x>50</x>
                <y>20</y>
                <width>401</width>
                <height>321</height>
               </rect>
              </property>
              <property name="text">
               <string>TextLabel</string>
              </property>
             </widget>
            </widget>
           </widget>
          </widget>
          <widget class="QWidget" name="page_expenses">
           <property name="geometry">
            <rect>
             <x>0</x>
             <y>0</y>
             <width>743</width>
             <height>408</height>
            </rect>
           </property>
           <attribute name="label">
            <string>Расходы</string>
           </attribute>
           <widget class="QPushButton" name="RegExButton">
            <property name="geometry">
             <rect>
              <x>10</x>
              <y>10</y>
              <width>201</width>
              <height>31</height>
             </rect>
            </property>
            <property name="text">
             <string>Добавить регулярный расход</string>
            </property>
           </widget>
           <widget class="QPushButton" name="OneExButton">
            <property name="geometry">
             <rect>
              <x>10</x>
              <y>50</y>
              <width>201</width>
              <height>31</height>
             </rect>
            </property>
            <property name="text">
             <string>Добавить единоразовый расход</string>
            </property>
           </widget>
           <widget class="QPushButton" name="lookStatExButton">
            <property name="geometry">
             <rect>
              <x>10</x>
              <y>90</y>
              <width>201</width>
              <height>31</height>
             </rect>
            </property>
            <property name="text">
             <string>Посмотреть статистику расходов</string>
            </property>
           </widget>
           <widget class="QStackedWidget" name="stackedExpenses">
            <property name="geometry">
             <rect>
              <x>240</x>
              <y>10</y>
              <width>491</width>
              <height>411</height>
             </rect>
            </property>
            <property name="currentIndex">
             <number>0</number>
            </property>
            <widget class="QWidget" name="mainEx">
             <widget class="QLabel" name="label_6">
              <property name="geometry">
               <rect>
                <x>130</x>
                <y>40</y>
                <width>200</width>
                <height>31</height>
               </rect>
              </property>
              <property name="text">
               <string/>
              </property>
             </widget>
            </widget>
            <widget class="QWidget" name="regularEx">
             <widget class="QLabel" name="label_7">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>10</y>
                <width>131</width>
                <height>16</height>
               </rect>
              </property>
              <property name="text">
               <string>Введите сумму:</string>
              </property>
             </widget>
             <widget class="QLabel" name="label_8">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>90</y>
                <width>161</width>
                <height>16</height>
               </rect>
              </property>
              <property name="text">
               <string>Выберите регулярность:</string>
              </property>
             </widget>
             <widget class="QLabel" name="label_9">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>170</y>
                <width>171</width>
                <height>16</height>
               </rect>
              </property>
              <property name="text">
               <string>Выберите тип расхода:</string>
              </property>
             </widget>
             <widget class="QComboBox" name="regEx">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>120</y>
                <width>221</width>
                <height>31</height>
               </rect>
              </property>
             </widget>
             <widget class="QComboBox" name="typeRegEx">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>200</y>
                <width>221</width>
                <height>31</height>
               </rect>
              </property>
             </widget>
             <widget class="QLineEdit" name="regExEdit">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>40</y>
                <width>221</width>
                <height>31</height>
               </rect>
              </property>
             </widget>
             <widget class="QPushButton" name="AddRegExButton">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>250</y>
                <width>111</width>
                <height>31</height>
               </rect>
              </property>
              <property name="text">
               <string>Добавить</string>
              </property>
             </widget>
             <widget class="QListWidget" name="listRegEx">
              <property name="geometry">
               <rect>
                <x>240</x>
                <y>30</y>
                <width>241</width>
                <height>341</height>
               </rect>
              </property>
             </widget>
             <widget class="QLabel" name="label_16">
              <property name="geometry">
               <rect>
                <x>240</x>
                <y>10</y>
                <width>181</width>
                <height>16</height>
               </rect>
              </property>
              <property name="text">
               <string>Список регулярных расходов:</string>
              </property>
             </widget>
             <widget class="QPushButton" name="deleteExButton">
              <property name="geometry">
               <rect>
                <x>318</x>
                <y>370</y>
                <width>91</width>
                <height>31</height>
               </rect>
              </property>
              <property name="text">
               <string>Удалить</string>
              </property>
             </widget>
            </widget>
            <widget class="QWidget" name="oneEx">
             <widget class="QPushButton" name="addOneExButton">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>170</y>
                <width>111</width>
                <height>31</height>
               </rect>
              </property>
              <property name="text">
               <string>Добавить</string>
              </property>
             </widget>
             <widget class="QComboBox" name="typeEx">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>120</y>
                <width>221</width>
                <height>31</height>
               </rect>
              </property>
             </widget>
             <widget class="QLineEdit" name="ExEdit">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>40</y>
                <width>221</width>
                <height>31</height>
               </rect>
              </property>
             </widget>
             <widget class="QLabel" name="label_13">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>10</y>
                <width>171</width>
                <height>16</height>
               </rect>
              </property>
              <property name="text">
               <string>Введите сумму:</string>
              </property>
             </widget>
             <widget class="QLabel" name="label_14">
              <property name="geometry">
               <rect>
                <x>10</x>
                <y>90</y>
                <width>151</width>
                <height>16</height>
               </rect>
              </property>
              <property name="text">
               <string>Выберите тип расхода:</string>
              </property>
             </widget>
            </widget>
            <widget class="QWidget" name="statEx">
             <widget class="QLabel" name="statExImg">
              <property name="geometry">
               <rect>
                <x>50</x>
                <y>20</y>
                <width>401</width>
                <height>321</height>
               </rect>
              </property>
              <property name="text">
               <string>TextLabel</string>
              </property>
             </widget>
            </widget>
           </widget>
          </widget>
          <widget class="QWidget" name="page_balace">
           <attribute name="label">
            <string>Кошелёк</string>
           </attribute>
           <widget class="QLabel" name="label_18">
            <property name="geometry">
             <rect>
              <x>20</x>
              <y>10</y>
              <width>191</width>
              <height>21</height>
             </rect>
            </property>
            <property name="text">
             <string>Сумма доходов за этот месяц:</string>
            </property>
           </widget>
           <widget class="QLabel" name="label_19">
            <property name="geometry">
             <rect>
              <x>20</x>
              <y>90</y>
              <width>211</width>
              <height>21</height>
             </rect>
            </property>
            <property name="text">
             <string>Сумма расходов за этот месяц:</string>
            </property>
           </widget>
           <widget class="QLabel" name="label_20">
            <property name="geometry">
             <rect>
              <x>20</x>
              <y>170</y>
              <width>231</width>
              <height>21</height>
             </rect>
            </property>
            <property name="text">
             <string>Нынешний баланс:</string>
            </property>
           </widget>
           <widget class="QLineEdit" name="summInc">
            <property name="geometry">
             <rect>
              <x>20</x>
              <y>40</y>
              <width>231</width>
              <height>31</height>
             </rect>
            </property>
           </widget>
           <widget class="QLineEdit" name="summEx">
            <property name="geometry">
             <rect>
              <x>20</x>
              <y>120</y>
              <width>231</width>
              <height>31</height>
             </rect>
            </property>
           </widget>
           <widget class="QLineEdit" name="balance">
            <property name="geometry">
             <rect>
              <x>20</x>
              <y>200</y>
              <width>231</width>
              <height>31</height>
             </rect>
            </property>
           </widget>
           <widget class="QLabel" name="label_26">
            <property name="geometry">
             <rect>
              <x>290</x>
              <y>30</y>
              <width>421</width>
              <height>351</height>
             </rect>
            </property>
            <property name="text">
             <string>TextLabel</string>
            </property>
           </widget>
          </widget>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="spendTab">
       <attribute name="title">
        <string>Категории трат</string>
       </attribute>
       <widget class="QListWidget" name="spendList">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>10</y>
          <width>261</width>
          <height>391</height>
         </rect>
        </property>
       </widget>
       <widget class="QLabel" name="catSpend">
        <property name="geometry">
         <rect>
          <x>340</x>
          <y>50</y>
          <width>391</width>
          <height>321</height>
         </rect>
        </property>
        <property name="text">
         <string>TextLabel</string>
        </property>
       </widget>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>785</width>
     <height>33</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Grafic:  # класс, создающий круговую диаграмму
    def __init__(self, kwargs, name, titl):
        self.title = titl  # заголовок диаграммы
        self.name = name  # название файла
        self.labels = kwargs.keys()  # части диаграммы
        self.sizes = kwargs.values()  # значения диаграммы

    def make(self):  # создание диаграммы и ее сохранение
        _, self.ax1 = plt.subplots()
        self.ax1.pie(self.sizes, labels=self.labels, autopct='%1.1f%%', startangle=120, pctdistance=0.7,
                     labeldistance=1.1)
        plt.title(self.title)
        plt.savefig(self.name)

class DatabaseManager:
    def __init__(self, db_name='finances_db.sqlite'):
        self.db_name = db_name
        self.required_tables = {  # нужные таблицы в БД
            'reg_inc': [
                ('id', 'INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL'),
                ('type', 'TEXT NOT NULL'),
                ('summ', 'INTEGER NOT NULL'),
                ('regular', 'TEXT NOT NULL')
            ],
            'one_inc': [
                ('id', 'INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL'),
                ('type', 'TEXT NOT NULL'),
                ('summ', 'INTEGER NOT NULL')
            ],
            'reg_ex': [
                ('id', 'INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL'),
                ('type', 'TEXT NOT NULL'),
                ('summ', 'INTEGER NOT NULL'),
                ('regular', 'TEXT NOT NULL')
            ],
            'one_ex': [
                ('id', 'INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL'),
                ('type', 'TEXT NOT NULL'),
                ('summ', 'INTEGER NOT NULL')
            ],
            'balance': [
                ('id', 'INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL'),
                ('type', 'TEXT NOT NULL'),
                ('summ', 'INTEGER NOT NULL')
            ]
        }

    def initialize_database(self, parent=None):
        if self._is_database_valid():  # если найдена подходящая база
            answer = QMessageBox.question(
                parent,
                'Найдена БД',
                'Найдена подходящая база данных, хотите загрузить?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.Yes
            )  # вопрос, загружать ли ее

            if answer == QMessageBox.StandardButton.No:  # если нет, то создание новой
                self._create_new_database()
        else:  # если не найдена, создание новой
            self._create_new_database()

        conn = sqlite3.connect(self.db_name)
        return conn

    def _is_database_valid(self):  # подходит ли база данных
        if not os.path.exists(self.db_name):  # если нет подходящей БД
            return False
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # иначе:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        existing_tables = {row[0] for row in cursor.fetchall()}  # считывание находящихся таблиц

        required_tables_set = set(self.required_tables.keys())
        if not required_tables_set.issubset(existing_tables):
            conn.close()
            return False

        for table_name, required_columns in self.required_tables.items():  # подходят ли столбцы в таблицах
            cursor.execute(f"PRAGMA table_info({table_name})")
            existing_columns = {row[1] for row in cursor.fetchall()}

            required_columns_names = {col[0] for col in required_columns}
            if not required_columns_names.issubset(existing_columns):
                conn.close()
                return False

        conn.close()
        return True

    def _create_new_database(self):  # создание новой БД
        if os.path.exists(self.db_name):  # если есть, то удаляем
            os.remove(self.db_name)

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # создание нужных таблиц
        cursor.execute('''
            CREATE TABLE reg_inc (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                type TEXT NOT NULL,
                summ INTEGER NOT NULL,
                regular TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE one_inc (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                type TEXT NOT NULL,
                summ INTEGER NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE reg_ex (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                type TEXT NOT NULL,
                summ INTEGER NOT NULL,
                regular TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE one_ex (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                type TEXT NOT NULL,
                summ INTEGER NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE balance (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                type TEXT NOT NULL,
                summ INTEGER NOT NULL
            )
        ''')

        conn.commit()
        conn.close()




class FinancialAnalyst(QMainWindow):  # создание самого приложения
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.db_manager = DatabaseManager()
        self.con = self.db_manager.initialize_database(self) # соединение с базой данных

        self.label_25.setPixmap(QPixmap('catwithcash.jpeg'))  # картинка
        self.label_25.setScaledContents(True)
        self.rec = [
            '<h3>Распродажа!</h3><p>Только в эту секунду все товары в магазине <b>Смешные ценники</b> за 1 рубль!.. '
            'Уже всё.</p>',
            '<h3>Кэшбек!</h3><p>Только в этом месяце возвращаем 0,0001% от покупки домашней пыли!</p>',
            '<h3>Акция!</h3><p>При покупке третьего телефона от 100.000 рублей возвращаем 10 рублей!</p>',
            '<h3>Распродажа!</h3><p>Я не придумала, извините.</p>',
            '<h3>Акция!</h3><p>Если вы сможете рассмешить нашего охранника, вы получите скидку 55%!<br><small>P.S. '
            'наш охранник не улыбался уже 55 лет.</small></p>',
            '<h3>Кэшбек!</h3><p>Если наш волшебник предскажет, что ваш товар сломается в течение 24 часов, вам вернут '
            '100% стоимости товара!</p>',
            '<h3>Кэшбек наоборот!</h3><p>Вы доплачиваете нам сверху 30% от стоимости товара!</p>',
            '<h3>Акция!</h3><p>Если вы скажете искренний комплимент нашему кассиру, есть шанс, что он даст вам скидку!'
            '<br><small>P.S. зависит от настроения кассира</small></p>',
            '<h3>Акция!</h3><p>Если вы сможете вынести товар из магазина и скрыться незамеченным, то он достается вам '
            'бесплатно!<br><small>P.S. за возможные последствия ответственности не несём</small></p>',
            '<h3>Распродажа!</h3><p>Только сегодня всё по цене крыла от самолёта! Успейте купить.</p>'
        ]  # текста "рекламы"

        self.rec_1.setHtml(choice(self.rec))  # случайные выборы отображаемой "рекламы"
        self.rec_2.setHtml(choice(self.rec))
        self.rec_3.setHtml(choice(self.rec))
        self.rec_4.setHtml(choice(self.rec))

        self.incomeButton.clicked.connect(self.go_to_incomes)  # кнопка на главной странице, переносящая на доходы
        self.expensesButton.clicked.connect(self.go_to_expenses)  # кнопка на главной странице, переносящая на расходы
        self.balanceButton.clicked.connect(self.go_to_balance)  # кнопка на главной странице, переносящая на баланс
        self.spendingButton.clicked.connect(
            self.go_to_spend)  # кнопка на главной странице, переносящая на категории трат
        self.RegIncButton.clicked.connect(self.reg_inc)  # кнопка регулярных доходов
        self.OneIncButton.clicked.connect(self.one_inc)  # кнопка единоразовых доходов
        self.lookStatIncButton.clicked.connect(self.stat_inc)  # кнопка статистики доходов
        self.RegExButton.clicked.connect(self.reg_ex)  # кнопка регулярных расходов
        self.OneExButton.clicked.connect(self.one_ex)  # кнопка единоразовых расходов
        self.lookStatExButton.clicked.connect(self.stat_ex)  # кнопка статистики расходов

        self.label_6.setText('<---\nВыберите раздел')  # вывод подсказки
        self.label_15.setText('<---\nВыберите раздел')  # вывод подсказки
        self.summInc.setReadOnly(True)  # только для чтения
        self.summEx.setReadOnly(True)  # только для чтения
        self.balance.setReadOnly(True)  # только для чтения

        self.incomes = 0  # сумма доходов
        self.expenses = 0  # сумма расходов
        self.summBalance = 0  # суммарный баланс
        self.data = {}
        self.spends = set()  # категории трат

        cur = self.con.cursor()
        query = 'SELECT type, summ, regular FROM reg_inc'  # считывание и сохранение уже существующих данных из БД
        res = cur.execute(query).fetchall()
        for row in res:
            self.listRegInc.addItem(f'{row[0]} | {row[1]} | {row[2]}')
            self.data[row[0]] = 0

        for row in res:
            if row[2] == 'Каждый день':
                self.data[row[0]] += int(row[1]) * 30
                self.incomes += int(row[1]) * 30
                self.summBalance += int(row[1]) * 30
            elif row[2] == 'Каждую неделю':
                self.data[row[0]] += int(row[1]) * 5
                self.incomes += int(row[1]) * 5
                self.summBalance += int(row[1]) * 5
            else:
                self.data[row[0]] += int(row[1])
                self.incomes += int(row[1])
                self.summBalance += int(row[1])

        query = 'SELECT type, summ FROM one_inc'
        res = cur.execute(query).fetchall()
        for row in res:
            if row[0] not in self.data:
                self.data[row[0]] = 0
            self.data[row[0]] += int(row[1])
            self.incomes += int(row[1])
            self.summBalance += int(row[1])

        Grafic(self.data, 'graf_inc', 'Статистика доходов').make()  # вывод на график
        self.statIncImg.setPixmap(QPixmap('graf_inc.png'))

        query = 'SELECT type, summ, regular FROM reg_ex'
        res = cur.execute(query).fetchall()
        self.data = {}
        for row in res:
            self.listRegEx.addItem(f'{row[0]} | {row[1]} | {row[2]}')
            self.data[row[0]] = 0

        for row in res:
            if row[2] == 'Каждый день':
                self.data[row[0]] += int(row[1]) * 30
                self.expenses += int(row[1]) * 30
                self.summBalance -= int(row[1]) * 30
            elif row[2] == 'Каждую неделю':
                self.data[row[0]] += int(row[1]) * 5
                self.expenses += int(row[1]) * 5
                self.summBalance -= int(row[1]) * 5
            else:
                self.data[row[0]] += int(row[1])
                self.expenses += int(row[1])
                self.summBalance -= int(row[1])

        query = 'SELECT type, summ FROM one_ex'
        res = cur.execute(query).fetchall()
        for row in res:
            if row[0] not in self.data:
                self.data[row[0]] = 0
            self.data[row[0]] += int(row[1])
            self.expenses += int(row[1])
            self.summBalance -= int(row[1])

        Grafic(self.data, 'graf_ex', 'Статистика расходов').make()  # вывод на график
        self.statExImg.setPixmap(QPixmap('graf_ex.png'))

        self.summInc.setText(str(self.incomes))  # вывод суммы доходов
        self.summEx.setText(str(self.expenses))  # вывод суммы расходов
        self.balance.setText(str(self.summBalance))  # вывод суммарного баланса

        self.statIncImg.setScaledContents(True)
        self.statExImg.setScaledContents(True)
        self.label_26.setScaledContents(True)
        self.catSpend.setScaledContents(True)

        self.tabWidget.currentChanged.connect(self.on_tab_changed)  # при изменении текущей страницы
        self.toolBox.currentChanged.connect(self.on_toolbox_changed)  # при изменении текущей страницы
        self.stackedIncomes.currentChanged.connect(self.on_stackInc_changed)  # при изменении текущей страницы
        self.stackedExpenses.currentChanged.connect(self.on_stackEx_changed)  # при изменении текущей страницы

        self.params = ['Каждый день', 'Каждую неделю', 'Каждый месяц']
        self.regularInc.addItems(self.params)  # добавление вариантов выбора
        self.regEx.addItems(self.params)  # добавление вариантов выбора

        self.params = ['Заработная плата', 'Рента', 'Карманные деньги', 'Социальные выплаты', 'Другое']
        self.typeRegInc.addItems(self.params)  # добавление вариантов выбора

        self.params = ['Премия', 'Продажа личного имущества', 'Другое']
        self.typeInc.addItems(self.params)  # добавление вариантов выбора

        self.params = ['Коммунальные услуги', 'Оплата обучения', 'Ипотека', 'Связь', 'Другое']
        self.typeRegEx.addItems(self.params)  # добавление вариантов выбора

        self.params = ['Продукты', 'Услуги', 'Развлечения', 'Товары для дома', 'Транспорт', 'Другое']
        self.typeEx.addItems(self.params)  # добавление вариантов выбора

        self.addRegIncButton.clicked.connect(self.add)  # кнопка добавления
        self.AddOneIncButton.clicked.connect(self.add)  # кнопка добавления
        self.AddRegExButton.clicked.connect(self.add)  # кнопка добавления
        self.addOneExButton.clicked.connect(self.add)  # кнопка добавления
        self.deleteIncButton.clicked.connect(self.delete)  # кнопка удаления
        self.deleteExButton.clicked.connect(self.delete)  # кнопка удаления

    def closeEvent(self, event): # Закрытие соединения с базой при выходе
        if hasattr(self, 'con'):
            self.con.close()
        event.accept()

    def delete(self):  # удаление элементов
        answer = QMessageBox.question(self, 'Удаление', f'Действительно удалить этот элемент?',
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                      QMessageBox.StandardButton.Yes)  # высвечивание вопроса

        if self.sender() == self.deleteIncButton:  # удаление регулярных доходов
            type, summ, reg = self.listRegInc.currentItem().text().split(' | ')  # считывание выбранного дохода

            if answer == QMessageBox.StandardButton.Yes:  # если ответ да, то удаляем
                cur = self.con.cursor()
                if reg == 'Каждый день':
                    self.incomes -= int(summ) * 30
                    self.summBalance -= int(summ) * 30
                elif reg == 'Каждую неделю':
                    self.incomes -= int(summ) * 5
                    self.summBalance -= int(summ) * 5
                else:
                    self.incomes -= int(summ)
                    self.summBalance -= int(summ)

                query = f"DELETE FROM reg_inc WHERE id = (SELECT id WHERE type = '{type}' AND summ = {summ} AND regular = '{reg}' LIMIT 1);"
                cur.execute(query)
                self.con.commit()
                self.listRegInc.takeItem(self.listRegInc.currentRow())  # удаление из списка

        elif self.sender() == self.deleteExButton:  # удаление регулярных расходов
            type, summ, reg = self.listRegEx.currentItem().text().split(' | ')  # считывание выбранного столбца

            if answer == QMessageBox.StandardButton.Yes:  # если даа, то удаляем
                cur = self.con.cursor()
                if reg == 'Каждый день':
                    self.expenses -= int(summ) * 30
                    self.summBalance += int(summ) * 30
                elif reg == 'Каждую неделю':
                    self.expenses -= int(summ) * 5
                    self.summBalance += int(summ) * 5
                else:
                    self.expenses -= int(summ)
                    self.summBalance += int(summ)

                query = f"DELETE FROM reg_ex WHERE id = (SELECT id WHERE type = '{type}' AND summ = {summ} AND regular = '{reg}' LIMIT 1);"
                cur.execute(query)
                self.con.commit()
                self.listRegEx.takeItem(self.listRegEx.currentRow())  # удаление из списка

    def add(self):  # добавление
        if self.sender() == self.addRegIncButton:  # добавление регулярных доходов
            summ = self.regIncEdit.text()  # считывание суммы
            reg = self.regularInc.currentText()  # считывание регулярности
            type = self.typeRegInc.currentText()  # считывание типа

            try:  # проверка, является ли числом
                if int(summ) > 0:  # проверка, больше ли нуля
                    self.listRegInc.addItem(f'{type} | {summ} | {reg}')
                    query = f"INSERT INTO reg_inc(type, summ, regular) VALUES ('{type}', {summ}, '{reg}')"
                    if reg == 'Каждый день':
                        self.incomes += int(summ) * 30
                        self.summBalance += int(summ) * 30
                    elif reg == 'Каждую неделю':
                        self.incomes += int(summ) * 5
                        self.summBalance += int(summ) * 5
                    else:
                        self.incomes += int(summ)
                        self.summBalance += int(summ)
                    cur = self.con.cursor()
                    cur.execute(query)
                    self.con.commit()

                else:  # если меньше, ты вывод ошибки
                    self.statusBar().showMessage('Ошибка, сумма должна быть больше нуля.', 5000)

            except ValueError:  # если нет, то вывод ошибки
                self.statusBar().showMessage('Ошибка, сумма должна быть числом.', 5000)
            self.regIncEdit.setText('')  # обнуление строки ввода

        elif self.sender() == self.AddOneIncButton:  # добавление единоразового дохода
            summ = self.incEdit.text()  # считывание суммы
            type = self.typeInc.currentText()  # считывание типа

            try:  # проверка, является ли числом
                if int(summ) > 0:  # проверка, больше ли нуля
                    query = f"INSERT INTO one_inc(type, summ) VALUES ('{type}', {summ})"
                    self.incomes += int(summ)
                    self.summBalance += int(summ)
                    cur = self.con.cursor()
                    cur.execute(query)
                    self.con.commit()

                else:  # если меньше, ты вывод ошибки
                    self.statusBar().showMessage('Ошибка, сумма должна быть больше нуля.', 5000)

            except Exception:  # если нет, то вывод ошибки
                self.statusBar().showMessage('Ошибка, сумма должна быть числом.', 5000)
            self.incEdit.setText('')  # обнуление строки ввода

        elif self.sender() == self.AddRegExButton:  # добавление регулярных расходов
            summ = self.regExEdit.text()  # считывание суммы
            reg = self.regEx.currentText()  # считывание регулярности
            type = self.typeRegEx.currentText()  # считывание типа

            try:  # проверка, является ли числом
                if int(summ) > 0:  # проверка, больше ли нуля
                    self.listRegEx.addItem(f'{type} | {summ} | {reg}')
                    query = f"INSERT INTO reg_ex(type, summ, regular) VALUES ('{type}', {summ}, '{reg}')"
                    if reg == 'Каждый день':
                        self.expenses += int(summ) * 30
                        self.summBalance -= int(summ) * 30
                    elif reg == 'Каждую неделю':
                        self.expenses += int(summ) * 5
                        self.summBalance -= int(summ) * 5
                    else:
                        self.expenses += int(summ)
                        self.summBalance -= int(summ)
                    cur = self.con.cursor()
                    cur.execute(query)
                    self.con.commit()
                else:  # если меньше, ты вывод ошибки
                    self.statusBar().showMessage('Ошибка, сумма должна быть больше нуля.', 5000)

            except ValueError:  # если нет, то вывод ошибки
                self.statusBar().showMessage('Ошибка, сумма должна быть числом.', 5000)
            self.regExEdit.setText('')  # обнуление строки ввода

        elif self.sender() == self.addOneExButton:  # добавление единоразового расхода
            summ = self.ExEdit.text()  # считывание суммы
            type = self.typeEx.currentText()  # считывание типа

            try:  # проверка, является ли числом
                if int(summ) > 0:  # проверка, больше ли нуля
                    query = f"INSERT INTO one_ex(type, summ) VALUES ('{type}', {summ})"
                    self.expenses += int(summ)
                    self.summBalance -= int(summ)
                    cur = self.con.cursor()
                    cur.execute(query)
                    self.con.commit()
                else:  # если меньше, ты вывод ошибки
                    self.statusBar().showMessage('Ошибка, сумма должна быть больше нуля.', 5000)

            except ValueError:  # если нет, то вывод ошибки
                self.statusBar().showMessage('Ошибка, сумма должна быть числом.', 5000)
            self.ExEdit.setText('')  # обнуление строки ввода

        self.summInc.setText(f'{self.incomes}')  # обновление доходов
        self.summEx.setText(f'{self.expenses}')  # обновление расходов
        self.balance.setText(f'{self.summBalance}')  # обновление баланса

    def on_stackInc_changed(self, index):
        if index == 3:  # если на 3 странице, то показать граф
            self.show_graf()

    def on_stackEx_changed(self, index):
        if index == 3:  # если на 3 странице, то показать граф
            self.show_graf()

    def on_tab_changed(self, index):
        if index == 1:  # если на 1 странице, то в зависимости от страницы
            self.on_toolbox_changed(self.toolBox.currentIndex())
        elif index == 2:  # если на 2 странице, то считать данные и обновить категории трат
            self.data = {}
            cur = self.con.cursor()
            query = 'SELECT type, summ, regular FROM reg_ex'
            res = cur.execute(query).fetchall()
            for row in res:
                self.data[row[0]] = 0
            for row in res:
                if row[2] == 'Каждый день':
                    self.data[row[0]] += int(row[1]) * 30
                elif row[2] == 'Каждую неделю':
                    self.data[row[0]] += int(row[1]) * 5
                else:
                    self.data[row[0]] += int(row[1])

            query = 'SELECT type, summ FROM one_ex'
            res = cur.execute(query).fetchall()
            for row in res:
                if row[0] not in self.data:
                    self.data[row[0]] = 0
                self.data[row[0]] += int(row[1])

            Grafic(self.data, 'graf_spend', 'Категории трат').make()
            self.catSpend.setPixmap(QPixmap('graf_spend.png'))

            self.spendList.clear()
            for key in self.data.keys():
                self.spends.add(key)
            for key in self.spends:
                self.spendList.addItem(key)

    def on_toolbox_changed(self, index):
        if index == 0:  # если на 0 странице, то показать главную страницу
            self.stackedIncomes.setCurrentIndex(0)
        elif index == 1:  # если на 1 странице, то показать главную страницу
            self.stackedExpenses.setCurrentIndex(0)
        elif index == 2:  # если на 2 странице, то показать граф
            self.show_graf()

    def show_graf(self):  # метод вывода графиков
        self.data = {}
        if self.toolBox.currentIndex() == 0:
            cur = self.con.cursor()
            query = 'SELECT type, summ, regular FROM reg_inc'
            res = cur.execute(query).fetchall()
            for row in res:
                self.data[row[0]] = 0
            for row in res:
                if row[2] == 'Каждый день':
                    self.data[row[0]] += int(row[1]) * 30
                elif row[2] == 'Каждую неделю':
                    self.data[row[0]] += int(row[1]) * 5
                else:
                    self.data[row[0]] += int(row[1])

            query = 'SELECT type, summ FROM one_inc'
            res = cur.execute(query).fetchall()
            for row in res:
                if row[0] not in self.data:
                    self.data[row[0]] = 0
                self.data[row[0]] += int(row[1])

            Grafic(self.data, 'graf_inc', 'Статистика доходов').make()
            self.statIncImg.setPixmap(QPixmap('graf_inc.png'))

        elif self.toolBox.currentIndex() == 1:
            cur = self.con.cursor()
            query = 'SELECT type, summ, regular FROM reg_ex'
            res = cur.execute(query).fetchall()
            for row in res:
                self.data[row[0]] = 0
            for row in res:
                if row[2] == 'Каждый день':
                    self.data[row[0]] += int(row[1]) * 30
                elif row[2] == 'Каждую неделю':
                    self.data[row[0]] += int(row[1]) * 5
                else:
                    self.data[row[0]] += int(row[1])
            query = 'SELECT type, summ FROM one_ex'
            res = cur.execute(query).fetchall()
            for row in res:
                if row[0] not in self.data:
                    self.data[row[0]] = 0
                self.data[row[0]] += int(row[1])

            Grafic(self.data, 'graf_ex', 'Статистика расходов').make()
            self.statExImg.setPixmap(QPixmap('graf_ex.png'))

        elif self.toolBox.currentIndex() == 2:
            if self.incomes == 0 and self.expenses == 0:
                self.data = {}
            else:
                self.data = {'Доходы': self.incomes, 'Расходы': self.expenses}
            Grafic(self.data, 'graf_bal', 'Баланс').make()
            self.label_26.setPixmap(QPixmap('graf_bal.png'))

    def go_to_incomes(self):  # переход к доходам
        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)

    def go_to_expenses(self):  # переход к расходам
        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(1)

    def go_to_balance(self):  # переход к балансу
        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(2)
        self.summInc.setText(str(self.incomes))
        self.summEx.setText(str(self.expenses))
        self.balance.setText(str(self.summBalance))

    def go_to_spend(self):  # переход к категориям трат
        self.tabWidget.setCurrentIndex(2)

    def reg_inc(self):  # переход к регулярным доходам
        self.stackedIncomes.setCurrentIndex(1)

    def one_inc(self):  # переход к единоразовым доходам
        self.stackedIncomes.setCurrentIndex(2)

    def stat_inc(self):  # переход к статистике доходов
        self.stackedIncomes.setCurrentIndex(3)

    def reg_ex(self):  # переход к регулярным расходам
        self.stackedExpenses.setCurrentIndex(1)

    def one_ex(self):  # переход к единоразовым расходам
        self.stackedExpenses.setCurrentIndex(2)

    def stat_ex(self):  # переход к статистике расходов
        self.stackedExpenses.setCurrentIndex(3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FinancialAnalyst()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
