
from datetime import date

dirsaida="files_out" +"\saida_posicao_olho_"+ str(date.today())+ ".txt"
arquivo= open(dirsaida,"a")
arquivo.write("ola mundo")
