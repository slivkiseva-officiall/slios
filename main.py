# license: GPL v2

import time
import os
import sys
import math
import random

# system class

class System:
	class Info:
		class Kernel:
			name = "slicore"
			ver = "7.1"
			
			
		class System:
			name = "slios"
			ver = "5"
			build = "0014"
			name_ver = "2512"
			code_name = "under construction" 
	
	@staticmethod
	def wait(time_for_sleep):
		time.sleep(time_for_sleep)
	
	@staticmethod
	def exit(code):
		sys.exit(code)
	
	@staticmethod
	def cs():
		os.system('cls' if os.name == 'nt' else 'clear')
	
	@staticmethod
	def show_error(msg="ядро выдает ошибку, так как программа или ядро выдало ошибку", enter_msg="нажмите enter"):
		print(msg)
		print(f"{enter_msg}...")
# kernel class

class SystemSettings:
	show_date = True
	old_taskbar = False

sys_set = SystemSettings()

class Kernel:
	@staticmethod
	def show_sd(msg, code):
		print(msg)
		print(code)
		input()
		sys.exit(1)

def sleep(y):
	time.sleep(y)

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')

loading = "#"
shutdown = "завершение работы"

for x in range(5):
	for i in range(5):
		print("slios 5.0", flush=True)
		print(loading, flush=True)
		System.wait(0.1)
		loading += "#"
		cls()
	loading = "#"

username = "user"
root = "root"
usingUser = None

tasks = []

hotbar = ["пуск", "о системе", "$time(%H:%M)"]
hotbar_preview = ["пуск", "о системе", "$time(%H:%M)"]
desktop_customize = tasks
enter = ""

# Файловый менеджер управляет реальными файлами
# ВНИМАНИЕ! вы можете удалить системные файлы, т.к. программа при root имеет доступ к системе!

class Filemanager:
	def __init__(self):
		self.running = True
		self.app_ver = "3.0"
	
	def app(self):
		self.running = True
		while self.running:
			cls()
			print(time_now())
			os.system('dir' if os.name == 'nt' else 'ls')
			print("создать файл, удалить файл")
			print("создать папку, удалить папку, выше, перейти в папку")
			print("выйти, версия")
			filemanager_app = input(enter)
			if filemanager_app == "выйти":
				self.close()
			elif filemanager_app == "выше":
				os.chdir("..")
			elif filemanager_app == "удалить файл":
				remove_filename = input("введите имя файла: ")
				if self.rmfile(remove_filename) != 0:
					input("ошибка\nнажмите enter...")
			elif filemanager_app == "создать файл":
				create_filename = input("введите имя нового файла: ")
				if self.createfile(create_filename) != 0:
					input("ошибка\nнажмите enter...")
			elif filemanager_app == "перейти в папку":
				folder_name = input("введите название папки: ")
				os.chdir(folder_name)
			elif filemanager_app == "создать папку":
				folder_name = input("введите имя папки: ")
				try:
					os.mkdir(folder_name)
				except:
					input("ошибка в создании папки\nнажмите enter...")
			elif filemanager_app == "удалить папку":
				folder_name = input("введите имя папки: ")
				os.rmdir(folder_name)
			elif filemanager_app == "версия":
				print(self.app_ver)
				input("нажмите enter...")
	
	def rmfile(self, name):
		if name is None:
			return 1
		if name in ("/", "\\", "/*"):
			return 2
		
		try:
			os.remove(name)
			return 0
		except:
			return 3
	
	def createfile(self, name):
		status = 0
		try:
			f = open(name, "x")
			status = 0
			f.close()
		except:
			status = 1
		return status
	
	def close(self):
		self.running = False

class Console:
	def __init__(self):
		self.running = True
		self.prompt = "[slios] >"
		self.app_ver = "2.0"
	
	def app(self):
		self.running = True
		print(f"welcome to console ver. {self.app_ver}")
		while self.running:
			command = input(self.prompt)
			self.execute(command)
			
	def execute(self, line):
		if line == "exit":
			self.close()
		elif line == "ls":
			os.system('dir' if os.name == 'nt' else 'ls')
		elif line.startswith("cd "):
			try:
				os.chdir(line[3:])
			except:
				print("невозможно перейти в папку")
		elif line.startswith("rm "):
			try:
				os.remove(line[3:])
			except:
				print("невозможно удалить файл")
		elif line.startswith("mkdir "):
			try:
				os.mkdir(line[6:])
			except:
				print("невоможно содать папку")
		elif line.startswith("rmdir "):
			try:
				os.rmdir(line[6:])
			except:
				print("невоможно удалить папку")
		elif line == "clear":
			cls()
		elif line == "ver":
			self.ver_output()
		elif line == "pp":
			print(os.getcwd())
		elif line == "shutdown":
			sys.exit(0)
		elif line == "cs":
			System.cs()
		elif line == "help":
			self.help()
		elif line == "ls":
			os.system("dir" if os.name == "nt" else "ls -CF --color=auto")
		elif line.startswith("cd"):
			os.chdir(line[3:])
	def ver_output(self):
		print(f"sli console ver {self.app_ver}")
	
	def help(self):
		print("exit - выйти из терминала")
		print("clear - очистить экран")
		print("ls - показать файлы и папки")
		print("cd - перейти в папку")
		print("pp - показать путь")
		print("rm - удалить файл")
		print("shutdown - выключить")
		print("cs - очистить экран")
		print("mkdir - создать папку")
		print("rmdir - удалить папку")
	
	def close(self):
		self.running = False

class Notes:
	def __init__(self):
		self.running = True
		self.app_ver = "3.0"
	
	def app(self):
		self.running = True
		while self.running:
			System.cs()
			print(time.strftime("%H:%M"))
			print(tasks)
			print("создать, удалить, удалить индексацией")
			print("выйти, версия")
			notes_input = input(enter)
			if notes_input == "выйти":
				self.running = False
			elif notes_input == "версия":
				input(f"{self.app_ver} \nнажмите enter")
			elif notes_input == "создать":
				name_of_task = input("введите имя новой заметки: ")
				if name_of_task in tasks:
					System.show_error("невозможно создать новую заметку, так как она существует.")
				else:
					tasks.append(name_of_task)
			elif notes_input == "удалить":
				if len(tasks) < 1:
					System.show_error("невоможно удалить заметку, так как ее не существует")
				else:
					name_of_task = input("введите имя заметки: ")
					if name_of_task in tasks:
						tasks.remove(name_of_task)
					else:
						System.show_error("невозможно удалить, так как такой заметки нет. ")
			elif notes_input == "удалить индексацией":
				if len(tasks) < 1:
					System.show_error("незможно удалить заметку, так как ее не существует")
				else: 
					index_of_task = int(input("введите индекс заметки (индекс начинается с 1): "))
					if index_of_task > len(tasks):
						System.show_error("невозможно удалить, так как ваш индекс больше чем реалный")
					elif index_of_task <= 0:
						System.show_error("невозможно удалить, так как ваш индекс равен или ниже нуля.")
					else:
						tasks.pop(index_of_task - 1)
	def close(self):
		self.running = False

def time_now(formatted=False, format="%H:%M:%S"):
	return time.strftime(format) if formatted == True else time.asctime(time.localtime(time.time()))

running = True
usingInSystem = False

filemanager = Filemanager()
console = Console()
notes = Notes()

custom_vars = {
	"notes": tasks,
	"user_uses": usingUser
}

while running:
	System.cs()
	print(time_now())
	print("выкл")
	print("выберете пользователя которым хотите сегодня пользоваться: ")
	print(f"root, {username}")
	guessUserOrpoweroff = input()
	if guessUserOrpoweroff == username:
		usingUser = username
		usingInSystem = True
	elif guessUserOrpoweroff == "выкл":
		for i in range(3):
			for x in range(4):
				print("slios", flush=True)
				print(shutdown, flush=True)
				shutdown+="."
				sleep(0.3)
				System.cs()
			shutdown = "завершение работы"
		break
	elif guessUserOrpoweroff == "root":
		usingUser = root
		usingInSystem = True
	while usingInSystem:
		if root != "root":
			root = "root"
		if usingUser == None:
			break
		System.cs()
		if sys_set.show_date:
			print(time_now())
		print(desktop_customize)
		if sys_set.old_taskbar != True:
			for i in range(len(hotbar)):
				if hotbar[i].startswith("$time"):
					print("\t", time.strftime("%H:%M"), end = "")
					continue
				print(hotbar[i], end="")
				if i != len(hotbar) - 1:
					print(", ", end="")
		else:
			print("пуск, о системе", end="")
		print()
		desktop = input(enter)
		if desktop == "о системе": 
			print(f"{System.Info.System.name} {System.Info.System.ver} {System.Info.System.name_ver} {System.Info.System.build}") 
			print(f"{System.Info.Kernel.name} {System.Info.Kernel.ver}")
			nothing = input(enter)
			match nothing:
				case "pigOS":
					username = "pigOS user"
				case "slios":
					username = "using slios;"
				case "motyaOS":
					username = "motyaUser"
				case "ilyaOS":
					username = "ilyaUser 3.0"
				case "woapOS": 
					username = "WoapOS_get"
				case "namedOS":
					username = "pls_name_OS"
		elif desktop == "пуск":
			print("выкл, файлы, параметры, консоль, заметки, калькулятор")
			start = input(enter)
			if start == "выкл":
				for i in range(3):
					for x in range(4):
						print("slios", flush=True)
						print(shutdown, flush=True)
						sleep(0.3)
						shutdown += "."
						cls()
					shutdown = "завершение работы"
				running = False
				break
			elif start == "консоль":
				console.app()
			elif start == "файлы":
				filemanager.app()
			elif start == "параметры":
				while True:
					cls()
					print(time_now())
					print(usingUser)
					print("переименовать пользователя, изменить пользователя, изменить рабочий стол, изменить промпт, изменить панель задач, другие настройки, выйти")
					settings = input(enter)
					if settings == "выйти":
						break
					elif settings == "переименовать пользователя":
						username = input(">>> ")
					elif settings == "изменить пользователя":
						usingInSystem = False
					elif settings == "изменить рабочий стол":
						print("переменные: notes, user_uses")
						answer = input(f"введите надпись или \"$\" для переменной\n{enter}")
						if answer.startswith("$"):
							customize_var = answer[1:]
							if customize_var in custom_vars:
								desktop_customize = custom_vars[customize_var]
							else:
								print("переменная не найдена")
								input("нажмите enter...")
						else:
							desktop_customize = answer
					elif settings == "изменить промпт":
						enter = input(enter)
					elif settings == "изменить панель задач":
						while True:
							print(hotbar_preview)
							print("убрать, добавить, применить")
							print("выйти")
							buffer = input()
							if buffer == "выйти":
								break
					elif settings == "другие настройки":
						print(f"1. отключить/включить отображение даты на рабочем столе ({sys_set.show_date})")
						print(f"2. Включить/отключить старый taskbar ({sys_set.old_taskbar})")
						buffer = input()
						match buffer:
							case "1":
								sys_set.show_date = True if sys_set.show_date != True else False
							case "2":
								sys_set.old_taskbar = True if sys_set.old_taskbar != True else False
							
			elif start == "заметки":
				notes.app()
			elif start == "калькулятор":
				try:
					print(eval(input(">>> "), {"__binutils__": None}, {}))
				except:
					print("ошибка ввода")
				finally:
					input("нажмите enter...")
		elif desktop == "файлы" and desktop in hotbar and sys_set.old_taskbar != True:
			filemanager.app()
		elif desktop == "консоль" and desktop in hotbar and sys_set.old_taskbar != True:
			console.app()
		elif desktop == "заметки" and desktop in hotbar and sys_set.old_taskbar != True:
			notes.app()
