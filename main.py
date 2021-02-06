import zipfile
numbers = ["0", "1", "2", "4", "5"] # digits used in password

x = 0
for a in range(0, 5):
    for b in range(0, 5):
        for c in range(0, 5):
            for d in range(0, 5):
                code = numbers[a]+numbers[b]+numbers[c]+numbers[d]
                with zipfile.ZipFile(r"C:\Users\Michal\Desktop\File.zip", "r") as zip_ref:
                    try:
                        zip_ref.extractall(r"C:\Users\Michal\Desktop", pwd=bytes(code,'utf-8'))
                    except:
                        continue
                    else:
                        print("Password found: "+code)
