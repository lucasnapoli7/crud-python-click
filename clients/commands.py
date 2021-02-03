import click
from clients.services import ClientService
from clients.models import Client


@click.group() #Convierte esta funcion en un decorador
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name', #Forma de llamarlo
type=str, #Tipo de dato
prompt=True, #Si no nos da el dato, el programa se lo pide
help='The client name') #Linea de ayuda
@click.option('-c', '--company',
type=str,
prompt=True,
help='The client company')
@click.option('-e', '--email',
type=str,
prompt=True,
help='The client email')
@click.option('-p', '--position',
type=str,
prompt=True,
help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client = Client(name, company, email, position)

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients = client_service.list_clients()
    #click.echo es un print pero nos asegura que será asi en todos los sistemas operativos
    click.echo('    ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION')
    click.echo('-' * 100)
    for client in clients:
        click.echo('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=client['uid'],
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


@clients.command()
@click.argument('client_uid',
                type=str)
@click.pass_context
def update(ctx, client_uid):
    """Updates a client"""
    client_services = ClientService(ctx.obj['clients_table']) #inicializa con el nombre de la tabla de los clientes
    clients_list = client_services.list_clients()

    client = [client for client in clients_list if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_services.update_client(client)

        click.echo('Client updated')
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)
    return client


@clients.command()
@click.argument('client_uid',
                type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client = [client for client in client_service.list_clients() if client['uid'] == client_uid]

    if client:
        click.echo('  NAME  |  COMPANY  |  EMAIL  |  POSITION')
        click.echo('-' * 100)
        click.echo(' {name} | {company} | {email} | {position}'.format(
            name=client[0]['name'],
            company=client[0]['company'],
            email=client[0]['email'],
            position=client[0]['position']))
        
        if click.confirm('\nAre you sure you want to delete the client with uid: {}'.format(client_uid)):
            client_service.delete_client(client_uid)
            click.echo('Client deleted')
        else:
            click.echo('Command canceled')
    else:
        click.echo('Client not found')

all = clients


