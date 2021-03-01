import os, sys,winshell,logging
#from imp import reload

#reload(logging)

diretorio =os.path.dirname(os.path.abspath(sys.argv[0]))

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename=os.path.join(diretorio,'erros.log'), filemode='w', level=logging.DEBUG)

par = input('Digite o diretório da pasta atalhos\n Exemplo X:\\atalhos:\n')


atalhos = {}

lista_de_resultados = []

logging.debug('Início da execução.')

try:
    for name in os.listdir(par):
#        print(name)
        if name.endswith(".lnk"):    
            x = name.replace('.lnk','')
            atalhos[x] =[os.path.join(par, name)]
            a=atalhos.get(x)
            c = winshell.shortcut(os.path.join(par, name))
            args =c.arguments.split() 
            if len(args)>0:
                cblconfi = (args[2])
            else:
                cblconfi = None
  
            
            if cblconfi != None and os.path.exists(cblconfi):
                
                with open (cblconfi,'r') as arq:
                    for linha in arq:
                        if ('iscobol.debug.code_prefix') in linha :
                            linha = linha.split()
                            dir_exe= linha[1].replace(r"\\","\\")
                            
                            with open (os.path.join(diretorio,'diretórios_exe.csv'),'a') as f:
                                f.write(x+';'+args[2]+';'+dir_exe+'\n')
            else:
                logging.debug('Diretório "'+str(cblconfi)+'" não encontrado, do atalho "'+str(name)+'"')
except Exception as e:
    logging.debug(e)
    a =1

    
if a==1:
    print('Houve erro na execução, consulte o log '+os.path.join(diretorio+'\erros.log')+' para mais detalhes.')
    pass

else:
    logging.debug('Fim da execução')
    print('Fim da execução')
    sys.exit(0)