drive = input("請問你有沒有開過車? ")
if drive != "有" and drive != "沒有":
	print("只能輸入有/沒有")
	raise SystemExit

age = int(input("請問你的年齡: "))
if drive == "有":
	if age >= 18:
		print("你通過測驗了。")
	else:
		print("奇怪，你怎麼會有開過車?")
elif drive == "沒有":
	if age >= 18:
		print("你可以去考駕照了阿。")
	else:
		print("很好，再過幾年就可以去考駕照了")
else:
	print("只能輸入有跟沒有")

