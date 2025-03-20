import sqlite3
import os

class Database:
    def __init__(self):
        try:
            # Veritabanı dosyasının tam yolunu al
            db_path = os.path.join(os.path.dirname(__file__), 'basketball.db')
            
            # Veritabanı bağlantısı
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            
            # Tabloları oluştur
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                team TEXT,
                position TEXT,
                age INTEGER,
                country TEXT,
                points REAL,
                rebounds REAL,
                assists REAL,
                steals REAL,
                blocks REAL,
                turnovers REAL
            )
            ''')

            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_id INTEGER,
                username TEXT,
                FOREIGN KEY (player_id) REFERENCES players (id)
            )
            ''')

            # Oyuncuları kontrol et ve yoksa ekle
            self.cursor.execute("SELECT COUNT(*) FROM players")
            count = self.cursor.fetchone()[0]
            
            if count == 0:  # Tablo boşsa oyuncuları ekle
                players = [
                    ('LeBron James', 'Los Angeles Lakers', 'Forward', 39, 'ABD', 25.4, 7.2, 8.1, 1.2, 0.5, 3.4),
                    ('Stephen Curry', 'Golden State Warriors', 'Guard', 35, 'ABD', 28.1, 4.5, 4.9, 0.8, 0.2, 3.1),
                    ('Giannis Antetokounmpo', 'Milwaukee Bucks', 'Forward', 29, 'Yunanistan', 30.8, 11.2, 6.3, 1.2, 1.0, 3.3),
                    ('Kevin Durant', 'Phoenix Suns', 'Forward', 35, 'ABD', 28.4, 6.8, 5.5, 0.8, 1.2, 3.2),
                    ('Alperen Şengün', 'Houston Rockets', 'Center', 21, 'Türkiye', 20.3, 9.2, 5.1, 1.2, 1.0, 2.9),
                    ('Luka Doncic', 'Dallas Mavericks', 'Guard', 25, 'Slovenya', 33.8, 9.2, 9.8, 1.4, 0.5, 3.5),
                    ('Nikola Jokic', 'Denver Nuggets', 'Center', 29, 'Sırbistan', 26.1, 12.3, 9.2, 1.2, 0.9, 3.1),
                    ('Joel Embiid', 'Philadelphia 76ers', 'Center', 30, 'Kamerun', 35.3, 11.3, 5.7, 1.1, 1.8, 3.2),
                    ('Jayson Tatum', 'Boston Celtics', 'Forward', 26, 'ABD', 27.2, 8.3, 4.9, 1.0, 0.7, 2.8),
                    ('Shai Gilgeous-Alexander', 'Oklahoma City Thunder', 'Guard', 25, 'Kanada', 31.4, 5.5, 6.5, 2.1, 0.8, 3.3),
                    ('Devin Booker', 'Phoenix Suns', 'Guard', 27, 'ABD', 27.5, 4.6, 7.2, 1.0, 0.4, 3.0),
                    ('Donovan Mitchell', 'Cleveland Cavaliers', 'Guard', 27, 'ABD', 28.2, 5.1, 6.2, 1.8, 0.4, 3.1),
                    ('Cade Cunningham', 'Detroit Pistons', 'Guard', 22, 'ABD', 22.7, 4.1, 7.5, 1.3, 0.3, 2.7),
                    ('Anthony Edwards', 'Minnesota Timberwolves', 'Guard', 22, 'ABD', 26.4, 5.2, 5.1, 1.3, 0.5, 2.8),
                    ('Furkan Korkmaz', 'Philadelphia 76ers', 'Guard', 26, 'Türkiye', 8.2, 2.1, 1.5, 0.5, 0.1, 1.4),
                    ('Victor Wembanyama', 'San Antonio Spurs', 'Center', 20, 'Fransa', 20.7, 10.2, 3.4, 1.2, 3.3, 2.9),
                    ('Jaylen Brown', 'Boston Celtics', 'Guard', 27, 'ABD', 23.1, 5.5, 3.7, 1.2, 0.3, 2.5),
                    ('Kristaps Porzingis', 'Boston Celtics', 'Center', 28, 'Letonya', 20.2, 7.1, 1.9, 0.7, 1.8, 2.2),
                    ('Jalen Brunson', 'New York Knicks', 'Guard', 27, 'ABD', 27.5, 3.8, 6.5, 0.9, 0.2, 2.4),
                    ('Julius Randle', 'New York Knicks', 'Forward', 29, 'ABD', 24.1, 9.2, 5.0, 0.6, 0.3, 2.3),
                    ('Paolo Banchero', 'Orlando Magic', 'Forward', 21, 'ABD', 22.6, 6.8, 5.4, 1.0, 0.6, 2.1),
                    ('Franz Wagner', 'Orlando Magic', 'Forward', 22, 'Almanya', 19.7, 5.4, 3.7, 1.1, 0.4, 1.9),
                    ('Tyrese Maxey', 'Philadelphia 76ers', 'Guard', 23, 'ABD', 25.9, 3.7, 6.2, 1.0, 0.5, 2.6),
                    ('De''Aaron Fox', 'Sacramento Kings', 'Guard', 26, 'ABD', 26.8, 4.2, 5.5, 1.8, 0.3, 2.7),
                    ('Domantas Sabonis', 'Sacramento Kings', 'Center', 27, 'Litvanya', 19.4, 13.7, 8.3, 0.8, 0.7, 2.4),
                    ('Lauri Markkanen', 'Utah Jazz', 'Forward', 26, 'Finlandiya', 23.2, 8.3, 1.7, 0.9, 0.6, 2.0),
                    ('Ja Morant', 'Memphis Grizzlies', 'Guard', 24, 'ABD', 25.1, 5.6, 8.1, 1.3, 0.3, 2.5),
                    ('Trae Young', 'Atlanta Hawks', 'Guard', 25, 'ABD', 26.4, 2.7, 10.8, 1.4, 0.2, 3.0),
                    ('Dejounte Murray', 'Atlanta Hawks', 'Guard', 27, 'ABD', 21.5, 5.1, 5.2, 1.4, 0.3, 2.3),
                    ('Mikal Bridges', 'Brooklyn Nets', 'Forward', 27, 'ABD', 21.7, 4.7, 3.6, 1.1, 0.5, 2.0)
                ]
                
                self.cursor.executemany('''
                INSERT INTO players (name, team, position, age, country, 
                                   points, rebounds, assists, steals, blocks, turnovers)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', players)
                
                self.conn.commit()
                print(f"{len(players)} oyuncu veritabanına eklendi!")
            
            print(f"Veritabanına bağlanıldı: {db_path}")
            
        except sqlite3.Error as e:
            print("Veritabanı başlatma hatası:", e)

    def get_all_players(self):
        try:
            self.cursor.execute('''
            SELECT id, name, team, position, age, country, 
                   points, rebounds, assists, steals, blocks, turnovers
            FROM players
            ORDER BY name
            ''')
            players = self.cursor.fetchall()
            if not players:
                print("Veritabanında oyuncu bulunamadı!")
            return players
        except sqlite3.Error as e:
            print("Oyuncuları getirme hatası:", e)
            return []

    def add_favorite(self, username, player_name):
        try:
            # Önce oyuncunun ID'sini bul
            self.cursor.execute("SELECT id FROM players WHERE name = ?", (player_name,))
            result = self.cursor.fetchone()
            if result:
                player_id = result[0]
                # Favori zaten var mı kontrol et
                self.cursor.execute('''
                SELECT id FROM favorites 
                WHERE username = ? AND player_id = ?
                ''', (username, player_id))
                
                if not self.cursor.fetchone():
                    # Favori yoksa ekle
                    self.cursor.execute('''
                    INSERT INTO favorites (player_id, username)
                    VALUES (?, ?)
                    ''', (player_id, username))
                    self.conn.commit()
                    print(f"Favori eklendi: {player_name}")
                    return True
            return False
        except sqlite3.Error as e:
            print("Favori ekleme hatası:", e)
            return False

    def remove_favorite(self, username, player_name):
        try:
            # Önce oyuncunun ID'sini bul
            self.cursor.execute("SELECT id FROM players WHERE name = ?", (player_name,))
            result = self.cursor.fetchone()
            if result:
                player_id = result[0]
                # Favoriyi sil
                self.cursor.execute('''
                DELETE FROM favorites 
                WHERE username = ? AND player_id = ?
                ''', (username, player_id))
                self.conn.commit()
                print(f"Favori silindi: {player_name}")
                return True
            return False
        except sqlite3.Error as e:
            print("Favori silme hatası:", e)
            return False

    def get_favorites(self, username):
        if not username:
            return []
            
        try:
            self.cursor.execute('''
            SELECT p.name, p.team, p.position, p.age, p.country, 
                   p.points, p.rebounds, p.assists, p.steals, p.blocks, p.turnovers
            FROM players p
            JOIN favorites f ON p.id = f.player_id
            WHERE f.username = ?
            ORDER BY p.name
            ''', (username,))
            favorites = self.cursor.fetchall()
            print(f"Favoriler getirildi: {len(favorites)} oyuncu")
            return favorites
        except sqlite3.Error as e:
            print("Favorileri getirme hatası:", e)
            return []

    def close(self):
        if self.conn:
            self.conn.close()
            print("Veritabanı bağlantısı kapatıldı") 