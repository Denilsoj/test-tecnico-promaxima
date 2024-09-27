# Desafio FullStack #

Software fullstack, para consultas de medicamentos e seus dados.

## Funcionalidades ##

**Busca com Filtros :**

    O usuário pode buscar por dados utilizando o filtro de Substância, CNPJ ou Laboratório

## Tecnologias ##

- Python
- Django
- Django Rest Framework
- Postgres
- JavaScript
- Vue
- Docker
- Docker Compose

## Preparando o ambiente ##

1. Clone o repositório:

        git clone https://github.com/Denilsoj/test-tecnico-promaxima.git
2. Entre no diretório do projeto:

        cd < diretorio-projeto >

3. ### Backend ###

   1. Entre no diretório backend:

            cd backend/

   2. Entre no dirtório dotenv_files e crie um arquivo .env:

                cd dotenv_files/  
                touch .env
                
   3. Copie todas as variaveis de ambiente do arquivo .env-exaple, logo em seguida atualize os valores de todas as variáveis de ambientes que estejam "CHANGE-ME", e então volte para o diretório backend;

            cp .env-exaple .env
            cd ..
   4. Crie e inicialize o container:

              docker-compose up --build

   5. Faça o backup da sua base de dados:
      - **Para isso abra uma nova janela do terminal**
      - Lembrando de sempre estar no diretório backend
      - E então acesse a linha de comando do container que está o postgres:

             docker exec -it psql sh
      - Então faça o backup da base de dados:
        
             pg_restore -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" /backups/backup_da_base.dump
      - Então saia da linha de comando:
  
            exit

4. ### Frontend ##

   1. Entre no diretório frontend:

            cd frontend/

   2. Instale as dependências:

            npm install
   3. Start o servidor:

            npm run dev

**Obs:** {

    Para gerar uma secretkey você pode fazer isso usando um gerador de hash na internet, como https://site112.com/gerador-hash

    Lembrar de colocar a senha do usuário adm quando for executar os comandos com o sudo,

    Nesse projeto é obrigatório ter o Docke e Docker compose na sua máquina, então se você não tiver acesse esse link para baixar https://www.docker.com/,

    Usuários de windows vão necessitar alterar os volumes no docker-compose.yml, por exemplo:
    
    volumes:
    /c/Users/seu-usuario/projeto/db_data:/var/lib/postgresql/data

    Para usuários windows recomendo que use o linux com wsl para criar os containers

}

## Guia de utilização ##

- Todos os medicamentos são listados com paginação, onde cada página possui 25 items;
- Temos 3 inputs de buscas onde para fazer buscas é necessário colocar algo em pelo menos um input, é possivel fazer pesquisas com base na substância, CNPJ, e laboratório;
- Então para fazer buscas basta colocar o nome da substância, ou do cnpj, ou do laboratório e então apertar no botão de busca que se encontra ao lado dos inputs;
- Quando se clica no botão sem ter nada nos inputs o filtro de busca é limpo, então a tabela de informações volta ao seu estado inicial, com todos os dados;
- Para navegar pela paginação basta clicar em um dos botões que se encontrão logo abaixo do rodapé da tabela, então para navegar em páginas específicas basta clicar em algum botão com numero individual, ou então também pode apertar nos botões de anterior ("<")  ou próximo (">");
