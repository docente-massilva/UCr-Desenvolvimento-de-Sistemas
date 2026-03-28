# DevOps, CI/CD e Computação em Nuvem

## Comandos docker 

Na pasta onde encontra-se o arquivo `dockerfile`, execute:

```
docker build . -t meu_app:2.0
```

O comando anterior, construirá uma nova imagem docker com o nome `meu_app:2.0`.

Após isso, execute:

```
docker run -d -p 80:8000 --name meu_app_web -t meu_app:2.0
```

Este comando deve criar um container com o nome `meu_app_web` a partir da imagem `meu_app:2.0` e redireciona da porta 80 da maquina hospedeira para a porta '8000' do container.

Para visualizar a lista de containers em execução, execute:

```
docker ps
```

Acesse o `localhost:80` para visualizar a aplicação

## Comandos docker compose

Execute o comando abaixo, reconstruir a imagem utilizada pelo serviço descrito no arquivo `docker-compose.yml`:

```
docker compose up -d --build
```

Acesse o `localhost:3000` para visualizar a aplicação

## Comandos rápidos:

- **docker ps**: listar containers;
- **docker logs `<nome do container>`**: visualizar logs do container `<nome do container>`;
- **docker stop `<nome do container>`**: parar a execução do container `<nome do container>`;

## Links de comandos:

- [Docker cheat sheet](https://www.hostinger.com/br/tutoriais/docker-cheat-sheet)