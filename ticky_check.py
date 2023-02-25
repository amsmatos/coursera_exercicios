#!/usr/bin/env python3

import re
import operator
import csv


fileopen = open("syslog.log")
fileread = fileopen.readlines()

info_msg = r'ticky: INFO ([\w ]*) '
get_user = r'\((.+)\)'
error_msg = r'ticky: ERROR ([\w ]*) '

#crio um dicionário que vai ter a contagem dos utilizadores que ESTIVERAM PRESENTES NO LOG
users = {}
#crio um dicionário que vai ter a contagem dos utilizadores que tiveram um INFO
user_info_count = {}
#crio um dicionário que vai ter a contagem dos utilizadores que tiveram um ERROR
user_error_count = {}
#crio um dicionário que vai ter a contagem de quantas vezes apareceu uma determinada mensagem de erro
error_msg_count = {}


for linha in fileread:
    if linha:
        user_name = re.search(get_user, linha)
        users[user_name.group(1)]= users.get(user_name.group(1),0)
        #print(user_name.group(1))
        info = re.search(info_msg, linha)
        if info:
            user_info = re.search(get_user, linha)
            #print("USER INFO:", user_info.group(1))
            user_info_count[user_info.group(1)]= user_info_count.get(user_info.group(1),0) + 1
        error = re.search(error_msg, linha)
        if error:
            user_error = re.search(get_user, linha)
            #print("USER ERROR:", user_error.group(1))
            user_error_count[user_error.group(1)]= user_error_count.get(user_error.group(1),0) + 1

            error_msg_count[error.group(1)] = error_msg_count.get(error.group(1),0) + 1

dicionario_final = {}

# Preencho o docionario final com todos os utilizadores no qual vão ter o valor 0 para info e 0 para error
for k,v in users.items():
    if k not in dicionario_final:
        dicionario_final[k] = [v,v]
    else:
        dicionario_final[k].append(v,v)


# agora atualizo o indice 0 que pertence ao info com a contagem de cada utilizador
for k,v in user_info_count.items():
    dicionario_final[k][0] = v

# agora atualizo o indice 1 que pertence ao error com a contagem de cada utilizador
for k,v in user_error_count.items():
    dicionario_final[k][1] = v



#print(sorted(dicionario_final.items()))
#print(sorted(user_info_count.items()))
#print(sorted(user_error_count.items()))
#print(sorted(error_msg_count.items(), key=operator.itemgetter(1), reverse = True))

# aqui vou exportar os dois dicionários para dois csv's

csv_users_col = ['Username', 'INFO', 'ERROR']

csv_msg_col = ['Error', 'Count']

try:
    with open('user_statistics.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_users_col)
        for k,v in sorted(dicionario_final.items()):
            linha = [k] + v
            writer.writerow(linha)
except IOError:
    print("I/O error")

try:
    with open('error_message.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_msg_col)
        for data in sorted(error_msg_count.items(), key=operator.itemgetter(1), reverse = True):
            #linha = k + v
            writer.writerow(data)
except IOError:
    print("I/O error")