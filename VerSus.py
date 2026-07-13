# import library yang dibutuh kan
import random
import time
import copy


# =========================================
# CONSTANS
# =========================================
# Status
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


# =========================================
# FUNCTION
# =========================================

def menu_utama():
  print("\n======= MENU UTAMA =======")
  print("1. Cari musuh")
  print("2. Inventori & Up Stats")
  print("3. Kembali")

def validasi_menu(pilihan):
  try:
    menu_int = int(pilihan)
    if menu_int in [1, 2, 3]:
      return menu_int
    else:
      print("Pilihan harus 1, 2,atau 3")
      return None
  except ValueError:
    print("Pilihan harus berupa angka")
    return None

def cari_musuh():
  """ MENCARI MUSUH """
  monster = random.choice(MONSTER)
  print("\nMencari musuh", end="")
  for i in range(5):
    print(".", end="")
    time.sleep(1)
  print()
  print(f"\nKamu menemukan monster {monster}")
  print(f"Hp monster: {DATA_MUSUH['HP']}", end="")
  print(f"\tMana monster: {DATA_MUSUH['MANA']}")
  time.sleep(1)
  return monster

def menu_skill():
  """ MENU SKILL """
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

def daftar_serangan(pilih_skill):
  if pilih_skill == "1":
    return "BASIC_ATTACK"
  elif pilih_skill == "2":
    return "SKILL1"
  elif pilih_skill == "3":
    return "SKILL2"
  elif pilih_skill == "4":
    return "SKILL3"

def serangan_monster(DATA_PLAYER, DATA_MUSUH, SKILL, copy_player, copy_musuh):
  """ SERANGAN MONSTER """
  skill_monster = random.choice(list(SKILL.keys()))
  print(f"\nMonster menyerang menggunakan {skill_monster}\n")
  time.sleep(1)

  # Jeda serangan
  for i in range(5):
    print("*  ", end="")
    time.sleep(1)

  # Logika serangan
  if SKILL[skill_monster]["DAMAGE"]:
    copy_player["HP"] -= SKILL[skill_monster]["DAMAGE"]
    copy_musuh["MANA"] -= SKILL[skill_monster]["MANA_COST"]

  tampilkan_status_player(copy_player, copy_musuh)

def tampilkan_status_player(copy_player, copy_musuh):
  """ TAMPILKAN STATUS PLAYER """
  if copy_player["HP"] <= 0:
    copy_player["HP"] = 0
  elif copy_musuh["HP"] <= 0:
    copy_musuh["HP"] = 0
  # Menampilkan data user dan monster
  print(f"\nHp player: {copy_player['HP']}", end="")
  print(f"\tMana player: {copy_player['MANA']}")
  time.sleep(1)

def tampilkan_status_musuh(copy_player, copy_musuh):
  """ TAMPILKAN STATUS MUSUH """
  if copy_player["HP"] <= 0:
    copy_player["HP"] = 0
  elif copy_musuh["HP"] <= 0:
    copy_musuh["HP"] = 0
  print(f"\nHp monster: {copy_musuh['HP']}", end="")
  print(f"\tMana monster: {copy_musuh['MANA']}")
  time.sleep(1)

def drop_item(inventori):
  """ DROP ITEM """
  hadiah = random.choice(ITEM)
  inventori.append(hadiah)
  print(f"Kamu mendapatkan {hadiah}")

def tampilkan_peningkatan_stats():
  """ TAMPILKAN PENINGKATAN STATS """
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


def cari_item_tersedia_up_hp(inventori):
  inventori_set = set(inventori)
  cari_item = set(["potion_hp", "herbal", "kotak_penyembuh"])
  print(f"\nItem yang tersedia {cari_item}")

  # mencari item yang cocok
  item_tersedia = inventori_set.intersection(cari_item)
  print(f"\nItem yang tersedia {item_tersedia}")

def cari_item_tersedia_up_mana(inventori):
  inventori_set = set(inventori)
  cari_item = set(["ramuan", "potion_mana"])

  # mencari item yang cocok
  item_tersedia = inventori_set.intersection(cari_item)
  print(f"\nItem yang tersedia {item_tersedia}")


def cari_item_tersedia_up_damage(inventori):
  inventori_set = set(inventori)
  cari_item = set(["pedang", "panah", "belati"])
    
  # mencari item yang cocok
  item_tersedia = inventori_set.intersection(cari_item)
  print(f"Item yang tersedia {item_tersedia}")

def logika_serangan(DATA_PLAYER, DATA_MUSUH, SKILL, copy_player, copy_musuh, inventori):
  """ LOGIKA SERANGAN """
  while True:
    # Tampilkan menu skill
    menu_skill()
    pilih_skill = input("\nPilih skill: ")
    tombol_skill = skill_pilihan(pilih_skill)
    print(f"\nKamu menyerang menggunakan {daftar_serangan(pilih_skill)}\n")

    # Jeda serangan
    for i in range(5):
       print("*  ", end="")
       time.sleep(1)

    # Serangan player
    if SKILL[daftar_serangan(pilih_skill)]["DAMAGE"]:
       copy_player["MANA"] -= SKILL[daftar_serangan(pilih_skill)]["MANA_COST"]
       copy_musuh["HP"] -= SKILL[daftar_serangan(pilih_skill)]["DAMAGE"]

       tampilkan_status_musuh(copy_player, copy_musuh)

    # Hasil pertarungan
    if copy_musuh["HP"] <= 0:
      print("\n", " * " * 10)
      print("Kamu Berhasil Mengalahkan Monster!!")
      drop_item(inventori)
      time.sleep(1)

      # kembali ke menu utama
      input("\nTekan enter untuk melanjutkan")
      break
    elif copy_player["HP"] <= 0:
      print("\n", " * " * 10)
      print("\nKamu kalah!!")
      time.sleep(1)

      # kembali ke menu utama
      input("\nTekan enter untuk melanjutkan")
      break

    # Serangan monster
    serangan_monster(DATA_PLAYER, DATA_MUSUH, SKILL, copy_player, copy_musuh)

def main():
  """ FUNGSI UTAMA - LOOP """
  print("\n" + "=" * 45)
  print("SELAMAT DATANG DI GAME VERSUS")
  print("=" * 45)

  while True:
    # Tampilkan menu utama
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

      # Proses war
      copy_player = copy.deepcopy(DATA_PLAYER)
      copy_musuh = copy.deepcopy(DATA_MUSUH)
      logika_serangan(DATA_PLAYER, DATA_MUSUH, SKILL, copy_player, copy_musuh, inventori)

    # Tampilkan inventori
    elif menu == 2:
      print("\n======== INVENTORI ========")
      print("Inventori: ", inventori)
      print("=" * 27)
      tampilkan_peningkatan_stats()

      # Input dan validasi menu
      while True:
        up = input("\nPilih Stats: ")
        validasi = validasi_up_skill(up)
        if validasi is not None:
          break

      # Logika up skill
      if validasi == 1:
        cari_item_tersedia_up_damage(inventori)

# =========================================
# MAIN PROGRAM
# =========================================
if __name__ == "__main__":
  main()
