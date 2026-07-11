# import library yang dibutuh kan
import random
import time
import copy

# =========================================
# CONSTANS
# =========================================
# Status
DATA_PLAYER = {
    "LEVEL": 1,
    "HP": 100,
    "MANA": 100
}

DATA_MUSUH = {
    "LEVEL": 1,
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

# Countdown Serangan
MIN_COUNTDOWN = 1
MAX_COUNTDOWN = 3

# Data Player
inventory = {
    "senjata": [],
    "ramuan": []
}

# =========================================
# FUNCTION
# =========================================

def menu_utama():
  print("\n======= MENU UTAMA =======")
  print("1. Cari musuh")
  print("2. Inventori & Up skill")
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

def logika_serangan(DATA_PLAYER, DATA_MUSUH, SKILL):
  """ LOGIKA SERANGAN """
  while True:
    # Tampilkan menu skill
    menu_skill()
    pilih_skill = input("\nPilih skill: ")
    tombol_skill = skill_pilihan(pilih_skill)

    # Copy
    copy_player = copy.deepcopy(DATA_PLAYER)
    copy_musuh = copy.deepcopy(DATA_MUSUH)

    # Serangan player
    if SKILL[daftar_serangan(pilih_skill)]["DAMAGE"]:
       copy_player["MANA"] -= SKILL[daftar_serangan(pilih_skill)]["MANA_COST"]
       copy_musuh["HP"] -= SKILL[daftar_serangan(pilih_skill)]["DAMAGE"]
       print(f"\nHp player: {copy_player['HP']}", end="")
       print(f"\tMana player: {copy_player['MANA']}")
       print(f"\nHp monster: {copy_musuh['HP']}", end="")
       print(f"\tMana monster: {copy_musuh['MANA']}")

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
      logika_serangan(DATA_PLAYER, DATA_MUSUH, SKILL)

# =========================================
# MAIN PROGRAM
# =========================================
if __name__ == "__main__":
  main()