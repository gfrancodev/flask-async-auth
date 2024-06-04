https://ponyorm.org/create/user 

{
    usuario 
    senha 
    data
    etc...
}


dto -> validar os dados
data -> vai para usecases 
usecase - caso de criação de usuário
service - chamar o serviço de usuário diretamente - domain do usuário 
service -> repository de usuário -> banco de dados 


Usuario(
    nome
    telefone
    tal tal
)

userService(data: Usuario) {
    userRepository.create(new Usuario(data))
}

Clean - Nomear o seu código de acordodo com aquilo que ele faz

Principios SOLID 

S - 
O -
L -
I -
D -

CORS - flask_cors OK
GZIP ENCODING - flask_compress OK
RATE LIMIT - flask_limiter 
SECURITY HEADERS - flask_talisman OK
GRACEFUL - signal & sys OK
DOC - flask_swagger_ui OK
