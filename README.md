# Projeto de Aprendizagem de Máquina utilizando Python

Esse projeto consiste em analisar e classificar os dados de uma base de dados sobre pessoas, seus gêneros na qual se identificam, seu nível de educação,
seus passatempos favoritos, em qual área elas moram, estações do ano favoritas, entre outros.

## Base de Dados
A base de dados se encontra dentro da pasta **data/raw**, e é composta por um arquivo Excel chamado **"desenhar_arvore_binaria_mountains_beach.xlsx" (Nome provisório)**

## Saída de Dados
A saída de dados está planejada para ser um arquivo com os dados processados que se encontram dentro da pasta data/processed, e até o momento não foi definido o formato do arquivo.

## Requisitos do Projeto
Esse projeto necessita que você tenha o Docker instalado em sua máquina, e caso você não tenha, você pode baixar o Docker através do link: [Docker](https://www.docker.com/products/docker-desktop)

## Execução do Projeto
Até o momento foi projetado dois arquivos diferentes de Docker em formatos diferentes, um estando no formato Dockerfile e o outro estando no formato docker-compose.yml.
Até encontrarmos uma solução para a execução do projeto, será necessário a execução do projeto manualmente.

### Comandos para execução manual do projeto

#### Usando o Dockerfile:
Caso você opte por usar o Dockerfile, você precisará abrir o terminal do CMD ou PowerShell caso você esteja no Windows, ou o terminal do Linux caso você esteja no Linux, e executar os seguintes comandos:

**Comando para construir a imagem do Docker à partir do Dockerfile que está na raiz do projeto:**

```bash 
docker build -t ml_people . 
```

**Em seguida, execute o comando para rodar o conteiner com a imagem que foi criada:**

```bash
docker run --name ml_people ml_people
```

#### Usando o docker-compose.yml:
Caso você opte por usar o docker-compose.yml, você precisará abrir o terminal do CMD ou PowerShell caso você esteja no Windows, ou o terminal do Linux caso você esteja no Linux, e executar o seguinte comando:

**Comando para rodar o conteiner com a imagem que foi criada:**

```bash
docker compose up -d
```

## Notas
**Esse projeto ainda está em desenvolvimento, e por isso pode estar sujeito a mudanças.**