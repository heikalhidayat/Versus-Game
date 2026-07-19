# import library yang dibutuh kan
import random
import time
import copy
import sqlite3

# =========================================
# CREATE DATABASE
# =========================================
def init_database():
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()

    # buat file database
    cursor.execute("CREATE TABLE IF NOT EXISTS memori (id_player INTEGER PRIMARY KEY, user_name VARCHAR(50), hp_player INTEGER, mana_player INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS inventori (id_item INTEGER PRIMARY KEY AUTOINCREMENT, id_player INTEGER, item_name VARCHAR(50))")

    conn.commit()
    conn.close()

init_database()

# =========================================
# CONSTANTS / GLOBALS
# =========================================
DATA_PLAYER = {
    "HP": 100,
    "MANA": 100
}

DATA_MUSUH = {
    "HP": 50,
    "MANA": 50
}

# daftar skill
SKILL = {
    "BASIC_ATTACK": {
        "DAMAGE": 5,
        "MANA_COST": 0
    },
    "SKILL1": {
        "DAMAGE": 10,
        "MANA_COST": 5
    },
    "SKILL2": {
        "DAMAGE": 15,
        "MANA_COST": 10
    },
    "SKILL3": {
        "DAMAGE": 30,
        "MANA_COST": 20,
    }
}

# Daftar monster
MONSTER = ["slime", "lizard", "goblin"]

# Daftar Item
ITEM = ["pedang", "panah", "belati", "potion_hp", "herbal", "kotak_penyembuh", "ramuan", "potion_mana"]

# Ability item
UP_DAMAGE = {
    "pedang": {
        "DAMAGE": 15,
        "MANA_COST": 10
    },
    "panah": {
        "DAMAGE": 10,
        "MANA_COST": 5
    },
    "belati": {
        "DAMAGE": 5,
        "MANA_COST": 0
    }
}

UP_HP = {
    "potion_hp": {
        "HP": 20
    },
    "herbal": {
        "HP": 10
    },
    "kotak_penyembuh": {
        "HP": 50
    }
}

UP_MANA = {
    "ramuan": {
        "MANA": 20
    },
    "potion_mana": {
        "MANA": 20
    }
}

# =========================================
# DATA PLAYER
# =========================================
inventori = []

# Helper kecil
def pause(seconds=0.5):
    """Jeda kecil untuk memberi efek 'dramatis' tanpa terlalu lama."""
    time.sleep(seconds)

# =========================================
# FUNCTION
# =========================================

def login_atau_daftar():
    UserName = input("Masukkan nama karakter: ")

    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()

    # Cek apakah user sdh terdaftar
    cursor.execute("SELECT id_player, hp_player, mana_player FROM memori WHERE user_name = ?", (UserName,))
    data_player = cursor.fetchone()

    if data_player is not None:
        id_player = data_player[0]
        hp_player = data_player[1]
        mana_player = data_player[2]
        print(f"\n[LOADING] Selamat datang kembali, {UserName} (ID: {id_player})")
        print(f"Status Anda: (HP: {hp_player}, Mana: {mana_player})")
        pause(0.5)

        # Load inventori dari database
        cursor.execute("SELECT item_name FROM inventori WHERE id_player = ?", (id_player,))
        items = cursor.fetchall()
        inventori_loaded = [item[0] for item in items]
        print(f"Inventori Anda: {inventori_loaded}")

        pause(0.5)
    else:
        cursor.execute("INSERT INTO memori (user_name, hp_player, mana_player) VALUES (?, ?, ?)", (UserName, DATA_PLAYER["HP"], DATA_PLAYER["MANA"]))
        conn.commit()
        id_player = cursor.lastrowid
        inventori_loaded = []
        print(f"\n[LOADING] Selamat datang, {UserName} (ID: {id_player})")

    conn.close()
    return id_player, UserName, inventori_loaded

def menu_utama():
    print("\n======= MENU UTAMA =======")
    print("1. Cari musuh")
    print("2. Inventori & Up Stats")
    print("3. Keluar")

def validasi_menu(pilihan):
    try:
        menu_int = int(pilihan)
        if menu_int in [1, 2, 3]:
            return menu_int
        else:
            print("Pilihan harus 1, 2, atau 3")
            return None
    except ValueError:
        print("Pilihan harus berupa angka")
        return None

def cari_musuh():
    """Mencari monster secara acak dan menampilkan stat dasar."""
    monster = random.choice(MONSTER)
    print("\nMencari musuh", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        pause(0.3)
    print()
    print(f"\nKamu menemukan monster {monster}")
    print(f"Hp monster: {DATA_MUSUH['HP']}\tMana monster: {DATA_MUSUH['MANA']}")
    pause(0.5)
    return monster

def menu_skill():
    """MENU SKILL"""
    print("\n===== Serang Monster =====")
    print("1. Basic Attack")
    print("2. Skill1")
    print("3. Skill2")
    print("4. Skill3")

def skill_pilihan(pilih_skill):
    try:
        skill_int = int(pilih_skill)
        if skill_int in [1, 2, 3, 4]:
            return skill_int
        else:
            print("Pilihan tidak tersedia!! Pilih 1, 2, 3, atau 4")
            return None
    except ValueError:
        print("Pilihan tidak valid!! Pilih berupa angka")
        return None

def daftar_serangan_from_int(idx):
    mapping = {1: "BASIC_ATTACK", 2: "SKILL1", 3: "SKILL2", 4: "SKILL3"}
    return mapping.get(idx, None)

def serangan_monster(copy_player, copy_musuh):
    """SERANGAN MONSTER: pilih skill acak, cek mana, lakukan serangan."""
    skill_monster = random.choice(list(SKILL.keys()))
    # Jika monster tidak cukup mana untuk skill, pakai BASIC_ATTACK
    mana_cost = SKILL[skill_monster]["MANA_COST"]
    if copy_musuh["MANA"] < mana_cost:
        skill_monster = "BASIC_ATTACK"
        mana_cost = SKILL[skill_monster]["MANA_COST"]

    print(f"\nMonster menyerang menggunakan {skill_monster}\n")
    pause(0.5)

    # Jeda serangan singkat
    for _ in range(3):
        print("*  ", end="", flush=True)
        pause(0.2)

    # Logika serangan
    dmg = SKILL[skill_monster]["DAMAGE"]
    copy_player["HP"] -= dmg
    copy_musuh["MANA"] -= mana_cost
    if copy_musuh["MANA"] < 0:
        copy_musuh["MANA"] = 0

    tampilkan_status_player(copy_player, copy_musuh)

def tampilkan_status_player(copy_player, copy_musuh):
    """Tampilkan status pemain"""
    if copy_player["HP"] <= 0:
        copy_player["HP"] = 0
    if copy_musuh["HP"] <= 0:
        copy_musuh["HP"] = 0
    print(f"\nHp player: {copy_player['HP']}\tMana player: {copy_player['MANA']}")
    pause(0.2)

def tampilkan_status_musuh(copy_player, copy_musuh):
    """Tampilkan status musuh"""
    if copy_player["HP"] <= 0:
        copy_player["HP"] = 0
    if copy_musuh["HP"] <= 0:
        copy_musuh["HP"] = 0
    print(f"\nHp monster: {copy_musuh['HP']}\tMana monster: {copy_musuh['MANA']}")
    pause(0.2)

def drop_item(id_player, inventori):
    """DROP ITEM: dapatkan item random ke inventori."""
    hadiah = random.choice(ITEM)
    
    # memasukkan hadiah ke database
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO inventori (id_player, item_name) VALUES (?, ?)", (id_player, hadiah))
    conn.commit()
    conn.close()
    
    print(f"Kamu mendapatkan {hadiah}")

def tampilkan_peningkatan_stats():
    print("\n==== PENINGKATAN STATS ====")
    print("1. Up Damage")
    print("2. Up HP")
    print("3. Up Mana")
    print("4. Kembali")

def validasi_up_skill(up):
    try:
        menu_int = int(up)
        if menu_int in [1, 2, 3, 4]:
            return menu_int
        else:
            print("Pilihan harus 1, 2, 3, atau 4")
            return None
    except ValueError:
        print("Pilihan harus berupa angka")
        return None

# Cari item tersedia tapi menjaga urutan dan jumlah (count)
def cari_item_tersedia_up_hp(inventori):
    available = []
    for name in UP_HP.keys():
        count = inventori.count(name)
        if count:
            available.append((name, count))
    print(f"\nItem yang tersedia untuk HP: {available}")
    return available

def cari_item_tersedia_up_mana(inventori):
    available = []
    for name in UP_MANA.keys():
        count = inventori.count(name)
        if count:
            available.append((name, count))
    print(f"\nItem yang tersedia untuk Mana: {available}")
    return available

def cari_item_tersedia_up_damage(inventori):
    available = []
    for name in UP_DAMAGE.keys():
        count = inventori.count(name)
        if count:
            available.append((name, count))
    print(f"\nItem yang tersedia untuk Damage: {available}")
    return available

def ambil_item_index(pilih_up_skill, max_index):
    """ubah input index (1-based) ke 0-based dan validasi."""
    try:
        idx = int(pilih_up_skill) - 1
        if 0 <= idx < max_index:
            return idx
        else:
            print(f"Pilihan tidak tersedia!! Pilih antara 1 dan {max_index}")
            return None
    except ValueError:
        print("Pilihan tidak valid!! Pilih berupa angka")
        return None

def apply_up_damage(item_name):
    """Terapkan efek damage dari item ke BASIC_ATTACK permanen."""
    if item_name in UP_DAMAGE:
        DATA_PLAYER.setdefault("_weapon_bonus", 0)
        bonus = UP_DAMAGE[item_name]["DAMAGE"]
        # tambahkan bonus ke BASIC_ATTACK DAMAGE
        SKILL["BASIC_ATTACK"]["DAMAGE"] += bonus
        print(f"Damage BASIC_ATTACK bertambah +{bonus}")
        pause(0.2)

def apply_up_hp(id_player, item_name):
    if item_name in UP_HP:
        bonus = UP_HP[item_name]["HP"]
        DATA_PLAYER["HP"] += bonus

        # Simpan HP baru ke database
        conn = sqlite3.connect('game.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE memori SET hp_player = ? WHERE id_player = ?", (DATA_PLAYER["HP"], id_player))
        conn.commit()
        conn.close()

        print(f"HP Max pemain bertambah +{bonus} (sekarang {DATA_PLAYER['HP']})")
        pause(0.2)

def apply_up_mana(id_player, item_name):
    if item_name in UP_MANA:
        bonus = UP_MANA[item_name]["MANA"]
        DATA_PLAYER["MANA"] += bonus

        # Simpan HP baru ke database
        conn = sqlite3.connect('game.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE memori SET mana_player = ? WHERE id_player = ?", (DATA_PLAYER["MANA"], id_player))
        conn.commit()
        conn.close()

        print(f"Mana Max pemain bertambah +{bonus} (sekarang {DATA_PLAYER['MANA']})")
        pause(0.2)

def gunakan_item_dari_daftar(id_player, available_list, inventori, apply_fn):
    """
    available_list: list of (name,count)
    apply_fn: function(item_name) -> apply effect
    """
    if not available_list:
        print("Tidak ada item yang tersedia pada kategori ini.")
        return

    # tampilkan sebagai daftar berindeks
    print("\nPilih item yang ingin digunakan:")
    for i, (name, count) in enumerate(available_list, start=1):
        print(f"{i}. {name} (x{count})")

    while True:
        pilih = input("\nPilih nomor item (atau 0 untuk batal): ")
        if pilih.strip() == "0":
            print("Dibatalkan.")
            return
        idx = ambil_item_index(pilih, len(available_list))
        if idx is not None:
            item_name = available_list[idx][0]

            # Terapkan efek
            apply_fn(id_player, item_name)

            # Hapus satu buah item dari inventori
            inventori.remove(item_name)

            # Hapus dari database
            conn = sqlite3.connect('game.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM inventori WHERE id_player = ? AND item_name = ? LIMIT 1", (id_player, item_name))
            conn.commit()
            conn.close()

            print(f"{item_name} telah digunakan dan dihapus dari inventori.")
            return

def logika_serangan(copy_player, copy_musuh, inventori):
    """LOGIKA PERTARUNGAN"""
    while True:
        menu_skill()
        pilih_skill = input("\nPilih skill: ")
        tombol_skill = skill_pilihan(pilih_skill)
        if tombol_skill is None:
            continue

        skill_key = daftar_serangan_from_int(tombol_skill)
        if skill_key is None:
            print("Skill tidak dikenali.")
            continue

        mana_cost = SKILL[skill_key]["MANA_COST"]
        if copy_player["MANA"] < mana_cost:
            print("Mana tidak cukup untuk menggunakan skill ini. Pilih skill lain.")
            continue

        print(f"\nKamu menyerang menggunakan {skill_key}\n")
        # Jeda serangan singkat
        for _ in range(3):
            print("*  ", end="", flush=True)
            pause(0.2)

        # Serangan player
        dmg = SKILL[skill_key]["DAMAGE"]
        copy_player["MANA"] -= mana_cost
        copy_musuh["HP"] -= dmg
        if copy_player["MANA"] < 0:
            copy_player["MANA"] = 0

        tampilkan_status_musuh(copy_player, copy_musuh)

        # Cek hasil pertarungan
        if copy_musuh["HP"] <= 0:
            print("\n", " * " * 10)
            print("Kamu Berhasil Mengalahkan Monster!!")
            drop_item(id_player, inventori)
            pause(0.5)
            input("\nTekan enter untuk melanjutkan")
            break
        if copy_player["HP"] <= 0:
            print("\n", " * " * 10)
            print("\nKamu kalah!!")
            pause(0.5)
            input("\nTekan enter untuk melanjutkan")
            break

        # Serangan monster
        serangan_monster(copy_player, copy_musuh)
        # Cek apakah player mati setelah serangan monster
        if copy_player["HP"] <= 0:
            print("\n", " * " * 10)
            print("\nKamu kalah!!")
            pause(0.5)
            input("\nTekan enter untuk melanjutkan")
            break

def main():
    """FUNGSI UTAMA - LOOP"""
    id_player, user_name, inventori = login_atau_daftar()
    print("\n" + "=" * 45)
    print("SELAMAT DATANG DI GAME VERSUS")
    print("=" * 45)

    while True:
        menu_utama()

        # Input dan validasi menu
        while True:
            pilihan = input("\nPilih menu: ")
            menu = validasi_menu(pilihan)
            if menu is not None:
                break

        # Logika game
        if menu == 1:
            # mencari monster
            cari_musuh()

            # Proses war dengan salinan stat
            copy_player = copy.deepcopy(DATA_PLAYER)
            copy_musuh = copy.deepcopy(DATA_MUSUH)
            logika_serangan(id_player, copy_player, copy_musuh, inventori)

        elif menu == 2:
            while True:
                print("\n======== INVENTORI ========")
                # Tampilkan inventori dengan hitungan
                if inventori:
                    counts = {}
                    for item in inventori:
                        counts[item] = counts.get(item, 0) + 1
                    print("Inventori: ")
                    for name, cnt in counts.items():
                        print(f"- {name} (x{cnt})")
                else:
                    print("Inventori kosong.")
                print("=" * 27)
                tampilkan_peningkatan_stats()

                # Input validasi menu
                while True:
                    up = input("\nPilih menu: ")
                    validasi = validasi_up_skill(up)
                    if validasi is not None:
                        break

                # Logika up skill
                if validasi == 1:
                    available = cari_item_tersedia_up_damage(inventori)
                    gunakan_item_dari_daftar(id_player, available, inventori, apply_up_damage)
                elif validasi == 2:
                    available = cari_item_tersedia_up_hp(inventori)
                    gunakan_item_dari_daftar(id_player, available, inventori, apply_up_hp)
                elif validasi == 3:
                    available = cari_item_tersedia_up_mana(inventori)
                    gunakan_item_dari_daftar(id_player, available, inventori, apply_up_mana)
                elif validasi == 4:
                    break

                # setelah satu aksi upgrade, tanyakan apakah ingin kembali atau lanjut
                lanjut = input("\nKembali ke menu utama? (y/n): ").strip().lower()
                if lanjut == "y":
                    break

        elif menu == 3:
            print("\nTerima kasih telah bermain! Sampai jumpa lagi")
            break

# =========================================
# MAIN PROGRAM
# =========================================
if __name__ == "__main__":
    main()
