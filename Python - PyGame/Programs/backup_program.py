import sys, os, time

# Prosthetei to path pou vrisketai to ektelesimo tou zip sto path tou diermineuti tis Python
sys.path.append(r'C:\Program Files (x86)\GnuWin32\bin')

# O pinakas pou exei ta arxeia pou theloume na kratisoume backup
source = ['C:\\Users\\Giannoutas\\Desktop\\Python', r'"C:\Users\Giannoutas\Desktop\Snake Hunter"']

# O kentrikos fakelos pou tha sozontai ta backups
target_dir = 'E:\\My_Backup'

# O fakelos pou exei ta backups tis imeras
today = target_dir + os.sep + time.strftime('%Y_%m_%d')

# O fakelos me ta backups pou tha dimiourgithei gia autin tin ektelesi tou programmatos
now = time.strftime('%H_%M_%S')

# Zitaei ena sxolio apo ton xristi gia na mpei sto telos tou onomatos tou backup
comment = input('Enter a comment: ')

# Dimiourgei tin pliri diadromi pou tha apothikeutei to backup
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# An den exei ginei allo backup tin sugkekrimeni mera, tote dimiourgei ton fakelo
if not os.path.exists(today):
    os.mkdir(today)
    print('Succesfully created directory', today)

# I entili zip etsi opos tha tin etrexe to leitourgiko ton windows
zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))
print(zip_command)
# Tuponei munima epituxias i sfalmatos analoga me tin poreia tis ektelesis tis entolis
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
