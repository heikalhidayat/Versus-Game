# 🎮 Versus Game

Sebuah permainan RPG berbasis teks (Text-based RPG) di mana pemain menghadapi monster dalam pertarungan satu lawan satu. Kelola karakter Anda, kumpulkan item, tingkatkan stats, dan taklukkan berbagai musuh yang menantang!

---

## 📋 Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Persyaratan Sistem](#persyaratan-sistem)
- [Instalasi](#instalasi)
- [Cara Bermain](#cara-bermain)
- [Sistem Game](#sistem-game)
  - [Karakter & Stats](#karakter--stats)
  - [Skill Serangan](#skill-serangan)
  - [Item & Equipment](#item--equipment)
  - [Database](#database)
- [Struktur File](#struktur-file)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

---

## 🌟 Fitur Utama

- **Sistem Login & Registrasi**: Buat karakter baru atau lanjutkan karakter yang sudah ada
- **Pertarungan Interaktif**: Lawan monster dengan memilih skill yang strategis
- **Sistem Skill Dinamis**: 4 jenis serangan dengan damage dan mana cost yang berbeda
- **Inventory Management**: Kumpulkan item dan kelola equipment Anda
- **Peningkatan Stats**: Upgrade HP, Mana, dan Damage menggunakan item
- **Persistent Data**: Data karakter disimpan dalam database SQLite
- **Animasi Teks**: Efek dramatis untuk meningkatkan pengalaman bermain

---

## 💻 Persyaratan Sistem

- **Python**: 3.6 atau lebih baru
- **SQLite3**: Sudah termasuk dalam Python standard library
- **OS**: Windows, macOS, atau Linux

---

## 📦 Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/heikalhidayat/Versus-Game.git
cd Versus-Game
```

### 2. Jalankan Game
```bash
python VerSus.py
```

**Catatan**: Database `game.db` akan dibuat otomatis pada kali pertama Anda menjalankan game.

---

## 🎮 Cara Bermain

### Memulai Game
1. Jalankan `VerSus.py`
2. Masukkan nama karakter Anda
3. Jika nama belum terdaftar, karakter baru akan dibuat dengan stats default

### Menu Utama
```
1. Cari Musuh     - Temukan monster dan lakukan pertarungan
2. Inventori      - Kelola item dan upgrade stats
3. Keluar         - Keluar dari game
```

### Sistem Pertarungan
1. Pilih skill yang ingin Anda gunakan (1-4)
2. Setiap skill memiliki damage dan mana cost yang berbeda
3. Monster akan membalas serangan Anda
4. Pertarungan berakhir ketika salah satu HP mencapai 0
5. Jika Anda menang, dapatkan item random

---

## ⚙️ Sistem Game

### Karakter & Stats

**Stat Awal Pemain:**
| Stat | Nilai |
|------|-------|
| HP | 100 |
| Mana | 100 |

**Stat Awal Monster:**
| Stat | Nilai |
|------|-------|
| HP | 50 |
| Mana | 50 |

### Skill Serangan

| Skill | Damage | Mana Cost | Deskripsi |
|-------|--------|-----------|-----------|
| Basic Attack | 5 | 0 | Serangan dasar tanpa memerlukan mana |
| Skill1 | 10 | 5 | Serangan menengah dengan efisiensi baik |
| Skill2 | 15 | 10 | Serangan kuat dengan mana cost sedang |
| Skill3 | 30 | 20 | Serangan ultimate dengan damage tertinggi |

**Tipe Monster:**
- Slime
- Lizard
- Goblin

### Item & Equipment

#### Item Peningkat Damage
| Item | Bonus Damage | Mana Cost |
|------|--------------|-----------|
| Belati | +5 | 0 |
| Panah | +10 | 5 |
| Pedang | +15 | 10 |

#### Item Penyembuh HP
| Item | Bonus HP |
|------|----------|
| Herbal | +10 |
| Potion HP | +20 |
| Kotak Penyembuh | +50 |

#### Item Pemulih Mana
| Item | Bonus Mana |
|------|-----------|
| Ramuan | +20 |
| Potion Mana | +20 |

### Database

Aplikasi menggunakan **SQLite** untuk menyimpan data pemain dan inventory.

**Tabel: `memori`**
```sql
CREATE TABLE memori (
    id_player INTEGER PRIMARY KEY,
    user_name VARCHAR(50),
    hp_player INTEGER,
    mana_player INTEGER
)
```

**Tabel: `inventori`**
```sql
CREATE TABLE inventori (
    id_item INTEGER PRIMARY KEY AUTOINCREMENT,
    id_player INTEGER,
    item_name VARCHAR(50)
)
```

---

## 📁 Struktur File

```
Versus-Game/
├── VerSus.py          # File main game
├── game.db            # Database (dibuat otomatis)
└── README.md          # Dokumentasi
```

---

## 🔧 Fungsi Utama

### Fungsi Game Logic
- `login_atau_daftar()` - Menangani login/registrasi pemain
- `cari_musuh()` - Mencari monster secara random
- `logika_serangan()` - Loop pertarungan antara pemain dan monster
- `serangan_monster()` - AI serangan monster
- `drop_item()` - Pemberian item ke pemain setelah kemenangan

### Fungsi Menu & Validasi
- `menu_utama()` - Menampilkan menu utama
- `validasi_menu()` - Validasi input menu
- `tampilkan_peningkatan_stats()` - Menu upgrade stats

### Fungsi Upgrade Stats
- `apply_up_damage()` - Upgrade damage permanen
- `apply_up_hp()` - Upgrade maksimal HP
- `apply_up_mana()` - Upgrade maksimal Mana
- `gunakan_item_dari_daftar()` - Fungsi general untuk menggunakan item

---

## 💡 Tips Bermain

1. **Manajemen Mana**: Jangan gunakan skill high-cost secara berlebihan, terutama early game
2. **Kumpulkan Item**: Kalahkan musuh sebanyak mungkin untuk mendapatkan item upgrade
3. **Prioritas Upgrade**: 
   - Early game: Fokus upgrade Damage atau HP
   - Mid game: Balance antara HP dan Damage
   - Late game: Maksimalkan Mana untuk skill powerful
4. **Pilih Skill Strategis**: Sesuaikan skill dengan mana yang tersedia

---

## 🐛 Troubleshooting

### Database Error
Jika mengalami error database, hapus file `game.db` dan jalankan game kembali.

### Karakter Data Hilang
Pastikan file `game.db` ada di folder yang sama dengan `VerSus.py`

---

## 📝 Catatan Pengembangan

- Menggunakan library standard Python: `random`, `time`, `copy`, `sqlite3`
- Desain database sederhana dengan 2 tabel utama
- Implementasi deep copy untuk mencegah state mutation selama pertarungan

---

## 🤝 Kontribusi

Kami menerima kontribusi! Jika Anda ingin menambahkan fitur atau memperbaiki bug:

1. Fork repository
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

---

## 📄 Lisensi

Project ini bebas digunakan untuk keperluan pribadi dan pendidikan.

---

## 👤 Author

**Heikal Hidayat**
- GitHub: [@heikalhidayat](https://github.com/heikalhidayat)

---

## 🎯 Roadmap Fitur Masa Depan

- [ ] Sistem boss fight dengan difficulty level berbeda
- [ ] Lebih banyak variasi monster dan skill
- [ ] Sistem party/multiplayer
- [ ] Leaderboard
- [ ] GUI menggunakan tkinter atau pygame
- [ ] Sound effects dan musik background
- [ ] Sistem quest dan achievement

---

**Terima kasih telah bermain Versus Game! Semoga Anda menikmati pengalaman bermainnya. 🎮✨**
