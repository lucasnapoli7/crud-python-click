import click

from clients import commands as clients_commands

CLIENTS_TABLE = '.clients.csv'

@click.group() #Esto define el punto de entrada
@click.pass_context #Nos da un objeto contexto
def cli(ctx): #Punto de entrada
    ctx.obj = {} #Objeto contexto inicializado como diccionario
    ctx.obj['clients_table'] = CLIENTS_TABLE


cli.add_command(clients_commands.all) #Registra los comandos. all es un alias a clients