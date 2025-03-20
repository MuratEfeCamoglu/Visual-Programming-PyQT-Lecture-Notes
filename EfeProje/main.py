from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget,
                           QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
                           QPushButton, QTableWidget, QTableWidgetItem, QMessageBox,
                           QComboBox, QDialog, QSpinBox, QHeaderView, QStackedWidget,
                           QFormLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
import sys
from database import Database
import random

class ResultDialog(QDialog):
    def __init__(self, filtered_players, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Filtreleme Sonuçları")
        self.setGeometry(200, 200, 1200, 600)
        
        layout = QVBoxLayout(self)
        
        # Başlık
        title = QLabel("Filtreleme Sonuçları")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Tablo
        self.table = QTableWidget()
        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels([
            "Ad", "Takım", "Pozisyon", "Yaş", "Ülke",
            "Sayı", "Ribaund", "Asist", "Top Çalma", "Blok", "Top Kaybı"
        ])
        
        # Verileri yükle
        self.table.setRowCount(len(filtered_players))
        for i, player in enumerate(filtered_players):
            # ID'yi atlayarak verileri ekle
            for j, value in enumerate(player[1:]):  # ID'yi atlayarak başla
                self.table.setItem(i, j, QTableWidgetItem(str(value)))
        
        self.table.resizeColumnsToContents()
        self.table.setAlternatingRowColors(True)
        layout.addWidget(self.table)
        
        # Kapat butonu
        close_button = QPushButton("Kapat")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

class FilterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Oyuncu Filtrele")
        self.setGeometry(200, 200, 400, 500)
        
        layout = QVBoxLayout(self)
        
        # Takım filtresi
        team_layout = QHBoxLayout()
        team_label = QLabel("Takım:")
        self.team_combo = QComboBox()
        teams = ["Hepsi", "Los Angeles Lakers", "Golden State Warriors", "Milwaukee Bucks", 
                "Phoenix Suns", "Houston Rockets", "Dallas Mavericks", "Denver Nuggets",
                "Philadelphia 76ers", "Boston Celtics", "Oklahoma City Thunder", 
                "Cleveland Cavaliers", "Detroit Pistons", "Minnesota Timberwolves",
                "San Antonio Spurs", "New York Knicks", "Orlando Magic", "Sacramento Kings",
                "Utah Jazz", "Memphis Grizzlies", "Atlanta Hawks", "Brooklyn Nets"]
        self.team_combo.addItems(teams)
        team_layout.addWidget(team_label)
        team_layout.addWidget(self.team_combo)
        
        # Pozisyon filtresi
        position_layout = QHBoxLayout()
        position_label = QLabel("Pozisyon:")
        self.position_combo = QComboBox()
        positions = ["Hepsi", "Guard", "Forward", "Center"]
        self.position_combo.addItems(positions)
        position_layout.addWidget(position_label)
        position_layout.addWidget(self.position_combo)
        
        # Ülke filtresi
        country_layout = QHBoxLayout()
        country_label = QLabel("Ülke:")
        self.country_combo = QComboBox()
        countries = ["Hepsi", "ABD", "Türkiye", "Yunanistan", "Slovenya", "Sırbistan",
                    "Kamerun", "Kanada", "Fransa", "Letonya", "Almanya", "Litvanya", "Finlandiya"]
        self.country_combo.addItems(countries)
        country_layout.addWidget(country_label)
        country_layout.addWidget(self.country_combo)
        
        # İstatistik filtreleri
        stats_group = QWidget()
        stats_layout = QFormLayout(stats_group)
        
        self.min_points = QSpinBox()
        self.min_rebounds = QSpinBox()
        self.min_assists = QSpinBox()
        self.min_steals = QSpinBox()
        self.min_blocks = QSpinBox()
        self.min_turnovers = QSpinBox()
        
        stats_layout.addRow("Min. Sayı:", self.min_points)
        stats_layout.addRow("Min. Ribaund:", self.min_rebounds)
        stats_layout.addRow("Min. Asist:", self.min_assists)
        stats_layout.addRow("Min. Top Çalma:", self.min_steals)
        stats_layout.addRow("Min. Blok:", self.min_blocks)
        stats_layout.addRow("Min. Top Kaybı:", self.min_turnovers)
        
        # Butonlar
        buttons = QHBoxLayout()
        apply_btn = QPushButton("Uygula")
        apply_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("İptal")
        cancel_btn.clicked.connect(self.reject)
        buttons.addWidget(apply_btn)
        buttons.addWidget(cancel_btn)
        
        # Ana layout'a ekle
        layout.addLayout(team_layout)
        layout.addLayout(position_layout)
        layout.addLayout(country_layout)
        layout.addWidget(stats_group)
        layout.addLayout(buttons)

class CompareDialog(QDialog):
    def __init__(self, player1, player2, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Oyuncu Karşılaştırma")
        self.setGeometry(200, 200, 800, 500)
        
        layout = QVBoxLayout(self)
        
        # Başlık
        title = QLabel(f"{player1[1]} vs {player2[1]}")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Karşılaştırma tablosu
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["İstatistik", player1[1], player2[1]])
        
        # İstatistik başlıkları
        stats = ["Takım", "Pozisyon", "Yaş", "Ülke", "Sayı", "Ribaund", 
                "Asist", "Top Çalma", "Blok", "Top Kaybı"]
        
        self.table.setRowCount(len(stats))
        
        # Verileri doldur
        for i, stat in enumerate(stats):
            # İstatistik adı
            self.table.setItem(i, 0, QTableWidgetItem(stat))
            # Player 1 değeri
            self.table.setItem(i, 1, QTableWidgetItem(str(player1[i+2])))  # +2 çünkü id ve name'i atlıyoruz
            # Player 2 değeri
            self.table.setItem(i, 2, QTableWidgetItem(str(player2[i+2])))
            
            # Sayısal değerleri karşılaştır ve renklendir
            if i >= 4:  # Sayısal istatistikler
                val1 = float(player1[i+2])
                val2 = float(player2[i+2])
                if val1 > val2:
                    self.table.item(i, 1).setBackground(Qt.green)
                elif val2 > val1:
                    self.table.item(i, 2).setBackground(Qt.green)
        
        self.table.resizeColumnsToContents()
        self.table.setAlternatingRowColors(True)
        layout.addWidget(self.table)
        
        # Kapat butonu
        close_button = QPushButton("Kapat")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

class FavoritesDialog(QDialog):
    def __init__(self, favorite_players, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Favori Oyuncular")
        self.setGeometry(200, 200, 1200, 600)
        
        layout = QVBoxLayout(self)
        
        # Başlık
        title = QLabel("Favori Oyuncular")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Tablo
        self.table = QTableWidget()
        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels([
            "Ad", "Takım", "Pozisyon", "Yaş", "Ülke",
            "Sayı", "Ribaund", "Asist", "Top Çalma", "Blok", "Top Kaybı"
        ])
        
        # Verileri yükle
        self.table.setRowCount(len(favorite_players))
        for i, player in enumerate(favorite_players):
            for j, value in enumerate(player):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))
        
        self.table.resizeColumnsToContents()
        self.table.setAlternatingRowColors(True)
        layout.addWidget(self.table)
        
        # Kapat butonu
        close_button = QPushButton("Kapat")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

class BasketballApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Efe'nin NBA Uygulaması")
        self.setGeometry(100, 100, 1200, 800)
        
        # Kullanıcı ve favori bilgileri
        self.current_user = None
        self.favorite_players = []
        
        # Veritabanı bağlantısı
        self.db = Database()
        
        # Ana widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        
        # Stack widget kullanarak ekranlar arası geçiş
        self.stack = QStackedWidget()
        
        # Login ekranını oluştur
        self.create_login_screen()
        
        # Ana ekranı oluştur
        self.create_main_screen()
        
        # Stack'e ekranları ekle
        self.stack.addWidget(self.login_screen)
        self.stack.addWidget(self.main_screen)
        
        # Layout'a stack'i ekle
        self.layout.addWidget(self.stack)
        
        # Dark tema uygula
        self.apply_dark_theme()

    def create_login_screen(self):
        # Login ekranını oluştur
        self.login_screen = QWidget()
        layout = QVBoxLayout(self.login_screen)
        
        title = QLabel("NBA Oyuncu Veritabanı")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        form = QFormLayout()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        
        form.addRow("Kullanıcı Adı:", self.username)
        form.addRow("Şifre:", self.password)
        
        login_btn = QPushButton("Giriş")
        login_btn.clicked.connect(self.check_login)
        
        layout.addLayout(form)
        layout.addWidget(login_btn)
        layout.setAlignment(Qt.AlignCenter)

    def create_main_screen(self):
        # Ana ekranı oluştur
        self.main_screen = QWidget()
        layout = QVBoxLayout(self.main_screen)
        
        # Üst butonlar
        btn_layout = QHBoxLayout()
        
        filter_btn = QPushButton("Filtrele")
        filter_btn.clicked.connect(self.show_filter)
        btn_layout.addWidget(filter_btn)
        
        fav_btn = QPushButton("Favoriler")
        fav_btn.clicked.connect(self.show_favorites)
        btn_layout.addWidget(fav_btn)
        
        compare_btn = QPushButton("Karşılaştır")
        compare_btn.clicked.connect(self.compare_players)
        btn_layout.addWidget(compare_btn)
        
        # Çıkış butonu
        logout_btn = QPushButton("Çıkış")
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff3333;
                color: white;
            }
            QPushButton:hover {
                background-color: #cc0000;
            }
        """)
        logout_btn.clicked.connect(self.logout)
        btn_layout.addWidget(logout_btn)
        
        layout.addLayout(btn_layout)
        
        # Oyuncu tablosu
        self.table = QTableWidget()
        self.table.setSelectionMode(QTableWidget.MultiSelection)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.setup_table()
        layout.addWidget(self.table)

    def setup_table(self):
        headers = ["Favori", "Ad", "Takım", "Pozisyon", "Yaş", "Ülke",
                  "Sayı", "Ribaund", "Asist", "Top Çalma", "Blok", "Top Kaybı"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.load_players()

    def load_players(self):
        try:
            # Veritabanından oyuncuları al
            players = self.db.get_all_players()
            if not players:
                print("Oyuncu verisi bulunamadı!")
                return
                
            # Favori listesini al
            favorites = self.db.get_favorites(self.current_user) if self.current_user else []
            
            # Tabloyu doldur
            self.table.setRowCount(len(players))
            for i, player in enumerate(players):
                # Favori butonu
                fav_btn = QPushButton("☆")
                fav_btn.setStyleSheet("background: transparent; color: gold; font-size: 20px;")
                
                # Eğer oyuncu favorilerdeyse yıldızı dolu göster
                if player[1] in [f[0] for f in favorites]:  # İsim kontrolü
                    fav_btn.setText("★")
                
                fav_btn.clicked.connect(lambda checked, p=player, b=fav_btn: self.toggle_favorite(p, b))
                self.table.setCellWidget(i, 0, fav_btn)
                
                # Oyuncu verilerini ekle (id hariç)
                for j, value in enumerate(player[1:]):  # id'yi atlayarak başla
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(i, j+1, item)
            
            self.table.resizeColumnsToContents()
            
        except Exception as e:
            print("Veri yükleme hatası:", e)
            QMessageBox.warning(self, "Hata", "Oyuncular yüklenirken bir hata oluştu!")

    def check_login(self):
        username = self.username.text().lower()
        if username == "efe" and self.password.text() == "0909":
            self.current_user = username
            self.favorite_players = self.db.get_favorites(self.current_user)
            self.stack.setCurrentIndex(1)  # Ana ekrana geç
            self.load_players()  # Oyuncuları yükle
            QMessageBox.information(self, "Başarılı", "Hoş geldin Efe!")
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre hatalı!")

    def show_filter(self):
        dialog = FilterDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            try:
                # Veritabanından tüm oyuncuları al
                filtered_players = self.db.get_all_players()
                
                # Temel filtreleme
                if dialog.team_combo.currentText() != "Hepsi":
                    filtered_players = [p for p in filtered_players if p[2] == dialog.team_combo.currentText()]
                if dialog.position_combo.currentText() != "Hepsi":
                    filtered_players = [p for p in filtered_players if p[3] == dialog.position_combo.currentText()]
                if dialog.country_combo.currentText() != "Hepsi":
                    filtered_players = [p for p in filtered_players if p[5] == dialog.country_combo.currentText()]
                
                # İstatistik filtreleme
                filtered_players = [p for p in filtered_players if 
                                  float(p[6]) >= dialog.min_points.value() and
                                  float(p[7]) >= dialog.min_rebounds.value() and
                                  float(p[8]) >= dialog.min_assists.value() and
                                  float(p[9]) >= dialog.min_steals.value() and
                                  float(p[10]) >= dialog.min_blocks.value() and
                                  float(p[11]) >= dialog.min_turnovers.value()]
                
                # Sonuçları göster
                if filtered_players:
                    result_dialog = ResultDialog(filtered_players, self)
                    result_dialog.exec_()
                else:
                    QMessageBox.information(self, "Bilgi", "Filtreleme kriterlerine uygun oyuncu bulunamadı!")
                    
            except Exception as e:
                print("Filtreleme hatası:", e)
                QMessageBox.warning(self, "Hata", "Filtreleme işlemi sırasında bir hata oluştu!")

    def show_favorites(self):
        if not self.favorite_players:
            QMessageBox.information(self, "Bilgi", "Henüz favori oyuncu eklenmemiş!")
            return
        
        dialog = FavoritesDialog(self.favorite_players, self)
        dialog.exec_()

    def compare_players(self):
        self.compare_selected_players()

    def compare_selected_players(self):
        try:
            selected_rows = set()
            for item in self.table.selectedItems():
                selected_rows.add(item.row())
            
            if len(selected_rows) != 2:
                QMessageBox.warning(self, "Uyarı", "Lütfen karşılaştırmak için 2 oyuncu seçin!")
                return
            
            # Veritabanından oyuncuları al
            players = self.db.get_all_players()
            if not players:
                QMessageBox.warning(self, "Hata", "Oyuncu verisi bulunamadı!")
                return
            
            # Seçili oyuncuları al
            row_list = list(selected_rows)
            player1 = players[row_list[0]]
            player2 = players[row_list[1]]
            
            # Karşılaştırma penceresini göster
            dialog = CompareDialog(player1, player2, self)
            dialog.exec_()
            
        except Exception as e:
            print("Karşılaştırma hatası:", e)
            QMessageBox.warning(self, "Hata", "Oyuncuları karşılaştırırken bir hata oluştu!")

    def toggle_favorite(self, player, button):
        if not self.current_user:
            return
        
        player_name = player[1]  # İsim artık ikinci sırada (id'den sonra)
        
        if button.text() == "★":  # Zaten favorideyse
            if self.db.remove_favorite(self.current_user, player_name):
                button.setText("☆")
        else:  # Favoriye ekle
            if self.db.add_favorite(self.current_user, player_name):
                button.setText("★")
        
        # Favorileri güncelle
        self.favorite_players = self.db.get_favorites(self.current_user)

    def logout(self):
        # Kullanıcı bilgilerini temizle
        self.username.clear()
        self.password.clear()
        # Favori listesini sıfırla
        self.favorite_players.clear()
        # Giriş ekranına dön
        self.stack.setCurrentIndex(0)
        QMessageBox.information(self, "Çıkış", "Oturum kapatıldı!")

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QMainWindow, QDialog {
                background-color: #000000;
                color: #ffffff;
            }
            QTableWidget {
                background-color: #ffffff;
                color: #000000;
                gridline-color: #cccccc;
                font-size: 12px;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QTableWidget::item:selected {
                background-color: #2196F3;
                color: white;
            }
            QHeaderView::section {
                background-color: #333333;
                color: #ffffff;
                padding: 8px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #2196F3;
                color: #ffffff;
                padding: 8px;
                border: none;
                border-radius: 4px;
                font-size: 13px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                padding: 8px;
                border: 1px solid #333333;
                border-radius: 4px;
                font-size: 13px;
            }
            QComboBox {
                background-color: #ffffff;
                color: #000000;
                padding: 8px;
                border: 1px solid #333333;
                border-radius: 4px;
                font-size: 13px;
            }
            QSpinBox {
                background-color: #ffffff;
                color: #000000;
                padding: 8px;
                border: 1px solid #333333;
                border-radius: 4px;
                font-size: 13px;
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasketballApp()
    window.show()
    sys.exit(app.exec_()) 